C, S, N = "Client Browser", "Server", "Nicepay"
CSN = [C, S, N]
SN = [S, N]


def msg(frm, to, *label, **opts):
    return {"from": frm, "to": to, "label": list(label), **opts}


def bracket(lane, *label, **opts):
    return ("bracket", {"lane": lane, "label": list(label), **opts})


def group(lanes, style="highlight", title=None, pad_left=46):
    return ("group", {"lanes": lanes, "style": style, "title": title, "pad_left": pad_left})


END = ("end",)

SDK_CALL = msg(C, N, "JS SDK를 통해 결제창 호출", "/ 카드사 인증")


def receipt(highlight):
    sections = [
        ("issue", "현금영수증 요청", "POST /v1/receipt/", "현금영수증 요청", "발급 처리", "현금영수증 응답", "현금영수증 전달"),
        ("cancel", "현금영수증 취소", "POST /v1/receipt/{tid}/cancel", "현금영수증 취소 요청", "취소 처리", "현금영수증 취소 응답", "현금영수증 취소 응답"),
        ("get", "현금영수증 조회", "GET /v1/receipt/{tid}", "현금영수증 조회 요청", "조회 처리", "현금영수증 조회 응답", "현금영수증 조회 응답"),
    ]
    items = []
    for key, c_req, sub, s_req, process, s_res, c_res in sections:
        on = key == highlight
        muted = not on
        if on:
            items.append(group(SN))
        items.append(("msg", msg(C, S, c_req, muted=muted), msg(S, N, s_req, sub=sub, muted=muted)))
        items.append(bracket(N, *process.split(" "), muted=muted))
        items.append(("msg", msg(N, S, s_res, muted=muted), msg(S, C, c_res, muted=muted)))
        if on:
            items.append(END)
        items.append(("gap", 10))
    return {"lanes": CSN, "items": items}


NETCANCEL_BLOCK = [
    ("msg", msg(S, N, "망취소 API 호출", sub="POST /v1/payments/netcancel")),
    bracket(N, "취소", "처리"),
    ("msg", msg(N, S, "취소 응답")),
]

SEQUENCES = {
    "payment-server-authorization": {
        "lanes": CSN,
        "items": [
            ("msg", SDK_CALL),
            bracket(N, "인증", "처리"),
            ("msg", msg(N, C, "returnUrl 로 이동")),
            bracket(C, side="left", dashed=True),
            group(SN, title="승인 API"),
            (
                "msg",
                msg(C, S, "인증 응답 코드", "tid(거래ID) 금액 체크", dashed=True),
                msg(S, N, "승인 API 호출", sub="POST /v1/payments/{tid}"),
            ),
            bracket(N, "승인", "처리"),
            ("msg", msg(N, S, "승인 응답"), msg(S, C)),
            END,
        ],
    },
    "payment-window-server-sdk": {
        "lanes": CSN,
        "items": [
            group(CSN, title="JS SDK"),
            ("msg", SDK_CALL),
            bracket(N, "인증", "처리"),
            ("msg", msg(N, C, "returnUrl 로 이동")),
            END,
            bracket(C, "결제 승인", "요청", side="left", dashed=True),
            (
                "msg",
                msg(C, S, "인증 응답 코드", "tid(거래ID) 금액 체크", dashed=True),
                msg(S, N, "승인 API 호출", sub="POST /v1/payments/{tid}"),
            ),
            bracket(N, "승인", "처리"),
            ("msg", msg(N, S, "승인 응답"), msg(S, C)),
        ],
    },
    "payment-client-authorization": {
        "lanes": CSN,
        "items": [
            ("msg", SDK_CALL),
            bracket(N, "인증", "처리"),
            ("mark", N),
            bracket(N, side="left", dashed=True),
            ("mark", N),
            bracket(N, "승인", "처리"),
            ("msg", msg(N, C, "returnUrl 로 이동")),
        ],
    },
    "payment-client-authorization-check": {
        "lanes": CSN,
        "items": [
            ("msg", SDK_CALL),
            bracket(N, "인증", "처리"),
            ("mark", N),
            bracket(N, side="left", dashed=True),
            ("mark", N),
            bracket(N, "승인", "처리"),
            ("msg", msg(N, C, "returnUrl 로 이동")),
            group(SN, style="warning", title="금액 검증"),
            ("msg", msg(S, N, "승인(결제)", "금액 체크", sub="POST /v1/check-amount/{tid}")),
            bracket(N, "승인", "체크"),
            ("msg", msg(N, S, "결과 응답")),
            END,
        ],
    },
    "netcancel-common": {
        "lanes": SN,
        "items": [
            ("msg", msg(S, N, "결제(승인) 요청")),
            bracket(N),
            bracket(S, side="left", dot=True),
            ("msg", msg(N, S, "Read-timeout 발생시", error="end")),
            group(SN, style="warning", title="망취소"),
            *NETCANCEL_BLOCK,
            END,
        ],
    },
    "netcancel-server-authorization": {
        "lanes": CSN,
        "items": [
            ("msg", SDK_CALL),
            bracket(N, "인증", "처리"),
            ("msg", msg(N, C, "returnUrl 로 이동")),
            bracket(C, side="left", dashed=True),
            (
                "msg",
                msg(C, S, "인증 응답 코드", "tid(거래ID) 금액 체크", dashed=True),
                msg(S, N, "승인 API 호출", sub="POST /v1/payments/{tid}"),
            ),
            bracket(N, "승인", "처리"),
            group(SN, style="warning", title="망취소"),
            ("msg", msg(N, S, "Read-timeout", "발생시", error="end")),
            *NETCANCEL_BLOCK,
            END,
        ],
    },
    "netcancel-client-authorization": {
        "lanes": CSN,
        "items": [
            ("msg", SDK_CALL),
            bracket(N, "인증", "처리"),
            ("mark", N),
            bracket(N, side="left", dashed=True),
            ("mark", N),
            bracket(N, "승인", "처리"),
            group(SN, style="warning", title="망취소"),
            ("msg", msg(N, S, "네트워크 유실", "발생시", error="end")),
            *NETCANCEL_BLOCK,
            END,
        ],
    },
    "netcancel-subscribe": {
        "lanes": SN,
        "items": [
            ("msg", msg(S, N, "빌키 승인", sub="POST /v1/subscribe/{bid}/payments")),
            bracket(N),
            bracket(S, side="left", dot=True),
            ("msg", msg(N, S, "Read-timeout 발생시", error="end")),
            group(SN, style="warning", title="망취소"),
            *NETCANCEL_BLOCK,
            END,
        ],
    },
    "payment-receipt-issue": receipt("issue"),
    "payment-receipt-cancel": receipt("cancel"),
    "payment-receipt-get": receipt("get"),
    "payment-token": {
        "lanes": CSN,
        "items": [
            ("msg", msg(C, S, "요청"), msg(S, N, "토큰 요청", sub="POST")),
            bracket(N, "토큰 생성", "30분 유효"),
            ("msg", msg(N, S, "토큰 응답")),
            bracket(S, "Header", "토큰 추가", side="left", dashed=True),
            ("msg", msg(S, N, "API 호출", sub="POST/GET")),
            bracket(N, "요청 처리"),
            ("msg", msg(N, S, "API 응답"), msg(S, C, "응답")),
        ],
    },
    "payment-subscribe-window": {
        "lanes": CSN,
        "footnote": "이후 빌키(bid)로 빌키승인, 빌키삭제 API를 호출합니다",
        "items": [
            ("step", "STEP 1", "빌링 결제창 호출"),
            ("msg", msg(C, N, "JS SDK로 빌링 결제창 호출", num=1, small="isBill: Y, amount: 0", small_mono=True)),
            bracket(N, "결제수단", "인증"),
            ("msg", msg(N, C, "returnUrl 로 인증 결과 전달", num=2)),
            bracket(C, side="left", dashed=True),
            ("msg", msg(C, S, "tid, isBill: Y 수신", num=3, dashed=True, small="금액, signature 체크")),
            ("step", "STEP 2", "빌키확정"),
            group(SN),
            ("msg", msg(S, N, "빌키확정 요청 (인증 후 10분 안)", num=4, sub="POST /v1/subscribe/{tid}/issue")),
            bracket(N, "빌키", "발급"),
            ("msg", msg(N, S, "빌키(bid) 응답, 가맹점 저장", num=5)),
            END,
            ("msg", msg(S, C, "정기결제 등록 완료")),
        ],
    },
    "payment-subscribe-billing": {
        "lanes": CSN,
        "items": [
            ("step", "STEP 1", "빌링 결제창 호출, 빌키확정"),
            ("note", "빌링 결제창 인증 후 POST /v1/subscribe/{tid}/issue 로 빌키(bid) 저장"),
            ("step", "STEP 2", "빌키승인"),
            group(SN, pad_left=150),
            ("msg", msg(S, N, "결제일마다 빌키승인 요청", num=1, sub="POST /v1/subscribe/{bid}/payments")),
            bracket(N, "승인", "처리"),
            bracket(S, "빌키(bid)로", "반복 정기결제", side="left", dot=True),
            ("msg", msg(N, S, "승인(결제) 응답", num=2)),
            END,
            ("step", "STEP 3", "빌키삭제"),
            ("msg", msg(C, S, "구독 해지 요청"), msg(S, N, "빌키삭제 요청", num=3, sub="POST /v1/subscribe/{bid}/expire")),
            bracket(N, "삭제", "처리"),
            ("msg", msg(N, S, "빌키삭제 응답", num=4), msg(S, C, "구독 해지 완료")),
        ],
    },
    "payment-subscribe-expire": {
        "lanes": CSN,
        "footnote": "삭제된 빌키(bid)는 복원과 빌키승인이 불가합니다",
        "items": [
            ("step", "STEP 1", "빌키확정, 빌키승인"),
            ("note", "빌키확정으로 저장한 빌키(bid)로 결제일마다 POST /v1/subscribe/{bid}/payments 호출"),
            ("step", "STEP 2", "빌키삭제"),
            group(CSN),
            ("msg", msg(C, S, "구독 해지 요청"), msg(S, N, "빌키삭제 요청", num=1, sub="POST /v1/subscribe/{bid}/expire")),
            bracket(N, "삭제", "처리"),
            ("msg", msg(N, S, "빌키삭제 응답", num=2)),
            END,
            ("msg", msg(S, C, "구독 해지 완료")),
        ],
    },
    "payment-webhook": {
        "lanes": SN,
        "items": [
            ("msg", msg(N, S, "승인 응답 전달", sub="POST <웹훅 End-Point>")),
            bracket(S, "비즈니스", "로직 처리", side="left"),
            bracket(N, "ResponseBody에 \"OK\" 문자열이", "없는 경우 1분 간격으로", "10회 재전송", dashed=True, dot=True),
            ("msg", msg(S, N, "HTTP status 200", "ResponseBody { \"OK\" }", dashed=True, error="mid")),
        ],
    },
    "sandbox-webhook": {
        "lanes": SN,
        "items": [
            ("msg", msg(N, S, "Test 메시지 전달", sub="POST <웹훅 End-Point>")),
            bracket(S, "비즈니스", "로직 처리", side="left"),
            bracket(N, "ResponseBody에 \"OK\"", "문자열이 없는 경우 실패", dashed=True, dot=True),
            ("msg", msg(S, N, "HTTP status 200", "ResponseBody { \"OK\" }")),
        ],
    },
}

CIDR = {
    "common-cidr-32": {
        "address": "255.255.255.255",
        "prefix": 32,
        "caption": "호스트 비트 {hosts}개, IP {count}개",
    },
    "common-cidr-31": {
        "address": "255.255.255.255",
        "prefix": 31,
        "caption": "호스트 비트 {hosts}개, IP {count}개",
    },
}

PLACEHOLDER = {
    "under_construction": {
        "title": "준비 중인 문서입니다",
        "body": "",
    },
}
