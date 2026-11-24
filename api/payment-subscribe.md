# 빌링

[빌링 결제창 호출](#빌링-결제창-호출) | [빌키확정](#빌키확정) | [빌키승인](#빌키승인) | [빌키삭제](#빌키삭제) | [더 알아보기](#더-알아보기)

<br>

## 빌링 결제창 호출
### Over-view
<img src="../image/payment-subscribe-window.svg" width="800px">  

### 설명
빌링 서비스는 정기결제(한번의 결제수단 등록으로 반복적인 결제)를 구현할 수 있는 서비스 입니다.  
빌링 서비스는 [빌링 결제창 호출](#빌링-결제창-호출), [빌키확정](#빌키확정), [빌키승인](#빌키승인), [빌키삭제](#빌키삭제) 순서로 연동 합니다.  

- 가맹점은 결제창을 `isBill: "Y"`, `amount: 0`으로 호출 합니다.
- 결제자가 결제수단을 인증하면 나이스페이는 인증 결과를 `returnUrl`로 POST 합니다. 이 단계에서는 bid(빌키)가 발급되지 않습니다.
- 가맹점 서버는 응답된 tid로 [빌키확정](#빌키확정) API를 호출하고, 응답된 bid(빌키)를 저장 합니다.
- 결제자의 카드정보는 결제창에서만 입력되며, 가맹점은 카드정보를 받거나 저장하지 않습니다.

<br>

> #### ⚠️ 중요
> Server 승인 모델로 발급된 [클라이언트 키](../common/api.md#클라이언트-키)에서만 사용이 가능 합니다.  
> 빌링 결제창 인증이 성공해도 bid(빌키)는 발급되지 않습니다. 인증 후 **10분 안에** [빌키확정](#빌키확정) API를 호출해야 합니다.  
> 인증 결과의 tid로 [승인](./payment-window-server.md#승인) API(`/v1/payments/{tid}`)를 호출하면 `U158`로 거절 됩니다.

<br>

### 지원 결제수단

| method        | 결제수단            | mallUserId |
|:-------------:|:---------------:|:----------:|
| card          | 신용카드            | 선택         |
| kakaopay      | 카카오페이           | 필수         |
| naverpayCard  | 네이버페이-신용카드      | 필수         |
| naverpayPoint | 네이버페이-포인트       | 필수         |
| tosspay       | 토스페이            | 필수         |

<br>

### 샘플 코드 (빌링 결제창 호출)

```html
<script src="https://pay.nicepay.co.kr/v1/js/"></script>
<script>
function billing() {
  AUTHNICE.requestPay({
    clientId: 'R2_xxxxxxxxxxxxxxxx',
    method: 'card',
    isBill: 'Y',
    amount: 0,
    orderId: 'your-unique-orderid',
    goodsName: '정기구독',
    mallUserId: 'user-1234',
    returnUrl: 'https://your.site.com/billing/return',
    fnError: function (result) {
      alert('개발자확인용 : ' + result.errorMsg + '')
    }
  });
}
</script>
```

<br>

### 빌링 결제창 요청 명세
[결제창 요청 명세](./payment-window-server.md#공통)와 같고, 아래 항목의 값이 다릅니다.

| Parameter  | Type    | 필수 | Byte | 설명 |
|:----------:|:-------:|:----:|:----:|:-----|
| isBill     | String  | O    | 1    | 빌링 결제창 호출 여부<br>Y : 빌링 결제창<br>- 일반결제에서는 보내지 않습니다. |
| amount     | Integer | O    | 12   | 결제금액<br>빌링 결제창은 `0`만 허용 합니다. |
| method     | String  | O    | 20   | 결제수단<br>[지원 결제수단](#지원-결제수단)만 허용 합니다. |
| orderId    | String  | O    | 64   | 가맹점에서 관리하는 Unique한 주문번호<br>요청마다 새 orderId를 보냅니다.<br>- 이미 쓴 orderId는 다시 쓰지 않습니다. |
| mallUserId | String  | △    | 20   | 상점에서 관리하는 사용자 아이디<br>카카오페이, 네이버페이, 토스페이는 필수 |

<br>

### 빌링 결제창 응답 명세
[결제창 응답 명세](./payment-window-server.md#응답-명세-server-승인-모델)와 같고, 아래 항목이 추가 됩니다.

| Parameter | Type   | 필수   | Byte | 설명 |
|:---------:|:------:|:------:|:----:|:-----|
| isBill    | String | 성공시 | 1    | Y : 빌링 결제창 인증 결과<br>- 인증에 성공한 경우(authResultCode=0000)에만 리턴됩니다. |

<br>

> #### ⚠️ 중요
> `returnUrl`로 응답된 `amount`(0), `orderId`, `signature`가 가맹점이 생성한 결제정보와 일치하는지 체크 후 [빌키확정](#빌키확정) API를 호출 해주세요.

<br>

## 빌키확정

### 빌키확정 설명
- 빌키확정은 빌링 결제창 인증 결과의 tid로 bid(빌키)를 발급받는 과정 입니다.
- `returnUrl`로 응답된 tid로 `/v1/subscribe/{tid}/issue` API를 호출하면 bid(빌키)가 응답 됩니다.
- 인증 후 10분이 지나면 `U157`이 응답 됩니다. 이 경우 [빌링 결제창 호출](#빌링-결제창-호출)부터 다시 진행 해주세요.

<br>

### 샘플 코드 (빌키확정)

```bash
curl -X POST 'https://api.nicepay.co.kr/v1/subscribe/{tid}/issue' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic ZWVjOGQzNTA4Y2IwNDI1ZGI5NTViMzBi...' 
-D '{
	"amount": 0
	,"ediDate": "2026-11-21T10:00:00.000+09:00"
	,"signData": "{위변조 검증 Data}"
}'
```

<br>

### 빌키확정 요청 명세
```bash
POST /v1/subscribe/{tid}/issue HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials> or Bearer <token>
Content-type: application/json;charset=utf-8
```
| Parameter     | Type    | 필수 | Byte | 설명 |
|:-------------:|:-------:|:----:|:----:|:-----|
| amount        | Integer | O    | 12   | 결제금액<br>`0`만 허용 합니다. |
| ediDate       | String  | O    | -    | 전문생성일시<br>ISO 8601 형식 |
| signData      | String  | O    | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(tid + amount + ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다. |
| returnCharSet | String  |      | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>utf-8(Default) / euc-kr |

- 경로의 `{tid}`는 빌링 결제창 `returnUrl`로 응답된 tid 입니다.

<br>

### 빌키확정 응답 명세
```bash
Content-type: application/json
```
| Parameter     | Type   | 필수 | Byte | 설명 |
|:-------------:|:------:|:----:|:----:|:-----|
| resultCode    | String | O    | 4    | 결과코드<br>0000 : 성공 / 그외 실패 |
| resultMsg     | String | O    | 100  | 결과메시지 |
| tid           | String | O    | 30   | 거래번호 |
| orderId       | String | O    | 64   | 상점 거래 고유번호 |
| bid           | String |      | 30   | 빌키<br>[빌키승인](#빌키승인), [빌키삭제](#빌키삭제) API 호출시 전달<br>- 성공시에만 리턴됩니다. |
| authDate      | String |      | -    | 인증일자 |
| cardCode      | String |      | 3    | 카드사 코드 |
| cardName      | String |      | 20   | 카드사 이름 |
| mallUserId    | String |      | 20   | 상점에서 관리하는 사용자 아이디 |
| status        | String | O    | 10   | 빌키확정 결과<br>issued : 발급 / failed : 실패 |
| messageSource | String | O    | 10   | 결과 출처<br>nicepay / external |

<br>

> #### ⚠️ 중요
> 성공 여부는 HTTP 상태가 아니라 `resultCode`로 판정 합니다.  
> bid(빌키)는 가맹점 서버에 안전하게 저장하고, 브라우저로 전달하지 않습니다.

<br>

### 빌키확정 예외처리
- 빌키확정 API 호출시 read-timeout이 발생한다면 같은 tid로 빌키확정 API를 다시 호출 해주세요.
- 이미 발급된 tid로 다시 호출하면 처음 빌키확정 응답과 같은 응답을 받습니다.
- 같은 tid의 빌키확정이 처리 중이면 `U156`이 응답 됩니다. 잠시 뒤 같은 tid로 다시 호출 해주세요.

<br>

### 빌키확정 결과 조회
빌키확정 응답을 받지 못한 경우, 같은 tid의 빌키확정 결과를 조회 합니다. 결과 조회는 확정 상태를 바꾸지 않습니다.

```bash
GET /v1/subscribe/{tid}/issue HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials> or Bearer <token>
```
- 응답은 [빌키확정 응답 명세](#빌키확정-응답-명세)와 같습니다.
- 빌키확정 API를 호출하기 전이면 `U162`가 응답 됩니다.

<br>

### 빌키확정 응답코드

| resultCode | 설명 | 조치 |
|:----------:|:-----|:-----|
| 0000 | 정상 처리되었습니다. | bid를 저장 합니다. |
| U100 | {0} 필수입력항목이 누락되었습니다. | 요청 값을 확인 합니다. |
| U119 | 지원하지 않는 지불수단입니다. | 빌링 결제창 호출부터 다시 진행 합니다. |
| U120 | TID가 유효하지 않습니다. | returnUrl로 응답된 tid를 그대로 전달 합니다. |
| U121 | 인증 요청내역이 존재하지 않습니다. | 인증한 clientId로 호출 합니다. (HTTP 404) |
| U155 | 2TR 빌링 인증 결과가 아닙니다. | 빌링 결제창(`isBill: "Y"`)의 tid만 전달 합니다. |
| U156 | 빌키 발급을 처리하고 있습니다. 잠시 뒤 다시 요청해 주세요. | 잠시 뒤 같은 tid로 다시 호출 합니다. |
| U157 | 인증 뒤 빌키 발급 유효시간이 지났습니다. | 빌링 결제창 호출부터 다시 진행 합니다. |
| U159 | 빌키 발급 결과를 저장하지 못해 발급에 실패했습니다. | 빌링 결제창 호출부터 다시 진행 합니다. |
| U162 | 빌키 발급을 요청하기 전입니다. | (결과 조회) 빌키확정 API를 호출 합니다. |
| U163 | 빌키 발급 결과를 확인할 수 없습니다. | 나이스페이에 문의 합니다. |
| U312 | SIGN DATA 검증에 실패하였습니다. | signData 생성규칙을 확인 합니다. |
| U502 | 요청 금액이 올바르지 않습니다. | amount를 0으로 전달 합니다. |
| 9999 | 일시적인 오류가 발생하였습니다. | 같은 tid로 다시 호출해 `status`를 확인 합니다. |

- 표에 없는 `resultCode`가 올 수 있습니다(결제수단사 응답 코드 등). `status`가 `failed`이면 빌키확정이 실패한 것이므로 빌링 결제창 호출부터 다시 진행 합니다.

<br>

## 빌키승인
### Over-view
<img src="../image/payment-subscribe-billing.svg" width="800px">  

### 설명
- 빌키 승인은 발급된 bid(빌키)를 통해 💳 결제(승인) 처리를 의미 합니다. 
- 등록된 빌키를 통해 `/v1/subscribe/{bid}/payments` API를 호출하면 💳 결제(승인) 처리가 됩니다.
- 빌키 승인을 위해 [빌키확정](#빌키확정)과정의 선행이 필요 합니다.

<br>

### 샘플 코드
```bash
curl -X POST 'https://api.nicepay.co.kr/v1/subscribe/{bid}/payments' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic ZWVjOGQzNTA4Y2IwNDI1ZGI5NTViMzBi...' 
-D '{
	"orderId":"{상점 거래 고유번호}"
	,"amount":500
	,"goodsName":"테스트 상품"
	,"cardQuota":0
	,"useShopInterest":false
}'
```

<br>

### 요청 명세 (Body)

```bash
POST /v1/subscribe/{bid}/payments  
HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials> or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter       | Type    | 필수 | Byte | 설명                                                             |
|-----------------|---------|------|------|------------------------------------------------------------------|
| orderId         | String  | O    | 64   | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br>결제된 orderId로   재호출 불가            |
| amount          | Integer | O    | 12   | 결제 금액                                                        |
| goodsName       | String  | O    | 40   | 상품명                                                           |
| cardQuota       | String  | O    | 2    | 할부개월<br> 0:일시불, 2:2개월, 3:3개월   …                                   |
| useShopInterest | Boolean | O    | -    | 상점분담무이자 사용여부 (현재 false만 사용 가능)<br>false : 유이자                                                   |
| buyerName       | String  | 　   | 30   | 구매자 이름                                                      |
| buyerTel        | String  | 　   | 20   | 구매자 전화번호<br>하이픈(-) 없이 숫자만   입력                                     |
| buyerEmail      | String  | 　   | 60   | 구매자 이메일                                                    |
| taxFreeAmt      | Integer | 　   | 12   | 면세공급가액<br>전체 거래금액(amount)중에서   면세에 해당하는 금액을 설정합니다. |
| mallReserved    | String  | 　   | 500  | 상점 정보 전달용 예비필드<br><br>승인응답 또는 webhook 시점에 요청 원문을 전달 합니다.<br> JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                       |
| ediDate         | String  | 　   | -    | 전문생성일시<br>ISO 8601 형식                                                    |
| signData        | String  | 　   | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(orderId + bid +   ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.        |
| returnCharSet   | String  | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                    |

<br>

### 응답 명세 (Body)
```bash
Content-type: application/json

{
    "resultCode":"0000"
    ,"resultMsg":"정상 처리되었습니다."
    ,"tid":"{빌키 승인 거래번호 }"
    ,"orderId":"{상점 거래 고유번호}"
    ,"ediDate":"2023-02-14T18:41:26.100+0900"
    ,"status":"paid"
    ,"paidAt":"2023-02-14T18:41:25.000+0900"
    ,"failedAt":"0"
    ,"cancelledAt":"0"
    ,"payMethod":"card"
    ,"amount":500
    ,"balanceAmt":500
    ,"goodsName":"테스트 상품"
    ,"useEscrow":false
    ,"currency":"KRW"
    ,"receiptUrl":"{매출전표 확인 URL}"
    ,"issuedCashReceipt":false
    ,"card":{
        "cardCode":"06"
        ,"cardName":"신한"
        ,"cardNum":"{카드번호}"
        ,"cardQuota":0
        ,"isInterestFree":false
        ,"cardType":"credit"
        ,"canPartCancel":true
        ,"acquCardCode":"06"
        ,"acquCardName":"신한"
    }
}

```
| Parameter         | Type    | 필수 | Byte | 설명                                                                                                           |
|-------------------|---------|------|------|----------------------------------------------------------------------------------------------------------------|
| resultCode        | String  | O    | 4    | 결제결과코드<br> 0000 : 성공 / 그외 실패                                                                                        |
| resultMsg         | String  | O    | 100  | 결제결과메시지                                                                                                 |
| tid               | String  | O    | 30   | 결제 승인 키<br>최초 승인(가상계좌-채번)에 성공한 원거래의 NICEPAY 거래키 입니다.                                              |
| cancelledTid      | String  | 　   | 30   | 취소 거래 키<br>NICEPAY가 발행하는 취소 응답 TID (부분취소시 tid와 다른 값이 응답됨)<br>- 취소   요청건에 한하여 응답됨<br>- cancels 객체에서 현재 취소된 거래정보를 찾을 때 사용 하시면 됩니다.                                         |
| orderId           | String  | O    | 64   | 상점 거래 고유번호                                                                                             |
| ediDate           | String  | O    | -    | 응답전문생성일시 ISO 8601 형식                                                                                 |
| signature         | String  | 　   | 256  | 위변조 검증 데이터<br>- 유효한 거래건에   한하여 응답<br>- 생성규칙 :   hex(sha256(tid + amount + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.                                                      |
| status            | String  | O    | 20   | 결제 처리상태<br>paid:결제완료,   ready:준비됨, failed:결제실패, cancelled:취소됨, partialCancelled:부분 취소됨, expired:만료됨<br>['paid', 'ready', 'failed', 'cancelled', 'partialCancelled',   'expired']                                      |
| paidAt            | String  | O    | -    | 결제완료시점 ISO 8601 형식<br>결제완료가 아닐 경우 0    |
| failedAt          | String  | O    | -    | 결제실패시점 ISO 8601 형식<br>결제실패가 아닐 경우 0                                                       |
| cancelledAt       | String  | O    | -    | 결제취소시점 ISO 8601 형식결제취소가 아닐 경우 0 <br>부분취소인경우, 가장   마지막건의 취소 시간                   |
| payMethod         | String  | O    | 10   | 결제수단<br><br>card:신용카드,<br>vbank:가상계좌,<br>bank:계좌이체,<br>cellphone:휴대폰,<br>naverpay=네이버페이, kakaopay=카카오페이, samsungpay=삼성페이                   |
| amount            | Integer     | O    | 12   | 결제 금액                                                                                                      |
| balanceAmt        | Integer     | O    | 12   | 취소 가능 잔액<br>부분취소 거래인경우, 전체금액에서   현재까지 취소된 금액을 차감한 금액.                                        |
| goodsName         | String  | O    | 40   | 상품명                                                                                                         |
| mallReserved      | String  | 　   | 500  | 상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                                     |
| useEscrow         | Boolean | O    | -    | 에스크로 거래 여부<br>false:일반거래 /   true:에스크로 거래                                                                          |
| currency          | String  | O    | 3    | 결제승인화폐단위<br>KRW:원화, USD:미화달러, CNY:위안화                                                                             |
| channel           | String  | 　   | 10   | pc:PC결제, mobile:모바일결제<br>['pc', 'mobile', 'null']                                                                                       |
| approveNo         | String  | 　   | 30   | 제휴사 승인 번호<br>신용카드, 계좌이체, 휴대폰                                                                                     |
| buyerName         | String  | 　   | 30   | 구매자 명                                                                                                      |
| buyerTel          | String  | 　   | 20   | 구매자 전화번호                                                                                                |
| buyerEmail        | String  | 　   | 60   | 구매자 이메일                                                                                                  |
| issuedCashReceipt | Boolean | 　   | -    | 현금영수증 발급여부<br>true:발행 /   false:미발행                                                                                     |
| receiptUrl        | String  | 　   | 200  | 매출전표 확인 URL                                                                                            |
| mallUserId        | String  | 　   | 20   | 상점에서 관리하는 사용자 아이디                                                                                |

<br>

### 할인정보 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |           | Type   | 필수 | 　Byte | 설명                   |
|-----------|-----------|--------|------|--------|------------------------|
| coupon    | 　        | Object | 　   | -      | 즉시할인 프로모션 정보 |
| 　        | couponAmt | Integer    | 　   | 12     | 즉시할인 적용된 금액   |

<br>

### 카드 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">


| Parameter |                | Type    | 필수 | 　Byte | 설명                                                                                                      |
|-----------|----------------|---------|----|-------|---------------------------------------------------------------------------------------------------------|
| card      | 　              | Object  | 　  | 　     | 신용카드 정보                                                                                                 |
| 　         | cardCode       | String  | O  | 3     | 신용카드사별 코드                                                                                               |
|           | cardName       | String  | O  | 20    | 결제 카드사 이름<br>예) 비씨                                                                                      |
|           | cardNum        | String  | 　  | 20    | 카드번호<br>앞 6자 마지막 4자를 제외한 가운데 숫자 마스킹 처리됨<br>예) 536112******1234<br>- 카카오머니/네이버포인트/페이코포인트 전액결제 거래인경우 null |
|           | cardQuota      | String  | O  | 3     | 할부개월<br>0:일시불, 2:2개월, 3:3개월   …                                                                         |
|           | isInterestFree | Boolean | O  | -     | 상점분담무이자 여부<br>true:무이자,   false:일반                                                                      |
|           | cardType       | String  | 　  | 1     | 카드 구분<br>credit:신용,   check:체크                                                                          |
|           | canPartCancel  | String  | O  | -     | 부분취소 가능 여부<br>true:가능,   false:불가능                                                                      |
|           | acquCardCode   | String  | O  | 3     | 매입카드사코드                                                                                                 |
|           | acquCardName   | String  | O  | 100   | 매입카드사명                                                                                                  |

<br>

## 빌키삭제
### Over-view
<img src="../image/payment-subscribe-expire.svg" width="800px">  

### 설명
빌키 삭제는 발급된 bid(빌키)를 삭제는 과정을 의미 합니다.  
등록된 빌키를  통해 `/v1/subscribe/{bid}/expire` API를 호출하면 빌키 삭제 처리가 됩니다.  
삭제된 빌키는 복원과 💳 승인(결제)가 불가 합니다.  

<br>

### 샘플 코드
``` bash
curl -X POST 'https://api.nicepay.co.kr/v1/subscribe/{bid}/expire' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic ZWVjOGQzNTA4Y2IwNDI1ZGI5NTViMzBiZjM...' 
-D '{
    "orderId": "{상점 거래 고유번호}"
}'
```

<br>

### 요청 명세 (Body)
```bash
POST /v1/subscribe/{bid}/expire   
HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials> or Bearer <token>
Content-type: application/json;charset=utf-8
```
| Parameter     | Type   | 필수 | Byte | 설명                                                          |
|---------------|--------|------|------|---------------------------------------------------------------|
| orderId       | String | O    | 64   | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호           |
| ediDate       | String | 　   | -    | 전문생성일시<br> ISO 8601 형식                                                 |
| signData      | String | 　   | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(orderId + bid +   ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.     |
| returnCharSet | String | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                 |	

<br>

### 응답 명세 (Body)
```bash
Accept: application/json

{
    "resultCode":"0000"
    ,"resultMsg":"정상 처리되었습니다."
    ,"tid":"{거래번호}"
    ,"orderId":"{상점 거래 고유번호}"
    ,"bid":"{삭제처리된 빌키}"
    ,"authDate":"2023-02-14T18:43:41.712+0900"
}

```
| Parameter  | TYPE   | 필수 | 크기 | 설명                                    |
|------------|--------|------|------|-----------------------------------------|
| resultCode | String | O    | 4    | 결제결과코드<br>0000 : 성공 / 그외 실패                 |
| resultMsg  | String | O    | 100  | 결제결과메시지<br>예시) 빌키가 정상적으로 생성되었습니다. |
| tid        | String | O    | 30   | 거래를 구분하는 transaction ID<br>예시) nictest00m01011104191651325596    |
| orderId    | String | O    | 64   | 상점 거래 고유번호                           |
| bid        | String | O    | 30   | 빌키<br>NICEPAY가 발급한 빌링 아이디            |
| authDate   | String | 　   | -    | ISO 8601 형식<br>처리에 성공한경우 리턴됩니다.           |


<br>

    
## 더 알아보기
결제 개발을 위해 더 상세한 정보가 필요하다면📌 `공통` 탭의 정보를 활용하고,  
API 개발을 위한 각 인터페이스의 개발 명세가 필요하다면 📚 `문서` 탭의 자료를 확인 해주세요.  
개발이 완료되어 운영에 필요한 정보와 Tip은 ☸️ `운영` 탭의 정보를 통해 확인이 가능 합니다. 

### 📌 공통
개발 전 필요한 `공통`적인 가이드 입니다.  
- [개발 준비](../common/preparations.md) 👉 [회원가입](../common/preparations.md#회원가입) | [API KEY확인](../common/preparations.md#api-key-확인) | [방화벽 정책](../common/preparations.md#방화벽-정책) | [IP 보안기능](../common/preparations.md#ip-보안-기능) | [타임아웃 정보](../common/preparations.md#타임아웃-정보)
- [API·JS SDK](../common/api.md) 👉 [URI 목록](../common/api.md#uri-목록) | [JS SDK목록](../common/api.md#js-sdk-목록) | [API KEY](../common/api.md#api-key) | [API·JS SDK인증](../common/api.md#apijs-sdk인증) | [Basic auth](../common/api.md#basic-auth) | [Bearer token](../common/api.md#bearer-token)
- [TEST·샘플코드](../common/test.md) 👉 [샌드박스 TEST](../common/test.md#샌드박스test) | [샌드박스 활용](../common/test.md#샌드박스-활용) | [웹로그 디버깅](../common/test.md#웹로그-디버깅) | [샘플코드](../common/test.md#샘플코드)
- [코드집](../common/code.md) 👉 [HTTP-상태코드](../common/code.md#http-상태코드) | [카드코드](../common/code.md#카드코드) | [은행코드](../common/code.md#은행코드) | [JS SDK 응답코드](../common/code.md#js-sdk-응답코드) | [API 응답코드](../common/code.md#api-응답코드)
  
### 📚 문서
`API 명세`와 `코드`가 포함된 기술문서 입니다.  
- [결제·발급](payment.md) 👉 [결제창](payment-window-server.md) | [빌링](payment-subscribe.md) | [현금영수증](payment-receipt.md) | [Access token](payment-access-token.md)
- [조회](status.md) 👉 [거래 조회](status-transaction.md) | [약관 조회](status-terms.md) | [카드 이벤트 조회](status-event.md) | [카드 무이자 조회](status-interest.md)
- [취소·환불·망취소](cancel.md) 👉  [취소·환불](cancel.md#취소환불) | [망 취소](cancel.md#망취소)
- [웹훅](hook.md) 👉 [웹훅](hook.md#웹훅)
- [APP](app.md) 👉 [iOS](app-ios.md#ios) | [iOS Swift](app-ios.md#ios-swift-웹뷰web-view개발-가이드) | [iOS Objective-c](app-ios.md#ios-objective-c-웹뷰web-view개발-가이드) | [Android](app-android.md) | [Android java](app-android.md#android-java-웹뷰web-view개발-가이드) | [Android kotlin](app-android.md#android-kotlin-웹뷰web-view개발-가이드)

### ☸️ 운영
`운영`에 필요한 정보 입니다.  
- [지원환경](../management/user.md) 👉 [개발환경](../management/user.md#개발환경) | [지원 브라우저](../management/user.md#브라우저)
- [오류관리](../management/user.md#오류관리) 👉 [오류관리](../management/user.md#오류관리)
- [개발정보](../management/admin.md) 👉 [기능 요약](../management/admin.md#기능-요약) | [KEY 정보](../management/admin.md#key정보) | [ip보안(ip접근제한)](../management/admin.md#ip보안ip접근-제한) | [웹훅](../management/admin.md#웹훅) | [로그](../management/admin.md#로그)
