# TEST·샘플코드
<div align="left"> 
 <a href="https://github.com/nicepayments/nicepay-node">
  <img src="https://img.shields.io/badge/node.js-339933?style=for-the-badge&logo=node.js&logoColor=white">
 </a>
 <a href="https://github.com/nicepayments/nicepay-python">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
 </a>
 <a href="https://github.com/nicepayments/nicepay-ruby">
  <img src="https://img.shields.io/badge/ruby-CC342D?style=for-the-badge&logo=ruby&logoColor=white">
 </a> 
 <a href="https://github.com/nicepayments/nicepay-asp">
  <img src="https://img.shields.io/badge/asp-007396?style=for-the-badge&logo=&logoColor=white">
 </a>
 <a href="https://github.com/nicepayments/nicepay-java">
  <img src="https://img.shields.io/badge/java-F7DF1E?style=for-the-badge&logo=&logoColor=white">
 </a>  
 <a href="https://github.com/nicepayments/nicepay-php">
  <img src="https://img.shields.io/badge/php-777BB4?style=for-the-badge&logo=php&logoColor=white">
 </a>
 <a href="https://github.com/nicepayments/nicepay-dotnet">
  <img src="https://img.shields.io/badge/.net-512BD4?style=for-the-badge&logo=.net&logoColor=white">
 </a>  
</div>

[샌드박스 TEST](../common/test.md#샌드박스test) | [샌드박스 활용](../common/test.md#샌드박스-활용) | [웹로드 디버깅](../common/test.md#웹로그-디버깅) | [샘플코드](../common/test.md#샘플코드) | [더 알아보기](#더-알아보기)

<br>

## 샌드박스(TEST)
### 샌드박스 준비  
[회원가입](/common/preparations.md#회원가입)을 하면 하나의 샌드박스(🔧 TEST 상점)을 생성 할 수 있습니다.  

#### 샌드박스(테스트상점) 생성
- 회원가입 후 로그인 하면 `테스트 상점 개설하기` 버튼이 활성화 됩니다.
- 버튼 클릭 후 TEST상점 이름을 입력하면 준비가 완료 됩니다.

![image](https://user-images.githubusercontent.com/86043374/128303655-26060514-b86c-4b15-a58d-f6eded03fa08.png)   

#### 샌드박스(테스트상점) TEST
샌드박스(테스트상점)으로 이동 후 개발정보 탭으로 이동하면 개발에 필요한 🔑 키값 확인이 가능하며 즉시 개발을 진행 할 수 있습니다.  
![image](https://user-images.githubusercontent.com/86043374/128303979-6244f466-43f9-4473-a93e-c7cd97748564.png)    

<br>

### 샌드박스 활용
회원가입을 하게되면 하나의 샌드박스(TEST 상점)을 생성 할 수 있습니다.  
생성된 샌드박스 상점을 통해 신규 서비스의 TEST 및 개발을 즉시 진행 할 수 있습니다.  
또한 샌드박스 시스템은 개발과 TEST의 번거로움을 줄이기 위해 다양한 장점과 기능을 제공합니다.  

#### 샌드박스 장점
- 즉시 TEST 및 개발이 가능 합니다.
- 결제가 발생되지 않아 편하게 TEST가 가능 합니다.
- 웹 로그를 통해 API 요청/응답 디버깅이 편리 합니다.
- 운영 환경에 영향이 없는 TEST시스템을 구성 할 수 있습니다.
 
#### 샌드박스의 기능
- TEST 결제 및 API 호출 : 상점 전용 TEST계정
- [웹훅 TEST하기](/management/admin.md#test호출) : 원클릭 🔔 웹훅 TEST
- TEST 결과 리포팅 : 운영 시스템 전환 전 간략하게 TEST정보를 요약

   
> 샌드박스 키와 운영상점에서 제공되는 키는 다르며, 실제 운영상점의 결제를 원하는 경우 해당 상점 KEY로 반드시 변경 해주세요.  
> 샌드박스 상점의 API 응답 전문은 실제 결제의 응답이 아닙니다.   
> 운영상점의 KEY로 서비스를 오픈 하는 경우 반드시 실제 거래를 통한 TEST를 진행 해주세요.

<br>

### 샌드박스를 통한 TEST
샌드박스 활용을 위한 준비가 되었다면 다음과 같은 방식으로 TEST개발이 가능합니다.  

<br>

- 결제창 JS 호출방식을 선택 후 샌드박스 도메인으로 변경 해주세요. 

|모델| 설명                                                                                      |
|:---:|:----------------------------------------------------------------------------------------|
|Server 승인| Endpoint: https://pay.nicepay.co.kr/v1/js/ <br> 결제창 호출(인증)과 결제(승인) API호출이 독립적으로 분리된 모델  |
|Client 승인| Endpont: https://pay.nicepay.co.kr/v1/js/  <br> 결제창 호출(인증)후 결제(승인)이 자동으로 처리되는 모델        |

> #### ⚠️ 중요  
> 요청 파라미터는 운영/샌드박스 모두 동일 합니다.  

<br>

- API 호출시 제약사항을 체크하고, API Host는 샌드박스 도메인(sandbox-api.nicepay.co.kr)을 사용 합니다.

```bash
HTTP/1.1  
Host: sandbox-api.nicepay.co.kr 
Authorization: Basic <credentials> or Bearer <token>
Content-type: application/json;charset=utf-8
```

| API                                                       | 샌드박스 지원여부 | Method | Endpoint                     | 제약사항    |
|:----------------------------------------------------------|:---------:|:------:|:-----------------------------|:--------|
| [AccessToken 발급](/api/payment-access-token.md)            |     ○     | `POST` | /v1/access-token             |         |
| [결제창 승인](/api/payment-window-server.md#승인)                |     ○     | `POST` | /v1/payments/{tid}           | 임의 값 응답 |
| [취소 요청](/api/cancel.md#취소환불망취소)                           |     △     | `POST` | /v1/payments/{tid}/cancel    | 부분취소 불가 |
| [거래조회-tid](/api/status-transaction.md#거래조회tid-활용)         |     ○     | `GET`  | /v1/payments/{tid}           |         |
| [거래조회-orderId](/api/status-transaction.md#거래조회orderid-활용) |     ○     | `GET`  | /v1/payments/find/{orderId}  |         |
| [빌키발급](/api/payment-subscribe.md#빌키발급)                    |     ○     | `POST` | /v1/subscribe/regist         | 임의 값 응답 |
| [빌키승인](/api/payment-subscribe.md#빌키승인)                    |     ○     | `POST` | /v1/subscribe/{bid}/payments | 임의 값 응답 | 
| [빌키삭제](/api/payment-subscribe.md#빌키삭제)                    |     ○     | `POST` | /v1/subscribe/{bid}/expire   |         |
| [약관조회](/api/status-terms.md#약관-조회)                        |     ×     | `GET`  | /v1/terms                    |         |
| [N정통Epay승인](/api/payment-epay.md#epay)                    |     ×     | `POST` | /v1/epay                     |         |
| [현금영수증 발급](/api/payment-receipt.md#현금영수증-발급)              |     ○     | `POST` | /v1/receipt/                 |         |
| [현금영수증 취소](/api/payment-receipt.md#현금영수증-취소)              |     ×     | `POST` | /v1/receipt/{tid}/cancel     |         |
| [현금영수증 거래조회](/api/payment-receipt.md#현금영수증-조회)            |     ○     | `GET`  | /v1/receipt/{tid}            |         | 
| [카드 이벤트 조회](/api/status-event.md#카드-이벤트)                  |     ×     | `GET`  | /v1/card/event               |         |
| [카드 무이자정보 조회](/api/status-interest.md#카드-무이자-조회)          |     ×     | `GET`  | /v1/card/interest-free       |         |
| [승인금액검증](/api/payment-window-client.md#승인-금액-검증)          |     ○     | `POST` | /v1/check-amount/{tid}       |         |


<br>

### 샌드박스를 통한 TEST 개발 예시
- `Server 승인` / `Basic` 인증 기준으로 결제창 TEST 개발흐름 예시를 설명 합니다.

#### JS Include
- 결제창 호출을 위한 JS SDK를 sandbox 도메인으로 변경합니다.
- clientId는 가맹점관리자 TEST상점에서 발급한 `클라이언트키`를 사용 합니다.

```bash
javascript
```
```html
<script src="https://pay.nicepay.co.kr/v1/js/"></script>

<script>
function serverAuth() {
  AUTHNICE.requestPay({
    clientId: '58e3b578555e45738d6b569e53d5ae54',
    method: 'card',
    orderId: random(),
    amount: 1004,
    goodsName: '나이스페이-상품',
    returnUrl: 'http://localhost:3000/serverAuth',
    fnError: function (result) {
      alert('고객용메시지 : ' + result.msg + '\n개발자확인용 : ' + result.errorMsg + '')
    }
  });
}

//Test orderId 생성
const random = (length = 8) => {
  return Math.random().toString(16).substr(2, length);
};	
</script>
  
<button onclick="serverAuth()">serverAuth 결제하기</button>

```  

> #### ⚠️ 중요  
> 샌드박스를 통한 TEST가 완료되면 운영계 도메인으로 변경 해주세요.

<br>  

<b>결제창 응답</b>
- 카드사 인증을 성공하면 authResultCode가 `0000`으로 응답 됩니다.

```bash
POST
Content-type: application/x-www-form-urlencoded
```
```bash
{
  authResultCode: '0000',
  authResultMsg: '인증 성공',
  tid: 'UT0000113m01012110051656331001',
  clientId: '58e3b578555e45738d6b569e53d5ae54',
  orderId: 'b0980639-52db-4504-9e4d-97200827dc48',
  amount: '1004',
  mallReserved: '',
  authToken: 'NICEUNTT9FBBD87FD2393AFEE45A7DCA61C194AA',
  signature: '7cc95c592e2a12f0292e1a20d68dd9eb8132fd3c0af675b981a4c1c2ce63a93b'
}
```
`authResultCode`가 `0000` 으로 응답된 경우 결제창을 통한 인증과정이 성공된 것을 의미합니다.  
인증과정이 성공한 경우 `tid(거래key)값`을 승인(결제) API로 전달하여 💳 결제(승인)을 요청 할 수 있습니다.  

<br>  

#### 결제(승인) API 호출
```bash
curl -X POST 'https://sandbox-api.nicepay.co.kr/v1/payments/UT0000113m01012110051656331001'
-H 'Content-Type: application/json' 
-H 'Authorization: Basic NThlM2I1Nzg1NTVlNDU3MzhkNmI1NjllNTNkNWFlNTQ6NGYxM2NhMjY3ZGZhNGZjNjk2NDE0OGJlZGNkYTE1ZWY=' 
-D '{
  "amount" : 1004
}'
```

> #### ⚠️ 중요  
> 샌드박스를 통한 TEST가 완료되면 운영계 도메인으로 변경 해주세요.

<br>

#### 결제(승인) 응답 예시
승인 API호출에 성공하면 실제 결제가 발생하지 않고, 임의 값이 응답됩니다.  
resultCode가 `0000`으로 응답되면 TEST성공 입니다.

```bash
POST
Content-type: application/json
```
```bash
{
  resultCode: '0000',
  resultMsg: '정상 처리되었습니다.',
  tid: 'UT0000113m01012110051656331001',
  cancelledTid: null,
  orderId: 'b0980639-52db-4504-9e4d-97200827dc48',
  ediDate: '2021-10-05T16:56:34.447+0900',
  signature: '28c2e8bae912847541d4885db17648f963c7cc8e8249ff010097d6f1395df993',
  status: 'paid',
  paidAt: '2021-10-05T16:56:34.000+0900',
  failedAt: '0',
  cancelledAt: '0',
  payMethod: 'card',
  amount: 1004,
  balanceAmt: 1004,
  goodsName: '나이스페이-상품',
  mallReserved: null,
  useEscrow: false,
  currency: 'KRW',
  channel: 'pc',
  approveNo: '000000',
  buyerName: null,
  buyerTel: null,
  buyerEmail: null,
  receiptUrl: 'https://npg.nicepay.co.kr/issue/IssueLoader.do?type=0&innerWin=Y&TID=UT0000113m01012110051656331001',
  mallUserId: null,
  issuedCashReceipt: false,
  coupon: null,
  card: {
    cardCode: '04',
    cardName: '삼성', // (샌드박스) 응답 결과는 삼성카드로 고정 
    cardNum: '12341234****1234',
    cardQuota: 0,
    isInterestFree: false,
    cardType: 'credit',
    canPartCancel: true,
    acquCardCode: '04',
    acquCardName: '삼성'
  },
  vbank: null,
  cancels: null,
  cashReceipts: null
}
```

> #### ⚠️ 중요  
> 실제 거래와 무관한 값이 응답되기 때문에 주의 합니다.  

<br>

### 웹로그 디버깅
간편한 디버깅을 위해 호출된 API 요청/응답 정보 💿 로그는 웹을 통해 확인이 가능합니다.  
로그는 단순한 호출 기록과, 상세기록을 나누어 확인 할 수 있습니다.  
API요청이 실패하는 경우 상세로그를 확인하여 쉽게 디버깅 해보세요.  

#### 단순 로그 확인
![image](https://user-images.githubusercontent.com/86043374/128304508-9be97076-2fec-474b-85d9-bcfc30b8045d.png)  
개발정보 -> 로그

- API 호출에 대한 성공 / 실패 정보의 빠른 확인이 가능합니다.
- API Target 요약 정보 확인이 편리 합니다.
- 주문번호 확인을 통해 이슈 거래 건 체크가 가능 합니다.

  
#### 상세 로그 확인
![image](https://user-images.githubusercontent.com/86043374/128304865-b0ba8f4a-adf7-45e7-b78a-53b0e01106fc.png)  

- 로그를 확인 중 상세한 정보 확인이 필요한 경우 해당 로그를 클릭하면 상세한 정보 확인이 가능합니다.
- 이슈 체크를 위해 로그 검토가 필요한 경우 '상세보기' 버튼을 클릭하면 상세 로그 화면으로 이동 합니다.
- 로그 상세보기를 통해 디버깅에 필요한 상세 정보를 확인 할 수 있습니다.
  
#### 개발정보
- [개발정보 활용](/management/admin.md#활용)
- [로그-기능설명](/management/admin.md#기능설명-3)
- [로그-상세보기](/management/admin.md#상세보기)

<br>

## 샘플코드	
나이스페이는 개발편의를 위해 다양한 언어의 샘플코드를 제공하고 있습니다.  

### 지원되는 언어
<div align="left"> 
 <a href="https://github.com/nicepayments/nicepay-node">
  <img src="https://img.shields.io/badge/node.js-339933?style=for-the-badge&logo=node.js&logoColor=white">
 </a>
 <a href="https://github.com/nicepayments/nicepay-python">
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
 </a>
 <a href="https://github.com/nicepayments/nicepay-ruby">
  <img src="https://img.shields.io/badge/ruby-CC342D?style=for-the-badge&logo=ruby&logoColor=white">
 </a> 
 <a href="https://github.com/nicepayments/nicepay-asp">
  <img src="https://img.shields.io/badge/asp-007396?style=for-the-badge&logo=&logoColor=white">
 </a>
 <a href="https://github.com/nicepayments/nicepay-java">
  <img src="https://img.shields.io/badge/java-F7DF1E?style=for-the-badge&logo=&logoColor=white">
 </a>  
 <a href="https://github.com/nicepayments/nicepay-php">
  <img src="https://img.shields.io/badge/php-777BB4?style=for-the-badge&logo=php&logoColor=white">
 </a>
 <a href="https://github.com/nicepayments/nicepay-dotnet">
  <img src="https://img.shields.io/badge/.net-512BD4?style=for-the-badge&logo=.net&logoColor=white">
 </a>  
</div>

<br>

    
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
- [취소·환불·망취소](/api/cancel.md) 👉  [취소·환불](/api/cancel.md#취소환불) | [망 취소](/api/cancel.md#망취소)
- [웹훅](/api/hook.md) 👉 [웹훅](/api/hook.md#웹훅)
- [APP](/api/app.md) 👉 [iOS](/api/app-ios.md#ios) | [iOS Swift](/api/app-ios.md#ios-swift-웹뷰web-view개발-가이드) | [iOS Objective-c](/api/app-ios.md#ios-objective-c-웹뷰web-view개발-가이드) | [Android](/api/app-android.md#) | [Android java](/api/app-android.md#android-java-웹뷰web-view개발-가이드) | [Android kotlin](/api/app-android.md#android-kotlin-웹뷰web-view개발-가이드)

### ☸️ 운영
`운영`에 필요한 정보 입니다.  
- [지원환경](/management/user.md) 👉 [개발환경](/management/user.md#개발환경) | [지원 브라우저](/management/user.md#브라우저)
- [오류관리](/management/user.md#오류관리) 👉 [오류관리](/management/user.md#오류관리)
- [개발정보](/management/admin.md) 👉 [기능 요약](/management/admin.md#기능-요약) | [KEY 정보](/management/admin.md#key정보) | [ip보안(ip접근제한)](/management/admin.md#ip보안ip접근-제한) | [웹훅](/management/admin.md#웹훅) | [로그](/management/admin.md#로그)
