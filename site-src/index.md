---
hide:
  - navigation
  - toc
---

<div class="landing" markdown>

<div class="landing-hero" markdown>

# NICEPAY for start 개발자 가이드

나이스페이 포스타트의 결제창 연동부터 승인, 조회, 취소, 웹훅까지 연동에 필요한 API 명세와 예제를 제공합니다.

[빠른 시작](quickstart.md){ .landing-button .landing-button--primary }
[API 레퍼런스](reference/index.html){ .landing-button }

</div>

<div class="landing-grid" markdown>

<div class="landing-section" markdown>

### 시작하기

- [빠른 시작](quickstart.md)
- [개발 준비](common/preparations.md)
- [API·JS SDK](common/api.md)
- [TEST·샘플코드](common/test.md)

</div>

<div class="landing-section" markdown>

### 결제·발급

- [결제창 (Server 승인)](api/payment-window-server.md)
- [결제창 (Client 승인)](api/payment-window-client.md)
- [빌링](api/payment-subscribe.md)
- [현금영수증](api/payment-receipt.md)

</div>

<div class="landing-section" markdown>

### 조회·취소

- [거래 조회](api/status-transaction.md)
- [취소·환불·망취소](api/cancel.md)
- [약관 조회](api/status-terms.md)
- [카드 무이자 조회](api/status-interest.md)

</div>

<div class="landing-section" markdown>

### 체크아웃

- [체크아웃 발급](api/checkout/checkout-create.md)
- [결제창 & 승인](api/checkout/checkout-pay-and-approve.md)
- [거래 조회](api/checkout/checkout-transaction-retrieve.md)
- [거래 취소](api/checkout/checkout-transaction-cancel.md)

</div>

<div class="landing-section" markdown>

### 웹훅·APP

- [웹훅](api/hook.md)
- [웹훅 URL 등록](api/webhook/webhook-create.md)
- [iOS](api/app-ios.md)
- [Android](api/app-android.md)

</div>

<div class="landing-section" markdown>

### 운영

- [지원환경](management/user.md)
- [개발정보](management/admin.md)
- [코드집](common/code.md)

</div>

<div class="landing-section" markdown>

### 서버 SDK

- [Node.js](https://github.com/nicepayments/nicepay-node)
- [Python](https://github.com/nicepayments/nicepay-python)
- [Java](https://github.com/nicepayments/nicepay-java)
- [PHP](https://github.com/nicepayments/nicepay-php)
- [Ruby](https://github.com/nicepayments/nicepay-ruby)
- [.NET](https://github.com/nicepayments/nicepay-dotnet)
- [ASP](https://github.com/nicepayments/nicepay-asp)

</div>

</div>

<div class="landing-section landing-docs" markdown>

### 문서 구성

| 문서 | 담은 내용 | 이럴 때 보세요 |
|---|---|---|
| 개발자 가이드 | 연동 흐름, 결제창 호출(JS SDK), 웹훅 수신 명세, 앱 연동, 코드집 | 처음 연동하거나 결제 흐름을 이해할 때 |
| [API 레퍼런스](reference/index.html) | 서버 API의 엔드포인트별 요청, 응답 명세와 예제 | 필드를 하나씩 확인하며 구현할 때 |
| [GitHub 저장소](https://github.com/nicepayments/nicepay-manual) | 두 문서의 Markdown 원문 | 변경 이력을 보거나 수정을 제안할 때 |

API 레퍼런스는 개발자 가이드의 API 명세 표로 만듭니다. 결제창 호출, 웹훅 수신, 앱 연동은 개발자 가이드에만 있습니다. 가이드의 각 API 제목 아래 "API 레퍼런스에서 보기" 링크를 누르면 같은 API의 레퍼런스로 이동합니다.

</div>

</div>
