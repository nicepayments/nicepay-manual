# 개발 준비

<br>

## 회원가입
회원가입을 하고 🔧 샌드박스를 활용하면 빠르게 개발 할 수 있어요.  
[회원가입 페이지](https://start.nicepay.co.kr/merchant/login/main.do)로 이동 후 무료로 회원가입을 해보세요.

## 개발정보

로그인 후 상점을 생성하면 개발에 필요한 정보를 `개발정보` 탭에서 확인 할 수 있습니다.  
개발정보의 기능을 통해 연동에 필요한 `KEY관리`, `IP보안`, `웹훅`과 `로그` 확인을 할 수 있습니다.

![image](https://user-images.githubusercontent.com/86043374/128664778-73f6915a-f131-44a5-98a6-b76eccf4ed2d.png)

## KEY 정보
개발정보 탭의 🔑 KEY 정보는 결제창 `승인 모델의 선택`과 `API 인증 방식`을 선택하여 KEY를 발급 및 삭제 할 수 있습니다.

![image](https://user-images.githubusercontent.com/86043374/128665135-7e576957-c6bc-4540-94b5-df99eef0a6e5.png)


### 클라이언트 키
클라이언트 키는 생성된 상점의 [개발정보](#개발정보) 탭에서 확인이 가능 합니다.  
생성된 클라이언트 키는 결제창을 호출 하거나 API인증을 위한 KEY값을 생성할 때 활용 됩니다.

### 클라이언트 키 Type
결제창 호출 방식에 따라 클라이언트 키는 2가지 Type중 선택하여 발급이 가능 합니다.
- Server 인증 : 결제창 요청(인증)과 결제(승인) API호출이 분리된 모델
- Client 인증  : 결제창 요청(인증)후 결제(승인)이 자동으로 처리되는 모델

### 시크릿 키
시크릿 키는 생성된 상점의 [개발정보](#개발정보) 탭에서 확인이 가능 합니다.  
생성된 시크릿 키는 API인증 키 생성에 활용 되며 API인증 방식에 따라 시크릿키 발급이 가능 합니다.

> #### ⚠️ 중요
> 샌드박스에서 제공되는 키와 운영상점에서 제공되는 키는 다릅니다.  
> 실제 운영상점의 결제를 원하는 경우 반드시 해당 상점 KEY로 변경 해주세요.   
> 운영상점의 시크릿 키가 외부에 노출되지 않도록 주의 해주세요.  
> 만약 노출된 경우 키를 변경하여 위험을 예방할 수 있습니다.  
> ( 로그인 > 개발정보 > 키 변경 )


### 재발급

개발정보 > KEY정보 > 재발급 버튼을 클릭하면 KEY 발급이 가능 합니다.  
최대 5개의 KEY생성이 가능하며 KEY를 변경하는 경우 TEST가 필요한 경우 생성하여 활용 할 수 있습니다.

![image](https://user-images.githubusercontent.com/86043374/128665322-0b1497a8-a56c-4eef-82a1-54ae39794142.png)

> #### ⚠️ 중요
> 시크릿키는 외부에 노출이 되지 않도록 주의가 필요하며 외부 유출시 반드시 KEY를 재발급하여 변경 해야 합니다.  
> 클라이언트 키와 시크릿 키가 삭제되는 경우 복구되지 않으며 삭제된 키를 통해 결제가 발생되지 않아 변경 작업 시 주의가 필요 합니다.


## 방화벽 정책
원활한 통신을 위해 서버의 HTTP 클라이언트가 `TLS 1.2`에 대응되는지 확인 해주세요.  
서버에서 결제 API호출을 위해 필요한 서비스의 IP를 방화벽에서 허용 해주세요.

| 서비스                | 도메인                       | 공인 IP Address                      | 방향       |
|--------------------|---------------------------|------------------------------------|----------|
| 결제창 연동 SDK (운영계)   | pay.nicepay.co.kr         | 121.133.126.85/27                  | OUTBOUND |
| 결제창 연동 SDK (샌드박스)  | sandbox-pay.nicepay.co.kr | 121.133.126.84/27                  | OUTBOUND |
| RESTful API (운영계)  | api.nicepay.co.kr         | 121.133.126.83/27                  | OUTBOUND |
| RESTful API (샌드박스) | sandbox-api.nicepay.co.kr | 121.133.126.84/27                  | OUTBOUND |
| 웹훅                 | -                         | 121.133.126.86 <br> 121.133.126.87 | INBOUND  |


## IP 보안 기능(IP접근 제한)
나이스페이 API는 모든 IP 대역에서 호출이 가능 합니다.   
처음 상점을 생성한 후 IP 보안 기능을 통해 API 호출이 가능한 IP를 제어한다면 한 단계 높은 🔒 보안수준을 유지할 수 있습니다.  
IP 등록 규칙은 `CIDR`체계를 따르며 Class체계 대비 유연하게 IP 대역을 제한할 수 있습니다.

### IP 보안 설정
![image](https://user-images.githubusercontent.com/86043374/128289743-abfd822e-b303-4e4a-bb94-ab6d6da77f4a.png)

- 로그인 후 [개발정보](#개발정보)에 접속하면 IP 보안 등록이 가능 합니다.
- 추가를 누른 후 설명과 `CIDR` 규칙을 입력 후 등록하면 등록된 IP대역만 API호출이 가능합니다.

### IP 보안 추가
개발정보 > IP보안 > 추가 버튼을 클릭하면 IP제한 규칙 등록을 위한 팝업이 노출 됩니다.  
설명과 IP제한 규칙을 등록하면 IP보안을 위한 준비가 완료 됩니다.

![image](https://user-images.githubusercontent.com/86043374/128665418-caa1390f-18ce-4925-bad2-0c890e80301a.png)

> ##### ⚠️ 중요
> IP제한 규칙을 추가하는 경우 등록된 `CIDR` 범위에서만 결제가 진행 됩니다.  
> 서비스 운영 중 IP제한 규칙을 추가하는 경우 주의 해주세요.

### CIDR 규칙과 등록
`network prefix / bit (0~32)` 범위 내에서 등록이 가능합니다.  
`CIDR` 대역이 넓은 경우 `CIDR` 계산기를 활용 하는 것을 권장 합니다.

<br>

🔧 예시1

<img src="../image/common-cidr-32.svg" width="600px">

```Bash
255.255.255.255 `1개` IP 범위를 CIDR 변환     
>> CIDR : 255.255.255.255/32  
```

<br>

🔧 예시2

<img src="../image/common-cidr-31.svg" width="600px">

```Bash
255.255.255.254~255 `2개` IP 범위를 CIDR 변환  
>> CIDR : 255.255.255.255/31  
```

<br>

## 타임아웃 정보

<img src="../image/netcancel-common.svg" width="600px">

HTTP 클라이언트 구성 시 타임아웃 예외 처리에 대한 정보 입니다.  
`Read-timeout`이 발생된 경우 반드시 [망 취소](#망취소)를 요청하여 결제 정보 불일치를 방지 해주세요.

- Connection timeout : `5s`
- Receive(Read) timeout : `30s`

<br>

## 샌드박스

회원가입을 하면 하나의 샌드박스(🔧 TEST 상점)을 생성 할 수 있습니다.

### 샌드박스(테스트 상점) 생성
- 회원가입 후 로그인 하면 `테스트 상점 개설하기` 버튼이 활성화 됩니다.
- 버튼 클릭 후 TEST상점 이름을 입력하면 준비가 완료 됩니다.

![image](https://user-images.githubusercontent.com/86043374/128303655-26060514-b86c-4b15-a58d-f6eded03fa08.png)

샌드박스(테스트상점)으로 이동 후 개발정보 탭으로 이동하면 개발에 필요한 🔑 키값 확인이 가능하며 즉시 개발을 진행 할 수 있습니다.  
![image](https://user-images.githubusercontent.com/86043374/128303979-6244f466-43f9-4473-a93e-c7cd97748564.png)


### 샌드박스 활용

회원가입을 하게되면 하나의 샌드박스(TEST 상점)을 생성 할 수 있습니다.  
생성된 샌드박스 상점을 통해 신규 서비스의 TEST 및 개발을 즉시 진행 할 수 있습니다.  
또한 샌드박스 시스템은 개발과 TEST의 번거로움을 줄이기 위해 다양한 장점과 기능을 제공합니다.

### 샌드박스 장점

- 즉시 TEST 및 개발이 가능 합니다.
- 결제가 발생되지 않아 편하게 TEST가 가능 합니다.
- 웹 로그를 통해 API 요청/응답 디버깅이 편리 합니다.
- 운영 환경에 영향이 없는 TEST시스템을 구성 할 수 있습니다.

### 샌드박스 가맹점 테스트

샌드박스 활용을 위한 준비가 되었다면 다음과 같은 방식으로 TEST개발이 가능합니다.

- 결제창 JS 호출방식을 선택 후 샌드박스 도메인으로 변경 해주세요.
- 승인 모델을 구분하는 기준은 가맹점의 clientId로 구분합니다.
- end-point: https://pay.nicepay.co.kr/v1/js/

|    모델     | 설명                                     |
|:---------:|:---------------------------------------|
| Server 승인 | 결제창 호출(인증)과 결제(승인) API호출이 독립적으로 분리된 모델 |
| Client 승인 | 결제창 호출(인증)후 결제(승인)이 자동으로 처리되는 모델       |

> #### ⚠️ 중요
> 요청 파라미터는 운영/샌드박스 모두 동일 합니다.

## 토큰 기반 인증

### Basic Authentication
API 엑세스 제어를 위해 `Basic` 인증 방식을 이용하는 방식 입니다.  
`HTTP Authorization header`에 Basic 인증 스킴으로 약속된 `credentials` 전달하면 API 엑세스 인증이 완료 됩니다.  
API 엑세스 방식은 생성된 시크릿키 인증방식에 따라 선택이 가능 합니다.

<br>

#### HTTP header Basic Authentication Scheme
```bash
Authorization: Basic <credentials>
```

#### Credentials 생성 알고리즘
```bash
Base64(`client-key:secret-key`)
```

#### Credentials 생성 예시
`Credentials` 생성을 위해 먼저 `클라이언트 키` + : + `시크릿키` 구성으로 문자열을 생성 합니다.
```bash
clientKey = 'af0d116236df437f831483ee9c500bc4'
secretKey = '433a8421be754b34989048cf148a5ffc'
>> `af0d116236df437f831483ee9c500bc4:433a8421be754b34989048cf148a5ffc`
```

생성된 문자열을 `Base64`로 encoding 하여 `Credentials` 값을 생성합니다.
```bash
// Base64('{clientId}:{secretKey}') 
Base64('af0d116236df437f831483ee9c500bc4:433a8421be754b34989048cf148a5ffc')
>> `YWYwZDExNjIzNmRmNDM3ZjgzMTQ4M2VlOWM1MDBiYzQ6NDMzYTg0MjFiZTc1NGIzNDk4OTA0OGNmMTQ4YTVmZmM=`
```  

생성된 `Credentials`를 `HTTP header`에 셋팅 하면 API 인증 준비가 완료 됩니다.
```bash
Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMTQ4M2VlOWM1MDBiYzQ6NDMzYTg0MjFiZTc1NGIzNDk4OTA0OGNmMTQ4YTVmZmM= 
```

### Bearer Authentication
API 엑세스 제어를 위해  `OAuth` 기반 `Bearer` 인증 스킴을 이용하는 방식 입니다.  
API 접속을 위해 `access token`을 API 서버에 제출해서 인증을 하게 되며,  
`Bearer token` 인증을 위해 사용되는 token 발급을 위해 [Access token](#access-token) API 호출이 선행 되어야 합니다.  
API 엑세스 방식은 생성된 시크릿키 인증방식에 따라 선택이 가능 합니다.

#### HTTP header Bearer Authentication Scheme
```bash
Authorization: Bearer <token>
```

#### Access Token 생성 API
- [Access token](#access-token)

#### Bearer Token 생성 예시
`Bearer token` 생성을 위해 `Access token` API 호출 합니다.  
Access token API호출을 위해 Basic 인증 스킴이 활용되며, `Credentials` 생성 방법은 [Basic auth 가이드](#basic-auth)를 참고 해주세요.

```shell
curl -X POST "https://api.nicepay.co.kr/v1/access-token" \
-H "Content-Type: application/json" \
-H "Authorization: Basic YWYwZDExNjIzNmRm..."
```

#### Access token API 응답 예시
```bash
{
  "resultCode": "0000",
  "resultMsg": "정상 처리되었습니다.",
  "accessToken": "6d0a7caa1b7358c8aa06ef3706e01bb1feb2c65dacc7147b258dfdd6191b5279",
  "tokenType": "Bearer",
  "expireAt": "2021-07-31T00:58:02.000+0900",
  "now": "2021-07-20T15:28:26.882+0900"
}
```

#### HTTP header Bearer token 셋팅
`Access token` API 응답 값 중 `accessToken` 값을 `Bearer token` 값으로 셋팅하면 API 호출 준비가 완료 됩니다.
```bash
Authorization: Bearer 6d0a7caa1b7358c8aa06ef3706e01bb1feb2c65dacc7147b258dfdd6191b5279
```
> 발급된 토큰은 ⏱️ 30분간 유효하며 발급된 토큰의 갱신은 지원하지 않습니다.  
> 토큰 만료시간 이후 요청 건에 대해 새로운 토큰이 발급되어 응답됩니다.  
> 기 발급된 토큰의 유효시간 이내 토큰 재발급 요청이 있는 경우 기존 토큰이 전달되며 유효시간은 기 발급 토큰과 동일합니다.

<br>

### 샌드박스를 통한 테스트 개발 예시
- `Basic 인증` / `Server 승인` 기준으로 결제창 TEST 개발 흐름 예시를 설명 합니다.

#### 결제창 호출을 위한 JS include
- 결제창 호출을 위한 JS SDK를 sandbox 도메인으로 변경합니다.
- clientId는 가맹점관리자 TEST상점에서 발급한 `클라이언트키`를 사용 합니다.

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

#### 결제창 응답
- 카드사 인증을 성공하면 authResultCode가 `0000`으로 응답 됩니다.

```bash
Content-type: application/x-www-form-urlencoded
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

#### 결제 요청 API 목록

- API 호출시 제약사항을 체크하고, API Host는 샌드박스 도메인(`sandbox-api.nicepay.co.kr`)을 사용 합니다.

```bash
GET/POST {URL} HTTP/1.1 
Host: sandbox-api.nicepay.co.kr 
Authorization: Basic <credentials> or Bearer <token>
Content-type: application/json;charset=utf-8
```

| API                                  | 샌드박스 지원여부 | Method | Endpoint                     | 제약사항    |
|:-------------------------------------|:---------:|:------:|:-----------------------------|:--------|
| [AccessToken 발급](#access-token)      |     ○     | `POST` | /v1/access-token             |         |
| [결제창 승인](#승인--결제-)                   |     ○     | `POST` | /v1/payments/{tid}           | 임의 값 응답 |
| [취소 요청](#취소환불망취소)                    |     △     | `POST` | /v1/payments/{tid}/cancel    | 부분취소 불가 |
| [거래조회-tid](#거래조회--with-tid-)         |     ○     | `GET`  | /v1/payments/{tid}           |         |
| [거래조회-orderId](#거래조회--with-orderid-) |     ○     | `GET`  | /v1/payments/find/{orderId}  |         |
| [빌키발급](#빌키발급)                        |     ○     | `POST` | /v1/subscribe/regist         | 임의 값 응답 |
| [빌키승인](#빌키승인)                        |     ○     | `POST` | /v1/subscribe/{bid}/payments | 임의 값 응답 | 
| [빌키삭제](#빌키삭제)                        |     ○     | `POST` | /v1/subscribe/{bid}/expire   |         |
| [약관조회](#약관-조회)                       |     ×     | `GET`  | /v1/terms                    |         |
| [N정통Epay승인](#epay)                   |     ×     | `POST` | /v1/epay                     |         |
| [현금영수증 발급](#현금영수증-발급)                |     ○     | `POST` | /v1/receipt/                 |         |
| [현금영수증 취소](#현금영수증-취소)                |     ×     | `POST` | /v1/receipt/{tid}/cancel     |         |
| [현금영수증 거래조회](#현금영수증-조회)              |     ○     | `GET`  | /v1/receipt/{tid}            |         | 
| [카드 이벤트 조회](#카드-이벤트)                 |     ×     | `GET`  | /v1/card/event               |         |
| [카드 무이자정보 조회](#카드-무이자-조회)            |     ×     | `GET`  | /v1/card/interest-free       |         |
| [승인금액검증](#승인-금액-검증)                  |     ○     | `POST` | /v1/check-amount/{tid}       |         |


#### 결제(승인) 응답 예시
승인 API호출에 성공하면 실제 결제가 발생하지 않고, 임의 값이 응답됩니다.  
resultCode가 `0000`으로 응답되면 TEST성공 입니다.

```bash
Content-type: application/json
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
    cardName: '삼성',  # (샌드박스) 응답 결과는 삼성카드로 고정 
    cardNum: '123412******1234',
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


## 로그

### 웹 로그 디버깅

나이스페이는 개발과 디버깅의 편의성을 위해 💿 웹로그를 제공하고 있습니다.
로그는 단순한 호출 기록과, 상세기록을 나누어 확인 할 수 있습니다.  
API요청이 실패하는 경우 상세로그를 확인하여 쉽게 디버깅 해보세요.

- 로그인 > 개발정보 하단에서 표기되는 단순 이벤트성 로그를 통해 최근 호출된 인터페이스 로그 확인이 가능하며
- 로그 list를 클릭하면 선택된 로그의 상세 정보 확인이 가능 합니다.

### 주요기능

- 로그 : 결과코드, 주문번호, ⏱️ 시간등이 표기된 단순 이벤트성 로그
- 상세 로그 : 조회 및 검색 기능과 `Request` / `Response body` 상세 정보를 제공하는 기능

### 상세보기

로그 '상세보기'는 요청된 인터페이스의 로그를 검색하여  
상세한 `Request` / `Response body` 정보를 제공하는 기능 입니다.  
상세보기는 다음과 같은 기능을 제공 합니다.

### 로그 검색

- 선택된 로그의 상세 `Request` / `Response body` 제공
- 선택된 거래와 연관된 거래의 Timeline
- 웹훅과 일반 로그의 분리


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

## API·JS SDK

### URI 목록
제공되는 API의 URI 목록 입니다. 빠른 검토를 위해 인터페이스 확인이 필요한 경우 목록의 링크를 클릭해주세요.

| API                                  | Method | Endpoint                     |
|:-------------------------------------|:------:|:-----------------------------|
| [AccessToken 발급](#access-token)      | `POST` | /v1/access-token             |
| [결제창 승인](#승인--결제-)                   | `POST` | /v1/payments/{tid}           |
| [취소 요청](#취소환불망취소)                    | `POST` | /v1/payments/{tid}/cancel    |
| [거래조회-tid](#거래조회--with-tid-)         | `GET`  | /v1/payments/{tid}           |
| [거래조회-orderId](#거래조회--with-orderid-) | `GET`  | /v1/payments/find/{orderId}  |
| [빌키발급](#빌키발급)                        | `POST` | /v1/subscribe/regist         |
| [빌키승인](#빌키승인)                        | `POST` | /v1/subscribe/{bid}/payments |
| [빌키삭제](#빌키삭제)                        | `POST` | /v1/subscribe/{bid}/expire   |
| [약관조회](#약관-조회)                       | `GET`  | /v1/terms                    |
| [N정통Epay승인](#epay)                   | `POST` | /v1/epay                     |
| [현금영수증 발급](#현금영수증-발급)                | `POST` | /v1/receipt/                 |
| [현금영수증 취소](#현금영수증-취소)                | `POST` | /v1/receipt/{tid}/cancel     |
| [현금영수증 거래조회](#현금영수증-조회)              | `GET`  | /v1/receipt/{tid}            |
| [카드 이벤트 조회](#카드-이벤트)                 | `GET`  | /v1/card/event               |
| [카드 무이자정보 조회](#카드-무이자-조회)            | `GET`  | /v1/card/interest-free       |
| [승인금액검증](#승인-금액-검증)                  | `POST` | /v1/check-amount/{tid}       |


### JS SDK
JS SDK는 결제창을 호출하는 경우 활용 됩니다.
JS SDK호출은 [클라이언트 키](#클라이언트-키)의 인증을 통해 호출 되며 결제창이 호출되고 클라이언트 키의 타입에 따라 결제(승인)되는 모델이 변경됩니다.

[클라이언트 키](#클라이언트-키) 는 로그인 후 개발정보에서 확인이 가능 합니다.

- 승인 모델을 구분하는 기준은 가맹점 관리자에서 발급한 `clientId`로 구분합니다.
- end-point: https://pay.nicepay.co.kr/v1/js/

|    모델     | 설명                                     |
|:---------:|:---------------------------------------|
| Server 승인 | 결제창 호출(인증)과 결제(승인) API호출이 독립적으로 분리된 모델 |
| Client 승인 | 결제창 호출(인증)후 결제(승인)이 자동으로 처리되는 모델       |

### JS SDK 인증이란?
JS SDK를 통해 💡 결제창 Method 호출시 `clientId` 필드에 `클라이언트 키`값을 셋팅 하면 준비가 완료 됩니다.  
JS SDK 모델에 따라 호출되는 JS SDK Include 방식과 Method 차이가 있습니다. 관련 부분은 하단 소스코드를 참조 해주세요.

### JS SDK 인증-Server & Client 승인 모델

```html
<script src="https://pay.nicepay.co.kr/v1/js/"></script>
<script>
function serverAuth() {
  AUTHNICE.requestPay({
    clientId: 'af0d116236df437f831483ee9c500bc4', // clientId에 따라 Server / Client 방식 분리
    method: 'vbank',
    orderId: 'your-unique-orderid',
    amount: 1004,
    goodsName: '나이스페이-상품',
    vbankHolder: '나이스',
    returnUrl: 'http://localhost:4567/serverAuth'
  });
}
</script>
```

> Client 승인 모델을 사용하는 경우 모든  💳 결제(승인)건 별 금액 검증이 필요 합니다.  
> 또한 사용자 네트워크 환경에 따라 인터페이스 응답의 유실이 발생 할 수 있어 [승인금액 검증 API](#승인-금액-검증)를 활용하여 금액체크를 반드시 해야 합니다.    
<br>


# 결제·발급

## Access token

### Over-view
<img src="../image/payment-token.svg" width="800px">

- [Bearer token](#bearer-token)방식 authorization을 활용하여 API를 호출하는 경우 활용 합니다.

> #### ⚠️ 중요
> [시크릿 키](#시크릿-키)를 [Basic auth](#basic-auth) 방식으로 생성한 경우 API 호출시 token 관리는 생략 할 수 있습니다.


### 샘플 코드

```shell
curl -X POST "https://api.nicepay.co.kr/v1/access-token" \
-H "Content-Type: application/json" \
-H "Authorization: Basic YWYwZDExNjIzNmRm..."
```

### 요청 명세

```bash
POST /v1/access-token  
HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```

|   Parameter   |  type  | 필수  | byte | 설명                                                    |
|:-------------:|:------:|:---:|:----:|:------------------------------------------------------|
| returnCharSet | String |     |  10  | 응답 파라메터 인코딩 방식<br> 값: utf-8/euc-kr <br> Default:utf-7 |


### 응답 명세 (Body)

```bash
Content-type: application/json
```

|  Parameter  |  type  | 필수  | byte | 설명                         |
|:-----------:|:------:|:---:|:----:|:---------------------------|
| resultCode  | String |  O  |  4   | 결과코드<br>0000: 성공/그 외 실패    |
|  resultMsg  | String |  O  | 100  | 결과 메시지                     |
| accessToken | String |  O  |  40  | access token               |
|  tokenType  | String |  O  |  10  | 인증 스킴 유형<br> Bearer 고정     |
|  expiredAt  | String |  O  |      | Token 만료 시각<br>ISO 8601 형식 |
|     now     | String |  O  |      | 현재 시각<br> ISO 8601 형식      |
  

## 결제 인증 (Server 승인 모델-JS SDK)

결제자가 브라우저에서 `pay.nicepay.co.kr/v1/js/` JS SDK의 `AUTHNICE.requestPay()` Method 호출시 결제창이 노출 됩니다.  
결제자는 💡 결제창을 통해 카드사 및 결제 원천사에 접근하여 인증과정을 진행 하고 나이스페이는 인증 및 💳 결제(승인) 처리 후 결과를 `AUTHNICE.requestPay()`의 object value로 전달된 `returnUrl`로 `POST` 합니다.


> #### ⚠️ 중요
> [클라이언트 키](#클라이언트-키)가 Server 승인 방식으로 발급 된 경우 Server승인 모델 결제창 사용이 가능 합니다.  
> [시크릿 키](#시크릿-키) 생성이 [Bearer token](#bearer-token) 방식인 경우 결제(승인)API 호출전 token 생성과정이 추가 됩니다.

### Over-view

<img src="../image/payment-window-server-sdk.svg" width="800px"> 

### 예외처리
- `returnUrl`로 인증응답이 될때 금액, 위변조검증 `signature`, 주문번호가 응답되며 반드시 생성한 결제정보와 일치하는지 체크 후 승인(결제) API를 호출 해주세요.


### 샘플 코드

```html
<script src="https://pay.nicepay.co.kr/v1/js/"></script> 
<script>
function serverAuth() {
  AUTHNICE.requestPay({
    clientId: 'af0d116236df437f831483ee9c500bc4',  // clientId에 따라 Server / Client 방식 분리
    method: 'card',
    orderId: 'your-unique-orderid',
    amount: 1004,
    goodsName: '나이스페이-상품',
    returnUrl: 'http://localhost:4567/serverAuth'
 });
}
</script>
```

- 먼저 https://pay.nicepay.co.kr/v1/js/ 를 Inclue 합니다.
- clientId 필드에 [클라이언트 키](#클라이언트-키) 값을 셋팅 하면 준비가 완료 됩니다.
- `AUTHNICE.requestPay()` method 호출시 결제창이 노출 됩니다.
- 💳 결제(승인)결과는 `returnUrl`로 전달된 `end-point`로 post 됩니다.


### 요청 명세 (Server 승인 모델)

#### 공통

|   Parameter   |  type   | 필수  | byte | 설명                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:-------------:|:-------:|:---:|:----:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   clientId    | String  |  O  | 50	  | 가맹점 식별코드, NICEPAY가 발급한 가맹점 식별 값 		                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 
|    method     | String  |  O  | 20	  | 결제수단 <br> card : 신용카드 <br> bank : 계좌이체 <br> directCard : 결제창 없이 카드사 바로 노출  <br> vbank : 가상계좌  <br> cellphone : 휴대폰 <br>naverpayCard : 네이버페이-신용카드 전액결제(포인트 이용불가) <br> kakaopay : 카카오페이(카드전액 또는 포인트전액) <br>kakaopayCard : 카카오페이-신용카드 전액결제 <br>kakaopayMoney : 카카오페이-머니 전액결제 <br>samsungpayCard : 삼성페이 카드전액 결제 <br>payco : 페이코 <br>ssgpay : SSGPAY <br>cardAndEasyPay : 신용카드와 간편결제 노출 <br>*cardAndEasyPay인 경우, 아래 파라미터와 함께 사용불가* <br>- cardCode, cardQuota, shopInterest, quotaInterest | 
|    orderId    | String  |  O  | 64	  | 가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br> 결제된 orderId로 재호출 불가                                                                                                                                                                                                                                                                                                                                                                                                                              | 
|    amount     | Int  	  |  O  | 12	  | 결제금액 (숫자만)		                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 
|   goodsName   | String  |  O  | 40	  | 상품명<br> - doubleQuota(")와 pipLine(&brvbar;) 2가지 특수문자는 '-'로 대체 됩니다.                                                                                                                                                                                                                                                                                                                                                                                                                   | 
|   returnUrl   | String  |  O  | 500	 | 인증 처리 후 redirect 되는 url 		                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 
| mallReserved  | String  |     | 500	 | 상점 정보 전상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                                                                                                                                                                                                                                                                                                               | 
|  mallUserId   | String  |     | 20	  | 상점에서 관리하는 사용자 아이디 		                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 
|   buyerName   | String  |     | 30	  | 구매자 이름 		                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 
|   buyerTel    | String  |     | 40	  | 구매자 전화번호<br> (-) 없이 숫자만 입력 		                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 
|  buyerEmail   | String  |     | 60	  | 구매자 이메일 		                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 
|   useEscrow   | Boolean |     |  -	  | true: 에스크로 거래 / false: 일반거래(default) 		                                                                                                                                                                                                                                                                                                                                                                                                                                              | 
|   currency    | String  |     |  3	  | KRW:원화, USD:미화달러, CNY:위안화 		                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 
|  logoImgUrl   | String  |     | 100	 | 로고 이미지의 full URL 전달<br>  ex) https://youre.site.com/image/logo.jpg<br> *채널별 사이즈 (단위 : pixel)*<br>모바일 : width 50 X height 50<br> 웹표준 : width 94 X height 25                                                                                                                                                                                                                                                                                                                           | 
|   language    | String  |     |  2	  | EN : 영문 / CN : 중문 / KO : 국문(Default)<br>NICEPAY 결제창 내 다국어를 지원<br>*sample)*<br>lang=EN -> 결제창 영문표기<br>lang=CN -> 결제창 중문표기                                                                                                                                                                                                                                                                                                                                                             | 
| returnCharSet | String  |     | 10	  | 가맹점 서버의 encoding 방식 전달<br> - utf-8(Default) / euc-kr		                                                                                                                                                                                                                                                                                                                                                                                                                               | 
|   skinType    | String  |     | 10	  | 결제창 스킨 설정<br>지원 옵션 red/green/purple/gray/dark                                                                                                                                                                                                                                                                                                                                                                                                                                        | 


<br>

#### 부가세 지정금액

| Parameter  | type | 필수  | byte | 설명                                     |
|:----------:|:----:|:---:|:----:|:---------------------------------------|
| taxFreeAmt | Int  |     | 12	  | 전체 거래금액(amount)중에서 면세에 해당하는 금액을 설정합니다. | 

<br>

#### 신용카드 & 간편결제
|  Parameter  |  type  | 필수  | byte | 설명                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:-----------:|:------:|:---:|:----:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  cardQuata  | String |     | 100	 | 할부개월 설정<br><br>[공통]<br>선택할 수 있는 할부기간을 제한한다.<br><br>[카드일반+PAYCO+네이버페이]<br>- 단독 설정 가능<br>- ','를 구분자로 할부개월 나열<br>- 일시불은 반드시 "00"으로 설정할것<br>- 2자리의 할부기간 설정 (3개월일 경우 반드시 '03' 으로 설정)<br>Ex) cardQuota=03 <br>- 설명 : 3 개월 할부만 가능하도록 함.<br>최소금액 : 50,000원 이상<br><br>[카카오페이, 삼성페이, SSGPAY]<br> - 단독 설정 사용불가. 반드시 cardCode와 함께 설정되어야 사용가능.<br> - 할부개월 복수설정 불가                                                                                                                                                                                                                                                                                                                                                           | 
|  cardCode   | String |     | 100	 | 특정카드사 선택옵션<br><br>[공통]<br>이용할 수 있는 카드 리스트를 제한 (코드집-카드코드 참고)<br>- 단독 설정 가능<br><br>[카드일반]<br>- ','를 구분자로 카드코드 나열<br>Ex1) cardCode=02<br>-> 국민 카드만 이용할 수 있도록 제한<br>Ex2) cardCode=02,04<br>-> 국민,삼성 카드만 이용할 수 있도록 제한<br><br>[간편결제]<br>- 복수설정 불가<br>- 카카오페이와 PAYCO는 각 간편결제에서 카드만 이용 가능함.<br>카카오페이는 카카오Money 이용불가, PAYCO는 페이코포인트 이용불가<br>  ex) cardCode = 06 (카드사 복수설정 불가)<br><br>*간편결제별 이용가능 카드리스트<br>*- 삼성페이 : 비씨,국민,하나(외환),삼성,신한,현대,롯데,NH,하나<br>- 카카오페이: 비씨,국민,하나(외환),삼성,신한,현대,롯데,씨티,NH,하나<br>- PAYCO : 비씨,국민,하나(외환),삼성,신한,현대,롯데,씨티,NH,하나,한미,신세계한미,수협,신협,우리,광주,전북,제주,해외비자,해외마스터,해외JCB,저축은행,은련,KDB산업,카카오뱅크<br>- SSGPAY : 비씨,국민,하나(외환),삼성,신한,현대,롯데,씨티,NH,하나,전북,케이뱅크<br>- 네이버페이 : 신한, 비씨, 국민, NH, 롯데, 삼성, 씨티, 하나, 현대 | 
| cardShowOpt | String |     | 50	  | 카드사별 인증창 호출방식 옵션<br><br>카드사별 호출방식 정의하여 카드사로 전달<br>- 1:안심클릭, 2:간편결제, 3:앱카드직접 호출<br>- '&brvbar;'를 구분자로 카드코드 나열<br>- 카드코드:노출유형&brvbar;카드코드:노출유형<br>ex) CardShowOpt=08:3&brvbar;02:3<br>- 이용가능 카드사목록 : 02(국민), 04(삼성), 06(신한), 07(현대), 08(롯데), 12(NH), 15(우리)                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 

<br>

#### 가상계좌
| Parameter       | Type   | 필수     | Byte | 설명                                                                               |
|-----------------|--------|----------|------|------------------------------------------------------------------------------------|
| vbankHolder     | String | O | 40   | 가상계좌 (가맹점 상호명, 사용자명) <br> *가상계좌 채번시 필수                                                 |
| vbankValidHours | Int    |          | 4    | 가상계좌 유효시간<br>- 시간단위로 입력.<br>- Default 값 D+7일<br>- vbankValidHours와 vbankExpDate가 함께 요청된경우 vbankValidHours가 우선함<br>ex) 10 을 입력하면, 가상계좌 발급후 10시간동안 해당 가상계좌를 이용할 수 있습니다.                                           |
| vbankExpDate	  |Int |          |      | 가상계좌 입금 만료일                                                            |

<br>

#### 휴대폰
| Parameter  |  Type  |  필수   |  Byte  | 설명             |
|:-----------|:------:|:-----:|:------:|:---------------|
| isDigital  |  Int   |   O   |   1    | 0: 컨텐츠, 1: 실물  |

<br>

#### 현금영수증
| Parameter          |   Type   |         필수          |  Byte  | 설명                                                                                                                                                                                                                                          |
|:-------------------|:--------:|:-------------------:|:------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| directReceiptType  |  String  |                     |   20   | 현금영수증 발급 유형<br>unPublished : 미발행<br>individual : 개인 소득공제용<br>company : 사업자 지출증빙용                                                                                                                                                            |
| directReceiptNo    |  String  |      네이버페이-포인트      |   20   | 현금영수증 발행대상 식별정보<br>휴대폰번호(10 자리 또는 11 자리) 또는 사업자번호(10 자리)<br>* directReceiptType 이 individual 또는 company 인 경우 필수<br>* directReceiptType 이 individual 인경우 휴대폰번호를 입력합니다.<br>* directReceiptType 이 company 인경우 사업자번호를 입력합니다.<br> * '-'없이 숫자만 입력 |

<br>

#### PC 옵션
| Parameter       |   Type    |   필수   |  Byte  | 설명                                                                                                                                   |
|:----------------|:---------:|:------:|:------:|:-------------------------------------------------------------------------------------------------------------------------------------|
| disableScroll   |  Boolean  |        |   -    | 결제창 스크롤 생성여부<br><br>true : 스크롤 생성 안함(Default : true)<br>false : 스크롤 생성                                                               |
| disableEdgeChk  |  Boolean  |        |   -    | Edge브라우저 가이드Alert 예외 여부<br><br>true : Edge브라우저 가이드문구 노출안함<br> false : Edge브라우저 가이드문구 노출(Default : false)                             |
| zIdxHigher      |  Boolean  |        |   -    | NICEPAY Layer z-index 조정 여부<br>true : NICEPAY Layer의 최하단 z-index를 11000 으로 설정<br>false : default z-index로 9999가 설정됨(Default : false) |

<br>

#### Mobile 옵션
| Parameter  |   Type   |  필수   |  Byte  | 설명                                                                                                                                                                                                                              |
|:-----------|:--------:|:-----:|:------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| appScheme  |  String  |       |  200   | 모바일 App Scheme 값 (APP 연동인 경우만 사용)<br>가맹점 독립 APP을 이용하여 개발시 (Webview 연동)<br>카드사를 포함한 제휴사 인증 완료 후 결과에대한 focus가 <br>가맹점 APP으로 돌아오기 위해 설정하는 가맹점 APP의 scheme 값을 설정<br>예) 가맹점 App 스킴이 nicepaysample인 경우<br>appScheme=nicepaysample://  |

<br>

### 응답 명세 (Server 승인 모델)

```bash
POST
Content-type: json
```

| Parameter       | Type    |    필수    |  Byte  | 설명                                                                                                                                                                                                                   |
|:----------------|:--------|:--------:|:------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| authResultCode  | String  |          |   4    | 인증결과 코드<br><br>0000 : 인증성공 / 그외 인증 실패<br>(0000인 경우에만 승인 API를 호출하여 승인요청)                                                                                                                                              |
| authResultMsg   | String  |          |  500   | 인증결과 메시지                                                                                                                                                                                                             |
| tid             | String  |   성공시    |   30   | 결제 인증 키<br><br>결제 승인을 위한  키값 입니다.<br>- 인증에 성공한 경우(authResultCode=0000)에만 리턴됩니다.                                                                                                                                      |
| clientId        | String  |          |   50   | 가맹점 식별코드<br><br>NICEPAY가 발급한 가맹점 식별값                                                                                                                                                                                 |
| orderId         | String  |          |   64   | 상점 거래 고유번호<br><br>인증 요청시 전달된 orderId값이 리턴됩니다.                                                                                                                                                                        |
| amount          | Int     |          |   12   | 결제 금액                                                                                                                                                                                                                |
| mallReserved    | String  |          |  500   | 상점 예약필드<br><br>인증 요청시 전달된 mallReserved값이 리턴됩니다.                                                                                                                                                                      |
| authToken       | String  |          |   40   | 인증 TOKEN                                                                                                                                                                                                             |
| signature       | String  |          |  256   | 위변조 검증 데이터<br><br>- 생성규칙 : hex(sha256(authToken + clientId + amount + SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- 인증에 성공한 경우(authResultCode=0000)에만 리턴됩니다.<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다. |

<br>

> #### ⚠️ 중요
> Server 승인 모델은 `authResultCode`가 `0000`인 경우 승인 API를 호출하면 💳 결제(승인)이 발생 합니다.  
> 승인 API를 호출하지 않는 경우 💳 결제(승인)이 발생되지 않습니다.  


## 승인 (결제)

- 결제창 [JS SDK](/api/payment.md#js-sdk) Server승인 모델에서 카드사 인증 완료 후 처리 구간의 명세 입니다.
- 결제창을 통해 결제자가 카드사 및 결제 원천사에 접근하여 인증과정을 완료하면 나이스페이는 인증결과를 `AUTHNICE.requestPay()`의 object value로 전달된 `returnUrl`로 POST 합니다.
- 가맹점은 POST 데이터의 금액 및 위변조 여부를 체크하고 응답된 tid을 승인 API로 전달 하면 💳 결제(승인)요청 처리가 완료 됩니다.

<br>

> #### ⚠️ 중요
> [클라이언트 키](#클라이언트-키)가 Server 승인 방식으로 발급 된 경우 Server승인 모델 결제창 사용이 가능 합니다.  
> [시크릿 키](#시크릿-키) 생성이 [Bearer token](#bearer-token) 방식인 경우 결제(승인)API 호출전 token 생성과정이 추가 됩니다.


### Over-view
<img src="../image/payment-server-authorization.svg" width="800px">

### 예외처리
- 승인 API 호출시 read-timeout이 발생한다면 [망 취소](/api/cancel.md#망취소)를 진행 해주세요.

<br>

### 샘플 코드

```bash
curl -X POST 'https://api.nicepay.co.kr/v1/payments/nicuntct1m0101210727200708A058' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3Zjgz...' 
-D '{
    "amount" : 1004
}'
```

<br>

### 요청 명세

```bash
POST /v1/payments/{tid} HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter     |   Type   |  필수   |  Byte  | 설명                                                                                                                  |
|:--------------|:--------:|:-----:|:------:|:--------------------------------------------------------------------------------------------------------------------|
| amount        |   Int    |   O   |   12   | 결제금액                                                                                                                |
| ediDate       |  String  |       |   -    | 전문생성일시<br><br>ISO 8601 형식                                                                                           |
| signData      |  String  |       |  256   | 위변조 검증 Data<br><br>생성규칙 : hex(sha256(tid + amount + ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| returnCharSet |  String  |       |   10   | 응답파라메터 인코딩 방식<br><br>가맹점 서버의 encoding 방식 전달<br>utf-8(Default) / euc-kr                                              |

<br>

### 응답 명세

#### 공통

```bash
Content-type: application/json
```

| Parameter         |  Type   |  필수   |  Byte  | 설명                                                                                                                                                                                       |
|:------------------|:-------:|:-----:|:------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| resultCode        | String  |   O   |   4    | 결제결과코드<br><br>0000   : 성공 / 그외 실패                                                                                                                                                        |
| resultMsg         | String  |   O   |  100   | 결제결과메시지                                                                                                                                                                                  |
| tid               | String  |   O   |   30   | 결제 승인 키<br><br>최초 승인(가상계좌-채번)에 성공한   원거래의 NICEPAY 거래키 입니다.                                                                                                                               |
| cancelledTid      | String  |   　   |   30   | 취소 거래 키 <br><br>NICEPAY가 발행하는 취소 응답 TID (부분취소시 tid와   다른 값이 응답됨)<br>- 취소 요청건에 한하여 응답됨<br>- cancels 객체에서 현재 취소된   거래정보를 찾을 때 사용 하시면 됩니다.                                                  |
| orderId           | String  |   O   |   64   | 상점 거래 고유번호                                                                                                                                                                               |
| ediDate           | String  |       |   -    | 응답전문생성일시 ISO 8601 형식                                                                                                                                                                     |
| signature         | String  |   　   |  256   | 위변조 검증 데이터<br><br>- 유효한 거래건에 한하여 응답<br>- 생성규칙 : hex(sha256(tid + amount +   ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>-   SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| status            | String  |   O   |   20   | 결제 처리상태<br><br>paid:결제완료, ready:준비됨, failed:결제실패, cancelled:취소됨, partialCancelled:부분 취소됨, expired:만료됨<br>['paid',   'ready', 'failed', 'cancelled', 'partialCancelled', 'expired']       |
| paidAt            | String  |   O   |   -    | 결제완료시점 ISO 8601 형식<br><br>결제완료가   아닐 경우 0                                                                                                                                                |
| failedAt          | String  |   O   |   -    | 결제실패시점 ISO 8601 형식<br><br>결제실패가   아닐 경우 0                                                                                                                                                |
| cancelledAt       | String  |   O   |   -    | 결제취소시점 ISO 8601 형식<br><br>결제취소가   아닐 경우 0 <br>부분취소인경우, 가장 마지막건의 취소 시간                                                                                                                    |
| payMethod         | String  |   O   |   10   | 결제수단<br><br>CARD:신용카드, VBANK:가상계좌,<br>naverpay=네이버페이, kakaopay=카카오페이, payco=페이코, ssgpay=SSGPAY, samsungpay=삼성페이                                                                          |
| amount            |   Int   |   O   |   12   | 결제 금액                                                                                                                                                                                    |
| balanceAmt        |   Int   |   O   |   12   | 취소 가능 잔액<br><br>부분취소   거래인경우, 전체금액에서 현재까지 취소된 금액을 차감한   금액.                                                                                                                              |
| goodsName         | String  |   O   |   40   | 상품명                                                                                                                                                                                      |
| mallReserved      | String  |   　   |  500   | 상점 정보 전달용   예비필드<br><br>returnUrl로 redirect되는   시점에 반환 됩니다.<br>JSON   string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                |
| useEscrow         | Boolean |   O   |   -    | 에스크로 거래 여부<br><br> false:일반거래 / true:에스크로 거래                                                                                                                                             |
| currency          | String  |   O   |   3    | 결제승인화폐단위<br><br> KRW:원화, USD:미화달러, CNY:위안화                                                                                                                                               |
| channel           | String  |   　   |   10   | pc:PC결제, mobile:모바일결제<br><br>['pc',   'mobile', 'null']                                                                                                                                  |
| approveNo         | String  |   　   |   30   | 제휴사 승인   번호<br><br>신용카드, 계좌이체, 휴대폰                                                                                                                                                       |
| buyerName         | String  |   　   |   30   | 구매자 명                                                                                                                                                                                    |
| buyerTel          | String  |   　   |   40   | 구매자 전화번호                                                                                                                                                                                 |
| buyerEmail        | String  |   　   |   60   | 구매자 이메일                                                                                                                                                                                  |
| issuedCashReceipt | Boolean |   　   |   -    | 현금영수증 발급여부<br><br>true:발행 / false:미발행                                                                                                                                                    |
| receiptUrl        | String  |   　   |  200   | 　매출전표 확인 URL                                                                                                                                                                             |
| mallUserId        | String  |   　   |   20   | 상점에서 관리하는 사용자   아이디                                                                                                                                                                      |

<br>

#### 할인정보 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |           |  Type   |  필수   |  　Byte  | 설명            |
|:----------|:----------|:-------:|:-----:|:-------:|:--------------|
| coupon    | 　         | Object  |   　   |    -    | 즉시할인 프로모션 정보  |
|           | couponAmt |   Int   |   　   |   12    | 즉시할인 적용된 금액   |

<br>

#### 카드 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |                |   Type    |  필수   |  　Byte  | 설명                                                                                                 |
|:----------|:---------------|:---------:|:-----:|:-------:|:---------------------------------------------------------------------------------------------------|
| card      | 　              |  Object   |   　   |    　    | 신용카드 정보                                                                                            |
| 　         | cardCode       |  String   |   O   |    3    | 신용카드사별 코드                                                                                          |
|           | cardName       |  String   |   O   |   20    | 결제 카드사 이름<br>예) 비씨                                                                                 |
|           | cardNum        | String  | 　   | 20     | 카드번호<br>앞 6자 마지막 4자를 제외한 가운데 숫자 마스킹 처리됨<br>예) 536112******1234<br>- 카카오머니/네이버포인트/페이코포인트 전액결제 거래인경우   null |
|           | cardQuota      |    Int    |   O   |    3    | 할부개월<br>0:일시불, 2:2개월, 3:3개월   …                                                                    |
|           | isInterestFree |  Boolean  |   O   |    -    | 상점분담무이자 여부<br>true:무이자,   false:일반                                                                 |
|           | cardType       |  String   |   　   |    1    | 카드 구분<br> credit:신용,   check:체크                                                                    |
|           | canPartCancel  |  String   |   O   |    -    | 부분취소 가능 여부<br>true:가능,   false:불가능                                                                 |
|           | acquCardCode   |  String   |   O   |    3    | 매입카드사코드                                                                                            |
|           | acquCardName   |  String   |   O   |   100   | 매입카드사명                                                                                             |

<br>

#### 현금영수증 <img src="https://img.shields.io/badge/-Array-blueviolet"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter     |              |   Type   |   필수   |  Byte  | 설명                                                                                                                                                                                                                                                                                                                                                                                                          |
|:--------------|:-------------|:--------:|:------:|:------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cashReceipts  | 　            |  Array   |   　    |   　    | 현금영수증 발급정보<br>-NaverPay-포인트 ,가상계좌 입금건에서 제공<br>-부분 취소시, 2건이상 존재가능                                                                                                                                                                                                                                                                                                                                            |
| 　             | receiptTid   |  String  |   O    |   30   | 현금영수증 TID                                                                                                                                                                                                                                                                                                                                                                                                   |
|               | orgTid       |  String  |   O    |   30   | 연관된 원 승인/취소 거래 TID<br>부분취소시, 원 부분취소   거래건의 TID와 매핑됨<br>- 원거래를 부분취소 하면,   신규 TID가 채번되고,<br>채번된 부분취소 TID가   셋팅 됩니다.                                                                                                                                                                                                                                                                                           |
|               | status       |  String  |   O    |   20   | 발급진행 상태<br><br>[발급]<br>issueRequested : 발급 접수 완료[1,3]<br>issueReqCancelled : 요청회수(국세청 발행 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>issued : 국세청 발급 완료[4]<br>issueFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10])<br><br>[취소]<br>cancelRequested : 취소 접수 완료[1,3]<br>cancelReqCancelled : 요청회수(국세청 취소 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>cancelled : 국세청 취소 완료[4]<br>cancelFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10]) |
|               | amount       |   Int    |   O    |   12   | 현금영수증 발행 총금액                                                                                                                                                                                                                                                                                                                                                                                                |
|               | taxFreeAmt   |   Int    |   O    |   12   | 현금영수증 전체 금액중에서 면세금액                                                                                                                                                                                                                                                                                                                                                                                         |
|               | receiptType  |  String  |   O    |   20   | 현금영수증 타입<br>individual : 개인 소득공제용<br>company : 사업자 지출증빙용                                                                                                                                                                                                                                                                                                                                                    |
|               | issueNo      |  String  |   O    |   30   | 현금영수증 국세청 발행번호                                                                                                                                                                                                                                                                                                                                                                                              |
|               | receiptUrl   |  String  |   O    |  200   | 현금영수증 매출전표 확인 URL                                                                                                                                                                                                                                                                                                                                                                                           |

<br>

#### 계좌이체 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">


| Parameter |          | Type   | 필수  | Byte | 설명               |
|-----------|----------|--------|-----|------|------------------|
| bank      | 　        | Object | 　   | 　    | 은행 정보            |
| 　         | bankCode | String | O   | 3    | 결제은행코드 (은행코드 참조) |
|           | bankName | String | O   | 20   | 결제은행명 (euc-kr)   |

<br>

#### 가상계좌 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">


| Parameter |              | Type   | 필수 | Byte | 설명                        |
|-----------|--------------|--------|------|------|-----------------------------|
| vbank     | 　           | Object | 　   | 　   | 가상계좌 정보               |
| 　        | vbankCode    | String | O    | 3    | 입금받을 가상계좌 은행코드  |
|           | vbankName    | String | O    | 20   | 입금받을 가상계좌 은행명    |
|           | vbankNumber  | String | O    | 20   | 입금받을 가상계좌 번호      |
|           | vbankExpDate | String | O    | -    | 가상계좌 입금 만료일<br>ISO 8601                    |
|           | vbankHolder  | String | O    | 40   | 입금받을 가상계좌 예금주명  |


## 결제 인증 (Client 승인 모델)

- 결제자가 브라우저에서 `pay.nicepay.co.kr/v1/js/` JS SDK의 `AUTHNICE.requestPay()` method 호출시 결제창이 노출 됩니다.
- 결제자는 결제창을 통해 카드사 및 결제 원천사에 접근하여 인증과정을 진행 하고 나이스페이는 인증결과를 `AUTHNICE.requestPay()`의 object value로 전달된 `returnUrl`로 POST 합니다.
- 가맹점은 POST 데이터의 금액 및 위변조 여부를 체크하고 응답된 tid을 승인 API로 전달 하면 💳 결제(승인)요청 처리가 완료 됩니다.

<br>

> #### ⚠️ 중요
> [클라이언트 키](클라이언트-키)가 Client 승인 방식으로 발급 된 경우 Client승인 모델 💡 결제창 사용이 가능 합니다.  
> 대량 결제 트래픽이 예상되는 경우 Server승인 모델 💡 결제창을 사용 해주세요.  
> 금액 변조 검증 미처리로 인한 모든 책임은 가맹점에 있습니다.

<br>

### Over-view
<img src="../image/payment-client-authorization.svg" width="800px">

### 예외처리
- `Http client`의 구성 없이 Client JS SDK 요청으로 💳 결제(승인)이 처리되는 단순화된 모델입니다.
- `client-side`에서 금액이 변조된 경우 변조된 금액으로 💳 결제(승인)이 발생 할 수 있습니다.
- 반드시 응답전문의 금액, 주문번호, 위변조검증 `signature`를 체크 해주세요.
- 금액검증은 [승인 금액 검증 API](#승인-금액-검증) 를 활용하면 체크가 편리 합니다.

<br>


### 샘플 코드

```html
<script src="https://pay.nicepay.co.kr/v1/js/"></script>
<script>
    function clientAuth() {
        AUTHNICE.requestPay({
            clientId: 'R1_af0d116236df437f831483ee9c500bc4',  // clientId에 따라 Server / Client 방식 분리
            method: 'card',
            orderId: 'your-unique-orderid',
            amount: 1004,
            goodsName: '나이스페이-상품',
            returnUrl: 'http://localhost:4567/serverAuth'
        });
    }
</script>
```

<br>

- 먼저 https://pay.nicepay.co.kr/v1/js/ 를 include 합니다.
- `clientId` 필드에 [클라이언트 키](#클라이언트-키) 값을 셋팅 하면 준비가 완료 됩니다.
- `AUTHNICE.requestPay()` method 호출시 결제창이 노출 됩니다.
- 결제(승인)결과는 `returnUrl`로 전달된 `end-point`로 post 됩니다.
- 응답된 post 데이터를 결제(승인)API로 전달하면 💳 결제(승인) 처리가 진행 됩니다.

<br>

> #### ⚠️ 중요
> Client 승인 모델을 사용하는 경우 모든 💳 결제(승인)건 별 금액 검증이 필요 합니다.
> 사용자 네트워크 환경에 따라 인터페이스 응답의 유실이 발생 할 수 있어 [승인금액 검증 API](승인-금액-검증)를 활용하여 금액체크를 반드시 해야 합니다.

<br>


### 요청 명세 (Client 승인 모델)

#### 공통

|   Parameter   |  type   | 필수  | byte | 설명                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:-------------:|:-------:|:---:|:----:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   clientId    | String  |  O  | 50	  | 가맹점 식별코드, NICEPAY가 발급한 가맹점 식별 값 		                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 
|    method     | String  |  O  | 20	  | 결제수단 <br> card : 신용카드 <br> bank : 계좌이체 <br> directCard : 결제창 없이 카드사 바로 노출  <br> vbank : 가상계좌  <br> cellphone : 휴대폰 <br>naverpayCard : 네이버페이-신용카드 전액결제(포인트 이용불가) <br> kakaopay : 카카오페이(카드전액 또는 포인트전액) <br>kakaopayCard : 카카오페이-신용카드 전액결제 <br>kakaopayMoney : 카카오페이-머니 전액결제 <br>samsungpayCard : 삼성페이 카드전액 결제 <br>payco : 페이코 <br>ssgpay : SSGPAY <br>cardAndEasyPay : 신용카드와 간편결제 노출 <br>*cardAndEasyPay인 경우, 아래 파라미터와 함께 사용불가* <br> - cardCode, cardQuota, shopInterest, quotaInterest | 
|    orderId    | String  |  O  | 64	  | 상점 거래 고유번호<br> 결제된 orderId로 재호출 불가                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 
|    amount     | Int  	  |  O  | 12	  | 결제금액 (숫자만)		                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 
|   goodsName   | String  |  O  | 40	  | 상품명<br> - doubleQuota(")와 pipLine(&brvbar;) 2가지 특수문자는 '-'로 대체 됩니다.                                                                                                                                                                                                                                                                                                                                                                                                                    | 
|   returnUrl   | String  |  O  | 500	 | 인증 처리 후 redirect 되는 url 		                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 
| mallReserved  | String  |     | 500	 | 상점 정보 전상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                                                                                                                                                                                                                                                                                                                | 
|  mallUserId   | String  |     | 20	  | 상점에서 관리하는 사용자 아이디 		                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 
|   buyerName   | String  |     | 30	  | 구매자 이름 		                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 
|   buyerTel    | String  |     | 40	  | 구매자 전화번호<br> (-) 없이 숫자만 입력 		                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 
|  buyerEmail   | String  |     | 60	  | 구매자 이메일 		                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 
|   useEscrow   | Boolean |     |  -	  | true: 에스크로 거래 / false: 일반거래(default) 		                                                                                                                                                                                                                                                                                                                                                                                                                                               | 
|   currency    | String  |     |  3	  | KRW:원화, USD:미화달러, CNY:위안화 		                                                                                                                                                                                                                                                                                                                                                                                                                                                          | 
|  logoImgUrl   | String  |     | 100	 | 로고 이미지의 full URL 전달<br>  ex) https://youre.site.com/image/logo.jpg<br> *채널별 사이즈 (단위 : pixel)*<br>모바일 : width 50 X height 50<br> 웹표준 : width 94 X height 25                                                                                                                                                                                                                                                                                                                            | 
|   language    | String  |     |  2	  | EN : 영문 / CN : 중문 / KO : 국문(Default)<br>NICEPAY 결제창 내 다국어를 지원<br>*sample)*<br>lang=EN -> 결제창 영문표기<br>lang=CN -> 결제창 중문표기                                                                                                                                                                                                                                                                                                                                                              | 
| returnCharSet | String  |     | 10	  | 가맹점 서버의 encoding 방식 전달<br> - utf-8(Default) / euc-kr		                                                                                                                                                                                                                                                                                                                                                                                                                                | 
|   skinType    | String  |     | 10	  | 결제창 스킨 설정<br>지원 옵션 red/green/purple/gray/dark                                                                                                                                                                                                                                                                                                                                                                                                                                         | 

<br>

#### 부가세 지정금액

| Parameter  | type | 필수  | byte | 설명                                     |
|:----------:|:----:|:---:|:----:|:---------------------------------------|
| taxFreeAmt | Int  |     | 12	  | 전체 거래금액(amount)중에서 면세에 해당하는 금액을 설정합니다. | 

<br>

#### 신용카드 & 간편결제

|  Parameter  |  type  | 필수  | byte | 설명                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:-----------:|:------:|:---:|:----:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  cardQuata  | String |     | 100	 | 할부개월 설정<br><br>[공통]<br>선택할 수 있는 할부기간을 제한한다.<br><br>[카드일반+PAYCO+네이버페이]<br>- 단독 설정 가능<br>- ','를 구분자로 할부개월 나열<br>- 일시불은 반드시 "00"으로 설정할것<br>- 2자리의 할부기간 설정 (3개월일 경우 반드시 '03' 으로 설정)<br>Ex) cardQuota=03 <br>- 설명 : 3 개월 할부만 가능하도록 함.<br>최소금액 : 50,000원 이상<br><br>[카카오페이, 삼성페이, SSGPAY]<br> - 단독 설정 사용불가. 반드시 cardCode와 함께 설정되어야 사용가능.<br> - 할부개월 복수설정 불가                                                                                                                                                                                                                                                                                                                                                           | 
|  cardCode   | String |     | 100	 | 특정카드사 선택옵션<br><br>[공통]<br>이용할 수 있는 카드 리스트를 제한 (코드집-카드코드 참고)<br>- 단독 설정 가능<br><br>[카드일반]<br>- ','를 구분자로 카드코드 나열<br>Ex1) cardCode=02<br>-> 국민 카드만 이용할 수 있도록 제한<br>Ex2) cardCode=02,04<br>-> 국민,삼성 카드만 이용할 수 있도록 제한<br><br>[간편결제]<br>- 복수설정 불가<br>- 카카오페이와 PAYCO는 각 간편결제에서 카드만 이용 가능함.<br>카카오페이는 카카오Money 이용불가, PAYCO는 페이코포인트 이용불가<br>  ex) cardCode = 06 (카드사 복수설정 불가)<br><br>*간편결제별 이용가능 카드리스트<br>*- 삼성페이 : 비씨,국민,하나(외환),삼성,신한,현대,롯데,NH,하나<br>- 카카오페이: 비씨,국민,하나(외환),삼성,신한,현대,롯데,씨티,NH,하나<br>- PAYCO : 비씨,국민,하나(외환),삼성,신한,현대,롯데,씨티,NH,하나,한미,신세계한미,수협,신협,우리,광주,전북,제주,해외비자,해외마스터,해외JCB,저축은행,은련,KDB산업,카카오뱅크<br>- SSGPAY : 비씨,국민,하나(외환),삼성,신한,현대,롯데,씨티,NH,하나,전북,케이뱅크<br>- 네이버페이 : 신한, 비씨, 국민, NH, 롯데, 삼성, 씨티, 하나, 현대 | 
| cardShowOpt | String |     | 50	  | 카드사별 인증창 호출방식 옵션<br><br>카드사별 호출방식 정의하여 카드사로 전달<br>- 1:안심클릭, 2:간편결제, 3:앱카드직접 호출<br>- '&brvbar;'를 구분자로 카드코드 나열<br>- 카드코드:노출유형&brvbar;카드코드:노출유형<br>ex) CardShowOpt=08:3&brvbar;02:3<br>- 이용가능 카드사목록 : 02(국민), 04(삼성), 06(신한), 07(현대), 08(롯데), 12(NH), 15(우리)                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 

<br>

#### 가상계좌

| Parameter        |   Type   |   필수   |  Byte  | 설명                                                                                                                                                                     |
|:-----------------|:--------:|:------:|:------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vbankHolder      |  String  |  가상계좌  |   40   | 가상계좌 (가맹점 상호명, 사용자명)                                                                                                                                                   |
| vbankValidHours  |   Int    |        |   4    | 가상계좌 유효시간<br>- 시간단위로 입력.<br>- Default 값 D+7일<br>- vbankValidHours와 vbankExpDate가 함께 요청된경우 vbankValidHours가 우선함<br>ex) 10 을 입력하면, 가상계좌 발급후 10시간동안 해당 가상계좌를 이용할 수 있습니다.  |
| vbankExpDate	    |   Int    |        |        | 가상계좌 입금 만료일                                                                                                                                                            |

<br>

#### 휴대폰

| Parameter  |  Type  |   필수    |  Byte  | 설명             |
|:-----------|:------:|:-------:|:------:|:---------------|
| isDigital  |  Int   |  휴대폰결제  |   1    | 0: 컨텐츠, 1: 실물  |

<br>

#### 현금영수증

| Parameter         |  Type  |    필수     | Byte | 설명                                                                                                                                                                                                                                           |
|:------------------|:------:|:---------:|:----:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| directReceiptType | String |           |  20  | 현금영수증 발급 유형<br>unPublished : 미발행<br>individual : 개인 소득공제용<br>company : 사업자 지출증빙용                                                                                                                                                             |
| directReceiptNo   | String | 네이버페이-포인트 |  20  | 현금영수증 발행대상 식별정보<br>휴대폰번호(10 자리 또는 11 자리) 또는 사업자번호(10 자리)<br>* directReceiptType 이 individual 또는 company 인 경우 필수<br>* directReceiptType 이 individual 인경우 휴대폰번호를 입력합니다.<br>* directReceiptType 이 company 인경우 사업자번호를 입력합니다.<br> * '-'없이 숫자만 입력  |

<br>

#### PC 옵션

| Parameter       |   Type    |   필수   |  Byte  | 설명                                                                                                                                   |
|:----------------|:---------:|:------:|:------:|:-------------------------------------------------------------------------------------------------------------------------------------|
| disableScroll   |  Boolean  |        |   -    | 결제창 스크롤 생성여부<br><br>true : 스크롤 생성 안함(Default : true)<br>false : 스크롤 생성                                                               |
| disableEdgeChk  |  Boolean  |        |   -    | Edge브라우저 가이드Alert 예외 여부<br><br>true : Edge브라우저 가이드문구 노출안함<br> false : Edge브라우저 가이드문구 노출(Default : false)                             |
| zIdxHigher      |  Boolean  |        |   -    | NICEPAY Layer z-index 조정 여부<br>true : NICEPAY Layer의 최하단 z-index를 11000 으로 설정<br>false : default z-index로 9999가 설정됨(Default : false) |

<br>

#### Mobile 옵션

| Parameter  |   Type   |  필수   |  Byte  | 설명                                                                                                                                                                                                                              |
|:-----------|:--------:|:-----:|:------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| appScheme  |  String  |       |  200   | 모바일 App Scheme 값 (APP 연동인 경우만 사용)<br>가맹점 독립 APP을 이용하여 개발시 (Webview 연동)<br>카드사를 포함한 제휴사 인증 완료 후 결과에대한 focus가 <br>가맹점 APP으로 돌아오기 위해 설정하는 가맹점 APP의 scheme 값을 설정<br>예) 가맹점 App 스킴이 nicepaysample인 경우<br>appScheme=nicepaysample://  |

<br>

### 응답 명세 (Client 승인 모델)

```bash
POST
Content-type: application/x-www-form-urlencoded
```

| Parameter          |   Type    |   필수   | Byte  | 설명                                                                                                                                                                                        |
|:-------------------|:---------:|:------:|:-----:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| success            |  Boolean  |        |       | 결제 성공 여부<br><br>true : 결제성공 또는 가상계좌 채번 성공, false:결재실패 또는 인증실패                                                                                                                             |
| authToken          |  String   |   O    |  40   | 인증 TOKEN<br><br>인증거래 Unique Key<br>- 인증 실패된 거래의 가맹점과 NICE간의 매핑 키로 사용 가능합니다.                                                                                                               |
| tid                |  String   |        |  30   | 결제 승인 키<br><br>인증성공후 승인이 시도된 경우 리턴됩니다.<br>승인(가상계좌-채번)에 사용된 NICEPAY 거래키 입니다.<br>- 승인성공 또는 승인실패 : tid<br>- 인증실패 : "" (빈값)                                                                   |
| orderId            |  String   |   O    |  64   | 상점 거래 고유번호                                                                                                                                                                                |
| clientId           |  String   |   O    |  50   | 가맹점 식별코드<br>NICEPAY가 발급한 가맹점 식별값                                                                                                                                                          |
| mallReserved       |  String   |        |  500  | 상점 예약필드<br><br>상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                            |
| resultCode         |  String   |   O    |   4   | 처리결과코드<br><br>0000 : 성공 / 그외 실패                                                                                                                                                           |
| resultMsg          |  String   |   O    |  100  | 처리결과메시지                                                                                                                                                                                   |
| amount             |    Int    |   O    |  12   | 결제 금액                                                                                                                                                                                     |
| goodsName          |  String   |   O    |  40   | 상품명<br><br>상품이름 (", * 특수문자 이용불가)                                                                                                                                                          |
| channel            |  String   |   O    |  10   | pc:PC결제, mobile:모바일결제                                                                                                                                                                     |
| status             |  String   |        |  20   | 결제 처리상태<br><br>paid:결제완료, ready:준비됨(가상계좌채번), failed:결제실패, cancelled:취소됨, partialCancelled:부분 취소됨, expired:만료됨<br>['paid', 'ready', 'failed', 'cancelled', 'partialCancelled', 'expired']  |
| ediDate            |  String   |        |   -   | 응답전문생성일시 <br><br>ISO 8601 형식                                                                                                                                                              |
| signature          |  String   |        |  256  | 위변조 검증 데이터<br><br>- 승인 성공 거래건에 한하여 응답<br>- 생성규칙 : hex(sha256(tid + amount + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.     |
| paidAt             |  String   |        |   -   | 결제완료시점<br><br>ISO 8601 형식<br> 결제완료가 아닐 경우 0                                                                                                                                               |
| failedAt           |  String   |        |   -   | 결제실패시점<br><br>ISO 8601 형식<br>결제실패가 아닐 경우 0                                                                                                                                                |
| payMethod          |  String   |   O    |  10   | 결제수단<br><br>card:신용카드, vbank:가상계좌,<br>naverpay=네이버페이, kakaopay=카카오페이, payco=페이코, ssgpay=SSGPAY, samsungpay=삼성페이                                                                           |
| useEscrow          |  Boolean  |        |   -   | 에스크로 거래 여부<br><br>false:일반거래 / true:에스크로 거래                                                                                                                                               |
| currency           |  String   |        |   3   | 결제승인화폐단위<br><br>KRW:원화, USD:미화달러, CNY:위안화                                                                                                                                                 |
| approveNo          |  String   |        |  30   | 제휴사 승인 번호<br>신용카드, 계좌이체, 휴대폰                                                                                                                                                              |
| couponAmt          |    Int    |        |  12   | 즉시할인 적용된 금액                                                                                                                                                                               |
| buyerName          |  String   |        |  30   | 구매자 명                                                                                                                                                                                     |
| buyerTel           |  String   |        |  40   | 구매자 전화번호                                                                                                                                                                                  |
| buyerEmail         |  String   |        |  60   | 구매자 이메일                                                                                                                                                                                   |
| issuedCashReceipt  |  Boolean  |        |   -   | 현금영수증 발급여부<br><br>true:발행 / false:미발행                                                                                                                                                     |
| receiptUrl         |  String   |        |  200  | 매출전표 확인 URL                                                                                                                                                                               |
| mallUserId         |  String   |        |  20   | 상점 사용자 아이디<br><br>상점에서 관리하는 사용자 아이디                                                                                                                                                       |
| cardCode           |  String   |        |   3   | 결제 카드사 코드                                                                                                                                                                                 |
| cardName           |  String   |        |  20   | 결제 카드사 이름                                                                                                                                                                                 |
| cardQuota          |    Int    |        |   3   | 할부개월<br><br>0:일시불, 2:2개월, 3:3개월 …                                                                                                                                                         |
| isInterestFree     |  Boolean  |        |   -   | 상점분담무이자 여부                                                                                                                                                                                |
| cardType           |  String   |        |   1   | 카드 구분                                                                                                                                                                                     |
| canPartCancel      |  String   |        |   -   | 부분취소 가능 여부                                                                                                                                                                                |
| acquCardCode       |  String   |        |   3   | 매입카드사코드                                                                                                                                                                                   |
| acquCardName       |  String   |        |  100  | 매입카드사명                                                                                                                                                                                    |
| vbankCode          |  String   |        |   3   | 입금받을 가상계좌 은행코드                                                                                                                                                                            |
| vbankName          |  String   |        |  20   | 입금받을 가상계좌 은행명                                                                                                                                                                             |
| vbankNumber        |  String   |        |  20   | 입금받을 가상계좌 번호                                                                                                                                                                              |
| vbankExpDate       |  String   |        |   -   | 가상계좌 입금 만료일<br><br>ISO 8601                                                                                                                                                               |
| vbankHolder        |  String   |        |  40   | 입금받을 가상계좌 예금주명                                                                                                                                                                            |
| bankCode           |  String   |   O    |   3   | 결제은행코드(은행 코드 참조)                                                                                                                                                                          |
| bankName           |  String   |   O    |  20   | 결제은행명(euc-kr)                                                                                                                                                                             |

<br>

## 승인 금액 검증

- Client승인 모델의 💡 결제창을 통해 결제 후 결제금액 체크에 대한 가이드 입니다.
- 결제자는 💡 결제창을 통해 카드사 및 결제 원천사에 접근하여 인증과정을 진행 하고 나이스페이는 인증 및 💳 결제(승인) 처리 후 결과를 `AUTHNICE.requestPay()`의 object value로 전달된 `returnUr`l로 POST 합니다.
- 이후 금액 위변조 여부 검증을 위해 '승인 금액 검증' API를 활용하여 💳 승인(결제)금액을 체크를 진행 합니다.
- 발생된 승인(결제)응답의 금액과 승인금액검증 체크를 통한 금액이 상이한 경우 반드시 결제취소 진행 해야 합니다.

> #### ⚠️ 중요
> Client승인 모델의 💡 결제창은 💳 승인(결제)금액 검증을 반드시 해야 합니다.
> 💳 승인(결제)금액 체크를 하지 않아 발생하는 문제의 책임은 가맹점에게 있습니다.

<br>

### Over-view
<img src="../image/payment-client-authorization-check.svg" width="800px"> 

### 샘플 코드

```bash
curl -X POST 'https://api.nicepay.co.kr/v1/check-amount/nicuntct1m0101210727200708A058' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3Zjgz...' 
-D '{
    "amount" : 1004
}' 
```

<br>

### 요청 명세

```bash
POST /v1/check-amount/{tid}  
HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials> or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter     |  Type  |  필수   |  Byte  | 설명                                                                                                              |
|:--------------|:------:|:-----:|:------:|:----------------------------------------------------------------------------------------------------------------|
| amount        |  Int   |   O   |   12   | 결제금액                                                                                                            |
| ediDate       | String |   　   |   -    | 전문생성일시<br>ISO 8601 형식                                                                                           |
| signData      | String |   　   |  256   | 위변조 검증 Data<br>생성규칙 : hex(sha256(tid + amount + ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| returnCharSet | String |   　   |   10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br> utf-8(Default) / euc-kr                                             |

<br>

### 응답 명세

```bash
POST
Content-type: application/json
```

| Parameter  | Type  |  필수   |  Byte  | 설명                                                                                                                                                                              |
|:-----------|:-----:|:-----:|:------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| resultCode |   S   |   O   |   4    | 결과코드<br> 0000 : 성공 / 그외 실패                                                                                                                                                      |
| resultMsg  |   S   |   O   |  100   | 결과메시지                                                                                                                                                                           |
| ediDate    |   S   |       |   -    | 응답전문생성일시 ISO 8601 형식                                                                                                                                                            |
| signature  |   S   |   O   |  256   | 위변조 검증 데이터<br> - 유효한 거래건에   한하여 응답<br> - 생성규칙 :   hex(sha256(tid + ediDate + SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br> - SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| isValid    |   B   |   O   |   -    | 결제금액 일치여부<br>true : 일치 /   false : 불일치(Default)<br>- "resultCode=0000 & isValid=false"로 응답 받은경우 금액이 변조된것으로 판단하고, 거래를취소 하시기 바랍니다.                                                |
| tid        |   S   |   O   |   30   | 검증한 결제 승인 키<br>검증에 사용된 NICEPAY 거래키<br>-   URI에 요청된 리소스의 tid가 그대로 응답 됩니다.                                                                                                        |


## 빌링

- [빌키발급](#빌키-발급)
- [빌키승인](#빌키-승인)
- [빌키삭제](#빌키-삭제)

<br>

## 빌키 발급

빌링 서비스는 정기결제(한번의 카드 등록을 통해 반복적인 결제)를 구현할 수 있는 서비스 입니다.  
빌링 서비스는 크게 3가지 파트 [빌키발급](#빌키발급), [빌키승인](#빌키승인), [빌키삭제](#빌키삭제) 부분으로 나뉘어 설명되며,  
각 파트의 명세와 샘플코드를 활용하면 쉽게 구현이 가능 합니다.    
빌키 발급은 결제자의 카드정보를 암호화된 키값으로 변환하는 과정 입니다.  
결제자의 카드정보를 암호화 하여 `/v1/subscribe/regist` API를 호출하면  
나이스페이는 카드정보를 암호화된 형태로 저장 하고 카드정보에 맵핑된 bid(빌키)를 응답 합니다.  
정기결제가 필요한 시점에 가맹점이 bid(빌키)를 빌키승인 API로 전달 하면 등록된 카드로 💳 결제(승인)이 발생 됩니다.

> #### ⚠️ 중요
> 1개의 카드로 n개 빌키 생성이 가능하며 정상 발급된 빌키는 모두 사용이 가능 합니다.

<br>

### Over-view
<img src="../image/payment-subscribe-regist.svg" width="800px"> 

### 샘플 코드

```bash
curl -X POST 'https://api.nicepay.co.kr/v1/subscribe/regist' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic ZWVjOGQzNTA4Y2IwNDI1ZGI5NTViMzBiZjM5...' 
-D '{
    "encData": "C41346B71984...",
    "orderId": "merchant-order-id",
    "encMode" : "A2"
}'
```

### 요청 명세 (Body)

```bash
POST /v1/subscribe/regist  
HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials> or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter     |  Type  | 필수  | Byte | 설명                                                                                                                                                                                                                                                                   |
|:--------------|:------:|:---:|:----:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| encData       | String |  O  | 512  | 결제정보 암호화 데이터<br>- 암호화 알고리즘 :   AES128<br>- 암호화 상세 :   AES/CBC/PKCS5padding<br>- 암호결과 인코딩 :   Hex Encoding<br>- 암호 KEY :   SecretKey 앞 16자리<br>- IV : SecretKey 앞 16자리<br>-   Hex(AES(cardNo=value&expYear=YY&expMonth=MM&idNo=value&cardPw=value))<br>*상세 명세는 하단 참조* |
| orderId       | String |  O  |  64  | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호                                                                                                                                                                                                                        |
| buyerName     | String |  　  |  30  | 구매자                                                                                                                                                                                                                                                                  |
| buyerEmail    | String |  　  |  60  | 구매자 이메일주소                                                                                                                                                                                                                                                            |
| buyerTel      | String |  　  |  20  | 구매자 전화번호<br> '-' 없이 숫자만 입력                                                                                                                                                                                                                                           |
| encMode       | String |  　  |  10  | 암호화 모드<br>encData 필드의 암호화 알고리즘 정의<br><br> A2 : AES256<br>•암호화 알고리즘 : AES256<br>•암호화 상세 : AES/CBC/PKCS5padding <br>•암호결과 인코딩 : Hex Encoding <br> •암호 KEY : SecretKey (32byte)<br>•IV : SecretKey 앞 16자리                                                               |
| ediDate       | String |  　  |  -   | 전문생성일시<br> ISO 8601 형식                                                                                                                                                                                                                                               |
| signData      | String |  　  | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(orderId + ediDate +   SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.                                                                                                                                                          |
| returnCharSet | String |  　  |  10  | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                                                                                                                                                                               |


<br>

### encData 필드 상세정보

| Parameter  |   Type   |     필수     |  Byte  | 설명                                        |
|:-----------|:--------:|:----------:|:------:|:------------------------------------------|
| cardNo     |  String  |     O      |   16   | 카드번호<br>숫자만 입력                            |
| expYear    |  String  |     O      |   2    | 유효기간(년)<br>포멧 : YY                        |
| expMonth   |  String  |     O      |   2    | 유효기간(월)<br>포멧 : MM                        |
| idNo       |  String  |  계약<br>옵션  |   13   | 개인 : 생년월일(6)/YYMMDD <br/> 법인 : 사업자번호(10)  |
| cardPw     |  String  |  계약<br>옵션  |   2    | 카드 비밀번호<br>비밀번호 앞 2자리                     |

<br>

### encData 필드 암호화 예시 (AES-128)

```bash
- 평문  : cardNo=1234567890123456&expYear=25&expMonth=12&idNo=800101&cardPw=12
- 암호키 : 2dcc2a0d63bf4694 (SecretKey 앞16자리)
- IV : 2dcc2a0d63bf4694 (SecretKey 앞16자리)
- 암호화결과 : `2127975b6d82c36136ba8197a997a994f6c086ff75a6d35e514c54a1e686545e60b76f11bec706de1082e43dd74ae5c5f0709dc1eca6c3cd20e1c0e9e9b7a85c6505461c91c865d82072e41ba5284bd7`
```

<br>

### encData 필드 암호화 예시 (AES-256)
```bash
- 평문 : cardNo=1234567890123456&expYear=25&expMonth=12&idNo=800101&cardPw=12
- 암호키 : 2dcc2a0d63bf469490bb19a201be3735
- IV  : 2dcc2a0d63bf4694 (SecretKey 앞16자리)
- 암호화결과 : `6ecfe97e521bc67c3053d74a9dbdba53033d343fc9e8e38e730964b22ef2e4a59607171b00a9da977141b3f79fffa1e80a16c08bc58666b479f554a966a363414347e62f2621f8df220c7a4a545592d0`
```

<br>

### 응답 명세 (Body)

```bash
POST
Content-type: application/json
```

| Parameter  | Type  |  필수   | Byte  | 설명                                                                                                                                                         |
|:-----------|:-----:|:-----:|:-----:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| resultCode |   S   |   O   |   4   | 결제결과코드<br>0000 : 성공 / 그외 실패                                                                                                                                |
| resultMsg  |   S   |   O   |  100  | 결제결과메시지<br>예시) 빌키가 정상적으로 생성되었습니다.                                                                                                                          |
| tid        |   S   |   O   |  30   | 거래번호<br>거래를 구분하는 transaction ID<br>예시) nictest00m01011104191651325596                                                                                      |
| orderId    |   S   |   O   |  64   | 상점 거래 고유번호                                                                                                                                                 |
| bid        |   S   |   　   |  30   | 빌키<br>NICEPAY가 발급하는 빌링 아이디<br>가맹점 DB 저장하여, 빌링승인   API 요청시 전달<br> - 회원   카드 정보와 매핑되어 관리되는 Key 값으로, 빌키승인   API 호출시 전달<br>예시) BIKYnictest00m1104191651325596  |
| authDate   |   S   |   　   |   -   | 인증일자<br>ISO 8601 형식                                                                                                                                        |
| cardCode   |   S   |   　   |   3   | 카드사 코드<br>신용카드사별 코드                                                                                                                                        |
| cardName   |   S   |   　   |  20   | 카드사 이름<br>예시) [삼성]                                                                                                                                         |

<br>


## 빌키 승인

- 빌키 승인은 발급된 bid(빌키)를 통해 💳 결제(승인) 처리를 의미 합니다.
- 등록된 빌키를 통해 `/v1/subscribe/{bid}/payments` API를 호출하면 💳 결제(승인) 처리가 됩니다.
- 빌키 승인을 위해 [빌키 발급](#빌키발급)과정의 선행이 필요 합니다.

<br>

### Over-view
<img src="../image/payment-subscribe-billing.svg" width="800px">  

### 샘플 코드

```bash
curl -X POST 'https://api.nicepay.co.kr/v1/subscribe/BIKYnicuntct2m2107272028532670/payments' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic ZWVjOGQzNTA4Y2IwNDI1ZGI5NTViMzBi...' 
-D '{
    "orderId": "merchant-order-id",
    "amount": 1004,
    "goodsName": ＂나이스상품",
    "cardQuota": 0,
    "useShopInterest": false
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

| Parameter       |   Type   |  필수   |  Byte  | 설명                                                                                                                     |
|:----------------|:--------:|:-----:|:------:|:-----------------------------------------------------------------------------------------------------------------------|
| orderId         |  String  |   O   |   64   | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br>결제된 orderId로   재호출 불가                                                 |
| amount          |   Int    |   O   |   12   | 결제 금액                                                                                                                  |
| goodsName       |  String  |   O   |   40   | 상품명                                                                                                                    |
| cardQuota       |   Int    |   O   |   2    | 할부개월<br> 0:일시불, 2:2개월, 3:3개월   …                                                                                       |
| useShopInterest | Boolean  |   O   |   -    | 상점분담무이자 사용여부 (현재 false만 사용 가능)<br>false : 유이자                                                                          |
| buyerName       |  String  |   　   |   30   | 구매자 이름                                                                                                                 |
| buyerTel        |  String  |   　   |   20   | 구매자 전화번호<br>하이픈(-) 없이 숫자만   입력                                                                                         |
| buyerEmail      |  String  |   　   |   60   | 구매자 이메일                                                                                                                |
| taxFreeAmt      |   Int    |   　   |   12   | 면세공급가액<br>전체 거래금액(amount)중에서   면세에 해당하는 금액을 설정합니다.                                                                     |
| mallReserved    |  String  |   　   |  500   | 상점 정보 전달용 예비필드<br><br>승인응답 또는 webhook 시점에 요청 원문을 전달 합니다.<br> JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가  |
| ediDate         |  String  |   　   |   -    | 전문생성일시<br>ISO 8601 형식                                                                                                  |
| signData        |  String  |   　   |  256   | 위변조 검증 Data<br>생성규칙 : hex(sha256(orderId + bid +   ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.      |
| returnCharSet   |  String  |   　   |   10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                                 |

<br>

### 응답 명세 (Body)

```bash
POST
Content-type: application/json
```

| Parameter          |   Type    |   필수   |  Byte  | 설명                                                                                                                                                                                  |
|:-------------------|:---------:|:------:|:------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| resultCode         |  String   |   O    |   4    | 결제결과코드<br> 0000 : 성공 / 그외 실패                                                                                                                                                        |
| resultMsg          |  String   |   O    |  100   | 결제결과메시지                                                                                                                                                                             |
| tid                |  String   |   O    |   30   | 결제 승인 키<br>최초 승인(가상계좌-채번)에 성공한 원거래의 NICEPAY 거래키 입니다.                                                                                                                                |
| cancelledTid       |  String   |   　    |   30   | 취소 거래 키<br>NICEPAY가 발행하는 취소 응답 TID (부분취소시 tid와 다른 값이 응답됨)<br>- 취소   요청건에 한하여 응답됨<br>- cancels 객체에서 현재 취소된 거래정보를 찾을 때 사용 하시면 됩니다.                                                    |
| orderId            |  String   |   O    |   64   | 상점 거래 고유번호                                                                                                                                                                          |
| ediDate            |  String   |   O    |   -    | 응답전문생성일시 ISO 8601 형식                                                                                                                                                                |
| signature          |  String   |   　    |  256   | 위변조 검증 데이터<br>- 유효한 거래건에   한하여 응답<br>- 생성규칙 :   hex(sha256(tid + amount + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다. |
| status             |  String   |   O    |   20   | 결제 처리상태<br>paid:결제완료,   ready:준비됨, failed:결제실패, cancelled:취소됨, partialCancelled:부분 취소됨, expired:만료됨<br>['paid', 'ready', 'failed', 'cancelled', 'partialCancelled',   'expired']    |
| paidAt             |  String   |   O    |   -    | 결제완료시점 ISO 8601 형식<br>결제완료가 아닐 경우 0                                                                                                                                                 |
| failedAt           |  String   |   O    |   -    | 결제실패시점 ISO 8601 형식<br>결제실패가 아닐 경우 0                                                                                                                                                 |
| cancelledAt        |  String   |   O    |   -    | 결제취소시점 ISO 8601 형식결제취소가 아닐 경우 0 <br>부분취소인경우, 가장   마지막건의 취소 시간                                                                                                                       |
| payMethod          |  String   |   O    |   10   | 결제수단<br><br>card:신용카드,<br>vbank:가상계좌,<br>bank:계좌이체,<br>cellphone:휴대폰,<br>naverpay=네이버페이, kakaopay=카카오페이, samsungpay=삼성페이                                                            |
| amount             |    Int    |   O    |   12   | 결제 금액                                                                                                                                                                               |
| balanceAmt         |    Int    |   O    |   12   | 취소 가능 잔액<br>부분취소 거래인경우, 전체금액에서   현재까지 취소된 금액을 차감한 금액.                                                                                                                               |
| goodsName          |  String   |   O    |   40   | 상품명                                                                                                                                                                                 |
| mallReserved       |  String   |   　    |  500   | 상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                     |
| useEscrow          |  Boolean  |   O    |   -    | 에스크로 거래 여부<br>false:일반거래 /   true:에스크로 거래                                                                                                                                           |
| currency           |  String   |   O    |   3    | 결제승인화폐단위<br>KRW:원화, USD:미화달러, CNY:위안화                                                                                                                                               |
| channel            |  String   |   　    |   10   | pc:PC결제, mobile:모바일결제<br>['pc', 'mobile', 'null']                                                                                                                                   |
| approveNo          |  String   |   　    |   30   | 제휴사 승인 번호<br>신용카드, 계좌이체, 휴대폰                                                                                                                                                        |
| buyerName          |  String   |   　    |   30   | 구매자 명                                                                                                                                                                               |
| buyerTel           |  String   |   　    |   20   | 구매자 전화번호                                                                                                                                                                            |
| buyerEmail         |  String   |   　    |   60   | 구매자 이메일                                                                                                                                                                             |
| issuedCashReceipt  |  Boolean  |   　    |   -    | 현금영수증 발급여부<br>true:발행 /   false:미발행                                                                                                                                                 |
| receiptUrl         |  String   |   　    |  200   | 매출전표 확인 URL                                                                                                                                                                         |
| mallUserId         |  String   |   　    |   20   | 상점에서 관리하는 사용자 아이디                                                                                                                                                                   |


<br>

#### 할인정보 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |           |  Type  |  필수   |  　Byte  | 설명            |
|:----------|:----------|:------:|:-----:|:-------:|:--------------|
| coupon    | 　         | Object |   　   |    -    | 즉시할인 프로모션 정보  |
| 　         | couponAmt |  Int   |   　   |   12    | 즉시할인 적용된 금액   |

<br>

#### 카드 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">


| Parameter  |                 |   Type    |   필수   |  　Byte   | 설명                                                                                           |
|:-----------|:----------------|:---------:|:------:|:--------:|:---------------------------------------------------------------------------------------------|
| card       | 　               |  Object   |   　    |    　     | 신용카드 정보                                                                                      |
| 　          | cardCode        |  String   |   O    |    3     | 신용카드사별 코드                                                                                    |
|            | cardName        |  String   |   O    |    20    | 결제 카드사 이름<br>예) 비씨                                                                           |
|           | cardNum        | String  | 　   | 20     | 카드번호<br>앞 6자 마지막 4자를 제외한 가운데 숫자 마스킹 처리됨<br>예) 536112******1234<br>- 카카오머니/네이버포인트/페이코포인트 전액결제 거래인경우   null |
|            | cardQuota       |    Int    |   O    |    3     | 할부개월<br>0:일시불, 2:2개월, 3:3개월   …                                                              |
|            | isInterestFree  |  Boolean  |   O    |    -     | 상점분담무이자 여부<br>true:무이자,   false:일반                                                           |
|            | cardType        |  String   |   　    |    1     | 카드 구분<br>credit:신용,   check:체크                                                               |
|            | canPartCancel   |  String   |   O    |    -     | 부분취소 가능 여부<br>true:가능,   false:불가능                                                           |
|            | acquCardCode    |  String   |   O    |    3     | 매입카드사코드                                                                                      |
|            | acquCardName    |  String   |   O    |   100    | 매입카드사명                                                                                       |

<br>


## 빌키 삭제

빌키 삭제는 발급된 bid(빌키)를 삭제는 과정을 의미 합니다.  
등록된 빌키를  통해 `/v1/subscribe/{bid}/expire` API를 호출하면 빌키 삭제 처리가 됩니다.  
삭제된 빌키는 복원과 💳 승인(결제)가 불가 합니다.

<br>

### Over-view
<img src="../image/payment-subscribe-expire.svg" width="800px">  

### 샘플 코드

``` bash
curl -X POST 'https://api.nicepay.co.kr/v1/subscribe/BIKYnicuntct2m2107272028532670/expire' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic ZWVjOGQzNTA4Y2IwNDI1ZGI5NTViMzBiZjM...' 
-D '{
    "orderId": "merchant-order-id"
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

| Parameter     |  Type  | 필수  | Byte  | 설명                                                                                                                 |
|:--------------|:------:|:---:|:-----:|:-------------------------------------------------------------------------------------------------------------------|
| orderId       | String |  O  |  64   | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호                                                                      |
| ediDate       | String |  　  |   -   | 전문생성일시<br> ISO 8601 형식                                                                                             |
| signData      | String |  　  |  256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(orderId + bid +   ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| returnCharSet | String |  　  |  10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                             |	

<br>

### 응답 명세 (Body)

```bash
POST
Content-type: application/json
```

| Parameter  |  TYPE   |  필수   |  크기   | 설명                                                             |
|:-----------|:-------:|:-----:|:-----:|:---------------------------------------------------------------|
| resultCode | String  |   O   |   4   | 결제결과코드<br>0000 : 성공 / 그외 실패                                    |
| resultMsg  | String  |   O   |  100  | 결제결과메시지<br>예시) 빌키가 정상적으로 생성되었습니다.                              |
| tid        | String  |   O   |  30   | 거래를 구분하는 transaction ID<br>예시) nictest00m01011104191651325596  |
| orderId    | String  |   O   |  64   | 상점 거래 고유번호                                                     |
| bid        | String  |   O   |  30   | 빌키<br>NICEPAY가 발급한 빌링 아이디                                      |
| authDate   | String  |   　   |   -   | ISO 8601 형식<br>처리에 성공한경우 리턴됩니다.                                |


## 현금영수증	

- [현금영수증 발급](#현금영수증-발급)
- [현금영수증 취소](#현금영수증-취소)
- [현금영수증 조회](#현금영수증-조회)

### 현금영수증 발급

현금영수증은 [발급](#현금영수증-발급), [취소](#현금영수증-취소), [조회](#현금영수증-조회) 과정을 통해 관리가 가능 합니다.  
현금영수증 발급요청이 성공하면 정보는 다음날 국세청으로 전달되고 현금영수증 발급을 처리를 진행 합니다.  
국세청의 발급 처리 기간을 고려하여 현금영수증 발급 요청 성공 ⏱️ D+2일 기준으로 [현금영수증 조회](#현금영수증-조회)를 처리하면 현금영수증 발급(승인)여부를 확인 할 수 있습니다.  
현금영수증 발급 요청은 결제자 정보 및 유형을 `/v1/receipt/` API로 전달 하는 것으로 완료 됩니다.

<br>


#### Over-view
<img src="../image/payment-receipt-issue.svg" width="800px">

> #### ⚠️ 중요
> 현금영수증 발급요청 성공은 국세청으로 현금영수증 데이터 전달을 위한 요청이 완료 되었음을 의미 합니다.  
> 국세청으로 발급처리 요청과 발급여부 조회까지의 시간간격은 영업일 기준 최대 ⏱️ D+2일 발생합니다.

<br>

#### 샘플 코드

```bash
curl -X POST 'https://api.nicepay.co.kr/v1/receipt' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjQ4...' 
-D '{
    "orderId" : "merchant-order-id",
    "amount" : 1000,
    "goodsName" : ＂나이스상품",
    "receiptType" : "individual",
    "receiptNo" : "01012341234",
    "supplyAmt" : 250,
    "goodsVat" : 250,
    "taxFreeAmt" : 250,
    "serviceAmt" : 250
}'
```

<br>

#### 요청 명세 (Body)

``` bash
POST /v1/receipt/  
HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials> or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter     | Type   | 필수  | 크기  | 상세 설명                                                                                                                                                          |
|---------------|--------|-----|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| orderId       | String | O   | 64  | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br>결제된 orderId로   재호출 불가                                                                                         |
| amount        | Int    | O   | 12  | 현금영수증 발행금액                                                                                                                                                     |
| goodsName     | String | O   | 40  | 상품명                                                                                                                                                            |
| receiptType   | String | O   | 20  | 현금영수증 발급 유형<br> individual : 개인 소득공제용<br>company : 사업자 지출증빙용                                                                                                   |
| receiptNo     | String | O   | 20  | 현금영수증 발행대상 식별정보<br>휴대폰번호(10 자리   또는 11 자리) 또는 사업자번호(10   자리)<br>- receiptType 이 individual 인경우 휴대폰번호 <br>- receiptType 이 company 인경우   사업자번호<br>- '-'없이 숫자만 입력 |
| supplyAmt     | Int    | O   | 12  | amount중 공급가액<br>전체 거래금액(amount)중에서   공급가액에 해당하는 금액<br>해당없을 경우 0                                                                                                |
| goodsVat      | Int    | O   | 12  | amount중 부가가치세<br>전체 거래금액(amount)중에서   부가세에 해당하는 금액<br>해당없을 경우 0                                                                                                |
| taxFreeAmt    | Int    | O   | 12  | amount중 면세공급가액<br> 전체 거래금액(amount)중에서   면세에 해당하는 금액<br>해당없을 경우 0                                                                                               |
| serviceAmt    | Int    | O   | 12  | amount중 봉사료<br> 전체 거래금액(amount)중에서   봉사료에 해당하는 금액<br>해당없을 경우 0                                                                                                 |
| buyerName     | String | 　   | 30  | 구매자 이름                                                                                                                                                         |
| buyerTel      | String | 　   | 40  | 구매자 전화번호<br>하이픈(-) 없이 숫자만   입력                                                                                                                                 |
| buyerEmail    | String | 　   | 60  | 구매자 이메일<br>전문생성일시<br>ISO 8601 형식                                                                                                                               |
| signData      | String | 　   | 256 | 위변조 검증 Data <br>생성규칙 : hex(sha256(orderId + amount +   ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.                                          |
| returnCharSet | String | 　   | 10  | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                                                                         |

<br>


#### 응답 명세 (Body)

```bash
Content-type: application/json
```

| Parameter  | TYPE   | 필수  | 크기  | 설명                                                                                                                                                                                   |
|------------|--------|-----|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| resultCode | String | O   | 4   | 결과코드<br>0000 : 성공 / 그외 실패                                                                                                                                                            |
| resultMsg  | String | O   | 100 | 결과메시지                                                                                                                                                                                |
| tid        | String | O   | 30  | 결제 승인 키<br>NICEPAY 거래키 입니다.                                                                                                                                                          |
| orderId    | String | O   | 64  | 상점 거래 고유번호                                                                                                                                                                           |
| approvedAt | String | O   | -   | 발급시점<br>ISO 8601 형식<br>발급완료가 아닐 경우 0                                                                                                                                                 |
| approveNo  | String | 　   | 30  | 현금영수증 국세청 발행번호<br>발급 성공시 리턴됩니다.                                                                                                                                                      |
| ediDate    | String |     | 14  | 응답전문생성일시<br>ISO 8601 형식                                                                                                                                                              |
| signature  | String | 　   | 256 | 위변조 검증 데이터<br>- 유효한 거래건에   한하여 응답<br>- 생성규칙 :   hex(sha256(tid + orderId + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다. |

<br>

## 현금영수증 취소

현금영수증 취소는 현금영수증 발급 성공 건의 취소를 의미 합니다.  
현금영수증 취소 요청은 현금영수증 발급요청 성공시 응답받은 tid와 취소 금액을 `/v1/receipt/{tid}/cancel` API에 전달하는 것으로 처리 됩니다.

<br>

#### Over-view
<img src="../image/payment-receipt-cancel.svg" width="800px">

> #### ⚠️ 중요
> 현금영수증 취소요청 성공은 국세청으로 현금영수증 취소 데이터 전달을 위한 요청이 완료 되었음을 의미 합니다.   
> 국세청으로 취소처리 요청과 조회까지의 시간간격은 영업일 기준 최대 ⏱️ D+2일 발생합니다.

<br>

#### 샘플 코드

``` bash
curl -X POST 'https://api.nicepay.co.kr/v1/receipt/nicuntct1m04012107272036221413/cancel' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMTQ4M2...' 
-D '{
    "orderId" : "merchant-order-id",
    "reason" : "sample-code"
}'
```

<br>

#### 요청 명세 (Body)

``` bash
POST /v1/receipt/{tid}/cancel  
HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter     |  Type   |  필수   |  Byte  | 설명                                                                                                    |
|:--------------|:-------:|:-----:|:------:|:------------------------------------------------------------------------------------------------------|
| orderId       | String  |   O   |   64   | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br>결제된 orderId로 재호출 불가                                  |
| reason        | String  |   O   |  100   | 취소사유                                                                                                  |
| cancelAmt     |   Int   |   　   |   12   | 취소요청금액<br>누락이면 전액취소<br>- 부분취소시 supplyAmt, goodsVat, taxFreeAmt, serviceAmt 필드 필수 전달                   |
| ediDate       | String  |   　   |   -    | 전문생성일시<br>ISO 8601 형식                                                                                 |
| signData      | String  |   　   |  256   | 위변조 검증 데이터<br>생성규칙 : hex(sha256(tid + ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| returnCharSet | String  |   　   |   10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                |
| supplyAmt     |   Int   |   　   |   12   | 취소금액(cancelAmt)중에서 공급가액에 해당하는 금액                                                                      |
| goodsVat      |   Int   |   　   |   12   | 취소금액(cancelAmt)중에서 부가세에 해당하는 금액                                                                       |
| taxFreeAmt    |   Int   |   　   |   12   | 취소금액(cancelAmt)중에서 면세에 해당하는 금액                                                                        |
| serviceAmt    |   Int   |   　   |   12   | cancelAmt중 봉사료<br>취소금액(cancelAmt)중에서 봉사료에 해당하는 금액                                                     |

<br>

#### 응답 명세 (Body)

``` bash
Content-type: application/json
```

| Parameter   |  Type   |  필수   |  크기   | 상세 설명                                                                                                                                                                                 |
|:------------|:-------:|:-----:|:-----:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| resultCode  | String  |   O   |   4   | 결과코드<br>0000 : 성공 / 그외 실패                                                                                                                                                             |
| resultMsg   | String  |   O   |  100  | 결과메시지                                                                                                                                                                                 |
| tid         | String  |   O   |  30   | 취소 거래 키<br>NICEPAY 거래키 입니다.                                                                                                                                                           |
| orderId     | String  |   O   |  64   | 상점 거래 고유번호                                                                                                                                                                            |
| cancelAmt   |   Int   |   O   |  12   | 취소금액<br>취소 실패일 경우 0                                                                                                                                                                   |
| balanceAmt  |   Int   |   O   |  12   | 취소 가능한 잔액<br>부분취소 거래인경우, 전체금액에서   현재까지 취소된 금액을 차감한 금액.                                                                                                                                |
| cancelledAt | String  |   O   |   -   | 취소시점<br>ISO 8601 형식<br>취소 실패일 경우 0                                                                                                                                                    |
| approveNo   | String  |   　   |  30   | 현금영수증 국세청 취소 승인번호<br>취소 성공시 리턴됩니다.                                                                                                                                                    |
| ediDate     | String  |       |  14   | 응답전문생성일시<br>ISO 8601 형식                                                                                                                                                               |
| signature   | String  |   　   |  256  | 위변조 검증 데이터<br>- 유효한 거래건에   한하여 응답<br>- 생성규칙 :   hex(sha256(tid + orderId + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |

<br>

### 현금영수증 조회

현금영수증 조회는 현금영수증 요청 건의 조회를 의미 합니다.  
현금영수증 발급요청 성공시 응답받은 tid `/v1/receipt/{tid}` API에 전달하는 것으로 조회 처리 됩니다.

> #### ⚠️ 중요
> 국세청으로 발급처리 요청과 발급여부 조회까지의 시간간격은 영업일 기준 최대 ⏱️ D+2일 발생합니다.

<br>

#### Over-view
<img src="../image/payment-receipt-get.svg" width="800px">  

<br>

#### 샘플 코드

``` bash
curl -X GET 'https://api.nicepay.co.kr/v1/receipt/nicuntct1m04012107272036221413' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMTQ4M2...' 
```

<br>

#### 요청 명세 (Body)

``` bash
GET /v1/receipt/{tid}   
HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter     |  Type   |  필수   |  Byte  | 설명                                                                                                       |
|:--------------|:-------:|:-----:|:------:|:---------------------------------------------------------------------------------------------------------|
| orderId       | String  |   O   |   64   | 상점 거래 고유번호<br> 가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br>결제된 orderId로   재호출 불가                                  |
| reason        | String  |   O   |  100   | 취소사유                                                                                                     |
| cancelAmt     |   Int   |   　   |   12   | 부분)취소요청금액<br>누락이면 전액취소<br>- 부분취소시 supplyAmt,   goodsVat, taxFreeAmt, serviceAmt 필드 필수 전달                 |
| ediDate       | String  |   　   |   -    | 전문생성일시<br>ISO 8601 형식                                                                                    |
| signData      | String  |   　   |  256   | 위변조 검증 Data<br>생성규칙 : hex(sha256(tid + ediDate +   SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| returnCharSet | String  |   　   |   10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                   |
| supplyAmt     |   Int   |   　   |   12   | 취소금액(cancelAmt)중에서   공급가액에 해당하는 금액                                                                       |
| goodsVat      |   Int   |   　   |   12   | 취소금액(cancelAmt)중에서   부가세에 해당하는 금액                                                                        |
| taxFreeAmt    |   Int   |   　   |   12   | 취소금액(cancelAmt)중에서   면세에 해당하는 금액                                                                         |
| serviceAmt    |   Int   |   　   |   12   | 취소금액(cancelAmt)중에서   봉사료에 해당하는 금액                                                                        |

<br>

#### 응답 명세 (Body)

``` bash
POST
Content-type: application/json
```

| Parameter   |   Type   |  필수   |  Byte  | 설명                                                                                                                                        |
|:------------|:--------:|:-----:|:------:|:------------------------------------------------------------------------------------------------------------------------------------------|
| resultCode  |  String  |   O   |   4    | 결과코드<br>0000 : 성공 / 그외 실패                                                                                                                 |
| resultMsg   |  String  |   O   |  100   | 결과메시지                                                                                                                                     |
| tid         |  String  |   O   |   30   | 취소 거래 키<br>NICEPAY 거래키 입니다.                                                                                                               |
| orderId     |  String  |   O   |   64   | 상점 거래 고유번호                                                                                                                                |
| cancelAmt   |   Int    |   O   |   12   | 취소금액<br>취소 실패일 경우 0                                                                                                                       |
| balanceAmt  |   Int    |   O   |   12   | 취소 가능한 잔액<br>부분취소 거래인경우, 전체금액에서   현재까지 취소된 금액을 차감한 금액.                                                                                    |
| cancelledAt |  String  |   O   |   -    | 취소시점<br>ISO 8601 형식<br>취소 실패일 경우 0                                                                                                        |
| approveNo   |  String  |   　   |   30   | 현금영수증 국세청 취소 승인번호<br> 취소 성공시 리턴됩니다.                                                                                                       |
| ediDate     |  String  |       |   14   | 응답전문생성일시<br>ISO 8601 형식                                                                                                                   |
| signature   |  String  |   　   |  256   | 위변조 검증 데이터<br>- 유효한 거래건에   한하여 응답<br>- 생성규칙 :   hex(sha256(tid + orderId + ediDate+ SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |


<br>

## EPAY

### 샘플 코드

```bash
curl -X POST "https://api.nicepay.co.kr/v1/epay/"
-H 'Content-Type: application/json' 
-H 'Authorization: Basic ZWVjOGQzNTA4Y2IwNDI1ZGI5NTViMzBiZjM...' 
-D '{
    "orderId": "merchant-order-id",
    "encData": "3e5219ba1e488866a3552695e9...",
    "amount": 1004,
    "goodsName": "나이스상품",
    "cardCode": 01,
    "cardQuota": 0,
    "useShopInterest": false
}'
```

<br>

### 요청 명세 (Body)

```bash
POST /v1/epay/  
HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter       |   Type   |  필수   |  Byte  | 상세 설명                                                                                                                                                                                                                         |
|:----------------|:--------:|:-----:|:------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| orderId         |  String  |   O   |   64   | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br> 결제된 orderId로 재호출 불가                                                                                                                                                         |
| encData         |  String  |   O   |   -    | 결제정보 암호화 데이터 [encData 상세정보 참고](#encdata-상세-정보)<br>결제정보 암호화 생성 규칙 [encData 암호화 정보 참고](#encdata-암호화-정보)<br>- Hex(AES(authFlag=value&cardNo=value&track2Data=value&cardExpire=value&TRID=value&CAVV=value&XID=value&ECI=value))  |
| amount          |   Int    |   O   |   12   | 결제 금액                                                                                                                                                                                                                         |
| goodsName       |  String  |   O   |   40   | 상품명                                                                                                                                                                                                                           |
| cardCode        |  String  |   O   |   2    | 카드사 코드                                                                                                                                                                                                                        |
| cardQuota       |   Int    |   O   |   2    | 할부개월<br>0:일시불, 2:2개월, 3:3개월 …                                                                                                                                                                                                 |
| useShopInterest | Boolean  |   O   |   -    | 상점분담무이자 사용여부<br>false : 유이자 / true : 무이자<br>- 사전 협의된 카드사에 한하여 무이자   결제 가능.<br>- 분담무이자 미등록된 카드사로   승인요청하면 결제 실패됩니다.                                                                                                            |
| useCardPoint    | Boolean  |   　   |   -    | 카드사포인트 사용 여부<br>false:포인트 미사용(default) / true:포인트 사용<br>- 사전에 협의된 카드사에 한하여   포인트 결제 가능합니다.<br>- 포인트 미보유 시 결제   실패됩니다.(일부 카드사 결제 허용)                                                                                           |
| buyerName       |  String  |   　   |   30   | 구매자 이름                                                                                                                                                                                                                        |
| buyerTel        |  String  |   　   |   40   | 구매자 전화번호<br>하이픈(-) 없이 숫자만 입력                                                                                                                                                                                                  |
| buyerEmail      |  String  |   　   |   60   | 구매자 이메일                                                                                                                                                                                                                       |
| taxFreeAmt      |   Int    |   　   |   12   | 면세공급가액<br>전체 거래금액(amount)중에서 면세에 해당하는 금액을 설정합니다.                                                                                                                                                                              |
| mallReserved    |  String  |   　   |  500   | 상점 정보 전달용 예비필드<br>승인응답 또는 webhook 시점에 요청 원문을 전달 합니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                                                              |
| encMode         |  String  |   　   |   10   | 암호화 모드<br>encData 필드의 암호화 알고리즘 정의<br>- A2 : AES256                                                                                                                                                                            |
| ediDate         |  String  |   　   |   -    | 전문생성일시 <br>ISO 8601 형식                                                                                                                                                                                                        |
| signData        |  String  |   　   |  256   | 위변조 검증 Data<br>생성규칙 : hex(sha256(orderId + amount +   ediDate + SecretKey)) <br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.                                                                                                         |
| returnCharSet   |  String  |   　   |   10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                                                                                                                                        |

<br>

#### encData 필드 상세정보

| Parameter  |   Type   |  필수   |  Byte  | 설명               |
|:-----------|:--------:|:-----:|:------:|:-----------------|
| authFlag   |  String  |   O   |   2    | 인증구분             |
| cardNo     |  String  |   O   |   16   | 카드번호             |
| track2Data |  String  |   O   |   39   | 　                |
| cardExpire |  String  |   O   |   4    | 유효기간(포멧:YYMM)    |
| TRID       |  String  |   　   |   20   | 나이스정보통신 인증 거래번호  |
| CAVV       |  String  |   　   |   30   | CAVV             |
| XID        |  String  |   　   |   30   | XID              |
| ECI        |  String  |   　   |   2    | ECI              |

<br>

#### encData 필드 암호화 정보

```bash
ex) 
카드 : 삼성 / 카드번호 : 5310123412341234 / track2Data : 375310123412341234=0000 / 유효기간 : 0000 / 
CAVV : AAABCGkWZSAhBwIIGRZlBSAAAAA= / XID : MjAyMTA3MDIwNzEyNTQ2MzE5OTg= / ECI : 05
SecretKey : 2dcc2a0d63bf469490bb19a201be3735

Case1. AES128
- 평문 : authFlag=0&cardNo=5310123412341234&track2Data=375310123412341234=0000&cardExpire=0000&CAVV=AAABCGkWZSAhBwIIGRZlBSAAAAA=&XID=MjAyMTA3MDIwNzEyNTQ2MzE5OTg=&ECI=05
- 암호키 : 2dcc2a0d63bf4694(SecretKey 앞16자리)
- IV : 2dcc2a0d63bf4694(SecretKey 앞16자리)
- 암호화결과 : 3e5219ba1e488866a3552695e954d5feb7824d18da81229cd21cee7c3de3f9b0f803c52f8482ccdda8186d31d010833766f2dba48c6205db8788d8c010e1ceb9bd2ab37c41ff370287de70f50af1cfbdd379283894683dbf42f8756085b6bfb54fc5fbe19b4a00400adf2d0f712f4671736e821a979b7d6f8e6c384a2ecd9c65a2c251513f704580ae7f16680d60f560a8c613d5cea104fa5bedfa6895ba0034
```

<br>

#### 카드사별 (결제) 승인요청 전문

| 카드사  |  AuthFlag  | Track2Data(39)           | 나이스정보통신<br>인증 응답 값 승인요청전문 셋팅                                         | 예시                                                                                                                                                                                  |
|:----:|:----------:|:-------------------------|:---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  비씨  |     2      | 37+REAL_CARD_NUM+=+유효기간  | TR_ID -> TRID <br>REAL_CARD_NUM -> cardNo                            | authFlag=2<br>cardNo=9100123412341234<br>track2Data=379100123412341234=2502<br>cardExpire=2502<br>TRID=1000031234                                                                   |
|  삼성  |     0      | 37+REAL_CARD_NUM+=+0000  | CAVV -> CAVV<br>XID -> XID<br>ECI -> ECI<br>REAL_CARD_NUM -> cardNo  | authFlag=0<br>cardNo=5310123412341234<br> track2Data=375310123412341234=0000<br>cardExpire=0000<br>CAVV=AAABCGkWZSAhBwIIGRZlBSAAAAA=<br> XID=MjAyMTA3MDIwNzEyNTQ2MzE5OTg=<br>ECI=05 |
|  현대  |     0      | 37+REAL_CARD_NUM+=+0000  | CAVV -> CAVV<br>XID -> XID<br>ECI -> ECI<br>REAL_CARD_NUM -> cardNo  | authFlag=0<br>cardNo=9490123412341234<br>track2Data=379490123412341234=0000<br>cardExpire=0000<br>CAVV=AAABCGkWZSAhBwIIGRZlBSAAAAA=<br>XID=MjAyMTA3MDIwNzEyNTQ2MzE5OTg=<br>ECI=05   |
|  롯데  |     0      | 37+REAL_CARD_NUM+=+9999  | CAVV -> CAVV<br>ECI('05'고정) -> ECI<br>REAL_CARD_NUM -> cardNo        | authFlag=0<br>cardNo=5217123412341234<br>track2Data=375217123412341234=9999<br>cardExpire=9999<br>CAVV=AAABCGkWZSAhBwIIGRZlBSAAAAA=<br>ECI=05                                       |
|  신한  |     2      | 37+OTC_NUM               | OTC_NUM 중 '='앞 15~16자리 cardNo 셋팅                                     | authFlag=2<br>cardNo=4450123412341234<br>track2Data=374450123412341234=22011234123400100000<br>cardExpire=9999                                                                      |
|  하나  |     2      | 37+OTC_NUM               | OTC_NUM 중 '='앞 15~16자리 cardNo 셋팅                                     | authFlag=2<br>cardNo=9417123412341234<br>track2Data=379417123412341234=22011234123400100000<br>cardExpire=9999                                                                      |
|  농협  |     2      | 37+OTC_NUM               | OTC_NUM 중 '='앞 15~16자리 cardNo 셋팅                                     | authFlag=2<br>cardNo=5461123412341234<br>track2Data=375461123412341234=22011234123400100000<br>cardExpire=9999                                                                      |
|  국민  |     2      | 37+OTC_NUM+=+8911        | OTC_NUM이 21 자리 인 경우<br>앞 16자리만 cardNo 셋팅                             | authFlag=2<br>cardNo=5570123412341234<br>track2Data=375570123412341234=8911<br>cardExpire=8911                                                                                      |

<br>

### 응답 명세 (Body)

```bash
POST
Content-type: application/json
```

| Parameter         |  Type   |  필수  |  Byte  | 설명                                                                                                                                                                                   |
|:------------------|:-------:|:----:|:------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| resultCode        | String  |  O   |   4    | 결제결과코드<br>0000 : 성공 / 그외 실패                                                                                                                                                          |
| resultMsg         | String  |  O   |  100   | 결제결과메시지                                                                                                                                                                              |
| tid               | String  |  O   |   30   | 결제 승인 키<br>최초 승인(가상계좌-채번)에 성공한 원거래의 NICEPAY 거래키 입니다.                                                                                                                                 |
| cancelledTid      | String  |  　   |   30   | 취소 거래 키<br>NICEPAY가 발행하는 취소 응답 TID (부분취소시 tid와 다른 값이 응답됨)<br>- 취소   요청건에 한하여 응답됨<br>- cancels 객체에서 현재 취소된 거래정보를 찾을 때 사용 하시면 됩니다.                                                     |
| orderId           | String  |  O   |   64   | 상점 거래 고유번호                                                                                                                                                                           |
| ediDate           | String  |  O   |   -    | 응답전문생성일시 ISO 8601 형식                                                                                                                                                                 |
| signature         | String  |  　   |  256   | 위변조 검증 데이터<br>- 유효한 거래건에   한하여 응답<br>- 생성규칙 :   hex(sha256(tid + amount + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| status            | String  |  O   |   20   | 결제 처리상태<br>paid:결제완료,   ready:준비됨, failed:결제실패, cancelled:취소됨, partialCancelled:부분 취소됨, expired:만료됨<br>['paid', 'ready', 'failed', 'cancelled', 'partialCancelled',   'expired']     |
| paidAt            | String  |  O   |   -    | 결제완료시점 ISO 8601 형식<br>결제완료가 아닐 경우 0                                                                                                                                                  |
| failedAt          | String  |  O   |   -    | 결제실패시점 ISO 8601 형식<br>결제실패가 아닐 경우 0                                                                                                                                                  |
| cancelledAt       | String  |  O   |   -    | 결제취소시점 ISO 8601 형식<br>결제취소가 아닐 경우 0<br>부분취소인경우, 가장   마지막건의 취소 시간                                                                                                                     |
| payMethod         | String  |  O   |   10   | 결제수단<br><br>card:신용카드,<br>vbank:가상계좌,<br>bank:계좌이체,<br>cellphone:휴대폰,<br>naverpay=네이버페이, kakaopay=카카오페이, samsungpay=삼성페이                                                             |
| amount            |   Int   |  O   |   12   | 결제 금액                                                                                                                                                                                |
| balanceAmt        |   Int   |  O   |   12   | 취소 가능 잔액<br>부분취소 거래인경우, 전체금액에서   현재까지 취소된 금액을 차감한 금액.                                                                                                                                |
| goodsName         | String  |  O   |   40   | 상품명                                                                                                                                                                                  |
| mallReserved      | String  |  　   |  500   | 상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br> 단, 큰따옴표(")는 이용불가                                                                     |
| useEscrow         | Boolean |  O   |   -    | 에스크로 거래 여부<br>false:일반거래 /   true:에스크로 거래                                                                                                                                            |
| currency          | String  |  O   |   3    | 결제승인화폐단위 <br> KRW:원화, USD:미화달러, CNY:위안화                                                                                                                                              |
| channel           | String  |  　   |   10   | pc:PC결제, mobile:모바일결제<br>['pc', 'mobile', 'null']                                                                                                                                    |
| approveNo         | String  |  　   |   30   | 제휴사 승인 번호<br>신용카드, 계좌이체, 휴대폰                                                                                                                                                         |
| buyerName         | String  |  　   |   30   | 구매자 명                                                                                                                                                                                |
| buyerTel          | String  |  　   |   40   | 구매자 전화번호                                                                                                                                                                             |
| buyerEmail        | String  |  　   |   60   | 구매자 이메일                                                                                                                                                                              |
| issuedCashReceipt | Boolean |  　   |   -    | 현금영수증 발급여부<br>true:발행 /   false:미발행                                                                                                                                                  |
| receiptUrl        | String  |  　   |  200   | 매출전표 확인 URL                                                                                                                                                                          |
| mallUserId        | String  |  　   |   20   | 상점에서 관리하는 사용자 아이디                                                                                                                                                                    |

<br>

#### 할인정보 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter  |            |   Type   |  필수   |  　Byte  | 설명            |
|:-----------|:-----------|:--------:|:-----:|:-------:|:--------------|
| coupon     | 　          |  Object  |   　   |    -    | 즉시할인 프로모션 정보  |
| 　          | couponAmt  |   Int    |   　   |   12    | 즉시할인 적용된 금액   |

<br>

#### 카드 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">


| Parameter  |                 |   Type    |  필수   |  　Byte  | 설명                                                                                            |
|:-----------|:----------------|:---------:|:-----:|:-------:|:----------------------------------------------------------------------------------------------|
| card       | 　               |  Object   |   　   |    　    | 신용카드 정보                                                                                       |
| 　          | cardCode        |  String   |   O   |    3    | 신용카드사별 코드                                                                                     |
|            | cardName        |  String   |   O   |   20    | 결제 카드사 이름<br>예) 비씨                                                                            |
|           | cardNum        | String  | 　   | 20     | 카드번호<br>앞 6자 마지막 4자를 제외한 가운데 숫자 마스킹 처리됨<br>예) 536112******1234<br>- 카카오머니/네이버포인트/페이코포인트 전액결제 거래인경우   null |
|            | cardQuota       |    Int    |   O   |    3    | 할부개월<br>0:일시불, 2:2개월, 3:3개월   …                                                               |
|            | isInterestFree  |  Boolean  |   O   |    -    | 상점분담무이자 여부<br>true:무이자,   false:일반                                                            |
|            | cardType        |  String   |   　   |    1    | 카드 구분<br>credit:신용,   check:체크                                                                |
|            | canPartCancel   |  String   |   O   |    -    | 부분취소 가능 여부<br>true:가능,   false:불가능                                                            |
|            | acquCardCode    |  String   |   O   |    3    | 매입카드사코드                                                                                       |
|            | acquCardName    |  String   |   O   |   100   | 매입카드사명                                                                                        |


<br>


# 조회

- [거래 조회](#거래-조회)
- [약관 조회](#약관-조회)
- [카드 이벤트 조회](#카드-이벤트-조회)
- [카드 무이자 조회](#카드-무이자-조회)

## 거래 조회

- 결제(승인) API를 호출 후 `Http-client`의 [timeout](#타임아웃-정보)이 발생하여 [결제취소](#취소--환불) 혹은 [망 취소](#망취소)를 고려해야 하는 경우
- 특정 결제(승인) 건의 데이터가 일부 유실되어 조회가 필요한 경우
- 결제(승인) 건의 데이터 위변조가 의심되어 원본 데이터 정보 체크가 필요한 경우

<br>

### Over-view
거래 조회는 💳 결제(승인)요청 성공 혹은 실패에 따른 정보확인이 필요한 경우 활용 할 수 있습니다.

<br>

### 샘플 코드

```bash
curl -X GET 'https://api.nicepay.co.kr/v1/payments/nicuntct1m0101210727200125A056' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMT...'
```

<br>

### 요청 명세

#### 거래조회(with tid)

```bash
GET /v1/payments/{tid} 
HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter     | Type  |  필수   |  크기   | 설명                                                                                                       |
|:--------------|:-----:|:-----:|:-----:|:---------------------------------------------------------------------------------------------------------|
| ediDate       |   S   |   　   |   -   | 전문생성일시<br>ISO 8601 형식                                                                                    |
| signData      |   S   |   　   |  256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(tid + ediDate +   SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| returnCharSet |   S   |   　   |  10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                   |

<br>

#### 거래조회(with orderId)

```bash
GET /v1/payments/find/{orderId} HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter     | Type |  필수  |  크기   | 설명                                                                                                       |
|:--------------|:----:|:----:|:-----:|:---------------------------------------------------------------------------------------------------------|
| orderDate     |  S   |  O   |   8   | 주문일자<br>YYYYMMDD                                                                                         |
| ediDate       |  S   |  　   |   -   | 전문생성일시<br> ISO 8601 형식                                                                                   |
| signData      |  S   |  　   |  256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(tid + ediDate +   SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| returnCharSet |  S   |  　   |  10   | 응답파라메터 인코딩 방식<br> 가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                  |

<br>

### 응답 명세 (Body)

#### 공통
```bash
Content-type: application/json
```

| Parameter         |   Type   |  필수   |  Byte  | 설명                                                                                                                                                                                 |
|:------------------|:--------:|:-----:|:------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| resultCode        |  String  |   O   |   4    | 결제결과코드<br>0000 : 성공 / 그외 실패                                                                                                                                                        |
| resultMsg         |  String  |   O   |  100   | 결제결과메시지                                                                                                                                                                            |
| tid               |  String  |   O   |   30   | 결제 승인 키<br>최초 승인(가상계좌-채번)에 성공한 원거래의 NICEPAY 거래키 입니다.                                                                                                                               |
| cancelledTid      |  String  |   　   |   30   | 취소 거래 키<br>NICEPAY가 발행하는 취소 응답 TID (부분취소시 tid와 다른 값이 응답됨)<br>- 취소   요청건에 한하여 응답됨<br>- cancels 객체에서 현재 취소된 거래정보를 찾을 때 사용 하시면 됩니다.                                                   |
| orderId           |  String  |   O   |   64   | 상점 거래 고유번호                                                                                                                                                                         |
| ediDate           |  String  |   O   |   -    | 응답전문생성일시 ISO 8601 형식                                                                                                                                                               |
| signature         |  String  |   　   |  256   | 위변조 검증 데이터<br>- 유효한 거래건에 한하여 응답<br>- 생성규칙 :   hex(sha256(tid + amount + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| status            |  String  |   O   |   20   | 결제 처리상태<br>paid:결제완료,   ready:준비됨, failed:결제실패, cancelled:취소됨, partialCancelled:부분 취소됨, expired:만료됨<br>['paid', 'ready', 'failed', 'cancelled', 'partialCancelled',   'expired']   |
| paidAt            |  String  |   O   |   -    | 결제완료시점 ISO 8601 형식<br>결제완료가 아닐 경우 0                                                                                                                                                |
| failedAt          |  String  |   O   |   -    | 결제실패시점 ISO 8601 형식<br>결제실패가 아닐 경우 0                                                                                                                                                |
| cancelledAt       |  String  |   O   |   -    | 결제취소시점 ISO 8601 형식<br>결제취소가 아닐 경우 0<br>부분취소인경우, 가장   마지막건의 취소 시간                                                                                                                   |
| payMethod         |  String  |   O   |   10   | 결제수단<br><br>card:신용카드,<br>vbank:가상계좌,<br>bank:계좌이체,<br>cellphone:휴대폰,<br>naverpay=네이버페이, kakaopay=카카오페이, samsungpay=삼성페이                                                           |
| amount            |   Int    |   O   |   12   | 결제 금액                                                                                                                                                                              |
| balanceAmt        |   Int    |   O   |   12   | 취소 가능 잔액<br>부분취소 거래인경우, 전체금액에서   현재까지 취소된 금액을 차감한 금액.                                                                                                                              |
| goodsName         |  String  |   O   |   40   | 상품명                                                                                                                                                                                |
| mallReserved      |  String  |   　   |  500   | 상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                    |
| useEscrow         | Boolean  |   O   |   -    | 에스크로 거래 여부<br>false:일반거래 /   true:에스크로 거래                                                                                                                                          |
| currency          |  String  |   O   |   3    | 결제승인화폐단위<br>KRW:원화, USD:미화달러, CNY:위안화                                                                                                                                              |
| channel           |  String  |   　   |   10   | pc:PC결제, mobile:모바일결제<br>['pc', 'mobile', 'null']                                                                                                                                  |
| approveNo         |  String  |   　   |   30   | 제휴사 승인 번호<br>신용카드, 계좌이체, 휴대폰                                                                                                                                                       |
| buyerName         |  String  |   　   |   30   | 구매자 명                                                                                                                                                                              |
| buyerTel          |  String  |   　   |   40   | 구매자 전화번호                                                                                                                                                                           |
| buyerEmail        |  String  |   　   |   60   | 구매자 이메일                                                                                                                                                                            |
| issuedCashReceipt | Boolean  |   　   |   -    | 현금영수증 발급여부<br>true:발행 /   false:미발행                                                                                                                                                |
| receiptUrl        |  String  |   　   |  200   | 　매출전표 확인 URL                                                                                                                                                                       |
| mallUserId        |  String  |   　   |   20   | 상점에서 관리하는 사용자 아이디                                                                                                                                                                  |

<br>

#### 할인정보 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |           |   Type   |  필수   |  　Byte  | 설명            |
|:----------|:----------|:--------:|:-----:|:-------:|:--------------|
| coupon    | 　         |  Object  |   　   |    -    | 즉시할인 프로모션 정보  |
| 　         | couponAmt |   Int    |   　   |   12    | 즉시할인 적용된 금액   |

<br>

#### 카드 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |                |   Type    |  필수   |  　Byte  | 설명                                                                                            |
|:----------|:---------------|:---------:|:-----:|:-------:|:----------------------------------------------------------------------------------------------|
| card      | 　              |  Object   |   　   |    　    | 신용카드 정보                                                                                       |
| 　         | cardCode       |  String   |   O   |    3    | 신용카드사별 코드                                                                                     |
|           | cardName       |  String   |   O   |   20    | 결제 카드사 이름<br>예) 비씨                                                                            |
|           | cardNum        | String  | 　   | 20     | 카드번호<br>앞 6자 마지막 4자를 제외한 가운데 숫자 마스킹 처리됨<br>예) 536112******1234<br>- 카카오머니/네이버포인트/페이코포인트 전액결제 거래인경우   null |
|           | cardQuota      |    Int    |   O   |    3    | 할부개월<br>0:일시불, 2:2개월, 3:3개월   …                                                               |
|           | isInterestFree |  Boolean  |   O   |    -    | 상점분담무이자 여부<br>true:무이자,   false:일반                                                            |
|           | cardType       |  String   |   　   |    1    | 카드 구분<br>credit:신용,   check:체크                                                                |
|           | canPartCancel  |  String   |   O   |    -    | 부분취소 가능 여부<br>true:가능,   false:불가능                                                            |
|           | acquCardCode   |  String   |   O   |    3    | 매입카드사코드                                                                                       |
|           | acquCardName   |  String   |   O   |   100   | 매입카드사명                                                                                        |

<br>

#### 현금영수증 <img src="https://img.shields.io/badge/-Array-blueviolet"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter    |             |  Type   |  필수   |  Byte  | 설명                                                                                                                                                                                                                                                                                                                                                                                                   |
|:-------------|:------------|:-------:|:-----:|:------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cashReceipts | 　           |  Array  |   　   |   　    | 현금영수증 발급정보<br>-NaverPay-포인트 ,가상계좌 입금건에서 제공<br>-부분 취소시, 2건이상 존재가능                                                                                                                                                                                                                                                                                                                                     |
| 　            | receiptTid  | String  |   O   |   30   | 현금영수증 TID                                                                                                                                                                                                                                                                                                                                                                                            |
|              | orgTid      | String  |   O   |   30   | 연관된 원 승인/취소 거래 TID<br>부분취소시, 원 부분취소   거래건의 TID와 매핑됨<br>- 원거래를 부분취소 하면,   신규 TID가 채번되고,<br>채번된 부분취소 TID가   셋팅 됩니다.                                                                                                                                                                                                                                                                                    |
|              | status      | String  |   O   |   20   | 발급진행 상태<br>[발급]<br>issueRequested : 발급 접수 완료[1,3]<br>issueReqCancelled : 요청회수(국세청 발행 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>issued : 국세청 발급 완료[4]<br>issueFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10])<br>[취소]<br>cancelRequested : 취소 접수 완료[1,3]<br>cancelReqCancelled : 요청회수(국세청 취소 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>cancelled : 국세청 취소 완료[4]<br>cancelFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10])  |
|              | amount      |   Int   |   O   |   12   | 현금영수증 발행 총금액                                                                                                                                                                                                                                                                                                                                                                                         |
|              | taxFreeAmt  |   Int   |   O   |   12   | 현금영수증 전체 금액중에서 면세금액                                                                                                                                                                                                                                                                                                                                                                                  |
|              | receiptType | String  |   O   |   20   | 현금영수증 타입<br>individual : 개인 소득공제용<br>company : 사업자 지출증빙용                                                                                                                                                                                                                                                                                                                                             |
|              | issueNo     | String  |   O   |   30   | 현금영수증 국세청 발행번호                                                                                                                                                                                                                                                                                                                                                                                       |
|              | receiptUrl  | String  |   O   |  200   | 현금영수증 매출전표 확인 URL                                                                                                                                                                                                                                                                                                                                                                                    |

<br>

#### 계좌이체 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter  |           |   Type   |  필수   |  Byte  | 설명                |
|:-----------|:----------|:--------:|:-----:|:------:|:------------------|
| bank       | 　         |  Object  |   　   |   　    | 은행 정보             |
| 　          | bankCode  |  String  |   O   |   3    | 결제은행코드 (은행코드 참조)  |
|            | bankName  |  String  |   O   |   20   | 결제은행명 (euc-kr)    |

<br>

#### 가상계좌 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |               |   Type   |  필수   |  Byte  | 설명                       |
|:----------|:--------------|:--------:|:-----:|:------:|:-------------------------|
| vbank     | 　             |  Object  |   　   |   　    | 가상계좌 정보                  |
| 　         | vbankCode     |  String  |   O   |   3    | 입금받을 가상계좌 은행코드           |
|           | vbankName     |  String  |   O   |   20   | 입금받을 가상계좌 은행명            |
|           | vbankNumber   |  String  |   O   |   20   | 입금받을 가상계좌 번호             |
|           | vbankExpDate  |  String  |   O   |   -    | 가상계좌 입금 만료일<br>ISO 8601  |
|           | vbankHolder   |  String  |   O   |   40   | 입금받을 가상계좌 예금주명           |


<br>

#### 취소 <img src="https://img.shields.io/badge/-Array-blueviolet"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |              |   Type   |  필수   |  　Byte  | 설명                     |
|:----------|:-------------|:--------:|:-----:|:-------:|:-----------------------|
| cancels   | 　            |  Array   |   　   |    　    | 취소/부분취소 내역             |
| 　         | tid          |  String  |   O   |   30    | 승인 취소 거래번호             |
|           | amount       |   Int    |   O   |   12    | 취소금액                   |
|           | cancelledAt  |  String  |   O   |    -    | 취소된 시각<br>ISO 8601     |
|           | reason       |  String  |   O   |   100   | 취소사유                   |
|           | receiptUrl   |  String  |   O   |   200   | 취소에 대한<br>매출전표 확인 URL  |
|           | couponAmt    |   Int    |   　   |   12    | 쿠폰 취소금액                |

<br>


## 약관 조회

## Over-view
약관 조회 API는 결제 호출 전 사용자에게 노출 해야 하는 약관정보를 응답 합니다.  
나이스페이 결제창을 활용하지 않는 결제수단의 경우 약관 정보 API를 활용하여 사용자에게 약관을 고지해야 합니다.

<br>

### 약관 조회 종류
- 전자금융거래 약관
- 개인정보 수집 및 이용 약관
- 개인정보 제 3자 제공약관
- 통신과금서비스 이용약관

<br>

### 샘플 코드

```bash
curl -X GET 'https://api.nicepay.co.kr/v1/terms?termsType={약관유형}'
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMT...'
```

<br>

### 요청 명세

```bash
GET /v1/terms?termsType={turmsType} 
HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter     |  Type   |  필수   |  Byte  | 설명                                                                                                                                                                                  |
|:--------------|:-------:|:-----:|:------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| termsType     | String  |   O   |   50   | 약관 유형<br>ElectronicFinancialTransactions:전자금융거래   약관<br>CollectPersonalInfo:개인정보 수집 및 이용 약관<br>SharingPersonalInformation:개인정보 제 3자 제공약관<br>TelecommunicationCharging:통신과금서비스 이용약관  |
| returnCharSet | String  |   　   |   10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                                                                                              |

<br>

### 응답 명세 (Body)

```bash
Content-type: application/json
```

| Parameter  |   Type   |  필수   |  Byte   | 상세 설명                      |
|:-----------|:--------:|:-----:|:-------:|:---------------------------|
| resultCode |  String  |   O   |    4    | 결과코드<br>0000 : 성공 / 그외 실패  |
| resultMsg  |  String  |   O   |   100   | 결과메시지                      |
| termsTitle |  String  |   O   |   100   | 약관제목                       |
| content    |  String  |   O   |  30000  | 약관내용                       |

<br>


## 카드 이벤트 조회

### Over-view
카드 이벤트 조회 API는 요청된 기준금액에 해당되는 카드사별 이벤트 정보를 응답 합니다.  
이벤트 정보를 결제자에게 전달하여 카드사 선택을 위한 정보를 편리하게 제공할 수 있습니다.

> 기준금액이 5만원 이하 인 경우 무이자는 미제공하는 것으로 응답 됩니다.

<br>

### 샘플 코드

```bash
curl -X GET 'https://api.nicepay.co.kr/v1/card/event?amount={금액}&useAuth=false&ediDate={ISO 8601 형식}&...' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMT...'
```

<br>

### 요청 명세

```bash
GET /v1/card/event?amount={금액}&useAuth=false&ediDate={ISO 8601 형식}&...   HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter     | Type |  필수   |  크기   | 설명                                                                                                |
|:--------------|:----:|:-----:|:-----:|:--------------------------------------------------------------------------------------------------|
| amount        |  N   |   O   |  12   | 기준금액<br>기준금액에 해당하는 카드 이벤트 정보를 제공합니다.                                                              |
| useAuth       |  B   |   O   |   -   | 인증 거래 여부<br>true : 인증 /   false : 비인증(빌링)                                                         |
| ediDate       |  S   |   O   |   -   | 전문생성일시<br>ISO 8601 형식                                                                             |
| mid           |  S   |   　   |  10   | 상점 MID<br>일반적으로 사용하지 않지만, mid가 요청된 경우, 최우선하여 제공.<br>(요청된 clientId하위 가맹점여부 검증 필수)                  |
| signData      |  S   |   　   |  256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(ediDate + SecretKey))<br> - SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| returnCharSet |  S   |   　   |  10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                            |

<br>

### 응답 명세 (Body)

```bash
POST
Content-type: application/json
```

| Parameter  |  Type   |  필수   |  Byte  | 설명                                                                                                                                                                    |
|:-----------|:-------:|:-----:|:------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| resultCode | String  |   O   |   4    | 결과코드<br>0000 : 성공 / 그외 실패                                                                                                                                             |
| resultMsg  | String  |   O   |  100   | 결과메시지                                                                                                                                                                 |
| ediDate    | String  |       |   -    | 응답전문생성일시<br>ISO 8601 형식                                                                                                                                               |
| signature  | String  |   　   |  256   | 위변조 검증 데이터<br>- 유효한 거래건에   한하여 응답<br>- 생성규칙 :   hex(sha256(ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| cardPoint  | String  |   　   |   　    | 포인트 결제 지원 카드<br>-콜론(:)을 구분자로 카드코드 나열<br>-카드사포인트는 amount에 관계 없이 이용가능한 카드사정보 제공<br>ex) 01:02:04:07<br>- 설명 : BC,국민,삼성,현대 카드는 카드사포인트 사용 가능                               |


### 무이자 할부정보 <img src="https://img.shields.io/badge/-Array-blueviolet">

| Parameter    |                 |   Type   |  필수   |  Byte  | 설명                                                                                              |
|:-------------|:----------------|:--------:|:-----:|:------:|:------------------------------------------------------------------------------------------------|
| interestFree |                 |  Array   |       |   -    | 제공되는 모든 무이자 할부정보<br>- NICEPAY에서 기본제공하는 무이자와 상점무이자가 merge된 정보<br>- 카드코드별 하나의 무이자 Object가 응답됩니다.  |
|              | cardCode        |  String  |   O   |   3    | 카드사 코드<br> 신용카드사별 코드                                                                            |
|              | cardName        |  String  |   O   |   20   | 카드사 이름<br>예) 비씨                                                                                 |
|              | freeInstallment |  String  |   O   |  200   | 무이자 할부개월 <br>콜론(:)을 구분자로 할부개월 나열<br>ex) 02:03:04:05<br>- 설명 : 2,3,4,5개월 무이자 할부 제공               |

<br>

## 카드 무이자 조회

### Over-view
카드 무이자 조회 API는 카드사 무이자 정보를 응답 합니다.  
무이자 조회 API를 통해 무이자 결제가 가능한 카드사와 금액구간 정보를 확인 할 수 있습니다.

<br>

### 샘플 코드

```bash
curl -X GET 'https://api.nicepay.co.kr/v1/card/interest-free?useAuth=true&ediDate={ISO 8601 형식 날짜 표현}' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMT...'
```

<br>

### 요청 명세

```bash
GET /v1/card/interest-free?useAuth=false&ediDate={..} 
HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter     |   Type    |  필수   |  Byte  | 설명                                                                                               |
|:--------------|:---------:|:-----:|:------:|:-------------------------------------------------------------------------------------------------|
| useAuth       |  Boolean  |   O   |   -    | 인증 거래 여부<br>true : 인증 /   false : 비인증(빌링)                                                        |
| ediDate       |  String   |   O   |   -    | 전문생성일시<br>ISO 8601 형식                                                                            |
| mid           |  String   |   　   |   10   | 상점 MID<br>일반적으로 사용하지 않지만, mid가 요청된 경우, 최우선하여 제공.(요청된 clientId하위 가맹점여부 검증 필수)                     |
| signData      |  String   |   　   |  256   | 위변조 검증 Data<br>생성규칙 : hex(sha256(ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| returnCharSet |  String   |   　   |   10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                           |

<br>

### 응답 명세 (Body)

```bash
Content-type: application/json
```

| Parameter  |  Type   |  필수   |  Byte  | 설명                                                                                                                                                                   |
|:-----------|:-------:|:-----:|:------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| resultCode | String  |   O   |   4    | 결과코드<br>0000 : 성공 / 그외 실패                                                                                                                                            |
| resultMsg  | String  |   O   |  100   | 결과 메시지                                                                                                                                                               |
| ediDate    | String  |       |   -    | 응답전문 생성일시<br>ISO 8601 형식                                                                                                                                             |
| signature  | String  |   　   |  256   | 위변조 검증 데이터<br>- 유효한 거래건에   한하여 응답<br>- 생성규칙 :   hex(sha256(ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다. |

#### 무이자 할부정보 <img src="https://img.shields.io/badge/-Array-blueviolet">

| Parameter    |                 |              |   Type   |  필수   |  Byte  | 설명                                                                                              |
|:-------------|:----------------|:-------------|:--------:|:-----:|:------:|:------------------------------------------------------------------------------------------------|
| interestFree |                 |              |  Array   |       |   -    | 제공되는 모든 무이자 할부정보<br>- NICEPAY에서 기본제공하는 무이자와 상점무이자가 merge된 정보<br>- 카드코드별 하나의 무이자 Object가 응답됩니다.  |
|              | cardCode        |              |  String  |   O   |   3    | 카드사 코드<br>신용카드사별 코드                                                                             |
|              | cardName        |              |  String  |   O   |   20   | 카드사 이름<br>예) 비씨                                                                                 |
|              | freeInstallment |              |  Array   |   O   |   -    | 무이자 할부 상세 정보                                                                                    |
|              |                 | minAmt       |   Int    |   O   |   12   | 이벤트 적용 최소 금액<br>ex) 50000                                                                       |
|              |                 | maxAmt       |   Int    |   O   |   14   | 이벤트 적용 최대 금액<br>ex) 99999999999999                                                              |
|              |                 | installment  |  String  |   O   |  100   | 무이자 할부개월<br>콜론(:)을 구분자로 할부개월 나열<br>ex) 02:03:04:05<br>- 설명 : 2,3,4,5개월 무이자 할부 제공                |
|              |                 | eventToDate  |  String  |   O   |   -    | 이벤트 제공 기한<br>ISO 8601 형식                                                                        |


<br>


# 취소·환불·망취소

- [취소/환불](#취소--환불)
  - [결제수단별 취소/환불](#결제수단별-취소환불)
- [망취소](#망취소)

## 취소·환불

### Over-view
💳 결제(승인)이 완료된 거래의 취소 및 환불에 대한 가이드 입니다.  
카드와 같은 비 현금성 결제의 경우 결제(승인) 완료 시 응답된 tid를 취소 API `/v1/payments/{tid}/cancel`에 POST 하는 것으로 처리가 됩니다.  
가상계좌와 같은 현금성 거래는 취소 API에 환불계좌 정보를 추가 전달 하는 것으로 처리가 됩니다.

<br>

### 결제수단 별 취소/환불

| 결제수단         |  전체취소  |  부분취소  |  전체환불  |  부분환불  |  취소 가능 기간  |
|:-------------|:------:|:------:|:------:|:------:|:----------:|
| 카드결제         |   O    |   O    |        |        |    1년 내    |
| 가상계좌 (발급 후)  |   O    |        |        |        |  입금 만료 전   |
| 가상계좌 (입금 후)  |        |        |   O    |   O    |    180일    |
| 현금영수증        |   O    |   O    |        |        |  발급 당해 년도  |
| 에스크로(배송등록 전) |   O    |        |        |        |     -      |
| 에스크로(배승등록 후) |   O    |        |        |        |     -      |
| 에스크로(구매결정 후) |   불가   |   불가   |   불가   |   불가   |     -      |
| 에스크로(구매거절 후) |   O    |        |   O    |        |     -      |

<br>

> #### ⚠️ 중요
> 환불 요청 성공 시 영업일 D+1 ⏱️ 17:00 기준 요청된 정보로 환불 처리 됩니다.  
> 정산 잔액이 부족하여 취소 및 환불이 불가한 경우 1:1 문의를 남겨 주세요.

<br>

### 샘플 코드

```bash
curl -X POST 'https://api.nicepay.co.kr/v1/payments/nicuntct1m0101210727200125A056/cancel' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3...' 
-D '{
    "reason" : "sample-code",
    "orderId" : "merchant-order-id"
}'
```

<br>

### 요청 명세

```bash
POST /v1/payments/{tid}/cancel  
HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter      |  Type   |  필수   |  Byte  | 설명                                                                                                     |
|:---------------|:-------:|:-----:|:------:|:-------------------------------------------------------------------------------------------------------|
| reason         | String  |   O   |  100   | 취소사유                                                                                                   |
| orderId        | String  |   O   |   64   | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br>-부분취소의 경우 중복된 orderId로 재호출 불가                         |
| cancelAmt      |   Int   |       |   12   | 부분)취소요청금액<br>값이 누락이면 전액취소                                                                              |
| mallReserved   | String  |       |  500   | 상점 예약필드<br>상점 정보 전달용 예비필드                                                                              |
| ediDate        | String  |       |   -    | 전문생성일시<br>ISO 8601 형식                                                                                  |
| signData       | String  |       |  256   | 위변조 검증 Data<br>생성규칙 : hex(sha256(tid + ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| returnCharSet  | String  |       |   10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                 |
| taxFreeAmt     |   Int   |       |   12   | 취소금액중 면세공급가액<br>취소금액(amount)중에서 면세에 해당하는 금액을 설정합니다.                                                    |
| refundAccount  | String  |       |   16   | 환불계좌번호                                                                                                 |
| refundBankCode | String  |       |   3    | 환불계좌코드                                                                                                 |
| refundHolder   | String  |       |   10   | 환불계좌 예금주명                                                                                              |

<br>

### 응답 명세 (Body)

```bash
POST
Content-type: application/json
```

| Parameter         |   Type   |  필수   |  Byte  | 설명                                                                                                                                                                                 |
|:------------------|:--------:|:-----:|:------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| resultCode        |  String  |   O   |   4    | 결제결과코드<br>0000 : 성공 / 그외 실패                                                                                                                                                        |
| resultMsg         |  String  |   O   |  100   | 결제결과메시지                                                                                                                                                                            |
| tid               |  String  |   O   |   30   | 결제 승인 키<br>최초 승인(가상계좌-채번)에 성공한 원거래의 NICEPAY 거래키 입니다.                                                                                                                               |
| cancelledTid      |  String  |   　   |   30   | 취소 거래 키<br>NICEPAY가 발행하는 취소 응답 TID (부분취소시 tid와 다른 값이 응답됨)<br>- 취소   요청건에 한하여 응답됨<br>- cancels 객체에서 현재 취소된 거래정보를 찾을 때 사용 하시면 됩니다.                                                   |
| orderId           |  String  |   O   |   64   | 상점 거래 고유번호                                                                                                                                                                         |
| ediDate           |  String  |   O   |   -    | 응답전문생성일시 ISO 8601 형식                                                                                                                                                               |
| signature         |  String  |   　   |  256   | 위변조 검증 데이터<br>- 유효한 거래건에 한하여 응답<br>- 생성규칙 :   hex(sha256(tid + amount + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| status            |  String  |   O   |   20   | 결제 처리상태<br>paid:결제완료,   ready:준비됨, failed:결제실패, cancelled:취소됨, partialCancelled:부분 취소됨, expired:만료됨<br>['paid', 'ready', 'failed', 'cancelled', 'partialCancelled',   'expired']   |
| paidAt            |  String  |   O   |   -    | 결제완료시점 ISO 8601 형식<br>결제완료가 아닐 경우 0                                                                                                                                                |
| failedAt          |  String  |   O   |   -    | 결제실패시점 ISO 8601 형식<br>결제실패가 아닐 경우 0                                                                                                                                                |
| cancelledAt       |  String  |   O   |   -    | 결제취소시점 ISO 8601 형식<br>결제취소가 아닐 경우 0<br>부분취소인경우, 가장   마지막건의 취소 시간                                                                                                                   |
| payMethod         |  String  |   O   |   10   | 결제수단<br><br>card:신용카드,<br>vbank:가상계좌,<br>bank:계좌이체,<br>cellphone:휴대폰,<br>naverpay=네이버페이, kakaopay=카카오페이, samsungpay=삼성페이                                                           |
| amount            |   Int    |   O   |   12   | 결제 금액                                                                                                                                                                              |
| balanceAmt        |   Int    |   O   |   12   | 취소 가능 잔액<br>부분취소 거래인경우, 전체금액에서   현재까지 취소된 금액을 차감한 금액.                                                                                                                              |
| goodsName         |  String  |   O   |   40   | 상품명                                                                                                                                                                                |
| mallReserved      |  String  |   　   |  500   | 상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                    |
| useEscrow         | Boolean  |   O   |   -    | 에스크로 거래 여부<br>false:일반거래 /   true:에스크로 거래                                                                                                                                          |
| currency          |  String  |   O   |   3    | 결제승인화폐단위<br>KRW:원화, USD:미화달러, CNY:위안화                                                                                                                                              |
| channel           |  String  |   　   |   10   | pc:PC결제, mobile:모바일결제<br>['pc', 'mobile', 'null']                                                                                                                                  |
| approveNo         |  String  |   　   |   30   | 제휴사 승인 번호<br>신용카드, 계좌이체, 휴대폰                                                                                                                                                       |
| buyerName         |  String  |   　   |   30   | 구매자 명                                                                                                                                                                              |
| buyerTel          |  String  |   　   |   40   | 구매자 전화번호                                                                                                                                                                           |
| buyerEmail        |  String  |   　   |   60   | 구매자 이메일                                                                                                                                                                            |
| issuedCashReceipt | Boolean  |   　   |   -    | 현금영수증 발급여부<br>true:발행 /   false:미발행                                                                                                                                                |
| receiptUrl        |  String  |   　   |  200   | 　매출전표 확인 URL                                                                                                                                                                       |
| mallUserId        |  String  |   　   |   20   | 상점에서 관리하는 사용자 아이디                                                                                                                                                                  |

<br>

#### 할인정보 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |           |   Type   |  필수   |  　Byte  | 설명            |
|:----------|:----------|:--------:|:-----:|:-------:|:--------------|
| coupon    | 　         |  Object  |   　   |    -    | 즉시할인 프로모션 정보  |
| 　         | couponAmt |   Int    |   　   |   12    | 즉시할인 적용된 금액   |

<br>

#### 카드 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |                |   Type   |  필수   |  　Byte  | 설명                                                                                            |
|:----------|:---------------|:--------:|:-----:|:-------:|:----------------------------------------------------------------------------------------------|
| card      | 　              |  Object  |   　   |    　    | 신용카드 정보                                                                                       |
| 　         | cardCode       |  String  |   O   |    3    | 신용카드사별 코드                                                                                     |
|           | cardName       |  String  |   O   |   20    | 결제 카드사 이름<br>예) 비씨                                                                            |
|           | cardNum        | String  | 　   | 20     | 카드번호<br>앞 6자 마지막 4자를 제외한 가운데 숫자 마스킹 처리됨<br>예) 536112******1234<br>- 카카오머니/네이버포인트/페이코포인트 전액결제 거래인경우   null |
|           | cardQuota      |   Int    |   O   |    3    | 할부개월<br>0:일시불, 2:2개월, 3:3개월   …                                                               |
|           | isInterestFree | Boolean  |   O   |    -    | 상점분담무이자 여부<br>true:무이자,   false:일반                                                            |
|           | cardType       |  String  |   　   |    1    | 카드 구분<br>credit:신용,   check:체크                                                                |
|           | canPartCancel  |  String  |   O   |    -    | 부분취소 가능 여부<br>true:가능,   false:불가능                                                            |
|           | acquCardCode   |  String  |   O   |    3    | 매입카드사코드                                                                                       |
|           | acquCardName   |  String  |   O   |   100   | 매입카드사명                                                                                        |

<br>

#### 현금영수증 <img src="https://img.shields.io/badge/-Array-blueviolet"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter     |              |   Type   |   필수   |  Byte  | 설명                                                                                                                                                                                                                                                                                                                                                                                                  |
|:--------------|:-------------|:--------:|:------:|:------:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cashReceipts  | 　            |  Array   |   　    |   　    | 현금영수증 발급정보<br>-NaverPay-포인트 ,가상계좌 입금건에서 제공<br>-부분 취소시, 2건이상 존재가능                                                                                                                                                                                                                                                                                                                                    |
| 　             | receiptTid   |  String  |   O    |   30   | 현금영수증 TID                                                                                                                                                                                                                                                                                                                                                                                           |
|               | orgTid       |  String  |   O    |   30   | 연관된 원 승인/취소 거래 TID<br>부분취소시, 원 부분취소   거래건의 TID와 매핑됨<br>- 원거래를 부분취소 하면,   신규 TID가 채번되고,<br>채번된 부분취소 TID가   셋팅 됩니다.                                                                                                                                                                                                                                                                                   |
|               | status       |  String  |   O    |   20   | 발급진행 상태<br>[발급]<br>issueRequested : 발급 접수 완료[1,3]<br>issueReqCancelled : 요청회수(국세청 발행 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>issued : 국세청 발급 완료[4]<br>issueFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10])<br>[취소]<br>cancelRequested : 취소 접수 완료[1,3]<br>cancelReqCancelled : 요청회수(국세청 취소 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>cancelled : 국세청 취소 완료[4]<br>cancelFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10]) |
|               | amount       |   Int    |   O    |   12   | 현금영수증 발행 총금액                                                                                                                                                                                                                                                                                                                                                                                        |
|               | taxFreeAmt   |   Int    |   O    |   12   | 현금영수증 전체 금액중에서 면세금액                                                                                                                                                                                                                                                                                                                                                                                 |
|               | receiptType  |  String  |   O    |   20   | 현금영수증 타입<br>individual : 개인 소득공제용<br>company : 사업자 지출증빙용                                                                                                                                                                                                                                                                                                                                            |
|               | issueNo      |  String  |   O    |   30   | 현금영수증 국세청 발행번호                                                                                                                                                                                                                                                                                                                                                                                      |
|               | receiptUrl   |  String  |   O    |  200   | 현금영수증 매출전표 확인 URL                                                                                                                                                                                                                                                                                                                                                                                   |

<br>

#### 계좌이체 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter  |           |   Type   |  필수   |  Byte  | 설명                |
|:-----------|:----------|:--------:|:-----:|:------:|:------------------|
| bank       | 　         |  Object  |   　   |   　    | 은행 정보             |
| 　          | bankCode  |  String  |   O   |   3    | 결제은행코드 (은행코드 참조)  |
|            | bankName  |  String  |   O   |   20   | 결제은행명 (euc-kr)    |

<br>

#### 가상계좌 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |              |  Type   |  필수   |  Byte  | 설명                       |
|:----------|:-------------|:-------:|:-----:|:------:|:-------------------------|
| vbank     | 　            | Object  |   　   |   　    | 가상계좌 정보                  |
| 　         | vbankCode    | String  |   O   |   3    | 입금받을 가상계좌 은행코드           |
|           | vbankName    | String  |   O   |   20   | 입금받을 가상계좌 은행명            |
|           | vbankNumber  | String  |   O   |   20   | 입금받을 가상계좌 번호             |
|           | vbankExpDate | String  |   O   |   -    | 가상계좌 입금 만료일<br>ISO 8601  |
|           | vbankHolder  | String  |   O   |   40   | 입금받을 가상계좌 예금주명           |

<br>

#### 취소 <img src="https://img.shields.io/badge/-Array-blueviolet"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |             |  Type   |  필수   |  　Byte  | 설명                     |
|:----------|:------------|:-------:|:-----:|:-------:|:-----------------------|
| cancels   | 　           |  Array  |   　   |    　    | 취소/부분취소 내역             |
| 　         | tid         | String  |   O   |   30    | 승인 취소 거래번호             |
|           | amount      |   Int   |   O   |   12    | 취소금액                   |
|           | cancelledAt | String  |   O   |    -    | 취소된 시각<br>ISO 8601     |
|           | reason      | String  |   O   |   100   | 취소사유                   |
|           | receiptUrl  | String  |   O   |   200   | 취소에 대한<br>매출전표 확인 URL  |
|           | couponAmt   |   Int   |   　   |   12    | 쿠폰 취소금액                |

<br>

## 망취소

### Over-view
결제 연동 시 네트워크 순단 혹은 `HTTP client`의 `Read-timeout`으로 결제(승인) 결과가 불확실하다면  
망취소 API를 호출하여 문제거래를 취소 해야 합니다.  
이러한 예외 처리를 통해 데이터 미 매칭의 불확실성을 해소 할 수 있습니다.  
사용 중인 결제(승인) 모델을 확인 후 예외 구간의 망취소 구현을 권장 합니다.

<br>

### 결제창 (Server 승인 모델)의 망취소 구현
<img src="../image/netcancel-server-authorization.svg" width="800px">   

<br>

### 결제창 (Client 승인 모델)의 망취소 구현
<img src="../image/netcancel-client-authorization.svg" width="800px">   

<br>

### 빌링 등 Server-side 결제의 망취소 구현
<img src="../image/netcancel-subscribe.svg" width="800px"> 

<br>

> #### ⚠️ 중요
> 망취소 유효기간은 ⏱️ 1시간으로, 요청 후 1시간 초과건은 망취소가 실패됩니다.  
> 일반적인 거래의 취소는 "취소`(/v1/payments/{tid}/cancel)`" 인터페이스를 사용하고  
> 승인요청 및 응답수신 처리에 실패한 경우에만 망취소 요청을 권장 합니다.

<br>

### 샘플 코드

```bash
curl -X POST 'https://api.nicepay.co.kr/v1/payments/netcancel' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3...' 
-D '{
    "orderID" : "your-order-id”,
}'
```

<br>

### 요청 명세

```bash
POST /v1/payments/netcancel  
HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter     |  Type   |  필수   |  Byte  | 설명                                                                                                         |
|:--------------|:-------:|:-----:|:------:|:-----------------------------------------------------------------------------------------------------------|
| orderId       | String  |   O   |   64   | 취소할 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br>-orderId가 unique한 경우에만 정상 처리됩니다.                      |
| mallReserved  | String  |       |  500   | 상점 예약필드<br>상점 정보 전달용 예비필드                                                                                  |
| ediDate       | String  |       |   -    | 전문생성일시<br>ISO 8601 형식                                                                                      |
| signData      | String  |       |  256   | 위변조 검증 Data<br>생성규칙 : hex(sha256(orderId + ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| returnCharSet | String  |       |   10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                     |

<br>

### 응답 명세 (Body)

```bash
POST
Content-type: application/json
```

| Parameter         |   Type   |  필수   |  Byte  | 설명                                                                                                                                                                                 |
|:------------------|:--------:|:-----:|:------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| resultCode        |  String  |   O   |   4    | 결제결과코드<br>0000 : 성공 / 그외 실패                                                                                                                                                        |
| resultMsg         |  String  |   O   |  100   | 결제결과메시지                                                                                                                                                                            |
| tid               |  String  |   O   |   30   | 결제 승인 키<br>최초 승인(가상계좌-채번)에 성공한 원거래의 NICEPAY 거래키 입니다.                                                                                                                               |
| cancelledTid      |  String  |   　   |   30   | 취소 거래 키<br>NICEPAY가 발행하는 취소 응답 TID (부분취소시 tid와 다른 값이 응답됨)<br>- 취소   요청건에 한하여 응답됨<br>- cancels 객체에서 현재 취소된 거래정보를 찾을 때 사용 하시면 됩니다.                                                   |
| orderId           |  String  |   O   |   64   | 상점 거래 고유번호                                                                                                                                                                         |
| ediDate           |  String  |   O   |   -    | 응답전문생성일시 ISO 8601 형식                                                                                                                                                               |
| signature         |  String  |   　   |  256   | 위변조 검증 데이터<br>- 유효한 거래건에 한하여 응답<br>- 생성규칙 :   hex(sha256(tid + amount + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| status            |  String  |   O   |   20   | 결제 처리상태<br>paid:결제완료,   ready:준비됨, failed:결제실패, cancelled:취소됨, partialCancelled:부분 취소됨, expired:만료됨<br>['paid', 'ready', 'failed', 'cancelled', 'partialCancelled',   'expired']   |
| paidAt            |  String  |   O   |   -    | 결제완료시점 ISO 8601 형식<br>결제완료가 아닐 경우 0                                                                                                                                                |
| failedAt          |  String  |   O   |   -    | 결제실패시점 ISO 8601 형식<br>결제실패가 아닐 경우 0                                                                                                                                                |
| cancelledAt       |  String  |   O   |   -    | 결제취소시점 ISO 8601 형식<br>결제취소가 아닐 경우 0<br>부분취소인경우, 가장   마지막건의 취소 시간                                                                                                                   |
| payMethod         |  String  |   O   |   10   | 결제수단<br><br>card:신용카드,<br>vbank:가상계좌,<br>bank:계좌이체,<br>cellphone:휴대폰,<br>naverpay=네이버페이, kakaopay=카카오페이, samsungpay=삼성페이                                                           |
| amount            |   Int    |   O   |   12   | 결제 금액                                                                                                                                                                              |
| balanceAmt        |   Int    |   O   |   12   | 취소 가능 잔액<br>부분취소 거래인경우, 전체금액에서   현재까지 취소된 금액을 차감한 금액.                                                                                                                              |
| goodsName         |  String  |   O   |   40   | 상품명                                                                                                                                                                                |
| mallReserved      |  String  |   　   |  500   | 상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                    |
| useEscrow         | Boolean  |   O   |   -    | 에스크로 거래 여부<br>false:일반거래 /   true:에스크로 거래                                                                                                                                          |
| currency          |  String  |   O   |   3    | 결제승인화폐단위<br>KRW:원화, USD:미화달러, CNY:위안화                                                                                                                                              |
| channel           |  String  |   　   |   10   | pc:PC결제, mobile:모바일결제<br>['pc', 'mobile', 'null']                                                                                                                                  |
| approveNo         |  String  |   　   |   30   | 제휴사 승인 번호<br>신용카드, 계좌이체, 휴대폰                                                                                                                                                       |
| buyerName         |  String  |   　   |   30   | 구매자 명                                                                                                                                                                              |
| buyerTel          |  String  |   　   |   40   | 구매자 전화번호                                                                                                                                                                           |
| buyerEmail        |  String  |   　   |   60   | 구매자 이메일                                                                                                                                                                            |
| issuedCashReceipt | Boolean  |   　   |   -    | 현금영수증 발급여부<br>true:발행 /   false:미발행                                                                                                                                                |
| receiptUrl        |  String  |   　   |  200   | 　매출전표 확인 URL                                                                                                                                                                       |
| mallUserId        |  String  |   　   |   20   | 상점에서 관리하는 사용자 아이디                                                                                                                                                                  |

<br>

#### 할인정보 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |           |  Type   |  필수   |  　Byte  | 설명            |
|:----------|:----------|:-------:|:-----:|:-------:|:--------------|
| coupon    | 　         | Object  |   　   |    -    | 즉시할인 프로모션 정보  |
| 　         | couponAmt |   Int   |   　   |   12    | 즉시할인 적용된 금액   |

<br>

#### 카드 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |                |   Type    |  필수   |  　Byte  | 설명                                                                                            |
|:----------|:---------------|:---------:|:-----:|:-------:|:----------------------------------------------------------------------------------------------|
| card      | 　              |  Object   |   　   |    　    | 신용카드 정보                                                                                       |
| 　         | cardCode       |  String   |   O   |    3    | 신용카드사별 코드                                                                                     |
|           | cardName       |  String   |   O   |   20    | 결제 카드사 이름<br>예) 비씨                                                                            |
|           | cardNum        | String  | 　   | 20     | 카드번호<br>앞 6자 마지막 4자를 제외한 가운데 숫자 마스킹 처리됨<br>예) 536112******1234<br>- 카카오머니/네이버포인트/페이코포인트 전액결제 거래인경우   null |
|           | cardQuota      |    Int    |   O   |    3    | 할부개월<br>0:일시불, 2:2개월, 3:3개월   …                                                               |
|           | isInterestFree |  Boolean  |   O   |    -    | 상점분담무이자 여부<br>true:무이자,   false:일반                                                            |
|           | cardType       |  String   |   　   |    1    | 카드 구분<br>credit:신용,   check:체크                                                                |
|           | canPartCancel  |  String   |   O   |    -    | 부분취소 가능 여부<br>true:가능,   false:불가능                                                            |
|           | acquCardCode   |  String   |   O   |    3    | 매입카드사코드                                                                                       |
|           | acquCardName   |  String   |   O   |   100   | 매입카드사명                                                                                        |

<br>

#### 현금영수증 <img src="https://img.shields.io/badge/-Array-blueviolet"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter    |             |  Type   |  필수   |  Byte  | 설명                                                                                                                                                                                                                                                                                                                                                                                                   |
|:-------------|:------------|:-------:|:-----:|:------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cashReceipts | 　           |  Array  |   　   |   　    | 현금영수증 발급정보<br>-NaverPay-포인트 ,가상계좌 입금건에서 제공<br>-부분 취소시, 2건이상 존재가능                                                                                                                                                                                                                                                                                                                                     |
| 　            | receiptTid  | String  |   O   |   30   | 현금영수증 TID                                                                                                                                                                                                                                                                                                                                                                                            |
|              | orgTid      | String  |   O   |   30   | 연관된 원 승인/취소 거래 TID<br>부분취소시, 원 부분취소   거래건의 TID와 매핑됨<br>- 원거래를 부분취소 하면,   신규 TID가 채번되고,<br>채번된 부분취소 TID가   셋팅 됩니다.                                                                                                                                                                                                                                                                                    |
|              | status      | String  |   O   |   20   | 발급진행 상태<br>[발급]<br>issueRequested : 발급 접수 완료[1,3]<br>issueReqCancelled : 요청회수(국세청 발행 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>issued : 국세청 발급 완료[4]<br>issueFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10])<br>[취소]<br>cancelRequested : 취소 접수 완료[1,3]<br>cancelReqCancelled : 요청회수(국세청 취소 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>cancelled : 국세청 취소 완료[4]<br>cancelFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10])  |
|              | amount      |   Int   |   O   |   12   | 현금영수증 발행 총금액                                                                                                                                                                                                                                                                                                                                                                                         |
|              | taxFreeAmt  |   Int   |   O   |   12   | 현금영수증 전체 금액중에서 면세금액                                                                                                                                                                                                                                                                                                                                                                                  |
|              | receiptType | String  |   O   |   20   | 현금영수증 타입<br>individual : 개인 소득공제용<br>company : 사업자 지출증빙용                                                                                                                                                                                                                                                                                                                                             |
|              | issueNo     | String  |   O   |   30   | 현금영수증 국세청 발행번호                                                                                                                                                                                                                                                                                                                                                                                       |
|              | receiptUrl  | String  |   O   |  200   | 현금영수증 매출전표 확인 URL                                                                                                                                                                                                                                                                                                                                                                                    |

<br>

#### 계좌이체 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">


| Parameter  |           |   Type   |  필수   |  Byte  | 설명                |
|:-----------|:----------|:--------:|:-----:|:------:|:------------------|
| bank       | 　         |  Object  |   　   |   　    | 은행 정보             |
| 　          | bankCode  |  String  |   O   |   3    | 결제은행코드 (은행코드 참조)  |
|            | bankName  |  String  |   O   |   20   | 결제은행명 (euc-kr)    |


<br>

#### 가상계좌 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |              |  Type   |  필수   |  Byte  | 설명                       |
|:----------|:-------------|:-------:|:-----:|:------:|:-------------------------|
| vbank     | 　            | Object  |   　   |   　    | 가상계좌 정보                  |
| 　         | vbankCode    | String  |   O   |   3    | 입금받을 가상계좌 은행코드           |
|           | vbankName    | String  |   O   |   20   | 입금받을 가상계좌 은행명            |
|           | vbankNumber  | String  |   O   |   20   | 입금받을 가상계좌 번호             |
|           | vbankExpDate | String  |   O   |   -    | 가상계좌 입금 만료일<br>ISO 8601  |
|           | vbankHolder  | String  |   O   |   40   | 입금받을 가상계좌 예금주명           |

<br>

#### 취소 <img src="https://img.shields.io/badge/-Array-blueviolet"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |             |   Type   |  필수   |  　Byte  | 설명                     |
|:----------|:------------|:--------:|:-----:|:-------:|:-----------------------|
| cancels   | 　           |  Array   |   　   |    　    | 취소/부분취소 내역             |
| 　         | tid         |  String  |   O   |   30    | 승인 취소 거래번호             |
|           | amount      |   Int    |   O   |   12    | 취소금액                   |
|           | cancelledAt |  String  |   O   |    -    | 취소된 시각<br>ISO 8601     |
|           | reason      |  String  |   O   |   100   | 취소사유                   |
|           | receiptUrl  |  String  |   O   |   200   | 취소에 대한<br>매출전표 확인 URL  |
|           | couponAmt   |   Int    |   　   |   12    | 쿠폰 취소금액                |

  
## 웹훅

- [웹훅 발송 흐름](#웹훅-발송-흐름)
- [웹훅 발송 시점](#웹훅-발송-시점)
- [웹훅 URL 추가](#웹훅-url-추가) : 결제수단을 선택하여 웹훅을 추가 하는 기능
- [웹훅 TEST 호출](#웹훅-test호출) : 웹훅 등록 후 등록된 `End-point`로 Test 전문을 전달하는 기능
- [웹훅 재전송](#웹훅-재전송) : 웹훅 전송 실패시 처리 가이드
- [웹훅 로그](#웹훅-로그) : 전달된 웹훅의 로그 확인 가이드
- [웹훅 응답 명세](#웹훅-응답-명세)

🔔 웹훅은 API의 이벤트를 `Server-side`로 응답 받아 추가적인 비즈니스 로직을 구현 할 수 있는 기능으로  
가상계좌 처럼 계좌 생성과 입금시점 차이가 발생하는 결제 수단을 사용하는 경우 반드시 구현이 필요 합니다.  
개발정보 탭 에서 제공되는 웹훅은 추가/삭제관리, TEST 호출, 재전송, 로그 체크 기능을 제공 합니다.

![image](https://user-images.githubusercontent.com/86043374/128665498-39293a3d-d1c0-4dc9-9502-d2b223d81597.png)

<br>

### Over-view
<img src="../image/payment-webhook.svg" width="800px"> 

### 웹훅 발송 흐름
- 등록된 웹훅 `End-point`로 이벤트 발생시 웹훅 전문 Post
- 가맹점은 Server에서 웹훅 전문 확인 후 비즈니스 로직을 처리
- 비즈니스 로직 처리 후 `HTTP Status 200`과 `ResponseBody`에 "OK” 문자열을 print하여 응답

<br>

### 웹훅 발송 시점
- 💳 결제(승인) 되었을 때(모든 지불수단)
- 가상계좌가 발급(채번) 되었을 때
- 가상계좌에 결제금액이 입금 되었을 때
- 결제가 취소 처리되었을 때 (API 또는 가맹점관리자 취소)

<br>

> #### ⚠️ 중요
> `Response body`에 "OK” 문자열이 없는 경우 실패로 처리되기 때문에 주의가 필요 합니다.  
> [방화벽 정책](#방화벽-정책)을 통해 `Inbound IP` 를 제한하는 것을 권장하고 있습니다.   
> 비즈니스 로직 처리 전 웹훅 전문에 포함된 위변조 검증값 `signature` 과 금액을 반드시 체크 해주세요.

<br>

### 웹훅 URL 추가

![image](https://user-images.githubusercontent.com/86043374/128665650-59e1c404-383c-45a8-958d-e97dfcf8f5bc.png)  
🔔 웹훅을 전달 받을 `End-point`와 결제수단을 선택하고 등록하면 웹훅 등록이 완료 됩니다.  
유효한 도메인을 등록해야 하며 등록 후 TEST호출 버튼을 통해 웹훅 전문이 정상적으로 응답되는지 반드시 확인 해 주세요.

<br>

### 웹훅 개발정보

![image](https://user-images.githubusercontent.com/86043374/128665763-ce74dccf-d672-4670-ad9c-5ce2a4e5e108.png)


### 웹훅 테스트 호출

#### 웹훅 테스트 호출 처리 프로세스
<img src="../image/sandbox-webhook.svg" width="800px">  
웹훅 등록 후 TEST호출 버튼을 클릭하면 등록된 `End-point`로 test 웹훅 전문이 전달 됩니다.  
또한 등록된 `End-point`에서 웹훅 처리가 성공적으로 되었는지 체크가 가능 합니다.  

<br>

### 웹훅 재전송

웹훅 재전송은 네트워크 이슈 등의 문제로 인해 웹훅 처리의 문제가 발생 하여  
재전송이 필요한 경우 활용 할 수 있습니다.  
웹훅 재전송은 다음과 같은 흐름으로 진행 됩니다.

- 로그인 > 개발정보 > 로그 상세보기 > 웹훅 탭 클릭
- 주문번호를 통해 재전송이 필요한 웹훅 검색
- 검색이 완료된 경우 거래를 선택하여 오른쪽 상단 재전송 버튼 클릭

> #### ⚠️ 중요
> 웹훅 재전송이 반복적으로 실패 하는 경우 다음과 같은 확인이 필요 합니다.
> - [방화벽 정책](#방화벽-정책) 확인 후 웹훅 Test버튼 클릭하여 정상인지 체크
> - [웹훅 매뉴얼](#over-view)을 통해 연동이 정상인지 체크

<br>

### 응답 명세 (Body)

```bash
POST
Content-type: application/json;charset=utf-8
```

| Parameter         |  Type   | 필수  | Byte | 설명                                                                                                                                                                                |
|:------------------|:-------:|:---:|:----:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| resultCode        | String  |  O  |  4   | 결제결과코드<br>0000 : 성공 / 그외 실패                                                                                                                                                       |
| resultMsg         | String  |  O  | 100  | 결제결과메시지                                                                                                                                                                           |
| tid               | String  |  O  |  30  | 결제 승인 키<br>최초 승인(가상계좌-채번)에 성공한 원거래의 NICEPAY 거래키 입니다.                                                                                                                              |
| cancelledTid      | String  |  　  |  30  | 취소 거래 키<br>NICEPAY가 발행하는 취소 응답 TID (부분취소시 tid와 다른 값이 응답됨)<br>- 취소   요청건에 한하여 응답됨<br>- cancels 객체에서 현재 취소된 거래정보를 찾을 때 사용 하시면 됩니다.                                                  |
| orderId           | String  |  O  |  64  | 상점 거래 고유번호                                                                                                                                                                        |
| ediDate           | String  |  O  |  -   | 응답전문생성일시 ISO 8601 형식                                                                                                                                                              |
| signature         | String  |  　  | 256  | 위변조 검증 데이터<br>- 유효한 거래건에 한하여 응답<br>- 생성규칙 :   hex(sha256(tid + amount + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다. |
| status            | String  |  O  |  20  | 결제 처리상태<br>paid:결제완료,   ready:준비됨, failed:결제실패, cancelled:취소됨, partialCancelled:부분 취소됨, expired:만료됨<br>['paid', 'ready', 'failed', 'cancelled', 'partialCancelled',   'expired']  |
| paidAt            | String  |  O  |  -   | 결제완료시점 ISO 8601 형식<br>결제완료가 아닐 경우 0                                                                                                                                               |
| failedAt          | String  |  O  |  -   | 결제실패시점 ISO 8601 형식<br>결제실패가 아닐 경우 0                                                                                                                                               |
| cancelledAt       | String  |  O  |  -   | 결제취소시점 ISO 8601 형식<br>결제취소가 아닐 경우 0<br>부분취소인경우, 가장   마지막건의 취소 시간                                                                                                                  |
| payMethod         | String  |  O  |  10  | 결제수단<br><br>card:신용카드,<br>vbank:가상계좌,<br>bank:계좌이체,<br>cellphone:휴대폰,<br>naverpay=네이버페이, kakaopay=카카오페이, samsungpay=삼성페이                                                          |
| amount            |   Int   |  O  |  12  | 결제 금액                                                                                                                                                                             |
| balanceAmt        |   Int   |  O  |  12  | 취소 가능 잔액<br>부분취소 거래인경우, 전체금액에서   현재까지 취소된 금액을 차감한 금액.                                                                                                                             |
| goodsName         | String  |  O  |  40  | 상품명                                                                                                                                                                               |
| mallReserved      | String  |  　  | 500  | 상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                   |
| useEscrow         | Boolean |  O  |  -   | 에스크로 거래 여부<br>false:일반거래 /   true:에스크로 거래                                                                                                                                         |
| currency          | String  |  O  |  3   | 결제승인화폐단위<br>KRW:원화, USD:미화달러, CNY:위안화                                                                                                                                             |
| channel           | String  |  　  |  10  | pc:PC결제, mobile:모바일결제<br>['pc', 'mobile', 'null']                                                                                                                                 |
| approveNo         | String  |  　  |  30  | 제휴사 승인 번호<br>신용카드, 계좌이체, 휴대폰                                                                                                                                                      |
| buyerName         | String  |  　  |  30  | 구매자 명                                                                                                                                                                             |
| buyerTel          | String  |  　  |  40  | 구매자 전화번호                                                                                                                                                                          |
| buyerEmail        | String  |  　  |  60  | 구매자 이메일                                                                                                                                                                           |
| issuedCashReceipt | Boolean |  　  |  -   | 현금영수증 발급여부<br>true:발행 /   false:미발행                                                                                                                                               |
| receiptUrl        | String  |  　  | 200  | 　매출전표 확인 URL                                                                                                                                                                      |
| mallUserId        | String  |  　  |  20  | 상점에서 관리하는 사용자 아이디                                                                                                                                                                 |

<br>

#### 할인정보 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |           |  Type  | 필수  | 　Byte | 설명           |
|:----------|:----------|:------:|:---:|:-----:|:-------------|
| coupon    | 　         | Object |  　  |   -   | 즉시할인 프로모션 정보 |
| 　         | couponAmt |  Int   |  　  |  12   | 즉시할인 적용된 금액  |

<br>

#### 카드 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |                |  Type   | 필수  | 　Byte | 설명                                                                                           |
|:----------|:---------------|:-------:|:---:|:-----:|:---------------------------------------------------------------------------------------------|
| card      | 　              | Object  |  　  |   　   | 신용카드 정보                                                                                      |
| 　         | cardCode       | String  |  O  |   3   | 신용카드사별 코드                                                                                    |
|           | cardName       | String  |  O  |  20   | 결제 카드사 이름<br>예) 비씨                                                                           |
|           | cardNum        | String  | 　   | 20     | 카드번호<br>앞 6자 마지막 4자를 제외한 가운데 숫자 마스킹 처리됨<br>예) 536112******1234<br>- 카카오머니/네이버포인트/페이코포인트 전액결제 거래인경우   null |
|           | cardQuota      |   Int   |  O  |   3   | 할부개월<br>0:일시불, 2:2개월, 3:3개월   …                                                              |
|           | isInterestFree | Boolean |  O  |   -   | 상점분담무이자 여부<br>true:무이자,   false:일반                                                           |
|           | cardType       | String  |  　  |   1   | 카드 구분<br>credit:신용,   check:체크                                                               |
|           | canPartCancel  | String  |  O  |   -   | 부분취소 가능 여부<br>true:가능,   false:불가능                                                           |
|           | acquCardCode   | String  |  O  |   3   | 매입카드사코드                                                                                      |
|           | acquCardName   | String  |  O  |  100  | 매입카드사명                                                                                       |

<br>

### 현금영수증 <img src="https://img.shields.io/badge/-Array-blueviolet"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter    |             |  Type  | 필수  | Byte | 설명                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-------------|:------------|:------:|:---:|:----:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cashReceipts | 　           | Array  |  　  |  　   | 현금영수증 발급정보<br>-NaverPay-포인트 ,가상계좌 입금건에서 제공<br>-부분 취소시, 2건이상 존재가능                                                                                                                                                                                                                                                                                                                                    |
| 　            | receiptTid  | String |  O  |  30  | 현금영수증 TID                                                                                                                                                                                                                                                                                                                                                                                           |
|              | orgTid      | String |  O  |  30  | 연관된 원 승인/취소 거래 TID<br>부분취소시, 원 부분취소   거래건의 TID와 매핑됨<br>- 원거래를 부분취소 하면,   신규 TID가 채번되고,<br>채번된 부분취소 TID가   셋팅 됩니다.                                                                                                                                                                                                                                                                                   |
|              | status      | String |  O  |  20  | 발급진행 상태<br>[발급]<br>issueRequested : 발급 접수 완료[1,3]<br>issueReqCancelled : 요청회수(국세청 발행 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>issued : 국세청 발급 완료[4]<br>issueFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10])<br>[취소]<br>cancelRequested : 취소 접수 완료[1,3]<br>cancelReqCancelled : 요청회수(국세청 취소 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>cancelled : 국세청 취소 완료[4]<br>cancelFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10]) |
|              | amount      |  Int   |  O  |  12  | 현금영수증 발행 총금액                                                                                                                                                                                                                                                                                                                                                                                        |
|              | taxFreeAmt  |  Int   |  O  |  12  | 현금영수증 전체 금액중에서 면세금액                                                                                                                                                                                                                                                                                                                                                                                 |
|              | receiptType | String |  O  |  20  | 현금영수증 타입<br>individual : 개인 소득공제용<br>company : 사업자 지출증빙용                                                                                                                                                                                                                                                                                                                                            |
|              | issueNo     | String |  O  |  30  | 현금영수증 국세청 발행번호                                                                                                                                                                                                                                                                                                                                                                                      |
|              | receiptUrl  | String |  O  | 200  | 현금영수증 매출전표 확인 URL                                                                                                                                                                                                                                                                                                                                                                                   |

<br>

### 계좌이체 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter  |           |   Type   |  필수   |  Byte  | 설명                |
|:-----------|:----------|:--------:|:-----:|:------:|:------------------|
| bank       | 　         |  Object  |   　   |   　    | 은행 정보             |
| 　          | bankCode  |  String  |   O   |   3    | 결제은행코드 (은행코드 참조)  |
|            | bankName  |  String  |   O   |   20   | 결제은행명 (euc-kr)    |

<br>

### 가상계좌 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |               |   Type   |  필수   |  Byte  | 설명                       |
|:----------|:--------------|:--------:|:-----:|:------:|:-------------------------|
| vbank     | 　             |  Object  |   　   |   　    | 가상계좌 정보                  |
| 　         | vbankCode     |  String  |   O   |   3    | 가상계좌 은행코드                |
|           | vbankName     |  String  |   O   |   20   | 가상계좌 은행명                 |
|           | vbankNumber   |  String  |   O   |   20   | 가상계좌 번호                  |
|           | vbankExpDate  |  String  |   O   |   -    | 가상계좌 입금 만료일<br>ISO 8601  |
|           | vbankHolder   |  String  |   O   |   40   | 가상계좌 예금주명                |

<br>

### 취소 <img src="https://img.shields.io/badge/-Array-blueviolet"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |             |   Type   |  필수   |  　Byte  | 설명                     |
|:----------|:------------|:--------:|:-----:|:-------:|:-----------------------|
| cancels   | 　           |  Array   |   　   |    　    | 취소/부분취소 내역             |
| 　         | tid         |  String  |   O   |   30    | 승인 취소 거래번호             |
|           | amount      |   Int    |   O   |   12    | 취소금액                   |
|           | cancelledAt |  String  |   O   |    -    | 취소된 시각<br>ISO 8601     |
|           | reason      |  String  |   O   |   100   | 취소사유                   |
|           | receiptUrl  |  String  |   O   |   200   | 취소에 대한<br>매출전표 확인 URL  |
|           | couponAmt   |   Int    |   　   |   12    | 쿠폰 취소금액                |



### 웹훅 로그
가맹점 디버깅 편의를 위해 웹훅 로그를 제공하고 있습니다.  
응답된 웹훅과 정보 비교가 필요하거나 재전송이 기능이 필요한 경우 활용 할 수 있습니다.  
웹훅 로그를 통해 다음과 같은 정보를 확인 할 수 있습니다.

- 웹훅이 전달된 시간과 정보
- 웹훅 전달시 body 정보
- 웹훅 재전송을 위한 버튼

<br>


# iOS

- [공통사항](#iOS-공통사항)
  - [지원환경](#iOS-지원환경)
  - [개발흐름](#iOS-개발흐름)
  - [appScheme 설정 - Client 승인 모델](#iOS-appscheme-설정---client-승인-모델)
  - [appScheme 설정 - Server 승인 모델](#iOS-appscheme-설정---server-승인-모델)

  - [URL Scheme 설정](#iOS-url-scheme-설정)
  - [3rd 어플리케이션 URL Scheme 등록](#iOS-3rd-어플리케이션-url-scheme-등록)
  - [3rd URL Scheme 리스트](#iOS-3rd-url-scheme-리스트)
  - [네트워크 보안 예외 설정](#iOS-네트워크-보안-예외-설정)

- [iOS-Swift 웹뷰(web-view)개발 가이드](#ios-swift-웹뷰--web-view--개발-가이드)
  - [결제 페이지 호출](#ios-swift-결제-페이지-호출)
  - [URL 처리 및 3rd 어플리케이션 호출](#ios-swift-url-처리-및-3rd-어플리케이션-호출)
  - [자바 스크립트 팝업 처리](#ios-swift-자바스크립트-팝업-처리)

- [iOS-Objective-C 웹뷰(web-view)개발 가이드](#ios-objective-c-웹뷰--web-view--개발-가이드)
  - [결제 페이지 호출](#ios-objective-c-결제-페이지-호출)
  - [URL 처리 및 3rd 어플리케이션 호출](#ios-objective-c-url-처리-및-3rd-어플리케이션-호출)
  - [자바 스크립트 팝업 처리](#ios-objective-c-자바스크립트-팝업-처리)


## iOS 공통사항
App 내 웹뷰를 통해 결제창을 연동하는 경우, 웹 환경에서 결제창을 통한 💳 결제(승인)이 가능하도록 개발이 선행 되어야 합니다.  
이 후 appScheme 값을 설정 합니다.  
카드사를 포함한 제휴사 인증 완료 후 전달된 가맹점 APP의 scheme을 확인하여 화면 focus가 이동 하게 됩니다.

<br>

### iOS 지원환경
- IOS 9.0 이상
- Xcode 7.x 이상
- Swift 4.0 이상

<br>

### iOS 개발흐름
결제창을 App내 에서 구현하는 경우 웹뷰(Web-view)를 통해 구현 처리가 가능 합니다.  
빠른 개발 진행을 원하는 경우 샘플코드를 검토 후 가이드 확인을 권장 합니다.

- 결제창 호출시 appScheme 값 셋팅
- 환경 설정
- URL Scheme 설정
- 예외처리 (java-script, 네트워크)

<br>

> #### ⚠️ 중요
> 가맹점 결제 요청 페이지 로드 실패 하는 경우 가맹점 페이지가 HTTP 라면 `info.plist` 내 네트워크 🔒 보안 예외 설정을 확인(ATS) 해주세요.  
> 3rd 어플리케이션 호출 불가한 경우 `info.plist` 내 `3rd URL Scheme` 설정을 확인 해주세요.  
> 3rd 어플리케이션에서 인증 or 결제 완료 후 가맹점 어플리케이션으로 미전환시 `info.plist` 내 가맹점 URL Scheme 설정을 확인해 주세요.  
> 결제 완료 후 웹 브라우저 호출이 되지 않는 경우 `info.plist` 내 가맹점 URL Scheme 설정 값과 결제창 JS SDK로 전달된 appScheme 값이 일치하는지 체크 해주세요.  
> 팝업창 미노출 되는 경우 웹뷰의 자바스크립트 오버라이딩 함수 재정를 해주세요.

<br>


### appScheme 설정 - Client 승인 모델

```html
<script src="https://pay.nicepay.co.kr/v1/js/"></script> 
<script>
    function serverAuth() {
        AUTHNICE.requestPay({
            clientId: 'R1_af0d116236df437f831483ee9c500bc4',
            appScheme: `nicepaysample://`,
            method: 'vbank',
            orderId: 'your-unique-orderid',
            amount: 1004,
            goodsName: '나이스페이-상품',
            returnUrl: 'http://localhost:4567/serverAuth'
        });
    }
</script>
```

<br>

### appScheme 설정 - Server 승인 모델

```html
<script src="https://pay.nicepay.co.kr/v1/js/"></script>
<script>
    function serverAuth() {
        AUTHNICE.requestPay({
            clientId: 'af0d116236df437f831483ee9c500bc4',
            appScheme: `nicepaysample://`,
            method: 'vbank',
            orderId: 'your-unique-orderid',
            amount: 1004,
            goodsName: '나이스페이-상품',
            returnUrl: 'http://localhost:4567/serverAuth'
        });
    }
</script>
```

<br>


### URL Scheme 설정

- 가맹점 어플리케이션에 URL Scheme 을 등록합니다. (JS SDK 호출시 appScheme 필드 값으로 URL Scheme 사용)
- `info.plist` 파일에 URL Scheme을 등록 합니다. (3rd 어플리케이션 -> 가맹점 어플리케이션 호출)

```bash
info.plist
```

```xml
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
            <string>kr.co.nicepay.swift.NicepayAppSample</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>nicepaysample</string>
        </array>
    </dict>
</array>
```

<br>

> #### ⚠️ 중요
> `info.plist` 파일에 URL Scheme 미설정 시 특정 3rd 어플리케이션에서 인증 or 결제 완료 후 가맹점 어플리케이션으로 자동 전환이 불가 합니다.

<br>

#### 3rd party app URL Scheme 등록

- `info.plist` 파일에 `3rd URL Scheme`을 등록 합니다. (가맹점 어플리케이션 -> 3rd 어플리케이션 호출)
- URL Scheme 미설정 시 3rd 어플리케이션 연동이 불가 합니다.

```bash
info.plist
```

```xml
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>kftc-bankpay</string>
    <string>ispmobile</string>
    <string>shinhan-sr-ansimclick</string>
    <string>smshinhanansimclick</string>
    <string>hdcardappcardansimclick</string>
    <string>smhyundaiansimclick</string>
    <string>mpocket.online.ansimclick</string>
    <string>scardcertiapp</string>
    <string>cloudpay</string>
    <string>nhappcardansimclick</string>
    <string>nonghyupcardansimclick</string>
    <string>kb-acp</string>
    <string>lotteappcard</string>
    <string>lottesmartpay</string>
    <string>citispay</string>
    <string>shinsegaeeasypayment</string>
    <string>kakaotalk</string>
    <string>tswansimclick</string>
    <string>nhallonepayansimclick</string>
    <string>citimobileapp</string>
    <string>payco</string>
    <string>hanaskcardmobileportal</string>
    <string>wooripay</string>
   <string>com.wooricard.wcard</string>
    <string>lpayapp</string>
    <string>hanawalletmembers</string>
    <string>tauthlink</string>
    <string>ktauthexternalcall</string>
    <string>upluscorporation</string>
    <string>liivbank</string>
   <string>kb-bankpay</string>
   <string>naversearchthirdlogin</string>
   <string>lmslpay</string>
</array>
```

<br>

#### 3rd URL Scheme 리스트

| APP                   | SCHEME                       |
|-----------------------|------------------------------|
| 신한 앱카드 결제             | shinhan-sr-ansimclick://     |
| 신한카드 일반결제             | smshinhanansimclick://       |
| 현대 앱카드 결제             | hdcardappcardansimclick://   |
| 현대카드 일반결제             | smhyundaiansimclick://       |
| 삼성 앱카드 결제             | mpocket.online.ansimclick:// |
| 삼성카드 일반결제             | scardcertiapp://             |
| 하나 앱카드 결제             | cloudpay://                  |
| 농협 앱카드 결제             | nhappcardansimclick://       |
| 농협카드 일반결제             | nonghyupcardansimclick://    |
| KB 앱카드 결제(KB Pay)     | kb-acp://                    |
| 롯데 앱카드 결제             | lotteappcard://              |
| 롯데카드 스마트결제            | lottesmartpay://             |
| 롯데카드 LPAY             | lpayapp://                   |
| 시티 앱카드 결제             | citispay://                  |
| ISP 인증결제              | ispmobile://                 |
| SSG-PAY 결제            | shinsegaeeasypayment://      |
| 시럽페이                  | tswansimclick://             |
| 농협카드 올원페이 결제          | nhallonepayansimclick://     |
| 시티 앱카드 모바일 결제         | citimobileapp://             |
| 페이코                   | payco://                     |
| 카카오페이                 | kakaotalk://                 |
| 하나카드 일반결제             | hanaskcardmobileportal://    |
| 우리 앱카드 결제             | wooripay://                  |
| 우리 앱카드 결제(리뉴얼)        | com.wooricard.wcard://       |
| 하나멤버스 월렛              | hanawalletmembers://         |
| SKT 본인인증(PASS) APP    | tauthlink://                 |
| KT 본인인증(PASS) APP     | ktauthexternalcall://        |
| LG U+ 본인인증(PASS)  APP | upluscorporation://          |
| 네이버페이 앱 로그인           | naversearchthirdlogin://     |
| LPAY 앱                | lmslpay://                   |
| 뱅크페이(금융결제원)           | kftc-bankpay://              |
| KB-리브페이               | liivbank://                  |
| KB 계좌이체 APP           | kb-bankpay://                |

<br>

### 네트워크 보안 예외 설정
- HTTP 또는 유효하지 않은 인증서를 가진 HTTPS 연결 시 예외 처리입니다.
- Apple에서는 하기와 같은 방법을 권장하지 않으며, 특정 도메인에 대해서만 예외 처리하도록 권장 합니다.

<br>

```bash
info.plist
```

```xml
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

<br>

## iOS-Swift 웹 뷰(web-view)개발 가이드

### 결제 페이지 호출

- 웹뷰의 load를 통해 결제 요청 URL을 호출 합니다. 가맹점 결제 요청 웹 페이지 예시

```bash
swift
```

```swift
override func viewDidLoad() {
        super.viewDidLoad()

        title = "구매하기 TEST"
        
        webView = WKWebView(frame: self.view.frame)
        webView?.navigationDelegate = self
        webView?.uiDelegate = self
        self.view.addSubview(webView!)
        
        let url = URL(string: PAY_URL)
        let request = URLRequest(url: url!)
        webView?.load(request)
 }
```

<br>

### URL 처리 및 3rd party app 호출

- URL에 포함된 App Scheme을 통해 어플리케이션 호출(openURL)
```bash
swift
```

```swift
func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
        let request = navigationAction.request
        let optUrl = request.url
        let optUrlScheme = optUrl?.scheme
        
        guard let url = optUrl, let scheme = optUrlScheme
            else {
                return decisionHandler(WKNavigationActionPolicy.cancel)
        }
        
        debugPrint("url : \(url)")
       
        if( scheme != "http" && scheme != "https" ) {
            if( scheme == "ispmobile" && !UIApplication.shared.canOpenURL(url) ) {  //ISP 미설치 시
                UIApplication.shared.openURL(URL(string: "http://itunes.apple.com/kr/app/id369125087?mt=8")!)
            } else if( scheme == "kftc-bankpay" && !UIApplication.shared.canOpenURL(url) ) {    //BANKPAY 미설치 시
                UIApplication.shared.openURL(URL(string: "http://itunes.apple.com/us/app/id398456030?mt=8")!)
            } else {
                if( UIApplication.shared.canOpenURL(url) ) {
                    UIApplication.shared.openURL(url)
                } else {
                    //1. App 미설치 확인
                    //2. info.plist 내 scheme 등록 확인
                }
            }
        }
        
        decisionHandler(WKNavigationActionPolicy.allow)
    }

```

<br>

### 자바스크립트 팝업 처리

- 웹뷰의 오버라이딩 함수를 재정의 하여 팝업 처리 하면 웹뷰 처리가 완료 됩니다.

```bash
swift
```
```swift
func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping () -> Void) {
        let alert = UIAlertController(title: "", message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "확인", style: .default, handler: { (UIAlertAction) in
            completionHandler()
        }))
        
        self.present(alert, animated: true, completion: nil)
}
```

<br>

## iOS-Objective-C 웹 뷰(web-view)개발 가이드

<br>

### 결제 페이지 호출
- 웹뷰의 loadRequest를 통해 결제 요청 URL을 호출 (가맹점 결제 요청 웹 페이지)
```bash
Object-C
```
```objective-c
(void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
    self.title = @"구매하기";
    
    self.webView = [[[WKWebView alloc] init] autorelease];
    self.webView.navigationDelegate = self;
    self.webView.UIDelegate = self;
    [self.view addSubview:self.webView];
    
    //nicepay 결제테스트 URL 입니다.
    //제공 된 샘플 상 payRequest 스크립트 페이지를 참고 하시여 개발 하시면 됩니다.
    [self.webView loadRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:PAY_URL]]];
}
```

<br>

### URL 처리 및 3rd party app 호출

- URL에 포함된 App Scheme을 통해 어플리케이션 호출(openURL)

```bash
Object-C
```

```objective-c
(void)webView:(WKWebView *)webView decidePolicyForNavigationAction:(WKNavigationAction *)navigationAction decisionHandler:(void (^)(WKNavigationActionPolicy))decisionHandler {
    NSURLRequest *request = navigationAction.request;
    NSURL *url = [request URL];
    NSString *urlScheme = [url scheme];
    
    NSLog(@"url : %@", url);
    
    if( ![urlScheme isEqualToString:@"http"] && ![urlScheme isEqualToString:@"https"] ) {
        if( [urlScheme isEqualToString:@"ispmobile"] && ![[UIApplication sharedApplication] canOpenURL:url] ) {
            //ISP App가 설치되어 있지 않을 경우 앱스토어로 이동
            [[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"http://itunes.apple.com/kr/app/id369125087?mt=8"]];
        } else if( [urlScheme isEqualToString:@"kftc-bankpay"] && ![[UIApplication sharedApplication] canOpenURL:url] ) {
            //BANKPAY App가 설치되어 있지 않을 경우 앱스토어로 이동
            [[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"http://itunes.apple.com/us/app/id398456030?mt=8"]];
        } else {
            if( [[UIApplication sharedApplication] canOpenURL:url] ) {
                [[UIApplication sharedApplication] openURL:url];    //App 실행
            } else {
                //1. App 미설치 확인
                //2. info.plist 내 scheme 등록 확인
            }
        }
    }
    
    decisionHandler(WKNavigationActionPolicyAllow);
}

```

<br>

### 자바스크립트 팝업 처리

- 웹뷰의 오버라이딩 함수를 재정의 하여 팝업 처리

```bash
Object-C
```

``` objective-c
(void)webView:(WKWebView *)webView runJavaScriptAlertPanelWithMessage:(NSString *)message initiatedByFrame:(WKFrameInfo *)frame completionHandler:(void (^)(void))completionHandler {

    UIAlertController *alertController = [UIAlertController alertControllerWithTitle:nil
                                                                    message:message
                                                                    preferredStyle:UIAlertControllerStyleAlert];
    [alertController addAction:[UIAlertAction actionWithTitle:@"확인"
                                                                    style:UIAlertActionStyleCancel
                                                                        handler:^(UIAlertAction *action) {
                                                                        completionHandler();
                                                                    }]];
    [self presentViewController:alertController animated:YES completion:^{}];
}

```


# Android

- [지원 환경](#Android-지원-환경)
- [개발 흐름](#Android-개발-흐름)
- [공통사항](#Android-공통사항)
  - [appScheme 설정 - Server 승인 모델, Client 승인 모델](#android-appscheme-설정--server-승인-모델-client-승인-모델)
  - [권한 설정](#Android-권한-설정)
  - [네트워크 보안정책 설정](#Android-네트워크-보안정책-설정)

- [Android-java 웹뷰(web-view)개발 가이드](#android-java-웹뷰--web-view--개발-가이드)
  - [Android-java 기본 설정 및 자바스크립트 허용](#android-java-기본-설정-및-자바스크립트-허용)
  - [Android-java 캐시 및 쿠키 설정](#android-java-캐시-및-쿠키-설정)
  - [Android-java 결제 페이지 호출](#Android-java-결제-페이지-호출)
  - [Android-java URL 및 Intent 처리](#android-java-uri-및-intent-처리)
- [Android-kotlin 웹뷰(web-view)개발 가이드](#android-kotlin-웹뷰--web-view--개발-가이드)
	- [Android-kotlin 기본 설정 및 자바스크립트 허용](#android-kotlin-기본-설정-및-자바스크립트-허용)
	- [Android-kotlin 캐시 및 쿠키 설정](#android-kotlin-캐시-및-쿠키-설정)
	- [Android-kotlin 결제 페이지 호출](#Android-kotlin-결제-페이지-호출)
	- [Android-kotlin URL 및 Intent 처리](#android-kotlin-uri-및-intent-처리)

## Android 지원 환경
- `Android 4.4` (KITKAT) 이상

<br>

## Android 개발 흐름
- `AndroidManifast.xml` 네트워크 🔒 보안 예외설정
- `웹뷰 자바스크립트 허용` 처리
- 캐시 및 쿠키 설정
- `URI Intent` 처리

<br>

## Android 공통사항
App 내 웹뷰를 통해 결제창을 연동하는 경우, 웹 환경에서 결제창을 통한 💳 결제(승인)이 가능하도록 개발이 선행 되어야 합니다.  
이 후 appScheme 값을 설정 합니다.
카드사를 포함한 제휴사 인증 완료 후 전달된 가맹점 APP의 scheme을 확인하여 화면 focus가 이동 하게 됩니다.

<br>

### appScheme 설정- Server 승인 모델, Client 승인 모델

```html
<script src="https://pay.nicepay.co.kr/v1/js/"></script>
<script>
    function serverAuth() {
        AUTHNICE.requestPay({
            clientId: 'af0d116236df437f831483ee9c500bc4', // clientId에 따라 Server / Client 방식 분리
            appScheme: `nicepaysample://`,
            method: 'vbank',
            orderId: 'your-unique-orderid',
            amount: 1004,
            goodsName: '나이스페이-상품',
            returnUrl: 'http://localhost:4567/serverAuth'
        });
    }
</script>
```

### Android 권한 설정
- `AndroidManifast.xml` 파일에 권한 및 네트워크 🔒 보안 예외 설정을 합니다.

```bash
AndroidManifast.xml 
```

```xml
<uses-permission android:name="android.permission.INTERNET" />

<application
  android:allowBackup="true"
  android:icon="@mipmap/ic_launcher"
  android:label="@string/app_name"
  android:roundIcon="@mipmap/ic_launcher_round"
  android:supportsRtl="true"
  android:theme="@style/AppTheme"
  android:usesCleartextTraffic="true"/>
```

<br>

### Android 네트워크 보안정책 설정
- 네트워크 TLS 기본값 변경으로 인해 일반 텍스트 사용 시 설정 (`Android 9.0` 이상)


```bash
AndroidManifast.xml 
```

```xml
<uses-permission android:name="android.permission.INTERNET" />

<application
  android:allowBackup="true"
  android:icon="@mipmap/ic_launcher"
  android:label="@string/app_name"
  android:roundIcon="@mipmap/ic_launcher_round"
  android:supportsRtl="true"
  android:theme="@style/AppTheme"
  android:usesCleartextTraffic="true">
```

<br>

## Android-java 웹 뷰(web-view)개발 가이드

### Android-java 기본 설정 및 자바스크립트 허용
- 웹뷰 커스텀 클래스를 설정하고 자바스크립트 실행 가능하도록 `enabled` 설정 합니다.

```bash
Android-java
```

```java
//setup default
mWebView.setWebViewClient(new WebViewClientClass());

//javascript allow
mWebView.getSettings().setJavaScriptEnabled(true);
```

<br>

### Android-java 캐시 및 쿠키 설정

- 캐시 모드는 웹뷰 기본값으로 설정 합니다.
- 쿠키 허용 설정 (`Android 5.0` 이상 시 `third-party 쿠키 허용` 추가)


```bash
Android-java
```

```java
//setup cache
/*
 * WebView에서 캐시사용 관련 Default 설정은 WebSettings.LOAD_DEFAULT 입니다.
 * ex) mWebView.getSettings().setCacheMode(WebSettings.LOAD_DEFAULT);
 * 가급적 캐시 사용 설정을 변경하지 않을것을 권고 드립니다.
 * @중요 : 'WebSettings.LOAD_CACHE_ELSE_NETWORK' 로 변경금지.
 * @중요 : Do not change the setting to 'WebSettings.LOAD_CACHE_ELSE_NETWORK'
 */
 mWebView.getSettings().setCacheMode(WebSettings.LOAD_DEFAULT);

 //setup cookie
 if( android.os.Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP ) {    //Android 5.0 이상
    mWebView.getSettings().setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);
    CookieManager cookieManager = CookieManager.getInstance();
    cookieManager.setAcceptCookie(true);
    cookieManager.setAcceptThirdPartyCookies(mWebView, true);
  } else {
    CookieManager cookieManager = CookieManager.getInstance();
  }

```

<br>

> ##### ⚠️ 중요
> 캐시 모드를 `WebSetting.LOAD_CACHE_ELSE_NETWORK` 으로 설정 시 일부 카드사 세션 오류가 발생 합니다.

<br>

### Android-java 결제 페이지 호출
- 웹뷰의 `postUrl`을 통해 결제 요청 URL 호출 (가맹점 결제 요청 페이지)

```bash
Android-java
```

```bash
//load url
 mWebView.postUrl(MERCHANT_URL, null);
```

<br>

### Android-java URI 및 Intent 처리
- URI에 포함된 요청 데이터를 Intent를 통해 어플리케이션을 호출 합니다.(`startActivity`)


```bash
Android-java
```

```java
private class WebViewClientClass extends WebViewClient {
  @Override
  public boolean shouldOverrideUrlLoading(WebView view, String url) {
    Log.i(TAG, "url : " + url);
      try {
        if (url != null && (url.startsWith("intent:") ||
          url.contains("market://") ||
          url.contains("vguard") ||
          url.contains("droidxantivirus") ||
          url.contains("v3mobile") ||
          url.contains(".apk") ||
          url.contains("mvaccine") ||
          url.contains("smartwall://") ||
          url.contains("nidlogin://") ||
          url.contains("http://m.ahnlab.com/kr/site/download"))) {
            Intent intent = null;
                    
            try {
                intent = Intent.parseUri(url, Intent.URI_INTENT_SCHEME);
            } catch (URISyntaxException ex) {
                Log.e(TAG, "[error] Bad request uri format : [" + url + "] =" + ex.getMessage());
                return false;
            }
                    
            if (Build.VERSION.SDK_INT < Build.VERSION_CODES.R) {
                if (getPackageManager().resolveActivity(intent, 0) == null) {
                String pkgName = intent.getPackage();
                    if (pkgName != null) {
                      Uri uri = Uri.parse("market://search?q=pname:" + pkgName);
                      intent = new Intent(Intent.ACTION_VIEW, uri);
                      startActivity(intent);
                    }
                } else {
                  Uri uri = Uri.parse(intent.getDataString());
                  intent = new Intent(Intent.ACTION_VIEW, uri);
                  startActivity(intent);
                }
            } else {
                try {
                  startActivity(intent);
                } catch (ActivityNotFoundException e) {
                  Uri uri = Uri.parse("market://search?q=pname:" + intent.getPackage());
                  intent = new Intent(Intent.ACTION_VIEW, uri);
                  startActivity(intent);
                }
            } 
          } else {
            view.loadUrl(url);
          }
      } catch (Exception e) {
        e.printStackTrace();
        return false;
      }
        return true;
  }
}
```

<br>

> #### ⚠️ 중요
> Android 하위 버전으로 개발 시 카드사 보안, 백신 프로그램 어플 등은 `intent://` 방식이 아닌 scheme 호출 방식으로 처리 될 수 있습니다.  
> 해당 문제가 발생되는 경우 scheme을 수동으로 추가해야 합니다  
> Ex) `cloudpay://~` 로 들어올 경우 `if( url.startwith("cloudpay”) 추가)`


## Android-kotlin 웹 뷰(web-view)개발 가이드

### Android-kotlin 기본 설정 및 자바스크립트 허용
- 웹뷰 커스텀 클래스를 설정하고 자바스크립트 실행 가능하도록 `enabled` 설정 합니다.

```bash
Android-kotlin

```

```kotlin
class WebViewActivity : AppCompatActivity() {
    companion object {
        const val MERCHANT_URL = "https://web.nicepay.co.kr/demo/v3/mobileReq.jsp"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_webview)

        webview.webViewClient = WebViewClientClass()

        val settings = webview.settings
        settings.javaScriptEnabled = true
    }
}
```

<br>

### Android-kotlin 캐시 및 쿠키 설정

- 캐시 모드는 웹뷰 기본값으로 설정 합니다.
- 쿠키 허용 설정 (`Android 5.0` 이상 시 `third-party 쿠키 허용` 추가)

<br>

```bash
Android-kotlin

```

```kotlin
//setup cache
/*
* WebView에서 캐시사용 관련 Default 설정은 WebSettings.LOAD_DEFAULT 입니다.
* ex) settings.cacheMode = WebSettings.LOAD_DEFAULT
* 가급적 캐시 사용 설정을 변경하지 않을것을 권고 드립니다.
* @중요 : 'WebSettings.LOAD_CACHE_ELSE_NETWORK' 로 변경금지.
* @중요 : Do not change the setting to 'WebSettings.LOAD_CACHE_ELSE_NETWORK'
*/
settings.cacheMode = WebSettings.LOAD_DEFAULT

if( android.os.Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP ) {    //Android 5.0 이상
  settings.setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW)
  CookieManager.getInstance().setAcceptCookie(true)
  CookieManager.getInstance().setAcceptThirdPartyCookies(webview, true)
} else {
  CookieManager.getInstance().setAcceptCookie(true)
}
```

<br>

> #### ⚠️ 중요
> 캐시 모드를 `WebSetting.LOAD_CACHE_ELSE_NETWORK` 으로 설정 시 일부 카드사 세션 오류가 발생 합니다.

<br>

### Android-kotlin 결제 페이지 호출
- 웹뷰의 `postUrl`을 통해 결제 요청 URL 호출 (가맹점 결제 요청 페이지)

<br>

```bash
Android-kotlin
```

```kotlin
//load url
webview.postUrl(MERCHANT_URL, null)
```

<br>

### Android-kotlin URI 및 Intent 처리
- URI에 포함된 요청 데이터를 Intent를 통해 어플리케이션을 호출 합니다.(`startActivity`)

<br>

```bash
Android-kotlin
```

```kotlin
private class WebViewClientClass : WebViewClient() {
  override fun shouldOverrideUrlLoading(view: WebView?, url: String?): Boolean {
    println("url : " + url)

      try {
        if( url != null && (url.startsWith("intent:")
                           || url.contains("market://")
                           || url.contains("vguard")
                           || url.contains("droidxantivirus")
                           || url.contains("v3mobile")
                           || url.contains(".apk")
                           || url.contains("mvaccine")
                           || url.contains("smartwall://")
                           || url.contains("nidlogin://")
                           || url.contains("http://m.ahnlab.com/kr/site/download")) ) {

          var intent: Intent? = null

          try {
            intent = Intent.parseUri(url, Intent.URI_INTENT_SCHEME)
          } catch (e: URISyntaxException) {
            println("error : " + e.printStackTrace())
          }

          if( Build.VERSION.SDK_INT < Build.VERSION_CODES.R ) {
            if( view?.context?.packageManager?.resolveActivity(intent!!, 0) == null ) {
              val pkgName = intent?.`package`
                if( pkgName != null ) {
                  val uri = Uri.parse("market://search?q=pname:" + pkgName)
                  intent = Intent(Intent.ACTION_VIEW, uri)
                  view?.context?.startActivity(intent)
                }
            } else {
              val uri = Uri.parse(intent?.dataString)
              intent = Intent(Intent.ACTION_VIEW, uri)
              view?.context?.startActivity(intent)
            }
          } else {
            try {
              view?.context?.startActivity(intent)
            } catch (e: ActivityNotFoundException) {
              val pkgName = intent?.`package`
                if( pkgName != null ) {
                  val uri = Uri.parse("market://search?q=pname:" + pkgName)
                  intent = Intent(Intent.ACTION_VIEW, uri)
                  view?.context?.startActivity(intent)
                }
            }
          }
        } else {
          view?.loadUrl(url)
        }

        } catch (e: Exception) {
          println("error : " + e.printStackTrace())
          return false
        }
          return true
        }
}
```

<br>

> #### ⚠️ 중요
> Android 하위 버전으로 개발 시 카드사 보안, 백신 프로그램 어플 등은 `intent://` 방식이 아닌 scheme 호출 방식으로 처리 될 수 있습니다.  
> 해당 문제가 발생되는 경우 scheme을 수동으로 추가해야 합니다  
> Ex) `cloudpay://~` 로 들어올 경우 `if( url.startwith("cloudpay”) 추가)`


<br>

# 지원환경

나이스페이는 API를 활용하기 위해 HTTP 클라이언트는 `TLS 1.2` 대응이 가능해야 하며,  
모던한 개발환경 지원을 위해 다양한 옵션과 편의성을 제공 하고 있습니다.

- 다양한 개발언어 지원
- node.js, python, ruby, jsp, php, classic asp, .net
- REST API
- HTTP Status code
- JS SDK를 통한 결제창 승인방식 옵션 👉[JS SDK 바로가기](/api/payment.md#js-sdk)
- 원천사 응답코드 👉[API 응답코드 바로가기](/common/code.md#api-응답코드)
- HTTP 클라이언트 `TLS 1.2`
- [웹훅](/management/admin.md#기능설명-2)
- [웹 로그를 통한 디버깅](/management/admin.md#기능설명-3)
- 샌드박스를 활요한 TEST 및 리포팅 👉[개발정보 활용 바로가기](/management/admin.md#활용)

<br>

# 브라우저

나이스페이 결제창은 `HTML5` 기반 PC/Mobile 브라우저에서 활용이 가능하도록 개발 되었습니다.  
또한 가맹점의 결제창 연동시 활용되는 JS SDK가 브라우저를 판단하여 결제창을 노출 하기 때문에  
한번의 개발로 PC/Mobile 대응이 가능한 장점이 있습니다.

<br>

## PC 지원 브라우저

|            | Chrome |  Firefox  |  IE 9 이상  |  Opera  |  Whale  |  Edge  |  Safari  |
|:-----------|:------:|:---------:|:---------:|:-------:|:-------:|:------:|:--------:|
| Windows XP |   O    |     O     |     O     |    *    |    *    |   *    |    *     |
| Windows 7  |   O    |     O     |     O     |    O    |    O    |   *    |    *     |
| Windows 8  |   O    |     O     |     O     |    O    |    O    |   *    |    *     |
| Windows 10 |   O    |     O     |     O     |    O    |    O    |   O    |    *     |
| Windows 11 |   O    |     O     |     O     |    O    |    O    |   O    |    *     |
| Mac-OSX    |   O    |     O     |     *     |    O    |    O    |   O    |    O     |

&ast;OS가 지원하지 않음

<br>

## Mobile 지원 브라우저

| App      |  분류   |   앱 이름   |  지원여부  |
|:---------|:-----:|:--------:|:------:|
| naver    | 브라우저  |  naver   |   O    |
| daum     | 브라우저  |   daum   |   O    |
| google   | 브라우저  |  google  |   O    |
| telegram |  메신저  |   텔레그램   |   O    |
| naver    |  메신저  |    밴드    |   O    |
| naver    |  메신저  |   line   |   O    |
| kakao    |  메신저  |   카카오톡   |   O    |
| kakao    |  SNS  |  카카오스토리  |   O    |
| facebook |  SNS  |   페이스북   |   O    |

<br>

# 오류관리


## 시스템 오류의 대응
나이스페이 시스템 혹은 원천사 시스템의 문제에 의해 결제오류가 발견되는 사항으로,  
대부분 모니터링 시스템에 의해 오류 확인 즉시 대응 되며 가맹점이 별도 대응을 하지 않아도 무관합니다.  
대응 방식은 💡 결제창의 공지, 해당 결제수단의 노출 제한을 통한 다른 결제방식 유도, 가맹점 공지 등이 있습니다.

<br>

## 결제고객 오류
나이스페이 모니터링 팀은 시스템과 결제고객의 오류를 감지하고 대응하기 위해 ⏱️ 24/7 365일 운영이 가능한 관제시스템을 유지하고 있습니다.  
결제고객이 결제를 진행 하는 과정에서 발생 가능한 오류는 크게 시스템적인 오류(나이스페이의 시스템 혹은 원천사의 시스템)와  
사용자 환경 오류(기기, 브라우저, 결제수단의 제약)으로 나누어 분류 할 수 있습니다.

<br>

### 사용자 환경 오류의 대응
대부분 결제고객의 오류는 환경적인 요인에 의해 발생되며 각 인터페이스에서 대응이 가능한 오류코드와 메시지를 응답 하고 있습니다.  
상세한 대응은 [FAQ](https://start.nicepay.co.kr/homepage/fnq.do)를 통해 확인이 가능 합니다.

<br>

> #### 결제창 호출이 되지 않는 경우
> JS SDK Include가 정상인지 Include를 위한 도메인에 접근이 가능한 네크워크 환경 구성인지 체크가 필요하며,  
> 결제자의 브라우저에서 java-script 허용, 쿠키 허용으로 옵션이 적용되어 있는지 체크가 필요 합니다.

<br>

> #### 결제창 호출 후 버튼 동작이 정상적이지 않은 경우
> JS SDK을 iframe에서 호출되는 경우 문제가 발생할 수 있으며 [JS SDK 옵션](/api/payment.md#js-sdk)을 통해 문제를 검토 합니다.

<br>

> #### 결제창 호출 후 카드사 인증을 완료 했으나 결제(승인)이 발생되지 않은 경우
> 결제자가 결제창을 통해 원천사 접근 후 인증과정 진행 과정에서 문제가 발생된 경우로  
> 해당 결제수단의 원천사를 통한 지원이 필요한 경우가 있습니다.  
> 또한 Server승인 모델 결제창을 사용하는 경우 승인 API가 정상적으로 호출 되었는지 체크 해주세요.

<br>

> #### 결제(승인)은 완료 했으나 오류가 발생된 경우
> 결과 코드와 메시지를 통해 대부분 사유 확인이 가능하며 대응이 어려운 경우 거래 tid와 함께 1:1문의를 남겨주세요.

<br>

# 코드집

[HTTP-상태코드](#http-상태코드) | [카드코드](#카드코드) | [은행코드](#은행코드) | [API 응답코드](#API-응답코드) 

<br>

## HTTP 상태코드

| http status | 설명                                              |
|:-----------:|:------------------------------------------------|
|     200     | OK, 요청이 정상 처리된 경우                               |
|     401     | Unauthorized, SecretKey 또는 토큰 없거나 인증에 실패한 경우    |
|     403     | Forbidden,                                      |
|     404     | Not Found, 요청한 리소스가 존재하지 않는 경우                  |
|     405     | Method Not Allowed, URI에서 지원하지 않는 method로 요청한경우 |

<br>

## 카드코드

| 코드  | 한글           | 영문           | 결제창 | 대표 웹 사이트                         |
|:---:|:-------------|:-------------|:---:|:---------------------------------|
| 01  | 비씨           | BC           |  O  | https://www.bccard.com/          |
| 02  | KB국민         | KB Kookmin   |  O  | https://card.kbcard.com/         |
| 03  | 하나(외환)       | KEB Bank     |  O  | https://www.hanacard.co.kr/      |
| 04  | 삼성           | SAMSUNG      |  O  | https://www.samsungcard.com/     |
| 06  | 신한           | SHINHAN      |  O  | https://www.shinhancard.com/     |
| 07  | 현대           | HYUNDAI      |  O  | https://www.hyundaicard.com/     |
| 08  | 롯데           | LOTTE        |  O  | https://www.lottecard.co.kr/     |
| 11  | 씨티           | CITI         |  O  | https://www.citibank.co.kr/      |
| 12  | NH채움         | NH           |  O  | https://card.nonghyup.com/       |
| 13  | 수협           | SUHYUP       |  O  | https://www.suhyup-bank.com/     |
| 14  | 신협           | SHINHYUP     |  O  | http://www.cu.co.kr/             |
| 15  | 우리           | WOORI        |  O  | https://pc.wooricard.com/        |
| 16  | 하나           | HANA SK      |  O  | https://www.hanacard.co.kr/      |
| 21  | 광주           | KWANGJU      |  O  | https://pib.kjbank.com/          |
| 22  | 전북           | JEONBUK      |  O  | https://www.jbbank.co.kr/        |
| 23  | 제주           | JEJU         |  O  | http://tamna.jeju.go.kr/         |
| 24  | 산은캐피탈        | KDB Capital  |  O  | https://www.kdbc.co.kr/cardhome  |
| 25  | 해외비자         | VISA         |  O  | https://www.visakorea.com/       |
| 26  | 해외마스터        | MASTER       |  O  | https://www.mastercard.us/       |
| 27  | 해외다이너스       | DINERS       |  O  | https://www.dinersclub.com/      |
| 28  | 해외AMX        | AMEX         |  O  | https://www.americanexpress.com/ |
| 29  | 해외JCB        | JCB          |  O  | https://www.jcb.co.jp/           |
| 31  | SK-OKCashBag | SK-OKCashBag |     | https://www.okcashbag.com        |                                  
| 32  | 우체국          | Post         |  O  | https://www.epostbank.go.kr/     |
| 33  | 저축은행         | Savings Bank |  O  | http://sbcheck.bccard.com/       |
| 34  | 은련           | UnionPay     |  O  | https://www.unionpayintl.com/    |
| 35  | 새마을금고        | MG           |  O  | https://www.kfcc.co.kr/          |
| 36  | KDB산업        | KDB Bank     |  O  | https://www.kdb.co.kr/           |
| 37  | 카카오뱅크        | Kakao Bank   |  O  | https://www.kakaobank.com/       |
| 38  | 케이뱅크         | KBank        |     | https://www.kbanknow.com/        |                                  
| 39  | 페이코포인트       | PAYCO        |  O  | https://www.payco.com/           |
| 40  | 카카오머니        | KAKAO        |  O  | https://www.kakaopay.com/        |
| 41  | SSG머니        | SSG          |  O  | https://www.ssgpay.com/          |
| 42  | 네이버포인트       | NAVER        |  O  | https://www.naverfincorp.com/    |

<br>

## 은행코드
| 코드  |    한글     | 영문                                                               | 가상계좌발급 | 대표 웹 사이트                             |
|-----|:---------:|:-----------------------------------------------------------------|:------:|:-------------------------------------|
| 001 |   한국은행    | Bank of Korea                                                    |        | http://www.bok.or.kr/                |                                      
| 002 |   산업은행    | KDB Bank                                                         |        | https://www.kdb.co.kr/               |                                      
| 003 |   기업은행    | IBK                                                              |   O    | https://www.ibk.co.kr/               |
| 004 |   국민은행    | Kookmin Bank                                                     |   O    | https://www.kbstar.com/              |
| 005 |   외환은행    | Korea Exchange Bank                                              |   O    | https://www.kebhana.com/             |
| 007 |   수협중앙회   | Suhyup Federation                                                |        | https://www.suhyup.co.kr/            |
| 008 |   수출입은행   | The Export-Import Bank of Korea                                  |        | https://www.koreaexim.go.kr/         |
| 011 |   농협중앙회   | National Agricultural Cooperative Federation                     |   O    | https://www.nonghyup.com/            |
| 012 |  농협회원조합   | National Agricultural Cooperative Federation of Members          |        | https://www.nonghyup.com/            |
| 020 |   우리은행    | WooriBank                                                        |   O    | https://www.wooribank.com/           |
| 023 |   SC은행    | SCBank                                                           |   O    | https://www.standardchartered.co.kr/ |
| 026 |   서울은행    | Seoul Bank                                                       |        | https://www.kebhana.com/             |
| 027 |  한국씨티은행   | Korea city Bank                                                  |        | https://www.citibank.co.kr/          |                                      
| 031 |   대구은행    | Daegu Bank                                                       |   O    | https://www.dgb.co.kr/               |
| 032 |   부산은행    | Busan Bank                                                       |   O    | https://www.busanbank.co.kr/         |
| 034 |   광주은행    | KwangjuBank                                                      |   O    | https://pib.kjbank.com/              |
| 035 |   제주은행    | Jeju Bank                                                        |        | https://www.e-jejubank.com/          | 
| 037 |   전북은행    | JeonBuk Bank                                                     |        | https://www.jbbank.co.kr/            |                                      
| 039 |   경남은행    | Kyongnam Bank                                                    |        | https://www.knbank.co.kr/            |                                      
| 045 | 새마을금고연합회  | KFCC Federation                                                  |        | https://www.kfcc.co.kr/              |                                      
| 048 |   신협중앙회   | National Credit Union Federation of Korea                        |        | http://www.cu.co.kr/                 |                                      
| 050 |  상호저축은행   | Mutual Savings Bank                                              |        | https://www.fsb.or.kr/               |                                      
| 071 | 정보통신부 우체국 | Postal Savings for the Ministry of Information and Communication |   O    | https://www.epostbank.go.kr/         |
| 081 |   하나은행    | HanaBank                                                         |   O    | https://www.kebhana.com/             |
| 088 |   신한은행    | ShinhanBank                                                      |   O    | https://www.shinhan.com/             |
| 089 |   케이뱅크    | K Bank                                                           |   O    | https://www.kbanknow.com/            |
| 090 |   카카오뱅크   | Kakao Bank                                                       |        | https://www.kakaobank.com/           | 

<br>

## API 응답코드

|  코드  | 메시지                                                      |
|:----:|:---------------------------------------------------------|
| 3001 | 카드 결제 성공                                                 |
| 3011 | 카드번호 오류                                                  |
| 3012 | 카드가맹점 정보 미확인                                             |
| 3013 | 카드 가맹점 개시 안됨                                             |
| 3014 | 카드가맹점 정보 오류                                              |
| 3021 | 유효기간 오류                                                  |
| 3022 | 할부개월오류                                                   |
| 3023 | 할부개월 한도 초과                                               |
| 3031 | 무이자할부 카드 아님                                              |
| 3032 | 무이자할부 불가 개월수                                             |
| 3033 | 무이자할부 가맹점 아님                                             |
| 3034 | 무이자할부 구분 미설정                                             |
| 3041 | 금액 오류(1000원 미만 신용카드   승인 불가)                             |
| 3051 | 해외카드 미등록 가맹점                                             |
| 3052 | 통화코드 오류                                                  |
| 3053 | 확인 불가 해외카드                                               |
| 3054 | 환률전환오류                                                   |
| 3055 | 인증시 달러승인 불가                                              |
| 3056 | 국내카드 달러승인불가                                              |
| 3057 | 인증 불가카드                                                  |
| 3061 | 국민카드 인터넷안전결제 적용 가맹점                                      |
| 3062 | 신용카드 승인번호 오류                                             |
| 3071 | 매입요청 가맹점 아님                                              |
| 3072 | 매입요청 TID 정보 불일치                                          |
| 3073 | 기매입 거래                                                   |
| 3081 | 카드 잔액 값 오류                                               |
| 3091 | 제휴카드 사용불가 가맹점                                            |
| 3095 | 카드사 실패 응답                                                |
| 4000 | 계좌이체 결제 성공                                               |
| 4001 | 회원사 서비스 불가 은행                                            |
| 4002 | 출금일자 불일치                                                 |
| 4003 | 출금요청금액 불일치                                               |
| 4004 | 거래번호(TID) 불일치                                            |
| 4005 | 회신 정보 불일치                                                |
| 4006 | 계좌이체 승인번호 오류                                             |
| 4007 | 은행 시스템 서비스 중단                                            |
| 4100 | 가상계좌 발급 성공                                               |
| 4110 | 가상계좌 입금 성공                                               |
| 4120 | 가상계좌 과오납체크 등록 성공                                         |
| 4101 | 가상계좌 최대거래금액 초과                                           |
| 4102 | 가상계좌 입금예정일 오류                                            |
| 4103 | 가상계좌 입금예정시간 오류                                           |
| 4104 | 가상계좌 정보 오류                                               |
| 4105 | 가상계좌 벌크계좌 사용불가.(건별계좌   사용 가맹점)                           |
| 4106 | 가상계좌 벌크계좌 사용불가.(벌크계좌   사용 가맹점)                           |
| 4107 | 가상계좌 계좌번호 미입력 오류                                         |
| 4108 | 가상계좌 Pool 가맹점 미등록 오류                                     |
| 4109 | 해당 계좌는 입금대기상태(다른 계좌   사용요망)                              |
| 4111 | 가상계좌 Pool 가맹점 계좌형태 설정   오류                               |
| 4112 | 벌크계좌의 경우 장바구니 개수를 10개   이내로 제한                           |
| 4113 | 장바구니 상점주문번호(MOID) 포맷   오류 (MID(10)+YYMMDD(6)+일련번호(4))    |
| 4114 | 장바구니 상점주문번호(MOID) 포맷   오류 (YYMMDD(6)+일련번호(max_size 14))  |
| 4115 | 해당 계좌번호는 6개월 이내 재사용   금지                                 |
| 4116 | 가상계좌 계좌번호 채번시도 횟수초과   오류(잠시후 재시도 요망)                     |
| 4117 | 가상계좌 발급 실패                                               |
| 4118 | 계좌번호 사용중지 상태                                             |
| 4119 | 가상계좌 채번내역 미존재 오류                                         |
| 4121 | 가상계좌 과오납체크 등록 실패                                         |
| 4122 | 가상계좌 입금요청 금액 불일치 오류                                      |
| 4123 | 가상계좌 채번취소(환불) 상태이므로   입금처리 실패                            |
| 4124 | 가상계좌 입금내역 기처리 완료                                         |
| 4125 | 가상계좌 입금만료 제한   설정오류(기준정보)                                |
| 4126 | 가상계좌 CPID 설정 오류                                          |
| 4127 | 가상계좌 CPID 미설정 오류                                         |
| 4141 | 금액오류(1원 이하 이체불가)                                         |
| 4142 | 가상계좌 과오납체크 미사용 가맹점                                       |
| 4143 | 가상계좌 과오납체크 미등록 오류                                        |
| 4145 | 예금주명 수정이 불가능한 MID                                        |
| 7001 | 현금영수증 처리 성공                                              |
| 7002 | 현금영수증 종류오류                                               |
| 7003 | 현금영수증 중복발급                                               |
| 7004 | 현금영수증 취소오류                                               |
| 7005 | 현금영수증 부가가치세 오류                                           |
| 7006 | 현금영수증 최대개수 초과                                            |
| 7007 | 현금영수증 요청개수 입력 오류                                         |
| 7008 | 현금영수증 서브몰 발행 미등록 업체                                      |
| 7009 | 현금영수증 처리 지불수단이 아닙니다.                                     |
| 7010 | VAN응답실패                                                  |
| 7011 | 현금영수증 미발행 요청입니다.                                         |
| 7012 | 현금영수증 Identity 번호 오류                                     |
| 7013 | 현금영수증 요청구분 값   오류(1:소득공제, 2:지출증빙)                        |
| 7014 | 현금영수증 서브몰 사업자번호로 발행시   필수값 누락                            |
| 7015 | 현금영수증 취소시 원승인번호 또는   원거래일자 누락                            |
| 7041 | 금액오류(0원 이하 발행불가)                                         |
| 7042 | 현금영수증 최대금액 초과오류                                          |
| A000 | 휴대폰결제 처리 성공                                              |
| A001 | 휴대폰결제 처리 실패                                              |
| A002 | 필수입력값(거래키) 누락                                            |
| A003 | 필수입력값(이통사구분) 누락                                          |
| A004 | 필수입력값(SMS승인번호) 누락                                        |
| A005 | 필수입력값(업체TID) 누락                                          |
| A006 | 필수입력값(휴대폰번호) 누락                                          |
| A041 | 결제금액 오류                                                  |
| A564 | 휴대폰결제ID설정 오류                                             |
| A565 | 휴대폰결제ID미설정 오류                                            |
| A566 | 휴대폰결제사 설정 오류                                             |
| A567 | 상품구분코드 설정 오류                                             |
| A568 | 서비스구분코드 설정 오류                                            |
| 0000 | 결제성공                                                     |
| 2000 | DB오류                                                     |
| 2011 | CINO미존재                                                  |
| 2012 | 주문번호없음                                                   |
| 2032 | 가맹점주문번호길이이상                                              |
| 2151 | 거래정지 가맹점                                                 |
| 2152 | 미등록가맹점                                                   |
| 2154 | 제휴사상태미확인                                                 |
| 2156 | 중복등록된거래요청                                                |
| 2157 | 허용되지않는입력방식                                               |
| 2158 | 중복등록된입력방식                                                |
| 2159 | 해당은행장애                                                   |
| 2201 | 기승인존재                                                    |
| F100 | 빌키가 정상적으로 생성되었습니다.                                       |
| F101 | 빌링 정보가 정상적으로 삭제되었습니다.                                    |
| F102 | 인증서 검증 오류.                                               |
| F103 | PKCS7 전자서명 검증 실패.                                        |
| F104 | 인증정보 확인중 오류가 발생하였습니다.                                    |
| F105 | OCSP인증 중 오류가 발생하였습니다.                                    |
| F106 | DB 처리중 오류가 발생하였습니다.   (TB_TRANS_REQ)                     |
| F107 | DB 처리중 오류가 발생하였습니다.   (TB_TRANS)                         |
| F108 | DB 처리중 오류가 발생하였습니다.   (TB_TRANS_HISTORY)                 |
| F109 | DB 처리중 오류가 발생하였습니다.   (TB_BILL_MASTER)                   |
| F110 | 빌키발급 처리중 오류가   발생하였습니다.                                  |
| F111 | PKCS7 전자서명 메시지가 존재하지   않습니다.                             |
| F112 | 유효하지않은 카드번호를 입력하셨습니다.   (card_bin 없음)                    |
| F113 | 본인의 신용카드 확인중 오류가   발생하였습니다.                              |
| F114 | 인증서가 유효하지 않습니다.                                          |
| F115 | 빌키 발급 불가 가맹점입니다.(중지)                                     |
| F116 | 빌키 발급 불가 가맹점입니다.(해지)                                     |
| F117 | 빌링 미사용 가맹점입니다.                                           |
| F118 | 해당카드는 사용이 불가능 합니다.   타사카드를 이용해주세요.                       |
| F200 | 빌링 요청승인이 정상적으로   이루어졌습니다.                                |
| F201 | 이미 등록된 카드   입니다(빌키발급실패).                                 |
| C000 | 에스크로배송등록 성공                                              |
| C002 | 에스크로 가맹점 아님                                              |
| C003 | 에스크로 거래만 배송등록 가능                                         |
| C004 | 에스크로결제 신청내역 미존재                                          |
| C005 | 에스크로배송등록 불가상태                                            |
| C006 | 거래내역이 존재하지 않음.                                           |
| C007 | 취소된 거래는 배송등록 불가.                                         |
| D000 | 에스크로구매결정 성공                                              |
| D002 | 에스크로 가맹점 아님                                              |
| D003 | 에스크로 거래만 구매결정 가능                                         |
| D004 | 에스크로결제 신청내역 미존재                                          |
| D005 | 에스크로구매결정 불가상태                                            |
| D006 | 거래내역이 존재하지 않음.                                           |
| D007 | 고객고유번호 미입력.                                              |
| D008 | 거래요청내역이 존재하지 않음.                                         |
| D009 | 고객고유번호 검증 실패.                                            |
| D010 | 구매결정 이미 처리됨.                                             |
| D011 | 취소된 거래는 구매결정 불가.                                         |
| E000 | 에스크로구매거절 성공                                              |
| E002 | 에스크로 가맹점 아님                                              |
| E003 | 에스크로 거래만 구매거절 가능                                         |
| E004 | 에스크로결제 신청내역 미존재                                          |
| E005 | 에스크로구매거절 불가상태                                            |
| E006 | 거래내역이 존재하지 않음.                                           |
| E007 | 고객고유번호 미입력.                                              |
| E008 | 거래요청내역이 존재하지 않음.                                         |
| E009 | 고객고유번호 검증 실패.                                            |
| E010 | 구매거절 이미 처리됨.                                             |
| E011 | 취소된 거래는 구매거절 불가.                                         |
| 2001 | 취소   성공                                                  |
| 2211 | 환불   성공 (2001과 함께 취소 성공 처리할 것)                           |
| 2003 | 취소   실패                                                  |
| 2010 | 취소   요청금액 0원 이하                                          |
| 2011 | 취소   금액 불일치                                              |
| 2012 | 취소   해당거래 없음                                             |
| 2013 | 취소   완료 거래                                               |
| 2014 | 취소   불가능 거래                                              |
| 2015 | 기   취소 요청                                                |
| 2016 | 취소   기한 초과                                               |
| 2017 | 취소   불가 회원사                                              |
| 2018 | 신용카드 매입후 취소 불가능 가맹점                                      |
| 2019 | 타   회원사 거래 취소 불가                                         |
| 2021 | 매입전취소                                                    |
| 2022 | 매입후취소                                                    |
| 2023 | 취소   한도 초과                                               |
| 2024 | 취소패스워드 불일치                                               |
| 2025 | 취소패스워드 미 입력                                              |
| 2026 | 입금액보다 취소금액이 큽니다.                                         |
| 2027 | 에스크로 거래는 구매 또는 구매거절 시 취소가능.                              |
| 2028 | 부분취소 불가능 가맹점.                                            |
| 2029 | 부분취소 불가능 결제수단.                                           |
| 2030 | 해당결제수단 부분취소 불가.                                          |
| 2031 | 전체금액취소 불가.                                               |
| 2032 | 취소금액이 취소가능금액보다   큼.                                      |
| 2033 | 부분취소 불가능금액. 전체취소 이용바람.                                   |
| A101 | SIGN DATA 검증에   실패하였습니다.                                 |
| A102 | "타입이 맞지않는 파라미터명   명시" + 은(는) 알 수 없는 TYPE 입니다.            |
| A106 | 날짜 형식이 올바르지 않습니다.                                        |
| A107 | 입금예정일이 지났습니다.                                            |
| A108 | 입금예정일을 오늘 이전 날짜로 설정할   수 없습니다.                           |
| A109 | 요청한 MID의 설정 정보가 없습니다.                                    |
| A110 | 외부 연동결과 실패에 대한 코드(외부   에러메세지 그대로 전달)                     |
| A111 | 다날 휴대폰 통신 오류입니다.                                         |
| A112 | 비정상적인 경로로 접속되었습니다.                                       |
| A113 | 결제 금액이 최소 금액보다 적습니다.                                     |
| A114 | 상점 MID가 유효하지 않습니다.                                       |
| A115 | TID가 유효하지 않습니다.                                          |
| A116 | 요청 금액이 올바르지 않습니다.                                        |
| A117 | 필수입력항목이 누락되었습니다.                                         |
| A118 | 조회 결과데이터 없음                                              |
| A119 | 일반 무이자 이벤트 조회 결과 없음                                      |
| A120 | 부분 무이자 이벤트 조회 결과 없음                                      |
| A121 | 정의되지 않은 카드코드 입니다.                                        |
| A122 | 타 상점 거래 처리 불가(MID   불일치)                                 |
| A123 | 거래금액 불일치(인증된 금액과 승인요청   금액 불일치)                          |
| A124 | 해당 BID가 존재하지 않습니다.                                       |
| A125 | BID가 유효하지 않습니다.                                          |
| A126 | 이미 삭제된 빌키이거나 존재하지 않은   빌키입니다                             |
| A127 | 주문번호 중복 오류                                               |
| A128 | 키인 가맹점 아닙니다.                                             |
| A144 | 가맹점 결과 통보에 실패하였습니다.                                      |
| A145 | 외화 결제는 결제수단 지정하여 이용   가능 합니다.                            |
| A146 | 외화 결제 불가한 결제수단 입니다.                                      |
| A147 | 필드 길이가 초과되었습니다.                                          |
| A148 | 빌링 승인은 별도 API 이용   바랍니다.                                 |
| A149 | 빌링 승인만 가능한 API   입니다.(일반결제는 별도 API이용)                    |
| A150 | ARS 이용 가맹점이 아닙니다.                                        |
| A201 | PID 생성이 누락되었습니다.                                         |
| A202 | 결과코드 생성이 누락되었습니다.                                        |
| A203 | 결과메시지 생성이 누락되었습니다.                                       |
| A204 | 전문 복호화 오류가 발생하였습니다.                                      |
| A205 | 전문 암호화 오류가 발생하였습니다.                                      |
| A210 | 인증 요청내역이 존재하지 않습니다.                                      |
| A211 | 해쉬값 검증에 실패하였습니다.                                         |
| A212 | 잘못된 데이터 형식입니다.                                           |
| A213 | API 초기화 오류.                                              |
| A214 | 해당하는 카드거래가 없습니다.                                         |
| A215 | 해당하는 핸드폰거래가 없습니다.                                        |
| A216 | 해당하는 계좌이체거래가 없습니다.                                       |
| A217 | 해당하는 가상계좌거래가 없습니다.                                       |
| A218 | 해당하는 전자상품권거래가 없습니다.                                      |
| A219 | 환율정보 설정 오류 입니다.                                          |
| A220 | 설정된 환율 정보가 없습니다.                                         |
| A221 | 노티 수신정보 없음.                                              |
| A222 | 카드코드가 일치하지 않습니다.                                         |
| A223 | billKey 정보를 찾을 수   없습니다.                                 |
| A224 | 허용되지 않은 IP입니다.                                           |
| A225 | TID 중복 오류                                                |
| A226 | 전문통신 과정에서 오류가   발생하였습니다.                                 |
| A227 | 필드명 중복 발생                                                |
| A241 | VISA3D 인증을 이용할 수 없는   카드 입니다.                            |
| A242 | 정의되지 않은 지불수단 입니다.                                        |
| A243 | 주문정보가 존재하지 않습니다.                                         |
| A244 | 주문내역 갱신에 실패하였습니다.                                        |
| A245 | 인증 시간이 초과 되었습니다.                                         |
| A246 | 비정상 과다접속으로 인한 오류입니다.                                     |
| A247 | 정의되지 않은 통화코드 입니다.                                        |
| A248 | 사용할 수 없는 화폐 단위   입니다.(계약정보 확인필요)                         |
| A249 | 주문정보저장 실패(ORDER_DATA   최대 길이 초과)                         |
| A250 | 휴대폰번호 변조 오류(요청 번호와   인증완료 번호 상이)                         |
| A251 | 거래내역이 존재하지 않습니다.                                         |
| A252 | Signature 생성에   실패하였습니다.                                 |
| A253 | 빌키(BID) 생성에 실패하였습니다.                                     |
| A254 | 제휴사 응답전문이 유효하지 않습니다.                                     |
| A255 | 타 상점 빌키(BID) 삭제 불가.                                      |
| A256 | ARS인증번호생성실패. 잠시후 재시도   바랍니다.                             |
| A257 | 주문정보 저장에 실패하였습니다.                                        |
| A258 | SMS 발송에 실패하였습니다.                                         |
| A299 | API 지연처리 발생.                                             |
| A300 | 기준정보 조회오류.                                               |
| A301 | 가맹점키 조회 오류입니다.                                           |
| A302 | 기준정보상 필수 설정 정보가 없습니다.                                    |
| A303 | 기준정보 CPID 설정 정보가   없습니다.                                 |
| A304 | DB테이블 INSERT 오류발생.                                       |
| A305 | 가맹점번호 기준정보 미설정 오류.                                       |
| A306 | DB테이블 UPDATE 실패.                                         |
| A307 | 기준정보 조회 결과 2행 이상 오류                                      |
| A400 | 대외기관 전문생성에 실패하였습니다.                                      |
| A401 | 대외계 전문통신 과정에서 오류가   발생하였습니다.                             |
| A402 | DB트랜잭션 처리에 실패하였습니다.                                      |
| A403 | 대외기관 응답 전문이 올바르지   않습니다.                                 |
| 9000 | "누락된 필드명" +   필드값이 누락되었습니다.                              |
| 9001 | 필드 길이가 잘못되었습니다.                                          |
| 9002 | Try-Catch-Exception:"Exception   내용"                     |
| S999 | 기타오류가 발생하였습니다.                                           |
| S001 | 요청템플릿이 존재하지 않습니다.                                        |
| S002 | 응답템플릿이 존재하지 않습니다.                                        |
| T001 | 수신메시지 인코딩 중 예외가   발생하였습니다.                               |
| T002 | 비정상적인 수신 전문입니다.                                          |
| T003 | 수신데이터 파싱 중 예외가   발생하였습니다.                                |
| T004 | 요청 전문의 헤더부 생성 중 오류가   발생하였습니다.                           |
| T005 | 요청 전문의 바디부 생성 중 오류가   발생하였습니다.                           |
| X001 | 서버 도메인명이 잘못 설정되었습니다.                                     |
| X002 | 서버로 소켓 연결 중 오류가   발생하였습니다.                               |
| X003 | 전문 수신 중 오류가 발생하였습니다.                                     |
| X004 | 전문 송신 중 오류가 발생하였습니다.                                     |
| V005 | 지원하지 않는 지불수단입니다.                                         |
| V101 | 암호화 플래그 미설정 오류입니다.                                       |
| V102 | 서비스모드를 설정하지 않았습니다.                                       |
| V103 | 지불수단을 설정하지 않았습니다.                                        |
| V104 | 상품개수 미설정 오류입니다.                                          |
| V201 | 상점ID 미설정 오류입니다.                                          |
| V202 | LicenseKey 미설정 오류입니다.                                    |
| V203 | 통화구분 미설정 오류입니다.                                          |
| V204 | MID 미설정 오류입니다.                                           |
| V205 | MallIP 미설정 오류입니다.                                        |
| V301 | 구매자이름 미설정 오류입니다.                                         |
| V302 | 구매자인증번호 미설정 오류입니다.                                       |
| V303 | 구매자연락처 미설정 오류입니다.                                        |
| V304 | 구매자메일주소 미설정 오류입니다.                                       |
| V401 | 상품명 미설정 오류입니다.                                           |
| V402 | 상품금액 미설정 오류입니다.                                          |
| V501 | 카드형태 미설정 오류입니다.                                          |
| V502 | 카드구분 미설정 오류입니다.                                          |
| V503 | 카드코드 미설정 오류입니다.                                          |
| V504 | 카드번호 미설정 오류입니다.                                          |
| V505 | 카드무이자여부 미설정 오류입니다.                                       |
| V506 | 카드인증구분 미설정 오류입니다.                                        |
| V507 | 카드형태 설정 오류입니다.                                           |
| V508 | 카드형태 허용하지 않는 값을   설정하였습니다.                               |
| V509 | 카드구분 허용하지 않는 값을   설정하였습니다.                               |
| V510 | 유효기간 미설정 오류입니다.                                          |
| V511 | 유효기간 허용하지 않는 값을   설정하였습니다.                               |
| V512 | 유효기간의 월 형태가 잘못   설정되었습니다.                                |
| V513 | 카드 비밀번호 미입력 오류입니다.                                       |
| V601 | 은행코드 미설정 오류입니다.                                          |
| V602 | 금융결제원 암호화 데이터 미설정   오류입니다.                               |
| V701 | 가상계좌입금만료일 미설정 오류입니다.                                     |
| VA01 | 거래KEY 미설정 오류입니다.                                         |
| VA02 | 이통사구분 미설정 오류입니다.                                         |
| VA03 | SMS승인번호 미설정 오류입니다.                                       |
| VA04 | 업체TID 미설정 오류입니다.                                         |
| VA05 | 휴대폰번호 미설정 오류입니다.                                         |
| VA09 | 고객고유번호(주민번호,사업자번호)   미설정 오류입니다.                          |
| VA10 | ENCODE 업체TID 미설정   오류입니다.                                |
| VB02 | 이통사구분 미설정 오류입니다.                                         |
| VB05 | 휴대폰번호 미설정 오류입니다.                                         |
| VB09 | 고객고유번호(주민번호,사업자번호)   미설정 오류입니다.                          |
| VB10 | 고객 IP 미설정 오류입니다.                                         |
| V801 | 취소금액 미설정 오류입니다.                                          |
| V802 | 취소사유 미설정 오류입니다.                                          |
| V803 | 취소패스워드 미설정 오류입니다.                                        |

<br>
