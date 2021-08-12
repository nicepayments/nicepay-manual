# API·JS SDK	

## URI 목록	
제공되는 API의 URI 목록 입니다. 빠른 검토를 위해 인터페이스 확인이 필요한 경우 목록의 링크를 클릭해주세요.

```bash
Authorization : Basic or Bearer
Content-Type : application/json
```

|              API            |     Method    |               Endpoint              |
|:---------------------------:|:-------------:|:-----------------------------------|
|       AccessToken 발급      |      POST     |     /v1/access-token                |
|      승인 요청(인증거래)    |      POST     |     /v1/payments/{tid}              |
|           취소 요청         |      POST     |     /v1/payments/{tid}/cancel       |
|         거래조회-tid        |       GET     |     /v1/payments/{tid}              |
|       거래조회-orderId      |       GET     |     /v1/payments/find/{orderId}     |
|           빌키발급          |      POST     |     /v1/subscribe/regist            |
|           빌키승인          |      POST     |     /v1/subscribe/{bid}/payments    |
|           빌키삭제          |      POST     |     /v1/subscribe/{bid}/expire      |
|           약관조회          |       GET     |     /v1/terms                       |
|         N정통Epay승인       |      POST     |     /v1/epay                        |
|        현금영수증 발급      |      POST     |     /v1/receipt/                    |
|        현금영수증 취소      |      POST     |     /v1/receipt/{tid}/cancel        |
|      현금영수증 거래조회    |       GET     |     /v1/receipt/{tid}               |
|       카드 이벤트 조회      |       GET     |     /v1/card/event                  |
|     카드 무이자정보 조회    |       GET     |     /v1/card/interest-free          |
|         승인금액검증        |      POST     |     /v1/check-amount/{tid}          |


## JS SDK 목록	
JS SDK는 결제창을 호출하는 경우 활용 됩니다.   
JS SDK호출은 [클라이언트 키](/common/api.md#클라이언트-키)의 인증을 통해 호출 되며 결제창이 호출되고 결제(승인)되는 모델에 따라 각각 다른 JS SDK를 제공하고 있습니다.  
[클라이언트 키](/common/api.md#클라이언트-키) 는 로그인 후 개발정보에서 확인이 가능 합니다.  

### JS SDK 목록
|모델|설명|
|:---:|:--|
|Server 승인| Endpoint: https://pay.nicepay.co.kr/v1/js/ <br>결제창 호출(인증)과 결제(승인) API호출이 독립적으로 분리된 모델 |
|Client 승인|Endpont: https://pay.nicepay.co.kr/v1/js/pay/  <br>결제창 호출(인증)후 결제(승인)이 자동으로 처리되는 모델 |

### API· JS SDK 인증  
- [JS SDK 인증](/common/api.md#js-sdk-인증)    

### JS SDK 정보  
- [JS SDK(client / server 승인)](/api/payment.md#js-sdk)
  
>  사용될 JS SDK 모델에 따라 필요한 클라이언트 키 타입이 상이 합니다.  
> [키 발급 방법](../management/admin.md#기능설명)을 확인하고 알맞은 클라이언트 키를 통해 결제창을 호출 해 주세요.  

## API KEY

### KEY 발급·변경  
처음 상점이 생성되면 [결제창 호출](/common/api.md#js-sdk-목록-1)을 위한 [Client key](/common/api.md#클라이언트-키)와 API 호출을 위한 [Secret key](/common/api.md#시크릿-키)가 생성되고 로그인 후 [개발정보](/management/admin.md#활용) 탭으로 이동하면 확인이 가능 합니다.  
만약의 경우 [Secret key](/common/api.md#시크릿-키)가 외부에 노출되어 보안상 문제가 발생하는 경우 [개발정보](/management/admin.md#활용) 페이지에 접근하여 키를 변경/삭제 할 수 있습니다.  
  
#### 결제창 JS SDK 목록  
- [JS SDK 목록](/common/api.md#js-sdk-목록)    

#### 개발정보
- [개발정보 활용](/management/admin.md#활용)    

#### Key 정보  
- [Client key](/common/api.md#클라이언트-키)
- [Secret key](/common/api.md#시크릿-키)
- [KEY정보-기능설명](/management/admin.md#기능설명)
- [KEY정보-재발급](/management/admin.md#재발급)  

### 클라이언트 키  
클라이언트 키는 생성된 상점의 [개발정보](/management/admin.md#활용) 탭에서 확인이 가능 합니다.  
생성된 클라이언트 키는 결제창을 호출 하거나 API인증을 위한 KEY값을 생성할 때 활용 됩니다.   

#### 클라이언트 키 Type  
결제창 호출 방식에 따라 클라이언트 키는 2가지 Type중 선택하여 발급이 가능 합니다.  
- Server 인증 : 결제창 요청(인증)과 결제(승인) API호출이 분리된 모델  
- Client 인증  : 결제창 요청(인증)후 결제(승인)이 자동으로 처리되는 모델  

#### 결제창 JS SDK 모델과 클라이언트 키  
- [JS SDK 목록](/common/api.md#js-sdk-목록)    

#### API-JS SDK 인증  
- [JS SDK 인증](/common/api.md#js-sdk-인증)
- [Basic auth](/common/api.md#basic-auth)
- [Bearer token](/common/api.md#bearer-token)


### 시크릿 키  
시크릿 키는 생성된 상점의 [개발정보](/management/admin.md#활용)탭에서 확인이 가능 합니다.  
생성된 시크릿 키는  API인증 키 생성에 활용 되며 API인증 방식에 따라 시크릿키 발급이 가능 합니다.    

#### API 인증방식
- [Basic auth](/common/api.md#basic-auth)
- [Bearer token](/common/api.md#bearer-token)  

#### Key 정보  
- [KEY정보-기능설명](/management/admin.md#기능설명)  
- [KEY정보-재발급](/management/admin.md#재발급)  


## API·JS SDK인증	

### JS SDK 인증  
JS SDK를 통해 결제창 Method 호출시 clientId 필드에 [클라이언트 키](/common/api.md#클라이언트-키)값을 셋팅 하면 준비가 완료 됩니다.  
JS SDK 모델에 따라 호출되는 JS SDK Include 방식과 Method 차이가 있습니다. 관련 부분은 하단 소스코드를 참조 해주세요.  

### JS SDK 인증-Server 승인 모델  
```Javascript  
<script src="https://pay.nicepay.co.kr/v1/js/"></script> //Server 승인 
<script>
function serverAuth() {
  AUTHNICE.requestPay({
    clientId: ‘af0d116236df437f831483ee9c500bc4’,
    method: ‘vbank’,
    orderId: ‘your-unique-orderid’,
    amount: 1004,
    goodsName: ‘나이스페이-상품’,
    vbankHolder: ‘나이스’,
    returnUrl: ‘http://localhost:4567/serverAuth’
  });
}
</script>
```

### JS SDK 인증-Client 승인 모델  
```Javascript  
<script src="https://pay.nicepay.co.kr/v1/js/pay/"></script> //Client 승인 
<script>
function serverAuth() {
  PAYNICE.requestPay({
    clientId: ‘af0d116236df437f831483ee9c500bc4’,
    method: ‘vbank’,
    orderId: ‘your-unique-orderid’,
    amount: 1004,
    goodsName: ‘나이스페이-상품’,
    vbankHolder: ‘나이스’
    returnUrl: ‘http://localhost:4567/serverAuth’
 });
}
</script>
```

> Client 승인 모델을 사용하는 경우 모든 결제(승인)건 별 금액 검증이 필요 합니다.  
> 또한 사용자 네트워크 환경에 따라 인터페이스 응답의 유실이 발생 할 수 있어 [승인금액 검증 API](/api/payment.md#승인-금액-검증)를 활용하여 금액체크를 반드시 해야 합니다.    


### Basic auth  
API 엑세스 제어를 위해 "Basic" 인증 방식을 이용하는 방식 입니다. HTTP Authorization header에 Basic 인증 스킴으로 약속된 credentials 전달하면 API 엑세스 인증이 완료 됩니다.  
API 엑세스 방식은 생성된 시크릿키 인증방식에 따라 선택이 가능 합니다.  
- [시크릿 키](/common/api.md#시크릿-키)  

#### HTTP header Basic 인증 스킴  
```bash
Authorization: Basic <credentials>
```
  
#### Credentials 생성 알고리즘  
```bash
Base64(client-key:secret-key)
```
  
#### Credentials 생성 예시  
Credentials 생성을 위해 먼저 클라이언트 키 + : + 시크릿키 구성으로 문자열을 생성 합니다.  
```bash
clientKey = ‘af0d116236df437f831483ee9c500bc4’
secretKey = ‘433a8421be754b34989048cf148a5ffc’
-> af0d116236df437f831483ee9c500bc4:433a8421be754b34989048cf148a5ffc
```
  
 생성된 문자열을 Base64 encode 하면 Credentials 값이 생성됩니다.
 ```bash
 Base64(‘af0d116236df437f831483ee9c500bc4:433a8421be754b34989048cf148a5ffc’)
-> YWYwZDExNjIzNmRmNDM3ZjgzMTQ4M2VlOWM1MDBiYzQ6NDMzYTg0MjFiZTc1NGIzNDk4OTA0OGNmMTQ4YTVmZmM= 
```  
생성된 Credentials를 HTTP header에 셋팅 하면 API 인증 준비가 완료 됩니다.   
```bash
Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMTQ4M2VlOWM1MDBiYzQ6NDMzYTg0MjFiZTc1NGIzNDk4OTA0OGNmMTQ4YTVmZmM= 
 ```
### Bearer token  
API 엑세스 제어를 위해  OAuth기반 "Bearer" 인증 스킴을 이용하는 방식 입니다.  
API 접속을 위해 access token을 API 서버에 제출해서 인증을 하게 되며, Bearer token 인증을 위해 사용되는 token 발급을 위해 [Access token](/api/payment.md#access-token) API 호출이 선행 되어야 합니다.  
API 엑세스 방식은 생성된 시크릿키 인증방식에 따라 선택이 가능 합니다.  

[시크릿 키](/common/api.md#시크릿-키)  

#### HTTP header Bearer 인증 스킴  
```bash
Authorization: Bearer <token>
```
#### Access Token 생성 API  
- [Access token](/api/payment.md#access-token)  


#### Bearer Token 생성 예시  
Bearer token 생성을 위해 Access token API 호출 합니다.  
API호출을 위해 Basic 인증 스킴이 활용되며, Credentials 생성 방법은 [Basic auth 가이드](/common/api.md#basic-auth)를 참고 해주세요.  

```cURL
curl -X POST "https://api.nicepay.co.kr/v1/access-token" 
-H "Content-Type: application/json" 
-H "Authorization: Basic YWYwZDExNjIzNmRm..."
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
Access token API 응답 값 중 accessToken값을 Bearer token 값으로 셋팅하면 API 호출 준비가 완료 됩니다.  
```bash
Authorization: Bearer 6d0a7caa1b7358c8aa06ef3706e01bb1feb2c65dacc7147b258dfdd6191b5279
```
>발급된 토큰은 30분간 유효하며 발급된 토큰의 갱신은 지원하지 않습니다.  
>토큰 만료시간 이후 요청 건에 대해 새로운 토큰이 발급되어 응답됩니다.  
>기 발급된 토큰의 유효시간 이내 토큰 재발급 요청이 있는 경우 기존 토큰이 전달되며 유효시간은 기 발급 토큰과 동일합니다.  
