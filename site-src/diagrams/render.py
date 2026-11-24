import os
import sys
from html import escape

from specs import CIDR, PLACEHOLDER, SEQUENCES

FONT = "Pretendard, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', sans-serif"
MONO = "'SF Mono', Menlo, Consolas, monospace"

INK = "#1a1f36"
TEXT = "#414552"
MUTED = "#8792a2"
FAINT = "#c1c9d2"
LINE = "#a3acb9"
BORDER = "#e3e8ee"
SURFACE = "#f6f8fa"
ACCENT = "#1f5eff"
ACCENT_BG = "#f3f6ff"
AMBER = "#d97706"
AMBER_BG = "#fffaf0"
DANGER = "#df1b41"
METHOD_COLOR = {"GET": "#228403", "POST": "#0570de", "PUT": "#b3530a", "PATCH": "#b3530a", "DELETE": "#df1b41"}

WIDTH = 760
LANE_X = {2: [180, 480], 3: [130, 380, 630]}


def text_width(s, size):
    w = 0
    for ch in s:
        if ord(ch) > 0x2E80:
            w += size * 1.0
        elif ch in "il.,:;|!'":
            w += size * 0.3
        elif ch.isupper() or ch in "mwMW@":
            w += size * 0.68
        else:
            w += size * 0.56
    return w


def t(x, y, s, size=12, fill=TEXT, anchor="middle", weight=400, family=FONT):
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>'
    )


def endpoint(x, y, s, muted):
    method, _, path = s.partition(" ")
    color = MUTED if muted else METHOD_COLOR.get(method, ACCENT)
    path_color = MUTED if muted else TEXT
    if not path:
        return t(x, y, s, 11, color, family=MONO, weight=600)
    total = text_width(method + " ", 11) + text_width(path, 11)
    start = x - total / 2
    return (
        f'<text x="{start:.1f}" y="{y:.1f}" font-family="{MONO}" font-size="11" text-anchor="start">'
        f'<tspan fill="{color}" font-weight="700">{escape(method)}</tspan>'
        f'<tspan fill="{path_color}" dx="6">{escape(path)}</tspan></text>'
    )


def arrowhead(x, y, direction, color):
    d = 7 if direction > 0 else -7
    return f'<path d="M{x:.1f},{y:.1f} l{-d},-4.5 l0,9 z" fill="{color}"/>'


def error_mark(x, y):
    return (
        f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="#fff" stroke="{DANGER}" stroke-width="1.6"/>'
        f'<path d="M{x-3.2:.1f},{y-3.2:.1f} l6.4,6.4 M{x+3.2:.1f},{y-3.2:.1f} l-6.4,6.4" '
        f'stroke="{DANGER}" stroke-width="1.6" stroke-linecap="round"/>'
    )


def number_badge(x, y, n):
    return (
        f'<circle cx="{x:.1f}" cy="{y - 4:.1f}" r="8" fill="{ACCENT}"/>'
        + t(x, y, str(n), 10, "#fff", weight=700)
    )


class Sequence:
    def __init__(self, spec):
        self.spec = spec
        self.lanes = spec["lanes"]
        xs = LANE_X[len(self.lanes)]
        self.x = dict(zip(self.lanes, xs))
        self.back = []
        self.front = []
        self.y = 84
        self.rows = []
        self.pending = []
        self.groups = []
        self.open_groups = []

    def lane_span(self, lanes):
        xs = [self.x[l] for l in lanes]
        return min(xs), max(xs)

    def row_messages(self, msgs):
        has_sub = any(m.get("sub") for m in msgs)
        lines = max(len(m.get("label", [])) + (1 if m.get("small") else 0) for m in msgs)
        top = 26 if has_sub else 10
        self.y += top + (14 if self.pending else 0)
        y = self.y
        self.resolve_pending(y)
        in_group = self.open_groups[-1] if self.open_groups else None
        for m in msgs:
            self.draw_message(m, y, in_group)
        self.rows.append(y)
        self.y = y + 22 + 17 * lines

    def draw_message(self, m, y, group):
        x1, x2 = self.x[m["from"]], self.x[m["to"]]
        direction = 1 if x2 > x1 else -1
        muted = m.get("muted", False)
        emphasis = group is not None and group["style"] == "highlight" and not muted
        color = MUTED if muted else (ACCENT if emphasis else TEXT)
        line = FAINT if muted else (ACCENT if emphasis else LINE)
        dash = ' stroke-dasharray="4 4"' if m.get("dashed") else ""
        error = m.get("error")
        end = x2 - direction * (10 if error == "end" else 1)
        self.front.append(
            f'<line x1="{x1 + direction * 4:.1f}" y1="{y}" x2="{end:.1f}" y2="{y}" '
            f'stroke="{line}" stroke-width="1.4"{dash}/>'
        )
        if error == "end":
            self.front.append(error_mark(x2, y))
        elif error == "mid":
            self.front.append(error_mark((x1 + x2) / 2 + direction * 60, y))
        else:
            self.front.append(arrowhead(x2 - direction * 2, y, direction, color))
        cx = (x1 + x2) / 2
        if m.get("sub"):
            self.front.append(endpoint(cx, y - 9, m["sub"], muted))
        ty = y + 19
        label_color = MUTED if muted else TEXT
        for i, label in enumerate(m.get("label", [])):
            if i == 0 and m.get("num"):
                start = cx - (text_width(label, 12) + 22) / 2
                self.front.append(number_badge(start + 8, ty, m["num"]))
                self.front.append(t(start + 22, ty, label, 12, label_color, anchor="start"))
            else:
                self.front.append(t(cx, ty, label, 12, label_color))
            ty += 17
        if m.get("small"):
            self.front.append(t(cx, ty, m["small"], 11, MUTED, family=MONO if m.get("small_mono") else FONT))

    def resolve_pending(self, y):
        for b in self.pending:
            self.draw_bracket(b, b["y0"], y)
        self.pending = []

    def draw_bracket(self, b, y0, y1):
        x = self.x[b["lane"]]
        side = 1 if b.get("side", "right") == "right" else -1
        reach = 26
        dash = ' stroke-dasharray="4 4"' if b.get("dashed") else ""
        color = MUTED if b.get("muted") else LINE
        x0 = x + side * 6
        self.front.append(
            f'<path d="M{x0},{y0} C{x0 + side * reach},{y0} {x0 + side * reach},{y1} {x0},{y1}" '
            f'fill="none" stroke="{color}" stroke-width="1.4"{dash}/>'
        )
        if b.get("dot"):
            self.front.append(f'<circle cx="{x0}" cy="{y1}" r="3" fill="{color}"/>')
        labels = b.get("label", [])
        if labels:
            mid = (y0 + y1) / 2 - (len(labels) - 1) * 8.5 + 4
            anchor = "start" if side > 0 else "end"
            lx = x0 + side * (reach + 6)
            for i, label in enumerate(labels):
                self.front.append(t(lx, mid + i * 17, label, 12, MUTED, anchor=anchor))

    def run(self):
        for item in self.spec["items"]:
            kind = item[0]
            if kind == "msg":
                self.row_messages(item[1:])
            elif kind == "bracket":
                b = dict(item[1])
                b["y0"] = self.rows[-1]
                self.pending.append(b)
            elif kind == "mark":
                self.y += 14 if self.pending else 0
                y = self.y + 18
                self.resolve_pending(y)
                self.front.append(f'<circle cx="{self.x[item[1]]}" cy="{y}" r="3" fill="{TEXT}"/>')
                self.rows.append(y)
                self.y = y + 22
            elif kind == "group":
                g = dict(item[1])
                g["y0"] = self.y + 6
                self.y += 14
                self.open_groups.append(g)
            elif kind == "end":
                g = self.open_groups.pop()
                g["y1"] = self.y + 4
                self.y += 18
                self.groups.append(g)
            elif kind == "step":
                self.y += 22
                y = self.y
                x0 = min(self.x.values()) - 70
                self.front.append(
                    f'<rect x="{x0}" y="{y - 13}" width="52" height="20" rx="10" fill="{SURFACE}" stroke="{BORDER}"/>'
                )
                self.front.append(t(x0 + 26, y + 1, item[1], 10, MUTED, weight=700))
                self.front.append(t(x0 + 64, y + 2, item[2], 13, INK, anchor="start", weight=700))
                self.y = y + 16
            elif kind == "note":
                self.y += 12
                y = self.y
                x0 = min(self.x.values()) - 70
                x1 = max(self.x.values()) + 70
                self.front.append(
                    f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="34" rx="8" fill="{SURFACE}" '
                    f'stroke="{BORDER}" stroke-dasharray="4 4"/>'
                )
                self.front.append(t((x0 + x1) / 2, y + 21, item[1], 11.5, TEXT))
                self.y = y + 40
            elif kind == "gap":
                self.y += item[1]
        self.y += 18
        return self.render()

    def render(self):
        height = self.y + (34 if self.spec.get("footnote") else 18)
        out = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}">',
            f'<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1}" rx="12" fill="#ffffff" stroke="{BORDER}"/>',
        ]
        for lane in self.lanes:
            x = self.x[lane]
            out.append(f'<line x1="{x}" y1="58" x2="{x}" y2="{self.y}" stroke="{BORDER}" stroke-width="2"/>')
        for g in self.groups:
            lo, hi = self.lane_span(g["lanes"])
            x0, x1 = lo - g.get("pad_left", 46), hi + 96
            if g["style"] == "highlight":
                fill, stroke = ACCENT_BG, ACCENT
            else:
                fill, stroke = AMBER_BG, AMBER
            out.append(
                f'<rect x="{x0}" y="{g["y0"]}" width="{x1 - x0}" height="{g["y1"] - g["y0"]}" rx="10" '
                f'fill="{fill}" stroke="{stroke}" stroke-opacity="0.55"/>'
            )
            if g.get("title"):
                w = text_width(g["title"], 11) + 16
                out.append(
                    f'<rect x="{x0 + 10}" y="{g["y0"] - 10}" width="{w:.0f}" height="20" rx="10" fill="{stroke}"/>'
                )
                out.append(t(x0 + 10 + w / 2, g["y0"] + 4, g["title"], 11, "#fff", weight=700))
        for lane in self.lanes:
            x = self.x[lane]
            w = text_width(lane, 13) + 28
            out.append(
                f'<rect x="{x - w / 2:.1f}" y="22" width="{w:.1f}" height="30" rx="15" fill="{SURFACE}" stroke="{BORDER}"/>'
            )
            out.append(t(x, 42, lane, 13, INK, weight=650))
        out.extend(self.front)
        if self.spec.get("footnote"):
            out.append(t(WIDTH / 2, self.y + 12, self.spec["footnote"], 11.5, MUTED))
        out.append("</svg>")
        return "\n".join(out)


def render_cidr(spec):
    prefix = spec["prefix"]
    cell, gap_octet = 18, 10
    width = 32 * cell + 3 * gap_octet
    x0 = (WIDTH - width) / 2
    height = 190
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}">',
        f'<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1}" rx="12" fill="#ffffff" stroke="{BORDER}"/>',
    ]
    octets = spec["address"].split(".")
    for i, octet in enumerate(octets):
        ox = x0 + i * (8 * cell + gap_octet)
        out.append(t(ox + 4 * cell, 46, octet, 18, INK, weight=650, family=MONO))
        if i < 3:
            out.append(t(ox + 8 * cell + gap_octet / 2, 46, ".", 18, MUTED, family=MONO))
    last_center = x0 + 3 * (8 * cell + gap_octet) + 4 * cell
    out.append(t(last_center + text_width(octets[3], 18) / 2 + 2, 46, f"/{prefix}", 18, ACCENT, anchor="start", weight=700, family=MONO))
    bits = "".join(format(int(o), "08b") for o in octets)
    for i, bit in enumerate(bits):
        ox = x0 + (i // 8) * gap_octet + i * cell
        host = i >= prefix
        fill = "#fdecef" if host else ACCENT_BG
        stroke = DANGER if host else "#c9d6ff"
        out.append(f'<rect x="{ox + 1}" y="64" width="{cell - 2}" height="24" rx="3" fill="{fill}" stroke="{stroke}"/>')
        out.append(t(ox + cell / 2, 81, bit, 11, DANGER if host else ACCENT, weight=600, family=MONO))
    end = x0 + (prefix // 8) * gap_octet + prefix * cell - (gap_octet if prefix % 8 == 0 and prefix < 32 else 0)
    out.append(
        f'<path d="M{x0 + 1},{98} q0,10 10,10 L{end - 11:.1f},{108} q10,0 10,-10" fill="none" stroke="{ACCENT}" stroke-width="1.4"/>'
    )
    out.append(t((x0 + end) / 2, 132, f"네트워크 비트 {prefix}개", 12.5, TEXT, weight=600))
    hosts = 32 - prefix
    out.append(t(WIDTH / 2, 164, spec["caption"].format(hosts=hosts, count=2 ** hosts), 11.5, MUTED))
    out.append("</svg>")
    return "\n".join(out)


def render_placeholder(spec):
    height = 200
    return "\n".join(
        [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}">',
            f'<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1}" rx="12" fill="{SURFACE}" stroke="{BORDER}" stroke-dasharray="6 6"/>',
            t(WIDTH / 2, 96, spec["title"], 18, INK, weight=700),
            t(WIDTH / 2, 124, spec["body"], 12.5, MUTED),
            "</svg>",
        ]
    )


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    written = []
    for name, spec in SEQUENCES.items():
        written.append((name, Sequence(spec).run()))
    for name, spec in CIDR.items():
        written.append((name, render_cidr(spec)))
    for name, spec in PLACEHOLDER.items():
        written.append((name, render_placeholder(spec)))
    for name, svg in written:
        with open(os.path.join(out_dir, name + ".svg"), "w", encoding="utf-8") as f:
            f.write(svg + "\n")
    print(f"rendered {len(written)} diagrams into {out_dir}")


if __name__ == "__main__":
    main(sys.argv[1])
