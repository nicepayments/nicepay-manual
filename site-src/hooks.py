import re

DUPLICATE_ID = re.compile(r'id="([^"]+)_(\d+)"')


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
    return html
