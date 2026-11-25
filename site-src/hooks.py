import hashlib
import html as htmllib
import importlib.util
import os
import posixpath
import re
import shutil
import urllib.parse

DUPLICATE_ID = re.compile(r'id="([^"]+)_(\d+)"')
EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U000023E9-\U000023FA\U00002600-\U000027BF\U00002B00-\U00002BFF\U0000FE0F\U0000200D]+"
)
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
LINK_BAR = re.compile(r"^\s*\[[^\]]+\]\([^)]*\)(\s*\|\s*\[[^\]]+\]\([^)]*\))*\s*$")
BLANKISH = re.compile(r"^\s*(<br\s*/?>)?\s*$")
QUOTE_WARNING = re.compile(r"^>\s*#{3,6}\s+(.*?)\s*$")
HEADING_WARNING = re.compile(r"^#{3,6}\s+(⚠️?.*?)\s*$")
SITE_HEADINGS = {
    "api/payment-window-server.md": {"결제창 (Server 승인 모델-JS SDK)": "결제창 호출 (JS SDK)"},
    "api/payment-window-client.md": {"결제창 (Client 승인 모델-JS SDK)": "결제창 호출 (JS SDK)"},
}
FOOTER_NAV = re.compile(r"^#{1,6}\s+더 알아보기\s*$")
HR = re.compile(r"^\s*(---+|\*\*\*+)\s*$")
DOC_INDEX_LINK = re.compile(r"^\s*\[전체 문서 목록\]\((\.\./)*README\.md\)\s*$")
HTTP_METHOD = re.compile(r"<code>(GET|POST|PUT|PATCH|DELETE)</code>")
TYPE_BADGE = re.compile(r'<img src="https://img\.shields\.io/badge/-(Object|Array|nullable)-[A-Za-z]+"\s*/?>')
TABLE = re.compile(r"<table>(.*?)</table>", re.S)
ROW = re.compile(r"<tr>(.*?)</tr>", re.S)
CELL = re.compile(r"<(t[hd])([^>]*)>(.*?)</\1>", re.S)
NAME_KEYS = {"parameter", "value", "필드", "오브젝트", "구분", ""}
TYPE_KEYS = {"type", "타입"}
SIZE_KEYS = {"byte", "크기", "길이"}
FENCE_OPEN = re.compile(r"^(\s*)```\s*([\w#+.-]*)\s*$")
SDK_BADGES = re.compile(
    r'<div align="left">\s*((?:<a href="[^"]+">\s*<img src="https://img\.shields\.io/badge/[^"]*style=for-the-badge[^"]*">\s*</a>\s*)+)</div>'
)
SDK_BADGE = re.compile(r'<a href="([^"]+)">\s*<img src="https://img\.shields\.io/badge/([^"?]+)\?[^"]*">\s*</a>')
SDK_NAMES = {"node.js": "Node.js", "python": "Python", "ruby": "Ruby", "asp": "ASP", "java": "Java", "php": "PHP", ".net": ".NET"}
IMG = re.compile(r"<img\b[^>]*>")
SRC = re.compile(r'\ssrc="([^"]+)"')
RASTER = re.compile(r"\.(png|jpe?g|gif|webp)(\?.*)?$", re.I)


def _strip_emoji(text):
    return EMOJI.sub("", text).strip()


def _drop_top_link_bar(lines):
    for i, line in enumerate(lines[:12]):
        if HEADING.match(line):
            continue
        if BLANKISH.match(line):
            continue
        if LINK_BAR.match(line):
            j = i + 1
            while j < len(lines) and BLANKISH.match(lines[j]):
                j += 1
            return lines[:i] + lines[j:]
        break
    return lines


def _drop_footer_nav(lines):
    for i, line in enumerate(lines):
        if FOOTER_NAV.match(line.strip()):
            head = lines[:i]
            while head and (BLANKISH.match(head[-1]) or HR.match(head[-1])):
                head.pop()
            return head
    return lines


def _quote_warnings_to_admonitions(lines):
    out = []
    i = 0
    while i < len(lines):
        m = QUOTE_WARNING.match(lines[i])
        if not m:
            out.append(lines[i])
            i += 1
            continue
        title = _strip_emoji(m.group(1)) or "중요"
        body = []
        i += 1
        while i < len(lines) and lines[i].lstrip().startswith(">"):
            body.append(re.sub(r"^\s*>\s?", "", lines[i]))
            i += 1
        if out and out[-1].strip():
            out.append("")
        out.append(f'!!! warning "{title}"')
        out.append("")
        out.extend(("    " + b) if b.strip() else "" for b in body)
        out.append("")
    return out


def _heading_warnings_to_admonitions(lines):
    out = []
    in_fence = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        m = None if in_fence else HEADING_WARNING.match(line)
        if not m:
            out.append(line)
            i += 1
            continue
        title = _strip_emoji(m.group(1)) or "중요"
        body = []
        i += 1
        while i < len(lines) and not HEADING.match(lines[i]):
            body.append(lines[i])
            i += 1
        while body and not body[-1].strip():
            body.pop()
        while body and not body[0].strip():
            body.pop(0)
        if out and out[-1].strip():
            out.append("")
        out.append(f'!!! warning "{title}"')
        out.append("")
        out.extend(("    " + b) if b.strip() else "" for b in body)
        out.append("")
    return out


def _headings_outside_fences(lines):
    in_fence = False
    for i, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        m = None if in_fence else HEADING.match(line)
        if m:
            yield i, len(m.group(1)), m.group(2)


def _next_content(lines, start):
    for i in range(start, len(lines)):
        if lines[i].strip():
            return i
    return None


def _promote_headings(lines, after):
    for i, level, text in list(_headings_outside_fences(lines)):
        if i > after and level > 1:
            lines[i] = "#" * (level - 1) + " " + text
    return lines


def _normalize_titles(lines, src, config):
    renames = SITE_HEADINGS.get(src, {})
    if renames:
        slugify = config["mdx_configs"]["toc"]["slugify"]
        for i, level, text in _headings_outside_fences(lines):
            if text in renames:
                lines[i] = f"{'#' * level} {renames[text]} {{#{slugify(text, '-')}}}"
    headings = list(_headings_outside_fences(lines))
    if not headings:
        return lines
    h2s = [h for h in headings if h[1] == 2]
    first = _next_content(lines, 0)
    top = next((h for h in headings if h[0] == first), None)
    if top is None:
        return lines
    if top[1] == 1:
        nxt = _next_content(lines, top[0] + 1)
        if len(h2s) == 1 and h2s[0][0] == nxt:
            lines[top[0]] = "# " + h2s[0][2]
            del lines[nxt]
            return _promote_headings(lines, top[0])
        return lines
    if top[1] == 2 and not any(h[1] == 1 for h in headings):
        if len(h2s) == 1:
            lines[top[0]] = "# " + top[2]
            return _promote_headings(lines, top[0])
        nxt = _next_content(lines, top[0] + 1)
        if any(h[0] == nxt and h[1] == 2 for h in headings):
            lines[top[0]] = "# " + top[2]
    return lines


def _strip_decorative_emoji(lines):
    out = []
    in_fence = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence:
            out.append(line)
            continue
        m = HEADING.match(line)
        if m:
            line = f"{m.group(1)} {_strip_emoji(m.group(2))}"
        else:
            line = re.sub(r"(?<=\S)[ \t]{2,}(?=\S)", " ", EMOJI.sub("", line)) if EMOJI.search(line) else line
        out.append(line)
    return out


def _separate_tables_from_fences(lines):
    out = []
    in_fence = False
    for line in lines:
        if out and not in_fence and out[-1].lstrip().startswith("```") and line.lstrip().startswith("|"):
            out.append("")
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        out.append(line)
    return out


def _label_fences_to_titles(lines):
    out = []
    in_fence = False
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith("```"):
            in_fence = not in_fence
        label = None if not in_fence else FENCE_OPEN.match(lines[i])
        if label and i + 2 < len(lines) and lines[i + 2].strip() == "```" and not lines[i + 1].lstrip().startswith("```"):
            text = lines[i + 1].strip()
            j = i + 3
            while j < len(lines) and not lines[j].strip():
                j += 1
            code = FENCE_OPEN.match(lines[j]) if j < len(lines) else None
            if text and '"' not in text and code and code.group(1) == label.group(1):
                out.append(f'{code.group(1)}```{code.group(2)} title="{text}"')
                i = j + 1
                continue
        out.append(lines[i])
        i += 1
    return out


def _sdk_links(match):
    items = []
    for href, badge in SDK_BADGE.findall(match.group(1)):
        name = badge.rsplit("-", 1)[0]
        items.append(f'<li><a href="{href}">{htmllib.escape(SDK_NAMES.get(name, name))}</a></li>')
    return '<ul class="sdk-links">' + "".join(items) + "</ul>"


def _cell_text(cell):
    text = htmllib.unescape(TAG.sub("", cell)).replace("\u3000", "")
    return re.sub(r"\s+", " ", text).strip()


def _with_attrs(attrs, classes, label=None):
    extra = f' class="{" ".join(classes)}"'
    if label:
        extra += f' data-label="{htmllib.escape(label)}"'
    return attrs + extra


def _spec_roles(headers):
    keys = [_cell_text(h).lower() for h in headers]
    type_at = next((i for i, k in enumerate(keys) if k in TYPE_KEYS), None)
    if not type_at or any(k not in NAME_KEYS for k in keys[:type_at]):
        return None
    roles = ["name"] * type_at + ["type"]
    for k in keys[type_at + 1:]:
        roles.append("req" if k == "필수" else "size" if k in SIZE_KEYS else "desc")
    if "desc" not in roles:
        return None
    return roles


def _spec_row(row, roles, labels):
    cells = CELL.findall(row)
    if len(cells) != len(roles) or any(tag != "td" for tag, _, _ in cells):
        return row, 0
    texts = [_cell_text(body) for _, _, body in cells]
    named = [i for i, r in enumerate(roles) if r == "name" and texts[i]]
    depth = named[0] if named else 0
    out = []
    for i, ((tag, attrs, body), role, text) in enumerate(zip(cells, roles, texts)):
        label = None
        if role == "name":
            classes = ["spec-name" if named and i == named[-1] else "spec-group"]
        elif role == "req":
            classes = ["spec-req"] + (["spec-required"] if text == "O" else [])
            label = labels[i]
        elif role == "size":
            classes = ["spec-size"]
            label = labels[i]
            text = "" if text == "-" else text
        else:
            classes = ["spec-" + role]
        if not text:
            classes.append("spec-empty")
        out.append(f"<{tag}{_with_attrs(attrs, classes, label)}>{body}</{tag}>")
    return "\n" + "\n".join(out) + "\n", depth


def _spec_table(match):
    body = match.group(1)
    rows = ROW.findall(body)
    if not rows:
        return match.group(0)
    headers = [c for tag, _, c in CELL.findall(rows[0]) if tag == "th"]
    roles = _spec_roles(headers)
    if not roles or len(headers) != len(roles):
        return match.group(0)
    labels = [_cell_text(h) for h in headers]

    def row(m):
        if "<th" in m.group(1):
            return m.group(0)
        inner, depth = _spec_row(m.group(1), roles, labels)
        cls = f' class="spec-depth-{depth}"' if depth else ""
        return f"<tr{cls}>{inner}</tr>"

    return "<table data-spec>" + ROW.sub(row, body) + "</table>"


def _diagram_img(tag, src, dark_src):
    light = tag.replace(f'src="{src}"', f'src="{src}#only-light"', 1)
    dark = tag.replace(f'src="{src}"', f'src="{dark_src}#only-dark"', 1)
    return (
        '<span class="diagram">'
        f'<span class="diagram__scroll">{light}{dark}</span>'
        '<span class="diagram__open">'
        f'<a class="diagram__light" href="{src}" target="_blank" rel="noopener">원본 크기로 열기</a>'
        f'<a class="diagram__dark" href="{dark_src}" target="_blank" rel="noopener">원본 크기로 열기</a>'
        "</span></span>"
    )


def _images(html, page, config):
    dark_dir = os.path.join(config["docs_dir"], "image", "dark")
    page_dir = posixpath.dirname(page.file.src_uri)

    def image(m):
        tag = m.group(0)
        src_m = SRC.search(tag)
        if not src_m:
            return tag
        src = src_m.group(1)
        if RASTER.search(src):
            return tag if "class=" in tag else tag[:-1].rstrip("/ ") + ' class="screenshot">'
        if "://" in src or not src.endswith(".svg"):
            return tag
        resolved = posixpath.normpath(posixpath.join(page_dir, src))
        name = posixpath.basename(resolved)
        if posixpath.dirname(resolved) != "image" or not os.path.exists(os.path.join(dark_dir, name)):
            return tag
        dark_src = posixpath.join(posixpath.dirname(src), "dark", name)
        return _diagram_img(tag, src, dark_src)

    return IMG.sub(image, html)


def _quickstart_only(lines):
    for i, line in enumerate(lines):
        m = HEADING.match(line)
        if m and "Quick guide" in m.group(2):
            return ["# 빠른 시작", ""] + lines[i + 1:]
    return lines


def _load_convert():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "openapi", "convert.py")
    spec = importlib.util.spec_from_file_location("nicepay_openapi_convert", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_CONVERT = _load_convert()


def _reference_href(src, method, path):
    tag = _CONVERT.tag_for(method.lower(), path)
    slug = urllib.parse.quote(re.sub(r"\s+", "-", tag.strip().lower()), safe="")
    base = posixpath.relpath("reference/index.html", posixpath.dirname(src) or ".")
    return f"{base}#tag/{slug}/{method.upper()}{path}"


def _anchor_heading(lines, line_no):
    if lines[line_no].lstrip().startswith("|"):
        for i in range(line_no + 1, len(lines)):
            m = HEADING.match(lines[i])
            if m and "요청" in m.group(2) and "명세" in m.group(2).replace(" ", ""):
                return i
        return None
    in_fence = False
    last = None
    for i, line in enumerate(lines[:line_no]):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence and HEADING.match(line):
            last = i
    return last


def _insert_reference_links(lines, src):
    if src not in _CONVERT.SOURCES:
        return lines
    _CONVERT._CURRENT_DIR[0] = posixpath.dirname(src)
    inserts = {}
    for ep in _CONVERT.find_endpoints(src, lines):
        at = _anchor_heading(lines, ep["line"] - 1)
        if at is None:
            continue
        href = htmllib.escape(_reference_href(src, ep["method"], ep["path"]))
        label = htmllib.escape(f'{ep["method"]} {ep["path"]}')
        inserts.setdefault(at, []).append(
            f'<p class="ref-link"><a href="{href}">API 레퍼런스에서 보기</a><code>{label}</code></p>'
        )
    for at in sorted(inserts, reverse=True):
        lines = lines[: at + 1] + [""] + inserts[at] + [""] + lines[at + 1 :]
    return lines


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri == "index.md":
        return markdown
    if page.file.src_uri not in _NAV_PAGES:
        page.meta["search"] = {"exclude": True}
    lines = markdown.split("\n")
    lines = _insert_reference_links(lines, page.file.src_uri)
    lines = _label_fences_to_titles(lines)
    if page.file.src_uri == "quickstart.md":
        lines = _quickstart_only(lines)
        page.meta["hide"] = ["navigation"]
    lines = _drop_top_link_bar(lines)
    lines = [l for l in lines if not (LINK_BAR.match(l) and "더 알아보기" in l)]
    lines = [l for l in lines if not DOC_INDEX_LINK.match(l)]
    if not page.file.src_uri.endswith("README.md"):
        lines = _drop_footer_nav(lines)
    lines = _quote_warnings_to_admonitions(lines)
    lines = _heading_warnings_to_admonitions(lines)
    if page.file.src_uri in _NAV_PAGES and page.file.src_uri != "quickstart.md":
        lines = _normalize_titles(lines, page.file.src_uri, config)
    lines = _strip_decorative_emoji(lines)
    lines = _separate_tables_from_fences(lines)
    return "\n".join(lines)


def _github_style_ids(html):
    ids = set(re.findall(r'id="([^"]+)"', html))
    renames = {}
    for base, n in DUPLICATE_ID.findall(html):
        if base in ids:
            renames[f"{base}_{n}"] = f"{base}-{n}"
    for old, new in renames.items():
        html = html.replace(f'id="{old}"', f'id="{new}"')
        html = html.replace(f'href="#{old}"', f'href="#{new}"')
    return html, renames


def _rename_toc(items, renames):
    for item in items:
        if item.id in renames:
            item.id = renames[item.id]
        _rename_toc(item.children, renames)


HTML_HEADING = re.compile(r'<h([1-6]) id="([^"]+)">(.*?)</h\1>', re.S)
HEADERLINK = re.compile(r'<a class="headerlink"[^>]*>.*?</a>', re.S)
OBJECT_LABEL = re.compile(r'<span class="type-label">(Object|Array)</span>')
SPACER = re.compile(r"(\s*<p>\s*<br\s*/?>\s*</p>\s*)+$")


def _fold_candidates(heads):
    marks = set()
    for n, (_, _, level, _, inner) in enumerate(heads):
        if OBJECT_LABEL.search(inner):
            marks.add(n)
        if _cell_text(HEADERLINK.sub("", inner)) != "공통":
            continue
        for m in range(n + 1, len(heads)):
            lv, text = heads[m][2], _cell_text(HEADERLINK.sub("", heads[m][4]))
            if lv < level or (lv == level and "명세" in text):
                break
            if lv == level:
                marks.add(m)
    runs, run = [], []
    for n in sorted(marks):
        if run and (n != run[-1] + 1 or heads[n][2] != heads[run[-1]][2]):
            runs.append(run)
            run = []
        run.append(n)
    if run:
        runs.append(run)
    return [n for r in runs if len(r) >= 2 for n in r]


def _fold_sections(html):
    heads = [(m.start(), m.end(), int(m.group(1)), m.group(2), m.group(3)) for m in HTML_HEADING.finditer(html)]
    folds = set(_fold_candidates(heads))
    if not folds:
        return html, set()
    out, pos, hidden = [], 0, set()
    for n in sorted(folds):
        start, end, level, hid, inner = heads[n]
        if start < pos:
            continue
        stop = next((h[0] for h in heads[n + 1:] if h[2] <= level), len(html))
        hidden.update(h[3] for h in heads[n:] if h[0] < stop)
        body = SPACER.sub("", html[end:stop])
        out.append(SPACER.sub("", html[pos:start]))
        out.append(
            f'<details class="spec-fold"><summary><h{level} id="{hid}">{inner}</h{level}></summary>'
            f"{body}</details>"
        )
        pos = stop
    out.append(html[pos:])
    return "".join(out), hidden


def _drop_toc(items, ids):
    items[:] = [item for item in items if item.id not in ids]
    for item in items:
        _drop_toc(item.children, ids)


def on_page_content(html, page, config, files):
    html, renames = _github_style_ids(html)
    if renames:
        _rename_toc(page.toc, renames)
    html = TYPE_BADGE.sub(r'<span class="type-label">\1</span>', html)
    html = SDK_BADGES.sub(_sdk_links, html)
    if page.file.src_uri in _NAV_PAGES:
        html, folded = _fold_sections(html)
        _drop_toc(page.toc.items, folded)
    html = HTTP_METHOD.sub(
        lambda m: f'<code class="http-method http-{m.group(1).lower()}">{m.group(1)}</code>', html
    )
    _PAGES[page.file.src_uri] = _summary(html)
    html = TABLE.sub(_spec_table, html)
    html = _images(html, page, config)
    if page.file.src_uri != "index.md":
        html = _insert_page_actions(html, page)
    return html


_PAGES = {}
_NAV_ORDER = []
_NAV_PAGES = set()
FIRST_PARAGRAPH = re.compile(r"<p>(.*?)</p>", re.S)
TAG = re.compile(r"<[^>]+>")


def _summary(html):
    for m in FIRST_PARAGRAPH.finditer(html):
        text = htmllib.unescape(TAG.sub("", m.group(1))).strip()
        text = re.sub(r"\s+", " ", text)
        if len(text) >= 10:
            return text[:140]
    return ""


def _insert_page_actions(html, page):
    md_name = posixpath.basename(page.file.src_uri)
    actions = (
        '<div class="page-actions">'
        f'<a class="page-action" href="{md_name}">Markdown 보기</a>'
        f'<button class="page-action" type="button" data-copy-md="{md_name}">Markdown 복사</button>'
        "</div>"
    )
    if "</h1>" in html:
        return html.replace("</h1>", "</h1>" + actions, 1)
    return actions + html


def on_nav(nav, config, files):
    _NAV_ORDER.clear()

    def walk(items, section):
        for item in items:
            if item.is_page:
                _NAV_ORDER.append((section, item))
            elif item.is_section:
                walk(item.children, item.title if section is None else section)

    walk(nav.items, None)
    _NAV_PAGES.clear()
    _NAV_PAGES.update(item.file.src_uri for _, item in _NAV_ORDER)
    return nav


def on_post_build(config):
    site_dir = config["site_dir"]
    docs_dir = config["docs_dir"]
    for src in list(_PAGES):
        source = os.path.join(docs_dir, src)
        target = os.path.join(site_dir, src)
        if os.path.exists(source) and not os.path.exists(target):
            os.makedirs(os.path.dirname(target), exist_ok=True)
            shutil.copyfile(source, target)

    base = config["site_url"].rstrip("/") + "/"
    lines = [
        f"# {config['site_name']}",
        "",
        "> NICEPAY for Startup(나이스페이 포스타트) 결제 연동 가이드와 API 명세입니다. 각 항목은 Markdown 원문 주소입니다.",
        "",
    ]
    current = object()
    for section, page in _NAV_ORDER:
        src = page.file.src_uri
        if src == "index.md":
            continue
        heading = section or "시작하기"
        if heading != current:
            lines += ["", f"## {heading}", ""]
            current = heading
        desc = _PAGES.get(src, "")
        title = page.title or src
        lines.append(f"- [{title}]({base}{src})" + (f": {desc}" if desc else ""))
    with open(os.path.join(site_dir, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines).strip() + "\n")


ASSET_REF = re.compile(r'((?:href|src)="(?:\.\./)*assets/extra\.(?:css|js))"')


SECONDARY_NAV = 'class="md-nav md-nav--secondary"'
GROUPED_TOC_MIN_ITEMS = 12


def _grouped_toc(page):
    items = list(page.toc.items) if page.toc else []
    if items and items[0].level == 1:
        items = items[0].children
    groups = [item for item in items if item.children]
    return len(groups) >= 2 and _toc_size(items) >= GROUPED_TOC_MIN_ITEMS


def _toc_size(items):
    return sum(1 + _toc_size(item.children) for item in items)


SITE_TITLE_SUFFIX = " 개발자 가이드"


def _split_site_title(output, config):
    name = config["site_name"]
    if not name.endswith(SITE_TITLE_SUFFIX):
        return output
    head = name[: -len(SITE_TITLE_SUFFIX)]
    marked = f'{head}<span class="site-title-suffix">{SITE_TITLE_SUFFIX}</span>'
    return re.sub(
        r'(<div class="md-header__topic">\s*<span class="md-ellipsis">\s*)' + re.escape(name),
        lambda m: m.group(1) + marked,
        output,
        count=1,
    )


def on_post_page(output, page, config):
    output = _split_site_title(output, config)
    if _grouped_toc(page):
        output = output.replace(SECONDARY_NAV, 'class="md-nav md-nav--secondary toc-grouped"')
    versions = {}
    for ext in ("css", "js"):
        path = os.path.join(config["docs_dir"], "assets", f"extra.{ext}")
        with open(path, "rb") as f:
            versions[ext] = hashlib.sha256(f.read()).hexdigest()[:10]
    return ASSET_REF.sub(lambda m: f'{m.group(1)}?v={versions[m.group(1).rsplit(".", 1)[1]]}"', output)
