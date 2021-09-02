<div align="right">
  <img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fnicepayments&count_bg=%233D7CC8&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://github.com/nicepayments">
</div>
<h3 align="center">
  🚀 나이스페이 개발자 가이드
</h3>

<!-- https://github.com/denvercoder1/readme-typing-svg -->
<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?lines=Hello!+Nicepay+%7Bdevelopers%7D&center=true&width=360&height=50">
</p>
                           
<br>





### 공통 
개발 전 필요한 `공통`적인 가이드 입니다.  
[개발 준비](common/preparations.md) | [API·JS SDK](common/api.md) | [TEST·샘플코드](common/test.md) | [코드집](common/code.md) | [더 알아보기](./common)
  
### 문서
`API 명세`와 `코드`가 포함된 기술문서 입니다.  
[결제·발급](api/payment.md) | [조회](api/status.md) | [거래·정산·대사](api/reconciliation.md) | [취소·환불·망취소](api/cancel.md) | [웹훅](api/hook.md) | [APP](api/app.md) | [더 알아보기](./api)

### 운영
`운영`에 필요한 정보 입니다.  
[지원환경](management/user.md) | [오류관리](/management/user.md#오류관리) | [개발정보](management/admin.md) | [더 알아보기](./management)

<br><br>

## ⚡ Quick guide

### 시작하기

빠른 개발을 위한 ⚡ Quick guide 입니다.  
가이드에 따라 순서대로 진행하면 ⏱️ 10분 정도의 시간으로 TEST개발이 가능 합니다.  

<br>

<b>📝 사전 준비 사항 </b>
- [회원가입](common/preparations.md#회원가입)
- [샌드박스 준비](common/test.md#샌드박스-준비)

> #### ⚠️ 중요
> 인터넷이 가능한 환경에서 Test 하는 것을 권장 합니다.  
> IP 제약이 있는 네트워크 환경에서 Test를 진행하는 경우 API호출을 위해 방화벽 작업이 필요할 수 있습니다.  
>  👉 [방화벽 정책 확인하기](common/preparations.md#방화벽-정책)

<br>

### Over-view
<img src="./image/payment-server-authorization.svg" width="800px">
  
### 설명
- 결제자가 브라우저에서 [JS SDK](/common/api.md#js-sdk-목록)의 Method인 `AUTHNICE.requestPay()` 를 통해 💡 결제창을 호출합니다.  
- 이후 결제자는 결제창에서 카드사 및 결제 원천사로 접근해 인증을 진행합니다.
- 나이스페이는 결제자의 인증결과를 `AUTHNICE.requestPay()`의 object value로 전달된 `returnUrl`로 POST 합니다.  
- 가맹점은 POST 데이터의 위변조 여부를 체크하고, 응답된 tid를 승인 API로 전달하면 💳 결제(승인)요청이 완료됩니다. 

<br>  
  
### JS Include
먼저 결제창 호출을 위해 JS SDK를 Include 해주세요.  
```javascript
<script src="https://pay.nicepay.co.kr/v1/js/"></script> //Server 승인
```

<br>

## 결제창 호출
JS SDK를 통해 결제창 Method 호출시 `clientId` 필드에 [클라이언트 키](common/api.md#클라이언트-키) 값을 셋팅 하면 준비가 완료 됩니다.  
이 후 `AUTHNICE.requestPay()` Method를 호출하면 결제창이 호출 됩니다.  

<b>JS SDK 인증 - Server 승인 모델</b>
```bash
javascript
```
```javascript
<script src="https://pay.nicepay.co.kr/v1/js/"></script> //Server 승인 
<script>
function serverAuth() {
  AUTHNICE.requestPay({
    clientId: ‘af0d116236df437f831483ee9c500bc4’,
    method: ‘card’,
    orderId: ‘193ee313-28d4-4af1-928c-e5f0e1f1bf88’,
    amount: 1004,
    goodsName: ‘나이스페이-상품’,
    returnUrl: ‘http://localhost:4567/serverAuth’
 });
}
</script>

serverAuth() //결제창 호출

```  

<b>결제창 응답</b>
```bash
POST
Content-type: application/x-www-form-urlencoded
```
```javascript
{
  authResultCode: '0000',
  authResultMsg: '인증 성공',
  tid: 'nicuntct1m0101210729113550A095',
  clientId: 'af0d116236df437f831483ee9c500bc4',
  orderId: '193ee313-28d4-4af1-928c-e5f0e1f1bf88',
  amount: '1004',
  mallReserved: 'null',
  authToken: 'NICEUNTTF6455CE3275BB65088CDB0E76D92313F',
  signature: 'e7d734896c7754aea648f8e7305b2a7501437469670908ef92749941040f384d'
}
```
`authResultCode`가 `0000` 으로 응답 되는 경우 결제창을 통한  인증과정이 성공한 것을 의미 합니다.  
인증과정이 성공한 경우 `tid(거래key)값`을 승인(결제) API로 전달하여 💳 결제(승인)을 요청 할 수 있습니다.  

<br>  

### 결제(승인) API 호출
```bash
curl -X POST 'https://api.nicepay.co.kr/v1/payments/nicuntct1m0101210729113550A095 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMTQ4M2VlOWM1MDBiYzQ6NDMzYTg0MjFiZTc1NGIzNDk4OTA0OGNmMTQ4YTVmZmM=' 
-D '{
  "amount" : 1004
}'
```
💡 결제창 인증 응답으로 전달된 tid를 `v1/payments/{tid}` API로 전달하면 결제(승인) 호출이 완료 됩니다.

### Authorization basic credentials 알고리즘
```bash
Base64(`client-key`:`secret-key`)
```
API 호출을 위해 `Authorization basic credentials` 생성은 클라이언트키 + : + 시크릿키 문자열을 `Base64` 인코딩하여 생성 합니다. 

```bash
clientKey = ‘af0d116236df437f831483ee9c500bc4’
secretKey = ‘433a8421be754b34989048cf148a5ffc’
>> `af0d116236df437f831483ee9c500bc4:433a8421be754b34989048cf148a5ffc`

Base64(‘af0d116236df437f831483ee9c500bc4:433a8421be754b34989048cf148a5ffc’)
>> `YWYwZDExNjIzNmRmNDM3ZjgzMTQ4M2VlOWM1MDBiYzQ6NDMzYTg0MjFiZTc1NGIzNDk4OTA0OGNmMTQ4YTVmZmM=`
```
예시처럼 최종 생성된 credentials을 API 호출 시 활용 합니다. 

### 결제(승인) 응답 예시
```bash
POST
Content-type: application/json
```
```json
{
  "resultCode": "0000",
  "resultMsg": "정상 처리되었습니다.",
  "tid": "nicuntct1m0101210729113550A095",
  "cancelledTid": null,
  "orderId": "193ee313-28d4-4af1-928c-e5f0e1f1bf88",
  "ediDate": "2021-07-29T12:01:51.205+0900",
  "signature": "68bd99a53d1d19e3ff7aedef99fc2bead165aa905f9a9e8f63cdc4da9702828b",
  "status": "paid",
  "paidAt": "2021-07-29T12:01:50.000+0900",
  "failedAt": "0",
  "cancelledAt": "0",
  "payMethod": "card",
  "amount": 1004,
  "balanceAmt": 1004,
  "goodsName": "나이스페이-상품",
  "mallReserved": null,
  "useEscrow": false,
  "currency": "KRW",
  "channel": "pc",
  "approveNo": "12015016",
  "buyerName": null,
  "buyerTel": null,
  "buyerEmail": "test@abc.com",
  "receiptUrl": "https://npg.nicepay.co.kr/issue/issueLoader.do?type=0&innerWin=Y&TID=nicuntct1m0101210729113550A095",
  "mallUserId": null,
  "issuedCashReceipt": false,
  "coupon": null,
  "card": {
    "cardCode": "07",
    "cardName": "현대",
    "cardNum": "****6800****7607",
    "cardQuota": 0,
    "isInterestFree": false,
    "cardType": "credit",
    "canPartCancel": true,
    "acquCardCode": "07",
    "acquCardName": "현대"
  },
  "vbank": null,
  "cancels": null,
  "cashReceipts": null
}
```
  
  
## 더 알아보기
결제 개발을 위해 더 상세한 정보가 필요하다면📌 `공통` 탭의 정보를 활용하고,  
API 개발을 위한 각 인터페이스의 개발 명세가 필요하다면 📚 `문서` 탭의 자료를 확인 해주세요.  
개발이 완료되어 운영에 필요한 정보와 Tip은 ☸️ `운영` 탭의 정보를 통해 확인이 가능 합니다. 

### 📌 공통
개발 전 필요한 `공통`적인 가이드 입니다.  
- [개발 준비](/common/preparations.md) 👉 [회원가입](/common/preparations.md#회원가입) | [API KEY확인](/common/preparations.md#api-key-확인) | [방화벽 정책](common/preparations.md#방화벽-정책) | [IP 보안기능](/common/preparations.md#ip-보안-기능) | [타임아웃 정보](/common/preparations.md#타임아웃-정보)
- [API·JS SDK](/common/api.md) 👉 [URI 목록](/common/api.md#uri-목록) | [JS SDK목록](/common/api.md#js-sdk-목록) | [API KEY](/common/api.md#api-key) | [API·JS SDK인증](/common/api.md#apijs-sdk인증) | [Basic auth](/common/api.md#basic-auth) | [Bearer token](/common/api.md#bearer-token)
- [TEST·샘플코드](/common/test.md) 👉 [샌드박스 TEST](/common/test.md#샌드박스test) | [샌드박스 활용](/common/test.md#샌드박스-활용) | [웹로그 디버깅](/common/test.md#웹로그-디버깅) | [샘플코드](/common/test.md#샘플코드)
- [코드집](/common/code.md) 👉 [HTTP-상태코드](/common/code.md#http-상태코드) | [카드코드](/common/code.md#카드코드) | [은행코드](/common/code.md#은행코드) | [JS SDK 응답코드](/common/code.md#js-sdk-응답코드) | [API 응답코드](/common/code.md#api-응답코드)
  
### 📚 문서
`API 명세`와 `코드`가 포함된 기술문서 입니다.  
- [결제·발급](/api/payment.md#) 👉 [결제창](/api/payment-window-server.md) | [빌링](/api/payment-subscribe.md) | [현금영수증](/api/payment-receipt.md) | [Access token](/api/payment-access-token.md)
- [조회](/api/status.md) 👉 [거래 조회](/api/status-transaction.md) | [약관 조회](/api/status-terms.md) | [카드 이벤트 조회](/api/status-event.md) | [카드 무이자 조회](/api/status-interest.md)
- [거래·정산·대사](/api/reconciliation.md) 👉 [거래대사](/api/reconciliation.md#거래대사) | [정산대사](/api/reconciliation.md#정산대사) | [입금대사](/api/reconciliation.md#입금대사)
- [취소·환불·망취소](/api/cancel.md) 👉  [취소·환불](/api/cancel.md#취소환불) | [망 취소](/api/cancel.md#망취소)
- [웹훅](/api/hook.md) 👉 [웹훅](/api/hook.md#웹훅)
- [APP](/api/app.md) 👉 [iOS](/api/app-ios.md#ios) | [iOS Swift](/api/app-ios.md#ios-swift-웹뷰web-view개발-가이드) | [iOS Objective-c](/api/app-ios.md#ios-objective-c-웹뷰web-view개발-가이드) | [Android](/api/app-android.md#) | [Android java](/api/app-android.md#android-java-웹뷰web-view개발-가이드) | [Android kotlin](/api/app-android.md#android-kotlin-웹뷰web-view개발-가이드)

### ☸️ 운영
`운영`에 필요한 정보 입니다.  
- [지원환경](/management/user.md) 👉 [개발환경](/management/user.md#개발환경) | [지원 브라우저](/management/user.md#브라우저)
- [오류관리](/management/user.md#오류관리) 👉 [오류관리](/management/user.md#오류관리)
- [개발정보](/management/admin.md) 👉 [기능 요약](/management/admin.md#기능-요약) | [KEY 정보](/management/admin.md#key정보) | [ip보안(ip접근제한)](/management/admin.md#ip보안ip접근-제한) | [웹훅](/management/admin.md#웹훅) | [로그](/management/admin.md#로그)
