import re

DUPLICATE_ID = re.compile(r'id="([^"]+)_(\d+)"')
EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U00002B00-\U00002BFF\U0000FE0F\U0000200D]+"
)
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
LINK_BAR = re.compile(r"^\s*\[[^\]]+\]\([^)]*\)(\s*\|\s*\[[^\]]+\]\([^)]*\))*\s*$")
BLANKISH = re.compile(r"^\s*(<br\s*/?>)?\s*$")
QUOTE_WARNING = re.compile(r"^>\s*#{3,6}\s+(.*?)\s*$")
FOOTER_NAV = re.compile(r"^#{1,6}\s+더 알아보기\s*$")
HR = re.compile(r"^\s*(---+|\*\*\*+)\s*$")
HTTP_METHOD = re.compile(r"<code>(GET|POST|PUT|PATCH|DELETE)</code>")


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


def _quickstart_only(lines):
    for i, line in enumerate(lines):
        m = HEADING.match(line)
        if m and "Quick guide" in m.group(2):
            return ["# 빠른 시작", ""] + lines[i + 1:]
    return lines


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri == "index.md":
        return markdown
    lines = markdown.split("\n")
    if page.file.src_uri == "quickstart.md":
        lines = _quickstart_only(lines)
    lines = _drop_top_link_bar(lines)
    lines = [l for l in lines if not (LINK_BAR.match(l) and "더 알아보기" in l)]
    if not page.file.src_uri.endswith("README.md"):
        lines = _drop_footer_nav(lines)
    lines = _quote_warnings_to_admonitions(lines)
    lines = _strip_decorative_emoji(lines)
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


def on_page_content(html, page, config, files):
    html, renames = _github_style_ids(html)
    if renames:
        _rename_toc(page.toc, renames)
    html = HTTP_METHOD.sub(
        lambda m: f'<code class="http-method http-{m.group(1).lower()}">{m.group(1)}</code>', html
    )
    return html
