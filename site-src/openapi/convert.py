import json
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

SOURCES = [
    "api/payment-access-token.md",
    "api/payment-window-server.md",
    "api/payment-window-client.md",
    "api/cancel.md",
    "api/status-transaction.md",
    "api/payment-subscribe.md",
    "api/payment-receipt.md",
    "api/status-terms.md",
    "api/status-event.md",
    "api/status-interest.md",
    "api/payment-epay.md",
    "api/checkout/checkout-create.md",
    "api/checkout/checkout-pay-and-approve.md",
    "api/checkout/checkout-status-retrieve.md",
    "api/checkout/checkout-transaction-retrieve.md",
    "api/checkout/checkout-transaction-cancel.md",
    "api/checkout/checkout-expire.md",
    "api/webhook/webhook-create.md",
    "api/webhook/webhook-retrieve.md",
    "api/webhook/webhook-update.md",
    "api/webhook/webhook-delete.md",
]

TAGS = [
    ("인증", "Access token 발급"),
    ("결제", "결제창 승인과 승인 금액 검증"),
    ("취소", "취소, 환불, 망취소"),
    ("조회", "거래 조회"),
    ("빌링", "빌키확정, 빌키승인, 빌키삭제"),
    ("현금영수증", "현금영수증 발급, 취소, 조회"),
    ("카드 정보", "카드 이벤트, 무이자 정보 조회"),
    ("약관", "약관 조회"),
    ("EPAY", "N정통 EPAY 승인"),
    ("체크아웃", "체크아웃 발급부터 거래 취소까지"),
    ("웹훅 URL", "웹훅 URL 등록, 조회, 수정, 삭제"),
]


def tag_for(method, path):
    if method == "get" and path.startswith("/v1/payments/") and "checkout" not in path:
        return "조회"
    rules = [
        ("/v1/access-token", "인증"),
        ("/v1/payments/checkout", "체크아웃"),
        ("/v1/checkout", "체크아웃"),
        ("/cancel", "취소"),
        ("/netcancel", "취소"),
        ("/v1/receipt", "현금영수증"),
        ("/v1/subscribe", "빌링"),
        ("/v1/card", "카드 정보"),
        ("/v1/terms", "약관"),
        ("/v1/epay", "EPAY"),
        ("/v1/check-amount", "결제"),
        ("/v1/payments/find", "조회"),
        ("webhook", "웹훅 URL"),
    ]
    for key, tag in rules:
        if key in path:
            return tag
    return "결제"


HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
REQ_LINE = re.compile(r"^(GET|POST|PUT|PATCH|DELETE)\s+(/[^\s?]*)")
FENCE = re.compile(r"^\s*```")
TYPE_MAP = {
    "string": "string",
    "integer": "integer",
    "intger": "integer",
    "int": "integer",
    "number": "integer",
    "boolean": "boolean",
    "bool": "boolean",
    "object": "object",
    "array": "array",
    "list": "array",
    "s": "string",
    "n": "integer",
    "b": "boolean",
}
NAME_HEADERS = {"parameter", "필드", "파라미터", "필드명", "key", "name", "parameter name"}
TYPE_HEADERS = {"type", "타입"}
REQ_HEADERS = {"필수"}
LEN_HEADERS = {"byte", "크기", "길이"}
DESC_HEADERS = {"설명", "상세 설명", "상세설명"}


def clean(text):
    text = text.replace("　", " ").replace("\t", " ")
    text = re.sub(r"<img[^>]*>", "", text)
    text = text.replace("&brvbar;", "¦")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def plain_name(cell):
    cell = clean(cell)
    cell = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", cell)
    cell = re.sub(r"[*`]", "", cell)
    cell = re.sub(r"<[^>]+>", "", cell)
    return cell.strip()


def description(parts):
    text = " <br> ".join(p for p in (clean(p) for p in parts) if p)
    text = re.sub(r"(\s*<br\s*/?>\s*)+", "\n", text, flags=re.I).strip()
    text = re.sub(r"\]\((\.\./)?([^)#:]+)\.md", lambda m: "](../" + _site_path(m.group(2)) + ".html", text)
    return "\n".join(line.strip() for line in text.split("\n")).replace("\n", "  \n")


_CURRENT_DIR = [""]


def _site_path(rel):
    return os.path.normpath(os.path.join(_CURRENT_DIR[0], rel)).replace(os.sep, "/")


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c for c in re.split(r"(?<!\\)\|", line)]


def parse_table(lines):
    header = [clean(c).lower().strip("*: ") for c in split_row(lines[0])]
    idx = {}
    for i, h in enumerate(header):
        if h in NAME_HEADERS and "name" not in idx:
            idx["name"] = i
        elif h in TYPE_HEADERS and "type" not in idx:
            idx["type"] = i
        elif h in REQ_HEADERS:
            idx["req"] = i
        elif h in LEN_HEADERS:
            idx["len"] = i
        elif h in DESC_HEADERS:
            idx.setdefault("desc", []).append(i)
    if "name" not in idx or "type" not in idx:
        return None
    nested = idx["name"] + 1 < len(header) and header[idx["name"] + 1] == "" and idx["type"] > idx["name"] + 1
    rows = []
    for line in lines[1:]:
        cells = split_row(line)
        if all(re.fullmatch(r"\s*:?-{2,}:?\s*", c or "-") for c in cells):
            continue
        get = lambda i: cells[i] if i is not None and i < len(cells) else ""
        desc_cols = idx.get("desc", [])
        extra = list(range(max(desc_cols) + 1, len(cells))) if desc_cols else []
        row = {
            "name": plain_name(get(idx["name"])),
            "child": plain_name(get(idx["name"] + 1)) if nested else "",
            "type": plain_name(get(idx["type"])).lower(),
            "required": plain_name(get(idx.get("req"))).upper() in {"O", "Y", "필수"},
            "len": plain_name(get(idx.get("len"))),
            "desc": [get(i) for i in desc_cols + extra],
        }
        if row["name"] or row["child"]:
            rows.append(row)
    return {"nested": nested, "rows": rows}


def field_schema(row):
    t = TYPE_MAP.get(re.sub(r"[^a-z]", "", row["type"]), "string")
    schema = {"type": t}
    desc = description(row["desc"])
    if re.fullmatch(r"\d+", row["len"] or ""):
        desc = (desc + "\n\n" if desc else "") + f"최대 {row['len']} byte"
    if desc:
        schema["description"] = desc
    if t == "array":
        schema["items"] = {"type": "object", "properties": {}}
    if t == "object":
        schema["properties"] = {}
    return schema


def merge_tables(tables):
    root = {"type": "object", "properties": {}, "required": []}
    count = 0
    for table in tables:
        parent = None
        for row in table["rows"]:
            if table["nested"] and not row["name"] and row["child"]:
                if parent is None:
                    continue
                container = parent["items"] if parent["type"] == "array" else parent
                container.setdefault("properties", {})[row["child"]] = field_schema(row)
                if row["required"]:
                    container.setdefault("required", [])
                    if row["child"] not in container["required"]:
                        container["required"].append(row["child"])
                count += 1
                continue
            name = row["name"]
            schema = field_schema(row)
            existing = root["properties"].get(name)
            if existing and existing.get("properties") and not schema.get("properties"):
                schema = existing
            root["properties"][name] = schema
            if row["required"] and name not in root["required"]:
                root["required"].append(name)
            if schema["type"] in ("object", "array"):
                parent = schema
            count += 1
    if not root["required"]:
        del root["required"]
    _prune(root)
    return root, count


def _prune(schema):
    for key in ("properties",):
        for child in schema.get(key, {}).values():
            _prune(child)
    if "items" in schema:
        _prune(schema["items"])
        if not schema["items"].get("properties"):
            schema["items"] = {"type": "object"}
    if schema.get("type") == "object" and "properties" in schema and not schema["properties"]:
        del schema["properties"]


def tables_in(lines, start, end):
    out = []
    i = start
    in_fence = False
    while i < end:
        if FENCE.match(lines[i]):
            in_fence = not in_fence
            i += 1
            continue
        if not in_fence and lines[i].lstrip().startswith("|"):
            j = i
            while j < end and lines[j].lstrip().startswith("|"):
                j += 1
            table = parse_table(lines[i:j])
            if table and table["rows"]:
                out.append(table)
            i = j
            continue
        i += 1
    return out


def headings(lines):
    out = []
    in_fence = False
    for i, line in enumerate(lines):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        m = None if in_fence else HEADING.match(line)
        if m:
            out.append((i, len(m.group(1)), m.group(2)))
    return out


def next_heading(hs, after, pred, limit):
    for i, level, text in hs:
        if after < i < limit and pred(level, text):
            return i
    return None


def section_bounds(hs, line, total):
    start = 0
    for i, level, _ in hs:
        if i <= line and level <= 2:
            start = i
    end = total
    for i, level, text in hs:
        if i > line and level <= 2:
            end = i
            break
    return start, end


def footer_line(hs, total):
    for i, _, text in hs:
        if "더 알아보기" in text:
            return i
    return total


def code_blocks(lines, start, end):
    blocks = []
    i = start
    while i < end:
        if FENCE.match(lines[i]):
            j = i + 1
            while j < end and not FENCE.match(lines[j]):
                j += 1
            blocks.append((i, "\n".join(lines[i + 1:j])))
            i = j + 1
        else:
            i += 1
    return blocks


def section_description(lines, hs, start, end):
    for i, level, text in hs:
        if start <= i < end and level >= 3 and text.replace(" ", "").endswith("설명") and "명세" not in text:
            stop = next_heading(hs, i, lambda lv, t: True, end) or end
            body = [l for l in lines[i + 1:stop] if l.strip() and not l.strip().startswith(("<br", "<img", ">"))]
            text = "\n".join(re.sub(r"<img[^>]*>", "", b).rstrip() for b in body)
            text = re.sub(r"[\U0001F300-\U0001FAFF☀-➿️]", "", text)
            text = re.sub(r"\]\((\.\./)?([^)#:]+)\.md", lambda m: "](../" + _site_path(m.group(2)) + ".html", text)
            return text.strip()
    return ""


def find_endpoints(rel, lines):
    hs = headings(lines)
    total = len(lines)
    footer = footer_line(hs, total)
    found = []
    in_fence = False
    for i, line in enumerate(lines[:footer]):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        m = REQ_LINE.match(line.strip())
        if m and in_fence:
            found.append((i, m.group(1), m.group(2), "req"))
    if not found:
        for i, line in enumerate(lines[:footer]):
            if line.lstrip().startswith("|") and "**" in line:
                cells = [plain_name(c) for c in split_row(line)]
                methods = [c for c in cells if c.upper() in ("GET", "POST", "PUT", "PATCH", "DELETE")]
                paths = [c for c in cells if c.startswith("/v1")]
                if methods and paths:
                    found.append((i, methods[0].upper(), paths[0], "table"))
                    break
    endpoints = []
    req_lines = [f[0] for f in found]
    for n, (line_no, method, path, kind) in enumerate(found):
        path = path.rstrip("/") or "/"
        s_start, s_end = section_bounds(hs, line_no, footer)
        s_end = min(s_end, footer)
        next_req = req_lines[n + 1] if n + 1 < len(req_lines) else footer
        resp = next_heading(hs, line_no, lambda lv, t: "응답 명세" in t.replace("응답명세", "응답 명세"), footer)
        req_start = line_no
        if kind == "req":
            k = line_no
            while k < footer and not FENCE.match(lines[k]):
                k += 1
            req_start = k + 1
        if kind == "table":
            req_start = next_heading(hs, line_no, lambda lv, t: "요청" in t and "명세" in t.replace(" ", ""), footer) or line_no
        shared_request_section = lines[s_start].startswith("## 요청")
        req_end = min(x for x in [resp or footer, next_req, footer if shared_request_section else s_end] if x > req_start)
        if resp is not None and resp > s_end:
            following = [h for h in hs if h[0] == s_end]
            if not (following and "응답" in following[0][2]):
                resp = None
        if resp is not None:
            r_end = s_end
            if resp >= s_end:
                _, r_end = section_bounds(hs, resp, footer)
            r_end = min(r_end, footer)
            response_tables = tables_in(lines, resp, r_end)
        else:
            response_tables = []
        request_tables = tables_in(lines, req_start, req_end)
        samples = [b for _, b in code_blocks(lines, s_start, s_end) if "curl" in b]
        endpoints.append(
            {
                "source": rel,
                "line": line_no + 1,
                "method": method,
                "path": path,
                "section": next((t for i, lv, t in hs if i == s_start), ""),
                "description": section_description(lines, hs, s_start, s_end),
                "request_tables": request_tables,
                "response_tables": response_tables,
                "sample": samples[0] if samples else None,
            }
        )
    return endpoints


def uri_names():
    names = {}
    with open(os.path.join(ROOT, "common/api.md"), encoding="utf-8") as f:
        for line in f:
            cells = [plain_name(c) for c in split_row(line)] if line.startswith("|") else []
            if len(cells) >= 3 and cells[1].upper() in ("GET", "POST"):
                names[(cells[1].upper(), cells[2].rstrip("/"))] = cells[0]
    return names


def build(out_path):
    names = uri_names()
    spec = {
        "openapi": "3.1.0",
        "info": {
            "title": "NicePay API",
            "version": "v1",
            "description": "NicePay 결제 API 명세입니다. 각 항목의 설명과 예제는 [개발자 가이드](../index.html)의 원문 문서에서 옮겼습니다.",
        },
        "servers": [
            {"url": "https://api.nicepay.co.kr", "description": "운영"},
            {"url": "https://sandbox-api.nicepay.co.kr", "description": "샌드박스"},
        ],
        "tags": [{"name": n, "description": d} for n, d in TAGS],
        "components": {
            "securitySchemes": {
                "basicAuth": {"type": "http", "scheme": "basic", "description": "clientId:secretKey를 Base64로 인코딩한 값"},
                "bearerAuth": {"type": "http", "scheme": "bearer", "description": "Access token API로 발급한 토큰"},
            }
        },
        "security": [{"basicAuth": []}, {"bearerAuth": []}],
        "paths": {},
    }
    report = []
    for rel in SOURCES:
        _CURRENT_DIR[0] = os.path.dirname(rel)
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            lines = f.read().split("\n")
        for ep in find_endpoints(rel, lines):
            method = ep["method"].lower()
            path = ep["path"]
            summary = names.get((ep["method"], path)) or re.sub(r"[\U0001F300-\U0001FAFF☀-➿]", "", ep["section"]).strip()
            path_params = re.findall(r"\{(\w+)\}", path)
            req_schema, req_count = merge_tables(ep["request_tables"])
            res_schema, res_count = merge_tables(ep["response_tables"])
            guide = os.path.splitext(rel)[0] + ".html"
            desc = ep["description"]
            desc = (desc + "\n\n" if desc else "") + f"[가이드 문서에서 보기](../{guide})"
            op = {
                "tags": [tag_for(method, path)],
                "summary": summary,
                "description": desc,
                "operationId": re.sub(r"\W+", "_", f"{method}_{path}").strip("_"),
                "parameters": [],
                "responses": {
                    "200": {
                        "description": "성공. 결과는 resultCode로 확인합니다.",
                        "content": {"application/json": {"schema": res_schema}} if res_count else {},
                    }
                },
            }
            props = req_schema.get("properties", {})
            for p in path_params:
                pschema = props.pop(p, {"type": "string"})
                op["parameters"].append(
                    {
                        "name": p,
                        "in": "path",
                        "required": True,
                        "schema": {"type": "string"},
                        "description": pschema.get("description", ""),
                    }
                )
            if "required" in req_schema:
                req_schema["required"] = [r for r in req_schema["required"] if r in props]
                if not req_schema["required"]:
                    del req_schema["required"]
            if props:
                if method == "get":
                    required = set(req_schema.get("required", []))
                    for name, schema in props.items():
                        op["parameters"].append(
                            {
                                "name": name,
                                "in": "query",
                                "required": name in required,
                                "schema": {k: v for k, v in schema.items() if k != "description"},
                                "description": schema.get("description", ""),
                            }
                        )
                else:
                    op["requestBody"] = {"required": True, "content": {"application/json": {"schema": req_schema}}}
            if not op["parameters"]:
                del op["parameters"]
            if not op["responses"]["200"]["content"]:
                del op["responses"]["200"]["content"]
            if ep["sample"]:
                op["x-codeSamples"] = [{"lang": "Shell", "label": "cURL (문서 예제)", "source": ep["sample"].strip()}]
            if path == "/v1/access-token":
                op["security"] = [{"basicAuth": []}]
            spec["paths"].setdefault(path, {})[method] = op
            report.append((ep["source"], ep["line"], ep["method"], path, summary, req_count, res_count))
    for path, ops in spec["paths"].items():
        donors = [op for op in ops.values() if op["responses"]["200"].get("content")]
        for op in ops.values():
            if not op["responses"]["200"].get("content") and donors:
                op["responses"]["200"]["content"] = donors[0]["responses"]["200"]["content"]
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(spec, f, ensure_ascii=False, indent=2)
    return report


if __name__ == "__main__":
    report = build(sys.argv[1])
    for src, line, method, path, summary, rq, rs in report:
        print(f"{method:6} {path:48} req={rq:<3} res={rs:<3} {summary}  ({src}:{line})")
    print(f"{len(report)} operations")
