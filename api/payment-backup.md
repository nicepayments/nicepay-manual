# 결제·발급	
[Access token](/api/payment-backup.md#access-token) | [결제창](/api/payment-backup.md#결제창) | [빌링](/api/payment-backup.md#빌링) | [EPAY](/api/payment-backup.md#epay) | [현금영수증](/api/payment-backup.md#현금영수증-1) | [더 알아보기](/api/payment-backup.md#더-알아보기)
<br>

## Access token

### Over-view
![image](https://user-images.githubusercontent.com/86043374/128323199-0e94d6b6-3f05-4c52-8675-d020c2b36728.png)  

#### 활용
- [Bearer token](/common/api.md#bearer-token)방식 authorization을 활용하여 API를 호출하는 경우 활용 합니다.
-모든 요청 건에 대해 token 생성 후 API를 호출 하는 것을 권장하고 있습니다.

> [시크릿 키](/common/api.md#시크릿-키)를 [Basic auth](/common/api.md#basic-auth) 방식으로 생성한 경우 API 호출시 token 관리는 생략 할 수 있습니다.

### 샘플 코드
```bash
curl -X POST "https://api.nicepay.co.kr/v1/access-token" 
-H "Content-Type: application/json" 
-H "Authorization: Basic YWYwZDExNjIzNmRm..."
```
### 요청 명세
```bash
POST /v1/access-token HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```

#### Body
|   Parameter  | type        |    필수    | byte |                             설명                           |
|:------------:|:-----------:|:----------:|:----:|:-----------------------------------------------------------| 
| returnCharSet|  String     |            |   10 | 응답 파라메터 인코딩 방식<br> 값: utf-8/euc-kr <br> Default:utf-7  |

### 응답 명세
```bash
POST
Content-type: application/json
```

#### Body
|   Parameter  | type        |    필수    | byte |                             설명                           |
|:------------:|:-----------:|:----------:|:----:|:-----------------------------------------------------------| 
| resultCode  |  String     |     O      |   4  | 결과코드<br>0000: 성공/그외 실패  |
| resultMsg   |  String     |     O      |   100 | 결과 메시지 |
| accessToken |  String     |     O      |   40  | access token  |
| tokenType   |  String     |     O      |   10  | 인증 스킴 유형<br> Bearer 고정  |
| expiredAt   |  String     |     O      |       | Token 만료 시각<br>ISO 8601 형식  |
| now         |  String     |     O      |       | 현재 시각<br> ISO 8601 형식  |


## 결제창 

### JS SDK

#### Over-view
JS SDK는 2가지 모델로(Server, Client 승인) 제공되며 모델에 따라 호출 방식과 연동 흐름의 차이가 발생합니다.  
아래 문서를 참조하여 결제창 모델을 선택 후 결제흐름을 확인 해주세요. 

##### 결제창 JS SDK 목록
- [JS SDK 목록](/common/api.md#js-sdk-목록)

##### API · JS SDK 인증
- [JS SDK 인증](/common/api.md#apijs-sdk인증)

##### 결제창 (Server 승인 모델)
![image](https://user-images.githubusercontent.com/86043374/128439952-6af2dea8-5bb1-4d98-89c4-afc1889eacd8.png)  

###### 설명
- 결제자가 브라우저에서 pay.nicepay.co.kr/v1/js/ JS SDK의 `AUTHNICE.requestPay()` method 호출시 결제창이 노출 됩니다.  
- 결제자는 결제창을 통해 카드사 및 결제 원천사에 접근하여 인증과정을 진행 하고 나이스페이는 인증결과를 `AUTHNICE.requestPay()`의 object value로 전달된 returnUrl로 POST 합니다.  
- 가맹점은 POST 데이터의 금액 및 위변조 여부를 체크하고 응답된 tid을 승인 API로 전달 하면 💳 결제(승인)요청 처리가 완료 됩니다. 

###### 예외처리
- `returnUrl`로 인증응답이 될때 금액, 위변조검증 `signature`, 주문번호가 응답되며 반드시 생성한 결제정보와 일치하는지 체크 후 💳 승인(결제) API를 호출 해주세요.

> [클라이언트 키](/common/api.md#클라이언트-키)가 Server 승인 방식으로 발급 된 경우 Server승인 모델 결제창 사용이 가능 합니다.  
> [시크릿 키](/common/api.md#시크릿-키) 생성이 [Bearer token](/common/api.md#bearer-token) 방식인 경우 💳 결제(승인)API 호출전 token 생성과정이 추가 됩니다.

##### 결제창 (Client 승인 모델)
![image](https://user-images.githubusercontent.com/86043374/128440339-b3366fd0-a8ca-46a5-8b42-d102d8c22123.png)  

###### 설명
- 결제자가 브라우저에서 pay.nicepay.co.kr/v1/js/pay/ JS SDK의 `PAYNICE.requestPay()` method 호출시 💡 결제창이 노출 됩니다.
- 결제자는 💡 결제창을 통해 카드사 및 결제 원천사에 접근하여 인증과정을 진행 하고 나이스페이는 인증 및 💳 결제(승인) 처리 후 결과를 `PAYNICE.requestPay()`의 object value로 전달된 `returnUrl`로 POST 합니다.

###### 예외처리
- `Http client`의 구성 없이 Client JS SDK 요청으로 💳 결제(승인)이 처리되는 단순화된 모델입니다.
- client-side에서 금액이 변조된 경우 변조된 금액으로 💳 결제(승인)이 발생 할 수 있습니다. 
- 반드시 응답전문의 금액, 주문번호, 위변조검증 `signature`를 체크 해주세요. 
- 금액검증은 [승인 금액 검증 API](/api/payment.md#승인-금액-검증) 를 활용하면 체크가 편리 합니다.

> [클라이언트 키](/common/api.md#클라이언트-키)가 Client 승인 방식으로 발급 된 경우 Client승인 모델 💡 결제창 사용이 가능 합니다.  
> 대량 결제 트레픽이 예상되는 경우 Server승인 모델을 사용 해주세요.  
> 금액 변조 검증 미처리로 인한 모든 책임은 가맹점에 있습니다.  

#### 샘플 코드
JS SDK를 통해 결제창 Method 호출시 `clientId` 필드에 [클라이언트 키](/common/api.md#클라이언트-키) 값을 셋팅 하면 준비가 완료 됩니다.  
JS SDK 모델에 따라 호출되는 JS SDK Include 방식과 Method 차이가 있습니다. 관련 부분은 하단 소스코드를 참조 해주세요.

##### JS SDK 인증-Server 승인 모델
```Javascript
<script src="https://pay.nicepay.co.kr/v1/js/"></script> //Server 승인 
<script>
function serverAuth() {
  AUTHNICE.requestPay({
    clientId: ‘af0d116236df437f831483ee9c500bc4’,
    method: ‘card’,
    orderId: ‘your-unique-orderid’,
    amount: 1004,
    goodsName: ‘나이스페이-상품’,
    returnUrl: ‘http://localhost:4567/serverAuth’
 });
}
</script>

```

##### JS SDK 인증-Client 승인 모델
```javascript
<script src="https://pay.nicepay.co.kr/v1/js/pay/"></script> //Client 승인 
<script>
function serverAuth() {
  PAYNICE.requestPay({
    clientId: ‘af0d116236df437f831483ee9c500bc4’,
    method: ‘card’,
    orderId: ‘your-unique-orderid’,
    amount: 1004,
    goodsName: ‘나이스페이-상품’,
    returnUrl: ‘http://localhost:4567/serverAuth’
 });
}
</script>

```

> Client 승인 모델을 사용하는 경우 모든 💳 결제(승인)건 별 금액 검증이 필요 합니다.  
> 또한 사용자 네트워크 환경에 따라 인터페이스 응답의 유실이 발생 할 수 있어 [승인금액 검증 API](/api/payment.md#승인-금액-검증)를 활용하여 금액체크를 반드시 해야 합니다.  

#### 요청 명세

##### 공통
- [JS SDK 샘플코드](/api/payment.md#샘플-코드-1)참조하여 필요한 파라미터 추가하면 결제창에 반영 됩니다. 

|   Parameter  | type        |    필수  | byte |                             설명                           |
|:------------:|:-----------:|:--------:|:----:|:-----------------------------------------------------------| 
| ClientId      | String     | O        | 50	 |  가맹점 식별코드, NICEPAY가 발급한 가맹점 식별 값 		| 
| ClientId      | String     | O        | 20	 | 결제수단 <br> card : 신용카드 <br> directCard : 결제창 없이 카드사 바로 노출  <br> vbank : 가상계좌  <br>naverpayCard : 네이버페이-신용카드 전액결제(포인트 이용불가) <br> kakaopay : 카카오페이(카드전액 또는 포인트전액) <br>kakaopayCard : 카카오페이-신용카드 전액결제 <br>kakaopayMoney : 카카오페이-머니 전액결제 <br>samsungpayCard : 삼성페이 카드전액 결제 <br>payco : 페이코 <br>ssgpay : SSGPAY <br>cardAndEasyPay : 신용카드와 간편결제 노출 <br>*cardAndEasyPay인 경우, 아래 파라미터와 함께 사용불가* <br>- cardCode, cardQuota, shopInterest, quotaInterest | 
| orderId      | String     | O         | 64	 |  가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br> 결제된 orderId로 재호출 불가| 
| amount       | Int  	    | O         | 12	 |  결제금액 (숫자만)		| 
| goodsName    | String     | O         | 40	 |  상품명<br> - doubleQuota(")와 pipLine(&brvbar;) 2가지 특수문자는 '-'로 대체 됩니다.| 
| returnUrl    | String     | O         | 500	 |  인증 처리 후 redirect 되는 url 		| 
| mallReserved | String     |           | 500	 |  상점 정보 전상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가| 
| mallUserId   | String     |           | 20	 |  상점에서 관리하는 사용자 아이디 		| 
| buyerName    | String     |           | 30	 |  구매자 이름 		| 
| buyerTel     | String     |           | 40	 |  구매자 전화번호<br> (-) 없이 숫자만 입력 		| 
| buyerEmail   | String     |           | 60	 |  구매자 이메일 		| 
| useEscrow    | Boolean    |           | -	 | true: 에스크로 거래 / false: 일반거래(default) 		| 
| currency     | String     |           | 3	 |  KRW:원화, USD:미화달러, CNY:위안화 		| 
| logoImgUrl   | String     |           | 100	 |  로고 이미지의 full URL 전달<br>  ex) https://youre.site.com/image/logo.jpg<br> *채널별 사이즈 (단위 : pixel)*<br>모바일 : width 50 X height 50<br> 웹표준 : width 94 X height 25| 
| language     | String     |           | 2	 |EN : 영문 / CN : 중문 / KO : 국문(Default)<br>NICEPAY 결제창 내 다국어를 지원<br>*sample)*<br>lang=EN -> 결제창 영문표기<br>lang=CN -> 결제창 중문표기| 
| returnCharSet| String     |           | 10	 |  가맹점 서버의 encoding 방식 전달<br> - utf-8(Default) / euc-kr		| 
| skinType     | String     |           | 10	 |  결제창 스킨 설정<br>지원 옵션 red/green/purple/gray/dark| 

##### 부가세 지정금액

|   Parameter  | type        |    필수  | byte |                             설명                           |
|:------------:|:-----------:|:--------:|:----:|:-----------------------------------------------------------| 
| taxFreeAmt      | Int     |        | 12	 | 전체 거래금액(amount)중에서 면세에 해당하는 금액을 설정합니다.| 

##### 신용카드 & 간편결제
|   Parameter  | type        |     필수     | byte |                             설명                           |
|:------------:|:-----------:|:------------:|:----:|:-----------------------------------------------------------| 
| cardQuata      | String     |            | 100	 |할부개월 설정<br><br>[공통]<br>선택할 수 있는 할부기간을 제한한다.<br><br>[카드일반+PAYCO+네이버페이]<br>- 단독 설정 가능<br>- ','를 구분자로 할부개월 나열<br>- 일시불은 반드시 "00"으로 설정할것<br>- 2자리의 할부기간 설정 (3개월일 경우 반드시 '03' 으로 설정)<br>Ex) cardQuota=03 <br>- 설명 : 3 개월 할부만 가능하도록 함.<br>최소금액 : 50,000원 이상<br><br>[카카오페이, 삼성페이, SSGPAY]<br> - 단독 설정 사용불가. 반드시 cardCode와 함께 설정되어야 사용가능.<br> - 할부개월 복수설정 불가| 
| cardCode      | String     |            | 100	 | 특정카드사 선택옵션<br><br>[공통]<br>이용할 수 있는 카드 리스트를 제한 (코드집-카드코드 참고)<br>- 단독 설정 가능<br><br>[카드일반]<br>- ','를 구분자로 카드코드 나열<br>Ex1) cardCode=02<br>-> 국민 카드만 이용할 수 있도록 제한<br>Ex2) cardCode=02,04<br>-> 국민,삼성 카드만 이용할 수 있도록 제한<br><br>[간편결제]<br>- 복수설정 불가<br>- 카카오페이와 PAYCO는 각 간편결제에서 카드만 이용 가능함.<br>카카오페이는 카카오Money 이용불가, PAYCO는 페이코포인트 이용불가<br>  ex) cardCode = 06 (카드사 복수설정 불가)<br><br>*간편결제별 이용가능 카드리스트<br>*- 삼성페이 : 비씨,국민,하나(외환),삼성,신한,현대,롯데,NH,하나<br>- 카카오페이: 비씨,국민,하나(외환),삼성,신한,현대,롯데,씨티,NH,하나<br>- PAYCO : 비씨,국민,하나(외환),삼성,신한,현대,롯데,씨티,NH,하나,한미,신세계한미,수협,신협,우리,광주,전북,제주,해외비자,해외마스터,해외JCB,저축은행,은련,KDB산업,카카오뱅크<br>- SSGPAY : 비씨,국민,하나(외환),삼성,신한,현대,롯데,씨티,NH,하나,전북,케이뱅크<br>- 네이버페이 : 신한, 비씨, 국민, NH, 롯데, 삼성, 씨티, 하나, 현대| 
| cardShowOpt      | String     |           | 50	 |카드사별 인증창 호출방식 옵션<br><br>카드사별 호출방식 정의하여 카드사로 전달<br>- 1:안심클릭, 2:간편결제, 3:앱카드직접 호출<br>- '&brvbar;'를 구분자로 카드코드 나열<br>- 카드코드:노출유형&brvbar;카드코드:노출유형<br>ex) CardShowOpt=08:3&brvbar;02:3<br>- 이용가능 카드사목록 : 02(국민), 04(삼성), 06(신한), 07(현대), 08(롯데), 12(NH), 15(우리)| 

##### 가상계좌
| Parameter       | Type   | 필수     | Byte | 설명                                                                               |
|-----------------|--------|----------|------|------------------------------------------------------------------------------------|
| vbankHolder     | String | 가상계좌 | 40   | 가상계좌 (가맹점 상호명, 사용자명)                                                 |
| vbankValidHours | Int    |          | 4    | 가상계좌 유효시간<br>- 시간단위로 입력.<br>- Default 값 D+7일<br>- vbankValidHours와 vbankExpDate가 함께 요청된경우 vbankValidHours가 우선함<br>ex) 10 을 입력하면, 가상계좌 발급후 10시간동안 해당 가상계좌를 이용할 수 있습니다.                                           |
| vbankExpDate	  |Int |          |      | 가상계좌 입금 만료일                                                            |

##### 다이렉트
| Parameter         | Type   | 필수              | Byte | 설명                                                              |
|-------------------|--------|-------------------|------|-------------------------------------------------------------------|
| directReceiptType | String |                   | 20   | 현금영수증 발급 유형<br>unPublished : 미발행<br>individual : 개인 소득공제용<br>company : 사업자 지출증빙용|
| directReceiptNo   | String | 네이버페이-포인트 | 20   | 현금영수증 발행대상 식별정보<br>휴대폰번호(10 자리 또는 11 자리) 또는 사업자번호(10 자리)<br>* directReceiptType 이 individual 또는 company 인 경우 필수<br>* directReceiptType 이 individual 인경우 휴대폰번호를 입력합니다.<br>* directReceiptType 이 company 인경우 사업자번호를 입력합니다.<br> * ’-‘없이 숫자만 입력|

##### PC 옵션
| Parameter      | Type    | 필수 | Byte | 설명                                                     |
|----------------|---------|------|------|----------------------------------------------------------|
| disableScroll  | Boolean |      | -    | 결제창 스크롤 생성여부<br><br>true : 스크롤 생성 안함(Default : true)<br>false : 스크롤 생성 |
| disableEdgeChk | Boolean |      | -    | Edge브라우저 가이드Alert 예외 여부<br><br>true : Edge브라우저 가이드문구 노출안함<br> false : Edge브라우저 가이드문구 노출(Default : false)|
| zIdxHigher     | Boolean |      | -    | NICEPAY Layer z-index 조정 여부<br>true : NICEPAY Layer의 최하단 z-index를 11000 으로 설정<br>false : default z-index로 9999가 설정됨(Default : false) |

##### Mobile 옵션
| Parameter | Type   | 필수 | Byte | 설명                                                                |
|-----------|--------|------|------|---------------------------------------------------------------------|
| appScheme | String |      | 200  | 모바일 App Scheme 값 (APP 연동인 경우만 사용)<br>가맹점 독립 APP을 이용하여 개발시 (Webview 연동)<br>카드사를 포함한 제휴사 인증 완료 후 결과에대한 focus가 <br>가맹점 APP으로 돌아오기 위해 설정하는 가맹점 APP의 scheme 값을 설정<br>예) 가맹점 App 스킴이 nicepaysample인 경우<br>appScheme=nicepaysample://|

#### 응답 명세 (Server 승인 모델)
```bash
POST
Content-type: application/x-www-form-urlencoded
```
| Parameter      | Type   | 필수   | Byte | 설명                                                                 |
|----------------|--------|--------|------|----------------------------------------------------------------------|
| authResultCode | String |        | 4    | 인증결과 코드<br><br>0000 : 인증성공 / 그외 인증 실패<br>(0000인 경우에만 승인 API를 호출하여 승인요청)                       |
| authResultMsg  | String |        | 500  | 인증결과 메시지                                                      |
| tid            | String | 성공시 | 30   | 결제 인증 키<br><br>결제 승인을 위한  키값 입니다.<br>- 인증에 성공한 경우(authResultCode=0000)에만 리턴됩니다.            |
| clientId       | String |        | 50   | 가맹점 식별코드<br><br>NICEPAY가 발급한 가맹점 식별값                                       |
| orderId        | String |        | 64   | 상점 거래 고유번호<br><br>인증 요청시 전달된 orderId값이 리턴됩니다.                           |
| amount         | Int    |        | 12   | 결제 금액                                                            |
| mallReserved   | String |        | 500  | 상점 예약필드<br><br>인증 요청시 전달된 mallReserved값이 리턴됩니다.                      |
| authToken      | String |        | 40   | 인증 TOKEN                                                           |
| signature      | String |        | 256  | 위변조 검증 데이터<br><br>- 생성규칙 : hex(sha256(authToken + clientId + amount + SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- 인증에 성공한 경우(authResultCode=0000)에만 리턴됩니다.<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.            |

> Server 승인 모델은 `authResultCode`가 `0000`인 경우 승인 API를 호출하면 💳 결제(승인)이 발생 합니다.  
> 승인 API를 호출하지 않는 경우 💳 결제(승인)이 발생되지 않습니다.  

- [결제창 승인 API](/api/payment.md#승인)

#### 응답 명세 (Client 승인 모델)
```bash
POST
Content-type: application/x-www-form-urlencoded
```
| Parameter         | Type    | 필수 | Byte | 설명                                                                                                                       |
|-------------------|---------|------|------|----------------------------------------------------------------------------------------------------------------------------|
| success           | Boolean |      |      | 결제 성공 여부<br><br>true : 결제성공 또는 가상계좌 채번 성공, false:결재실패 또는 인증실패                                                      |
| authToken         | String  | O    | 40   | 인증 TOKEN<br><br>인증거래 Unique Key<br>- 인증 실패된 거래의 가맹점과 NICE간의 매핑 키로 사용 가능합니다.                                                          |
| tid               | String  |      | 30   | 결제 승인 키<br><br>인증성공후 승인이 시도된 경우 리턴됩니다.<br>승인(가상계좌-채번)에 사용된 NICEPAY 거래키 입니다.<br>- 승인성공 또는 승인실패 : tid<br>- 인증실패 : "" (빈값)|
| orderId           | String  | O    | 64   | 상점 거래 고유번호|
| clientId          | String  | O    | 50   | 가맹점 식별코드<br>NICEPAY가 발급한 가맹점 식별값|
| mallReserved      | String  |      | 500  | 상점 예약필드<br><br>상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가|
| resultCode        | String  | O    | 4    | 처리결과코드<br><br>0000 : 성공 / 그외 실패|
| resultMsg         | String  | O    | 100  | 처리결과메시지|
| amount            | Int     | O    | 12   | 결제 금액|
| goodsName         | String  | O    | 40   | 상품명<br><br>상품이름 (“, * 특수문자 이용불가) |
| channel           | String  | O    | 10   | pc:PC결제, mobile:모바일결제|
| status            | String  |      | 20   | 결제 처리상태<br><br>paid:결제완료, ready:준비됨(가상계좌채번), failed:결제실패, cancelled:취소됨, partialCancelled:부분 취소됨, expired:만료됨<br>['paid', 'ready', 'failed', 'cancelled', 'partialCancelled', 'expired']                                                    |
| ediDate           | String  |      | -    | 응답전문생성일시 <br><br>ISO 8601 형식|
| signature         | String  |      | 256  | 위변조 검증 데이터<br><br>- 승인 성공 거래건에 한하여 응답<br>- 생성규칙 : hex(sha256(tid + amount + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.|
| paidAt            | String  |      | -    | 결제완료시점<br><br>ISO 8601 형식<br> 결제완료가 아닐 경우 0    |
| failedAt          | String  |      | -    | 결제실패시점<br><br>ISO 8601 형식<br>결제실패가 아닐 경우 0|
| payMethod         | String  | O    | 10   | 결제수단<br><br>CARD:신용카드, VBANK:가상계좌,<br>naverpay=네이버페이, kakaopay=카카오페이, payco=페이코, ssgpay=SSGPAY, samsungpay=삼성페이                                 |
| useEscrow         | Boolean |      | -    | 에스크로 거래 여부<br><br>false:일반거래 / true:에스크로 거래|
| currency          | String  |      | 3    | 결제승인화폐단위<br><br>KRW:원화, USD:미화달러, CNY:위안화                                                                                         |
| approveNo         | String  |      | 30   | 제휴사 승인 번호<br>신용카드, 계좌이체, 휴대폰                                                                                                 |
| couponAmt         | Int     |      | 12   | 즉시할인 적용된 금액                                                                                                       |
| buyerName         | String  |      | 30   | 구매자 명                                                                                                                  |
| buyerTel          | String  |      | 40   | 구매자 전화번호                                                                                                            |
| buyerEmail        | String  |      | 60   | 구매자 이메일                                                                                                              |
| issuedCashReceipt | Boolean |      | -    | 현금영수증 발급여부<br><br>true:발행 / false:미발행                                                                                                   |
| receiptUrl        | String  |      | 200  | 매출전표 확인 URL                                                                                                          |
| mallUserId        | String  |      | 20   | 상점 사용자 아이디<br><br>상점에서 관리하는 사용자 아이디                                                                                            |
| cardCode          | String  |      | 3    | 결제 카드사 코드                                                                                                           |
| cardName          | String  |      | 20   | 결제 카드사 이름                                                                                                           |
| cardQuota         | Int     |      | 3    | 할부개월<br><br>0:일시불, 2:2개월, 3:3개월 …                                                                                               |
| isInterestFree    | Boolean |      | -    | 상점분담무이자 여부                                                                                                        |
| cardType          | String  |      | 1    | 카드 구분                                                                                                                  |
| canPartCancel     | String  |      | -    | 부분취소 가능 여부                                                                                                         |
| acquCardCode      | String  |      | 3    | 매입카드사코드                                                                                                             |
| acquCardName      | String  |      | 100  | 매입카드사명                                                                                                               |
| vbankCode         | String  |      | 3    | 입금받을 가상계좌 은행코드                                                                                                 |
| vbankName         | String  |      | 20   | 입금받을 가상계좌 은행명                                                                                                   |
| vbankNumber       | String  |      | 20   | 입금받을 가상계좌 번호                                                                                                     |
| vbankExpDate      | String  |      | -    | 가상계좌 입금 만료일<br><br>ISO 8601                                                                                                                   |
| vbankHolder       | String  |      | 40   | 입금받을 가상계좌 예금주명|

### 승인

#### Over-view
![image](https://user-images.githubusercontent.com/86043374/128475651-768bba87-5558-4e04-88b8-0ba14aa7e957.png)  

##### 설명
- 💡 결제창 [JS SDK](/api/payment.md#js-sdk) Server승인 모델에서 카드사 인증 완료 후 처리 구간의 명세 입니다.
- 💡 결제창을 통해 결제자가 카드사 및 결제 원천사에 접근하여 인증과정을 완료하면 나이스페이는 인증결과를 `AUTHNICE.requestPay()`의 object value로 전달된 `returnUrl`로 POST 합니다.
- 가맹점은 POST 데이터의 금액 및 위변조 여부를 체크하고 응답된 tid을 승인 API로 전달 하면 💳 결제(승인)요청 처리가 완료 됩니다. 

##### 예외처리
- 승인 API 호출시 `read-timeout`이 발생한다면 [망 취소](/api/cancel.md#망취소)를 진행 해주세요.

> [클라이언트 키](/common/api.md#클라이언트-키)가 Server 승인 방식으로 발급 된 경우 Server승인 모델 결제창 사용이 가능 합니다.  
> [시크릿 키](/common/api.md#시크릿-키) 생성이 [Bearer token](/common/api.md#bearer-token) 방식인 경우 💳 결제(승인)API 호출전 token 생성과정이 추가 됩니다.  

#### 샘플 코드
```bash
curl -X POST 'https://api.nicepay.co.kr/v1/payments/nicuntct1m0101210727200708A058' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3Zjgz...' 
-D '{
    "amount" : 1004
}'
```
#### 요청 명세
```bash
POST /v1/payments/{tid} HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```
| Parameter     | Type   | 필수 | Byte | 설명                                                       |
|---------------|--------|------|------|------------------------------------------------------------|
| amount        | Int    | O    | 12   | 결제금액                                                   |
| ediDate       | String |      | -    | 전문생성일시<br><br>ISO 8601 형식                          |
| signData      | String |      | 256  | 위변조 검증 Data<br><br>생성규칙 : hex(sha256(tid + amount + ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| returnCharSet | String |      | 10   | 응답파라메터 인코딩 방식<br><br>가맹점 서버의 encoding 방식 전달<br>utf-8(Default) / euc-kr                                    |

#### 응답 명세

##### 공통
```bash
POST
Content-type: application/json
```
| Parameter         |  Type    | 필수 | Byte | 설명                                                                                                         |
|-------------------|----------|------|------|--------------------------------------------------------------------------------------------------------------|
| resultCode        |  String  | O    | 4    | 결제결과코드<br><br>0000   : 성공 / 그외 실패                                                             |
| resultMsg         | String  | O    | 100  | 결제결과메시지                                                                                               |
| tid               | String  | O    | 30   | 결제 승인 키<br><br>최초 승인(가상계좌-채번)에 성공한   원거래의 NICEPAY 거래키 입니다.                              |
| cancelledTid      | String  | 　   | 30   | 취소 거래 키 <br><br>NICEPAY가 발행하는 취소 응답 TID (부분취소시 tid와   다른 값이 응답됨)<br>- 취소 요청건에 한하여 응답됨<br>- cancels 객체에서 현재 취소된   거래정보를 찾을 때 사용 하시면 됩니다.                                     |
| orderId           |  String  | O    | 64   | 상점 거래 고유번호                                                                                           |
| ediDate           |  String  | O    | -    | 응답전문생성일시 ISO 8601 형식                                                                               |
| signature         |  String  | 　   | 256  | 위변조 검증 데이터<br><br>- 유효한 거래건에 한하여 응답<br>- 생성규칙 : hex(sha256(tid + amount +   ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>-   SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.                                                  |
| status            |  String  | O    | 20   | 결제 처리상태<br><br>paid:결제완료, ready:준비됨, failed:결제실패, cancelled:취소됨, partialCancelled:부분 취소됨, expired:만료됨<br>['paid',   'ready', 'failed', 'cancelled', 'partialCancelled', 'expired']                                    |
| paidAt            |  String  | O    | -    | 결제완료시점 ISO 8601 형식<br><br>결제완료가   아닐 경우 0                                             |
| failedAt          |  String  | O    | -    | 결제실패시점 ISO 8601 형식<br><br>결제실패가   아닐 경우 0                                                               |
| cancelledAt       |  String  | O    | -    | 결제취소시점 ISO 8601 형식<br><br>결제취소가   아닐 경우 0 <br>부분취소인경우, 가장 마지막건의 취소 시간  |
| payMethod         | String  | O    | 10   | 결제수단<br><br>CARD:신용카드, VBANK:가상계좌,<br>naverpay=네이버페이, kakaopay=카카오페이, payco=페이코, ssgpay=SSGPAY, samsungpay=삼성페이                   |
| amount            |  Int     | O    | 12   | 결제 금액                                                                                                    |
| balanceAmt        |Int     | O    | 12   | 취소 가능 잔액<br><br>부분취소   거래인경우, 전체금액에서 현재까지 취소된 금액을 차감한   금액.                        |
| goodsName         |  String  | O    | 40   | 상품명                                                                                                       |
| mallReserved      |String  | 　   | 500  | 상점 정보 전달용   예비필드<br><br>returnUrl로 redirect되는   시점에 반환 됩니다.<br>JSON   string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                                   |
| useEscrow         |  Boolean | O    | -    | 에스크로 거래 여부<br><br> false:일반거래 / true:에스크로 거래                                                  |
| currency          |  String  | O    | 3    | 결제승인화폐단위<br><br> KRW:원화, USD:미화달러, CNY:위안화                                                                |
| channel           | String  | 　   | 10   | pc:PC결제, mobile:모바일결제<br><br>['pc',   'mobile', 'null']                                            |
| approveNo         | String  | 　   | 30   | 제휴사 승인   번호<br><br>신용카드, 계좌이체, 휴대폰                                                   |
| buyerName         |  String  | 　   | 30   | 구매자 명                                                                                                    |
| buyerTel          | String  | 　   | 40   | 구매자 전화번호                                                                                              |
| buyerEmail        |  String  | 　   | 60   | 구매자 이메일                                                                                                |
| issuedCashReceipt |  Boolean | 　   | -    | 현금영수증 발급여부<br><br>true:발행 / false:미발행                                                              |
| receiptUrl        |  String  | 　   | 200  | 　매출전표 확인 URL                                                                                          |
| mallUserId        | String  | 　   | 20   | 상점에서 관리하는 사용자   아이디                                                                            |

##### 할인정보
| Parameter |             | Type   | 필수 | 　Byte | 설명                   |
|-----------|-----------|--------|------|--------|------------------------|
| coupon    | 　        | Object | 　   | -      | 즉시할인 프로모션 정보 |
|           | couponAmt | Int    | 　   | 12     | 즉시할인 적용된 금액   |

##### 카드
| Parameter |                | Type    | 필수 | 　Byte | 설명                                                              |
|-----------|----------------|---------|------|--------|-------------------------------------------------------------------|
| card      | 　             | Object  | 　   | 　     | 신용카드 정보                                                     |
| 　        | cardCode       | String  | O    | 3      | 신용카드사별 코드                                                 |
|           | cardName       | String  | O    | 20     | 결제 카드사 이름<br>예) 비씨                                                          |
|           | cardNum        | String  | 　   | 20     | 카드번호<br><br> 3번째 range 마스킹 처리됨<br>예) 53611234****1234<br>*- 카카오머니/네이버포인트/페이코포인트 전액결제 거래인경우   null |
|           | cardQuota      | Int     | O    | 3      | 할부개월<br>0:일시불, 2:2개월, 3:3개월   …                                    |
|           | isInterestFree | Boolean | O    | -      | 상점분담무이자 여부<br>true:무이자,   false:일반                                         |
|           | cardType       | String  | 　   | 1      | 카드 구분<br> credit:신용,   check:체크                                         |
|           | canPartCancel  | String  | O    | -      | 부분취소 가능 여부<br>true:가능,   false:불가능                                         |
|           | acquCardCode   | String  | O    | 3      | 매입카드사코드                                                    |
|           | acquCardName   | String  | O    | 100    | 매입카드사명                                                      |

##### 현금영수증
| Parameter    |             | Type   | 필수 | Byte | 설명                                                                                             |
|--------------|-------------|--------|------|------|--------------------------------------------------------------------------------------------------|
| cashReceipts | 　          | Array  | 　   | 　   | 현금영수증 발급정보<br>-NaverPay-포인트 ,가상계좌 입금건에서 제공<br>-부분 취소시, 2건이상 존재가능 |
| 　           | receiptTid  | String | O    | 30   | 현금영수증 TID                                                                                   |
|              | orgTid      | String | O    | 30   | 연관된 원 승인/취소 거래 TID<br>부분취소시, 원 부분취소   거래건의 TID와 매핑됨<br>- 원거래를 부분취소 하면,   신규 TID가 채번되고,<br>채번된 부분취소 TID가   셋팅 됩니다.                                                             |
|              | status      | String | O    | 20   | 발급진행 상태<br><br>[발급]<br>issueRequested : 발급 접수 완료[1,3]<br>issueReqCancelled : 요청회수(국세청 발행 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>issued : 국세청 발급 완료[4]<br>issueFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10])<br><br>[취소]<br>cancelRequested : 취소 접수 완료[1,3]<br>cancelReqCancelled : 요청회수(국세청 취소 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>cancelled : 국세청 취소 완료[4]<br>cancelFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10])                               |
|              | amount      | Int    | O    | 12   | 현금영수증 발행 총금액                                                                           |
|              | taxFreeAmt  | Int    | O    | 12   | 현금영수증 전체 금액중에서 면세금액                                                              |
|              | receiptType | String | O    | 20   | 현금영수증 타입<br>individual : 개인 소득공제용<br>company : 사업자 지출증빙용                                          |
|              | issueNo     | String | O    | 30   | 현금영수증 국세청 발행번호                                                                       |
|              | receiptUrl  | String | O    | 200  | 현금영수증 매출전표 확인 URL                                                                     |

##### 가상계좌

| Parameter |              | Type   | 필수 | Byte | 설명                        |
|-----------|--------------|--------|------|------|-----------------------------|
| vbank     | 　           | Object | 　   | 　   | 가상계좌 정보               |
| 　        | vbankCode    | String | O    | 3    | 입금받을 가상계좌 은행코드  |
|           | vbankName    | String | O    | 20   | 입금받을 가상계좌 은행명    |
|           | vbankNumber  | String | O    | 20   | 입금받을 가상계좌 번호      |
|           | vbankExpDate | String | O    | -    | 가상계좌 입금 만료일<br>ISO 8601                    |
|           | vbankHolder  | String | O    | 40   | 입금받을 가상계좌 예금주명  |
### 승인 금액 검증

#### Over-view
![image](https://user-images.githubusercontent.com/86043374/128476426-2319e929-d289-4a6b-bde8-569e92adcf59.png)  

##### 설명
- Client승인 모델의 결제창을 통해 결제 후 결제금액 체크에 대한 가이드 입니다.
- 결제자는 💡 결제창을 통해 카드사 및 결제 원천사에 접근하여 인증과정을 진행 하고 나이스페이는 인증 및 💳 결제(승인) 처리 후 결과를 `PAYNICE.requestPay()`의 object value로 전달된 `returnUrl`로 POST 합니다.
- 이후 금액 위변조 여부 검증을 위해 ‘승인 금액 검증’ API를 활용하여 💳 승인(결제)금액을 체크를 진행 합니다.
- 발생된 💳 승인(결제)응답의 금액과 승인금액검증 체크를 통한 금액이 상이한 경우 결제취소 진행 해야 합니다.

> [클라이언트 키](/common/api.md#클라이언트-키)가 Client 승인 방식으로 발급 된 경우 해당되는 사항으로 Server 승인 방식의 💡 결제창을 활용하는 경우 💳 승인(결제) 요청전 금액과 위변조데이터 체크를 권장 합니다.  
> Client승인 모델의 결제창은 💳 승인(결제)금액 검증을 반드시 해야 하며 💳 승인(결제)금액 체크를 하지 않아 발생하는 문제의 책임은 가맹점에게 있습니다.  

	
#### 샘플 코드
```bash
curl -X POST 'https://api.nicepay.co.kr/v1/check-amount/nicuntct1m0101210727200708A058' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3Zjgz...' 
-D '{
    "amount" : 1004
}' 
```
#### 요청 명세 
```bash
POST /v1/check-amount/{tid} HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```
| Parameter     | Type   | 필수 | Byte | 설명                                                       |
|---------------|--------|------|------|------------------------------------------------------------|
| amount        | Int    | O    | 12   | 결제금액                                                   |
| ediDate       | String | 　   | -    | 전문생성일시<br>ISO 8601 형식                                              |
| signData      | String | 　   | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(tid + amount + ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.|
| returnCharSet | String | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br> utf-8(Default) / euc-kr                                    |
#### 응답 명세
```bash
POST
Content-type: application/json
```
| Parameter  | Type | 필수 | Byte | 설명                                                                                                          |
|------------|------|------|------|---------------------------------------------------------------------------------------------------------------|
| resultCode | S    | O    | 4    | 결과코드<br> 0000 : 성공 / 그외 실패                                                                                       |
| resultMsg  | S    | O    | 100  | 결과메시지                                                                                                    |
| ediDate    | S    | O    | -    | 응답전문생성일시 ISO 8601 형식                                                                                |
| signature  | S    | O    | 256  | 위변조 검증 데이터<br> - 유효한 거래건에   한하여 응답<br> - 생성규칙 :   hex(sha256(tid + ediDate + SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br> - SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.                                                     |
| isValid    | B    | O    | -    | 결제금액 일치여부<br>true : 일치 /   false : 불일치(Default)<br>- "resultCode=0000 & isValid=false"로 응답 받은경우 금액이 변조된것으로 판단하고, 거래를취소 하시기 바랍니다. |
| tid        | S    | O    | 30   | 검증한 결제 승인 키<br>검증에 사용된 NICEPAY 거래키<br>-   URI에 요청된 리소스의 tid가 그대로 응답 됩니다. |


## 빌링
### 빌키발급
#### Over-view
![image](https://user-images.githubusercontent.com/86043374/128476945-800bb3a9-340f-4916-85f4-9742a5a35b32.png)  

##### 설명
빌링 서비스는 정기결제(한번의 카드 등록을 통해 반복적인 결제)를 구현할 수 있는 서비스 입니다.  
빌링 서비스는 크게 3가지 파트 [빌키발급](/api/payment.md#빌키발급), [빌키승인](/api/payment.md#빌키승인), [빌키삭제](/api/payment.md#빌키삭제) 부분으로 나뉘어 설명되며,  
각 파트의 명세와 샘플코드를 활용하면 쉽게 구현이 가능 합니다.    
빌키 발급은 결제자의 카드정보를 암호화된 키값으로 변환하는 과정 입니다.  
결제자의 카드정보를 암호화 하여 `/v1/subscribe/regist` API를 호출하면  
나이스페이는 카드정보를 암호화된 형태로 저장 하고 카드정보에 맵핑된 bid(빌키)를 응답 합니다.  
정기결제가 필요한 시점에 가맹점이 bid(빌키)를 빌키승인 API로 전달 하면 등록된 카드로 💳 결제(승인)이 발생 됩니다.  


> 1개의 카드로 n개 빌키 생성이 가능하며 정상 발급된 빌키는 모두 사용이 가능 합니다.  

#### 샘플 코드
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

#### 요청 명세
```bash
POST /v1/subscribe/regist HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```
| Parameter     | Type   | 필수 | Byte | 설명                                                                      |
|---------------|--------|------|------|---------------------------------------------------------------------------|
| encData       | String | O    | 512  | 결제정보 암호화 데이터<br>- 암호화 알고리즘 :   AES128<br>- 암호화 상세 :   AES/CBC/PKCS5padding<br>- 암호결과 인코딩 :   Hex Encoding<br>- 암호 KEY :   SecretKey 앞 16자리<br>- IV : SecretKey 앞 16자리<br>-   Hex(AES(cardNo=value&expYear=YY&expMonth=MM&idNo=value&cardPw=value))<br>*상세 명세는 하단 참조*|
| orderId       | String | O    | 64   | 상점 주문번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호                       |
| buyerName     | String | 　   | 30   | 구매자                                                                    |
| buyerEmail    | String | 　   | 60   | 구매자 이메일주소                                                         |
| buyerTel      | String | 　   | 40   | 구매자 전화번호<br> '-' 없이 숫자만 입력                                                      |
| encMode       | String | 　   | 10   | 암호화 모드<br>encData 필드의 암호화 알고리즘 정의<br><br> A2 : AES256<br>•암호화 알고리즘 : AES256<br>•암호화 상세 : AES/CBC/PKCS5padding <br>•암호결과 인코딩 : Hex Encoding <br> •암호 KEY : SecretKey (32byte)<br>•IV : SecretKey 앞 16자리                                                 |
| ediDate       | String | 　   | -    | 전문생성일시<br> ISO 8601 형식                                                             |
| signData      | Int    | 　   | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(orderId + ediDate +   SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.|
| returnCharSet | String | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                |
##### encData 필드 상세
| Parameter | Type   | 필수 | Byte | 설명                      |
|-----------|--------|------|------|---------------------------|
| cardNo    | String | O    | 16   | 카드번호<br>숫자만 입력               |
| expYear   | String | O    | 2    | 유효기간(년)<br>포멧 : YY                 |
| expMonth  | String | O    | 2    | 유효기간(월)<br>포멧 : MM                 |
| idNo      | String | 계약<br>옵션 | 13   | 생년월일(6)/사업자번호<br>포멧(생년월일) :   YYMMDD |
| cardPw    | String | 계약<br>옵션 | 2    | 카드 비밀번호<br>비밀번호 앞 2자리         |
##### encData 필드 암호화 예시 (AES-128)
```bash
- 평문  : cardNo=1234567890123456&expYear=25&expMonth=12&idNo=800101&cardPw=12
- 암호키 : 2dcc2a0d63bf4694 (SecretKey 앞16자리)
- IV : 2dcc2a0d63bf4694 (SecretKey 앞16자리)
- 암호화결과 : 2127975b6d82c36136ba8197a997a994f6c086ff75a6d35e514c54a1e686545e60b76f11bec706de1082e43dd74ae5c5f0709dc1eca6c3cd20e1c0e9e9b7a85c6505461c91c865d82072e41ba5284bd7
```

##### encData 필드 암호화 예시 (AES-256)
```bash
- 평문 : cardNo=1234567890123456&expYear=25&expMonth=12&idNo=800101&cardPw=12
- 암호키 : 2dcc2a0d63bf469490bb19a201be3735
- IV  : 2dcc2a0d63bf4694 (SecretKey 앞16자리)
- 암호화결과 : 6ecfe97e521bc67c3053d74a9dbdba53033d343fc9e8e38e730964b22ef2e4a59607171b00a9da977141b3f79fffa1e80a16c08bc58666b479f554a966a363414347e62f2621f8df220c7a4a545592d0
```

#### 응답 명세
```bash
POST
Content-type: application/json
```
| Parameter  | Type | 필수 | Byte | 설명                                                                           |
|------------|------|------|------|--------------------------------------------------------------------------------|
| resultCode | S    | O    | 4    | 결제결과코드<br>0000 : 성공 / 그외 실패                                                        |
| resultMsg  | S    | O    | 100  | 결제결과메시지<br>예시) 빌키가 정상적으로 생성되었습니다.                                        |
| tid        | S    | O    | 30   | 거래번호<br>거래를 구분하는 transaction ID<br>예시) nictest00m01011104191651325596                                           |
| orderId    | S    | O    | 64   | 상점 거래 고유번호                                                             |
| bid        | S    | 　   | 30   | 빌키<br>NICEPAY가 발급하는 빌링 아이디<br>가맹점 DB 저장하여, 빌링승인   API 요청시 전달<br> - 회원   카드 정보와 매핑되어 관리되는 Key 값으로, 빌키승인   API 호출시 전달<br>예시) BIKYnictest00m1104191651325596                                           |
| authDate   | S    | 　   | -    | 인증일자<br>ISO 8601 형식                                                                  |
| cardCode   | S    | 　   | 3    | 카드사 코드<br>신용카드사별 코드                                                              |
| cardName   | S    | 　   | 20   | 카드사 이름<br>예시) [삼성]                                                                   |
### 빌키승인
#### Over-view
![image](https://user-images.githubusercontent.com/86043374/128481958-8e45e101-02c7-4511-af61-24d3d0e76768.png)  

##### 설명
- 빌키 승인은 발급된 bid(빌키)를 통해 💳 결제(승인) 처리를 의미 합니다. 
- 등록된 빌키를 통해 `/v1/subscribe/{bid}/payments` API를 호출하면 💳 결제(승인) 처리가 됩니다.
- 빌키 승인을 위해 [빌키 발급](/api/payment.md#빌키발급)과정의 선행이 필요 합니다.

#### 샘플 코드
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

#### 요청 명세
```bash
POST /v1/subscribe/{bid}/payments HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```
| Parameter       | Type    | 필수 | Byte | 설명                                                             |
|-----------------|---------|------|------|------------------------------------------------------------------|
| orderId         | String  | O    | 64   | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br>결제된 orderId로   재호출 불가            |
| amount          | Int     | O    | 12   | 결제 금액                                                        |
| goodsName       | String  | O    | 40   | 상품명                                                           |
| cardQuota       | Int     | O    | 2    | 할부개월<br> 0:일시불, 2:2개월, 3:3개월   …                                   |
| useShopInterest | Boolean | O    | -    | 상점분담무이자 사용여부 (현재 false만 사용 가능)<br>false : 유이자                                                   |
| buyerName       | String  | 　   | 30   | 구매자 이름                                                      |
| buyerTel        | String  | 　   | 40   | 구매자 전화번호<br>하이픈(-) 없이 숫자만   입력                                     |
| buyerEmail      | String  | 　   | 60   | 구매자 이메일                                                    |
| taxFreeAmt      | Int     | 　   | 12   | 면세공급가액<br>전체 거래금액(amount)중에서   면세에 해당하는 금액을 설정합니다. |
| mallReserved    | String  | 　   | 500  | 상점 정보 전달용 예비필드<br><br>승인응답 또는 webhook 시점에 요청 원문을 전달 합니다.<br> JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                       |
| ediDate         | String  | 　   | -    | 전문생성일시<br>ISO 8601 형식                                                    |
| signData        | String  | 　   | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(orderId + bid +   ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.        |
| returnCharSet   | String  | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                    |
#### 응답 명세
```bash
POST
Content-type: application/json
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
| payMethod         | String  | O    | 10   | 결제수단<br>CARD:신용카드,   VBANK:가상계좌,<br>naverpay=네이버페이,   kakaopay=카카오페이, payco=페이코, ssgpay=SSGPAY, samsungpay=삼성페이                   |
| amount            | Int     | O    | 12   | 결제 금액                                                                                                      |
| balanceAmt        | Int     | O    | 12   | 취소 가능 잔액<br>부분취소 거래인경우, 전체금액에서   현재까지 취소된 금액을 차감한 금액.                                        |
| goodsName         | String  | O    | 40   | 상품명                                                                                                         |
| mallReserved      | String  | 　   | 500  | 상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                                     |
| useEscrow         | Boolean | O    | -    | 에스크로 거래 여부<br>false:일반거래 /   true:에스크로 거래                                                                          |
| currency          | String  | O    | 3    | 결제승인화폐단위<br>KRW:원화, USD:미화달러, CNY:위안화                                                                             |
| channel           | String  | 　   | 10   | pc:PC결제, mobile:모바일결제<br>['pc', 'mobile', 'null']                                                                                       |
| approveNo         | String  | 　   | 30   | 제휴사 승인 번호<br>신용카드, 계좌이체, 휴대폰                                                                                     |
| buyerName         | String  | 　   | 30   | 구매자 명                                                                                                      |
| buyerTel          | String  | 　   | 40   | 구매자 전화번호                                                                                                |
| buyerEmail        | String  | 　   | 60   | 구매자 이메일                                                                                                  |
| issuedCashReceipt | Boolean | 　   | -    | 현금영수증 발급여부<br>true:발행 /   false:미발행                                                                                     |
| receiptUrl        | String  | 　   | 200  | 매출전표 확인 URL                                                                                            |
| mallUserId        | String  | 　   | 20   | 상점에서 관리하는 사용자 아이디                                                                                |
##### 할인정보
| Parameter |           | Type   | 필수 | 　Byte | 설명                   |
|-----------|-----------|--------|------|--------|------------------------|
| coupon    | 　        | Object | 　   | -      | 즉시할인 프로모션 정보 |
| 　        | couponAmt | Int    | 　   | 12     | 즉시할인 적용된 금액   |
##### 카드

| Parameter |                | Type    | 필수 | 　Byte | 설명                                                              |
|-----------|----------------|---------|------|--------|-------------------------------------------------------------------|
| card      | 　             | Object  | 　   | 　     | 신용카드 정보                                                     |
| 　        | cardCode       | String  | O    | 3      | 신용카드사별 코드                                                 |
|           | cardName       | String  | O    | 20     | 결제 카드사 이름<br>예) 비씨                                                          |
|           | cardNum        | String  | 　   | 20     | 카드번호<br>3번째 range 마스킹 처리됨<br>예) 53611234****1234*<br>- 카카오머니/네이버포인트/페이코포인트 전액결제 거래인경우   null |
|           | cardQuota      | Int     | O    | 3      | 할부개월<br>0:일시불, 2:2개월, 3:3개월   …                                    |
|           | isInterestFree | Boolean | O    | -      | 상점분담무이자 여부<br>true:무이자,   false:일반                                         |
|           | cardType       | String  | 　   | 1      | 카드 구분<br>credit:신용,   check:체크                                         |
|           | canPartCancel  | String  | O    | -      | 부분취소 가능 여부<br>true:가능,   false:불가능                                         |
|           | acquCardCode   | String  | O    | 3      | 매입카드사코드                                                    |
|           | acquCardName   | String  | O    | 100    | 매입카드사명                                                      |
### 빌키삭제
#### Over-view
![image](https://user-images.githubusercontent.com/86043374/128650600-80501115-d3c8-4701-811a-84e60fcc44b0.png)  

##### 설명
- 빌키 삭제는 발급된 bid(빌키)를 삭제는 과정을 의미 합니다.
- 등록된 빌키를  통해 `/v1/subscribe/{bid}/expire` API를 호출하면 빌키 삭제 처리가 됩니다.
- 삭제된 빌키는 복원과 승인(결제)가 불가 합니다.

``` bash
curl -X POST 'https://api.nicepay.co.kr/v1/subscribe/BIKYnicuntct2m2107272028532670/expire' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic ZWVjOGQzNTA4Y2IwNDI1ZGI5NTViMzBiZjM...' 
-D '{
    "orderId": “merchant-order-id"
}'
```

#### 요청 명세
```bash
POST /v1/subscribe/{bid}/expire HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```
| Parameter     | Type   | 필수 | Byte | 설명                                                          |
|---------------|--------|------|------|---------------------------------------------------------------|
| orderId       | String | O    | 64   | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호           |
| ediDate       | String | 　   | -    | 전문생성일시<br> ISO 8601 형식                                                 |
| signData      | String | 　   | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(orderId + bid +   ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.     |
| returnCharSet | String | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                 |	
#### 응답 명세
```bash
POST
Content-type: application/json
```
| Parameter  | TYPE   | 필수 | 크기 | 설명                                    |
|------------|--------|------|------|-----------------------------------------|
| resultCode | String | O    | 4    | 결제결과코드<br>0000 : 성공 / 그외 실패                 |
| resultMsg  | String | O    | 100  | 결제결과메시지<br>예시) 빌키가 정상적으로 생성되었습니다. |
| tid        | String | O    | 30   | 거래를 구분하는 transaction ID<br>예시) nictest00m01011104191651325596    |
| orderId    | String | O    | 64   | 상점 주문번호                           |
| bid        | String | O    | 30   | 빌키<br>NICEPAY가 발급한 빌링 아이디            |
| authDate   | String | 　   | -    | ISO 8601 형식<br>처리에 성공한경우 리턴됩니다.           |
## EPAY	

### Over-view

### 샘플 코드
```bash
curl -X POST "https://api.nicepay.co.kr/v1/epay/" 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic ZWVjOGQzNTA4Y2IwNDI1ZGI5NTViMzBiZjM...' 
-D '{
    "orderId": “merchant-order-id",
    "encData": "3e5219ba1e488866a3552695e9...",
    "amount": 1004,
    "goodsName": "나이스상품",
    "cardCode": 01,
    "cardQuota": 0,
    "useShopInterest": false
}'
```

### 요청 명세
```bash
POST /v1/epay/ HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```
| Parameter       | Type    | 필수 | Byte | 상세 설명                                                                                                           |
|-----------------|---------|------|------|---------------------------------------------------------------------------------------------------------------------|
| orderId         | String  | O    | 64   | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br> 결제된 orderId로 재호출 불가                                                                                        |
| encData         | String  | O    | -    | 결제정보 암호화 데이터 (encData 상세정보 참고)<br>결제정보 암호화 생성 규칙 (encData 암호화 정보 참고)<br>- Hex(AES(authFlag=value&cardNo=value&track2Data=value&cardExpire=value&TRID=value&CAVV=value&XID=value&ECI=value)) |
| amount          | Int     | O    | 12   | 결제 금액                                                                                                           |
| goodsName       | String  | O    | 40   | 상품명                                                                                                              |
| cardCode        | String  | O    | 2    | 카드사 코드                                                                                                         |
| cardQuota       | Int     | O    | 2    | 할부개월<br>0:일시불, 2:2개월, 3:3개월 …                                                                                        |
| useShopInterest | Boolean | O    | -    | 상점분담무이자 사용여부<br>false : 유이자 / true : 무이자<br>- 사전 협의된 카드사에 한하여 무이자   결제 가능.<br>- 분담무이자 미등록된 카드사로   승인요청하면 결제 실패됩니다.                                                     |
| useCardPoint    | Boolean | 　   | -    | 카드사포인트 사용 여부<br>false:포인트 미사용(default) / true:포인트 사용<br>- 사전에 협의된 카드사에 한하여   포인트 결제 가능합니다.<br>- 포인트 미보유 시 결제   실패됩니다.(일부 카드사 결제 허용)                                                       |
| buyerName       | String  | 　   | 30   | 구매자 이름                                                                                                         |
| buyerTel        | String  | 　   | 40   | 구매자 전화번호<br>하이픈(-) 없이 숫자만 입력                                                                                          |
| buyerEmail      | String  | 　   | 60   | 구매자 이메일                                                                                                       |
| taxFreeAmt      | Int     | 　   | 12   | 면세공급가액<br>전체 거래금액(amount)중에서 면세에 해당하는 금액을 설정합니다.                                                      |
| mallReserved    | String  | 　   | 500  | 상점 정보 전달용 예비필드<br>승인응답 또는 webhook 시점에 요청 원문을 전달 합니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                                          |
| encMode         | String  | 　   | 10   | 암호화 모드<br>encData 필드의 암호화 알고리즘 정의<br>- A2 : AES256                                                                                                      |
| ediDate         | String  | 　   | -    | 전문생성일시 <br>ISO 8601 형식                                                                                                       |
| signData        | String  | 　   | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(orderId + amount +   ediDate + SecretKey)) <br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.                                                           |
| returnCharSet   | String  | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                                                                       |
#### encData 상세 정보
| Parameter  | Type   | 필수 | Byte | 설명                         |
|------------|--------|------|------|------------------------------|
| authFlag   | String | O    | 2    | 인증구분                     |
| cardNo     | String | O    | 16   | 카드번호                     |
| track2Data | String | O    | 39   | 　                           |
| cardExpire | String | O    | 4    | 유효기간(포멧:YYMM)          |
| TRID       | String | 　   | 20   | 나이스정보통신 인증 거래번호 |
| CAVV       | String | 　   | 30   | CAVV                         |
| XID        | String | 　   | 30   | XID                          |
| ECI        | String | 　   | 2    | ECI                          |

#### encData 암호화 정보
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

#### 카드사별 (결제) 승인요청 전문
| 카드사 | AuthFlag | Track2Data(39)              | 나이스정보통신<br>인증 응답 값 승인요청전문 셋팅  | 예시                                               |
|--------|----------|-----------------------------|----------------------------------------|----------------------------------------------------|
| 비씨   | 2        | 37+REAL_CARD_NUM+=+유효기간 | TR_ID -> TRID <br>REAL_CARD_NUM -> cardNo  | authFlag=2<br>cardNo=9100123412341234<br>track2Data=379100123412341234=2502<br>cardExpire=2502<br>TRID=1000031234                                    |
| 삼성   | 0        | 37+REAL_CARD_NUM+=+0000     | CAVV -> CAVV<br>XID -> XID<br>ECI -> ECI<br>REAL_CARD_NUM -> cardNo | authFlag=0<br>cardNo=5310123412341234<br> track2Data=375310123412341234=0000<br>cardExpire=0000<br>CAVV=AAABCGkWZSAhBwIIGRZlBSAAAAA=<br> XID=MjAyMTA3MDIwNzEyNTQ2MzE5OTg=<br>ECI=05                            |
| 현대   | 0        | 37+REAL_CARD_NUM+=+0000     | CAVV -> CAVV<br>XID -> XID<br>ECI -> ECI<br>REAL_CARD_NUM -> cardNo                         | authFlag=0<br>cardNo=9490123412341234<br>track2Data=379490123412341234=0000<br>cardExpire=0000<br>CAVV=AAABCGkWZSAhBwIIGRZlBSAAAAA=<br>XID=MjAyMTA3MDIwNzEyNTQ2MzE5OTg=<br>ECI=05                                             |
| 롯데   | 0        | 37+REAL_CARD_NUM+=+9999     | CAVV -> CAVV<br>ECI(’05’고정) -> ECI<br>REAL_CARD_NUM -> cardNo                           | authFlag=0<br>cardNo=5217123412341234<br>track2Data=375217123412341234=9999<br>cardExpire=9999<br>CAVV=AAABCGkWZSAhBwIIGRZlBSAAAAA=<br>ECI=05                           |
| 신한   | 2        | 37+OTC_NUM                  | OTC_NUM 중 ‘=’앞 15~16자리 cardNo 셋팅 | authFlag=2<br>cardNo=4450123412341234<br>track2Data=374450123412341234=22011234123400100000<br>cardExpire=9999                                    |
| 하나   | 2        | 37+OTC_NUM                  | OTC_NUM 중 ‘=’앞 15~16자리 cardNo 셋팅 | authFlag=2<br>cardNo=9417123412341234<br>track2Data=379417123412341234=22011234123400100000<br>cardExpire=9999                                    |
| 농협   | 2        | 37+OTC_NUM                  | OTC_NUM 중 ‘=’앞 15~16자리 cardNo 셋팅 | authFlag=2<br>cardNo=5461123412341234<br>track2Data=375461123412341234=22011234123400100000<br>cardExpire=9999                                    |
| 국민   | 2        | 37+OTC_NUM+=+8911           | OTC_NUM이 21 자리 인 경우<br>앞 16자리만 cardNo 셋팅              | authFlag=2<br>cardNo=5570123412341234<br>track2Data=375570123412341234=8911<br>cardExpire=8911                                    |

### 응답 명세
```bash
POST
Content-type: application/json
```
| Parameter         | Type    | 필수 | Byte | 설명                                                                                                           |
|-------------------|---------|------|------|----------------------------------------------------------------------------------------------------------------|
| resultCode        | String  | O    | 4    | 결제결과코드<br>0000 : 성공 / 그외 실패                                                                                        |
| resultMsg         | String  | O    | 100  | 결제결과메시지                                                                                                 |
| tid               | String  | O    | 30   | 결제 승인 키<br>최초 승인(가상계좌-채번)에 성공한 원거래의 NICEPAY 거래키 입니다.                                              |
| cancelledTid      | String  | 　   | 30   | 취소 거래 키<br>NICEPAY가 발행하는 취소 응답 TID (부분취소시 tid와 다른 값이 응답됨)<br>- 취소   요청건에 한하여 응답됨<br>- cancels 객체에서 현재 취소된 거래정보를 찾을 때 사용 하시면 됩니다.                                         |
| orderId           | String  | O    | 64   | 상점 거래 고유번호                                                                                             |
| ediDate           | String  | O    | -    | 응답전문생성일시 ISO 8601 형식                                                                                 |
| signature         | String  | 　   | 256  | 위변조 검증 데이터<br>- 유효한 거래건에   한하여 응답<br>- 생성규칙 :   hex(sha256(tid + amount + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.                                                      |
| status            | String  | O    | 20   | 결제 처리상태<br>paid:결제완료,   ready:준비됨, failed:결제실패, cancelled:취소됨, partialCancelled:부분 취소됨, expired:만료됨<br>['paid', 'ready', 'failed', 'cancelled', 'partialCancelled',   'expired']                                      |
| paidAt            | String  | O    | -    | 결제완료시점 ISO 8601 형식<br>결제완료가 아닐 경우 0                                                                                         |
| failedAt          | String  | O    | -    | 결제실패시점 ISO 8601 형식<br>결제실패가 아닐 경우 0                                                                                         |
| cancelledAt       | String  | O    | -    | 결제취소시점 ISO 8601 형식<br>결제취소가 아닐 경우 0<br>부분취소인경우, 가장   마지막건의 취소 시간                                                                    |
| payMethod         | String  | O    | 10   | 결제수단<br>CARD:신용카드,   VBANK:가상계좌,<br>naverpay=네이버페이,   kakaopay=카카오페이, payco=페이코, ssgpay=SSGPAY, samsungpay=삼성페이                   |
| amount            | Int     | O    | 12   | 결제 금액                                                                                                      |
| balanceAmt        | Int     | O    | 12   | 취소 가능 잔액<br>부분취소 거래인경우, 전체금액에서   현재까지 취소된 금액을 차감한 금액.                                        |
| goodsName         | String  | O    | 40   | 상품명                                                                                                         |
| mallReserved      | String  | 　   | 500  | 상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br> 단, 큰따옴표(")는 이용불가                                                                                     |
| useEscrow         | Boolean | O    | -    | 에스크로 거래 여부<br>false:일반거래 /   true:에스크로 거래                                                                          |
| currency          | String  | O    | 3    | 결제승인화폐단위 <br> KRW:원화, USD:미화달러, CNY:위안화                                                                             |
| channel           | String  | 　   | 10   | pc:PC결제, mobile:모바일결제<br>['pc', 'mobile', 'null']                                                                                       |
| approveNo         | String  | 　   | 30   | 제휴사 승인 번호<br>신용카드, 계좌이체, 휴대폰                                                                                     |
| buyerName         | String  | 　   | 30   | 구매자 명                                                                                                      |
| buyerTel          | String  | 　   | 40   | 구매자 전화번호                                                                                                |
| buyerEmail        | String  | 　   | 60   | 구매자 이메일                                                                                                  |
| issuedCashReceipt | Boolean | 　   | -    | 현금영수증 발급여부<br>true:발행 /   false:미발행                                                                                     |
| receiptUrl        | String  | 　   | 200  | 매출전표 확인 URL                                                                                            |
| mallUserId        | String  | 　   | 20   | 상점에서 관리하는 사용자 아이디                                                                                |
#### 할인정보
| Parameter |           | Type   | 필수 | 　Byte | 설명                   |
|-----------|-----------|--------|------|--------|------------------------|
| coupon    | 　        | Object | 　   | -      | 즉시할인 프로모션 정보 |
| 　        | couponAmt | Int    | 　   | 12     | 즉시할인 적용된 금액   |

#### 카드

| Parameter |                | Type    | 필수 | 　Byte | 설명                                                              |
|-----------|----------------|---------|------|--------|-------------------------------------------------------------------|
| card      | 　             | Object  | 　   | 　     | 신용카드 정보                                                     |
| 　        | cardCode       | String  | O    | 3      | 신용카드사별 코드                                                 |
|           | cardName       | String  | O    | 20     | 결제 카드사 이름<br>예) 비씨                                                          |
|           | cardNum        | String  | 　   | 20     | 카드번호<br>3번째 range 마스킹 처리됨<br>예) 53611234****1234*<br>- 카카오머니/네이버포인트/페이코포인트 전액결제 거래인경우   null |
|           | cardQuota      | Int     | O    | 3      | 할부개월<br>0:일시불, 2:2개월, 3:3개월   …                                    |
|           | isInterestFree | Boolean | O    | -      | 상점분담무이자 여부<br>true:무이자,   false:일반                                         |
|           | cardType       | String  | 　   | 1      | 카드 구분<br>credit:신용,   check:체크                                         |
|           | canPartCancel  | String  | O    | -      | 부분취소 가능 여부<br>true:가능,   false:불가능                                         |
|           | acquCardCode   | String  | O    | 3      | 매입카드사코드                                                    |
|           | acquCardName   | String  | O    | 100    | 매입카드사명                                                      |

	
## 현금영수증	
### 발급
#### Over-view
![image](https://user-images.githubusercontent.com/86043374/128650911-346b8f5c-3a5f-4c51-a599-e5454d071661.png)  

##### 설명
현금영수증은 [발급](/api/payment.md#발급), [취소](/api/payment.md#취소), [조회](/api/payment.md#조회) 과정을 통해 관리가 가능 합니다.  
현금영수증 발급요청이 성공하면 정보는 다음날 국세청으로 전달되고 현금영수증 발급을 처리를 진행 합니다.  
국세청의 발급 처리 기간을 고려하여 현금영수증 발급 요청 성공 ⏱️ D+2일 기준으로 [현금영수증 조회](/api/payment.md#조회) 를 처리하면 현금영수증 발급(승인)여부를 확인 할 수 있습니다.  
- 현금영수증 발급 요청은 결제자 정보 및 유형을 `v1/receipt/` API로 전달 하는 것으로 완료 됩니다.  

> 현금영수증 발급요청 성공은 국세청으로 현금영수증 데이터 전달을 위한 요청이 완료 되었음을 의미 합니다.  
> 국세청으로 발급처리 요청과 발급여부 조회까지의 시간간격은 영업일 기준 최대 ⏱️ D+2일 발생합니다.

#### 샘플 코드
```bash
curl -X POST 'https://api.nicepay.co.kr/v1/receipt' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjQ4...' 
-D '{
    "orderId" : “merchant-order-id",
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

#### 요청 명세
``` bash
POST /v1/receipt/ HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```
| Parameter     | Type   | 필수 | 크기 | 상세 설명                                                        |
|---------------|--------|------|------|------------------------------------------------------------------|
| orderId       | String | O    | 64   | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br>결제된 orderId로   재호출 불가                                   |
| amount        | Int    | O    | 12   | 현금영수증 발행금액                                              |
| goodsName     | String | O    | 40   | 상품명                                                           |
| receiptType   | String | O    | 20   | 현금영수증 발급 유형<br> individual : 개인 소득공제용<br>company : 사업자 지출증빙용                                      |
| receiptNo     | String | O    | 20   | 현금영수증 발행대상 식별정보<br>휴대폰번호(10 자리   또는 11 자리) 또는 사업자번호(10   자리)<br>- receiptType 이 individual 인경우 휴대폰번호 <br>- receiptType 이 company 인경우   사업자번호<br>- ’-‘없이 숫자만 입력                                            |
| supplyAmt     | Int    | O    | 12   | amount중 공급가액<br>전체 거래금액(amount)중에서   공급가액에 해당하는 금액<br>해당없을 경우 0                                                  |
| goodsVat      | Int    | O    | 12   | amount중 부가가치세<br>전체 거래금액(amount)중에서   부가세에 해당하는 금액<br>해당없을 경우 0                                                  |
| taxFreeAmt    | Int    | O    | 12   | amount중 면세공급가액<br> 전체 거래금액(amount)중에서   면세에 해당하는 금액<br>해당없을 경우 0                                                  |
| serviceAmt    | Int    | O    | 12   | amount중 봉사료<br> 전체 거래금액(amount)중에서   봉사료에 해당하는 금액<br>해당없을 경우 0                                                  |
| buyerName     | String | 　   | 30   | 구매자 이름                                                      |
| buyerTel      | String | 　   | 40   | 구매자 전화번호<br>하이픈(-) 없이 숫자만   입력                                     |
| buyerEmail    | String | 　   | 60   | 구매자 이메일<br>전문생성일시<br>ISO 8601 형식                                                    |
| signData      | String | 　   | 256  | 위변조 검증 Data <br>생성규칙 : hex(sha256(orderId + amount +   ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.        |
| returnCharSet | String | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                    |
#### 응답 명세
```bash
POST
Content-type: application/json
```
| Parameter  | TYPE   | 필수 | 크기 | 설명                                                                 |
|------------|--------|------|------|----------------------------------------------------------------------|
| resultCode | String | O    | 4    | 결과코드<br>0000 : 성공 / 그외 실패                                              |
| resultMsg  | String | O    | 100  | 결과메시지                                                           |
| tid        | String | O    | 30   | 결제 승인 키<br>NICEPAY 거래키 입니다.                                               |
| orderId    | String | O    | 64   | 상점 거래 고유번호                                                   |
| approvedAt | String | O    | -    | 발급시점<br>ISO 8601 형식<br>발급완료가 아닐 경우 0                                               |
| approveNo  | String | 　   | 30   | 현금영수증 국세청 발행번호<br>발급 성공시 리턴됩니다.                                              |
| ediDate    | String | O    | 14   | 응답전문생성일시<br>ISO 8601 형식                                                        |
| signature  | String | 　   | 256  | 위변조 검증 데이터<br>- 유효한 거래건에   한하여 응답<br>- 생성규칙 :   hex(sha256(tid + orderId + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.            |
### 취소

#### Over-view
![image](https://user-images.githubusercontent.com/86043374/128651176-11bc3c86-cf48-417f-bbef-387e387cb204.png)  

##### 설명
현금영수증은 [발급](/api/payment.md#발급), [취소](/api/payment.md#취소), [조회](/api/payment.md#조회) 과정을 통해 관리되며 현금영수증 취소는 현금영수증 발급 성공 건의 취소를 의미 합니다.  

- 현금영수증 취소 요청은 현금영수증 발급요청 성공시 응답받은 tid와 취소 금액을 `/v1/receipt/{tid}/cancel` API에 전달하는 것으로 처리 됩니다.


> 현금영수증 취소요청 성공은 국세청으로 현금영수증 취소 데이터 전달을 위한 요청이 완료 되었음을 의미 합니다.   
> 국세청으로 취소처리 요청과 조회까지의 시간간격은 영업일 기준 최대 ⏱️ D+2일 발생합니다.  

#### 샘플 코드
``` bash
curl -X POST 'https://api.nicepay.co.kr/v1/receipt/nicuntct1m04012107272036221413/cancel' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMTQ4M2...' 
-D '{
    "orderId" : “merchant-order-id",
    "reason" : “sample-code"
}'
```


#### 요청 명세
``` bash
POST /v1/receipt/{tid}/cancel HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```
| Parameter     | Type   | 필수 | Byte | 설명                                                                    |
|---------------|--------|------|------|-------------------------------------------------------------------------|
| orderId       | String | O    | 64   | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br>결제된 orderId로 재호출 불가                                            |
| reason        | String | O    | 100  | 취소사유                                                                |
| cancelAmt     | Int    | 　   | 12   | 취소요청금액<br>누락이면 전액취소<br>- 부분취소시 supplyAmt, goodsVat, taxFreeAmt, serviceAmt 필드 필수 전달 |
| ediDate       | String | 　   | -    | 전문생성일시<br>ISO 8601 형식                                                           |
| signData      | String | 　   | 256  | 위변조 검증 데이터<br>생성규칙 : hex(sha256(tid + ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.               |
| returnCharSet | String | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                           |
| supplyAmt     | Int    | 　   | 12   | 취소금액(cancelAmt)중에서 공급가액에 해당하는 금액                      |
| goodsVat      | Int    | 　   | 12   | 취소금액(cancelAmt)중에서 부가세에 해당하는 금액                        |
| taxFreeAmt    | Int    | 　   | 12   | 취소금액(cancelAmt)중에서 면세에 해당하는 금액                          |
| serviceAmt    | Int    | 　   | 12   | cancelAmt중 봉사료<br>취소금액(cancelAmt)중에서 봉사료에 해당하는 금액                        |

#### 응답 명세
``` bash
POST
Content-type: application/json
```
| Parameter   | Type   | 필수 | 크기 | 상세 설명                                                               |
|-------------|--------|------|------|-------------------------------------------------------------------------|
| resultCode  | String | O    | 4    | 결과코드<br>0000 : 성공 / 그외 실패                                                 |
| resultMsg   | String | O    | 100  | 결과메시지                                                              |
| tid         | String | O    | 30   | 취소 거래 키<br>NICEPAY 거래키 입니다.                                                  |
| orderId     | String | O    | 64   | 상점 거래 고유번호                                                      |
| cancelAmt   | Int    | O    | 12   | 취소금액<br>취소 실패일 경우 0                                                      |
| balanceAmt  | Int    | O    | 12   | 취소 가능한 잔액<br>부분취소 거래인경우, 전체금액에서   현재까지 취소된 금액을 차감한 금액. |
| cancelledAt | String | O    | -    | 취소시점<br>ISO 8601 형식<br>취소 실패일 경우 0                                                      |
| approveNo   | String | 　   | 30   | 현금영수증 국세청 취소 승인번호<br>취소 성공시 리턴됩니다.                                                 |
| ediDate     | String | O    | 14   | 응답전문생성일시<br>ISO 8601 형식                                                           |
| signature   | String | 　   | 256  | 위변조 검증 데이터<br>- 유효한 거래건에   한하여 응답<br>- 생성규칙 :   hex(sha256(tid + orderId + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.               |

### 조회
#### Over-view
![image](https://user-images.githubusercontent.com/86043374/128651289-dfbf7f80-ddd1-4f7a-ab44-ede0a817635f.png)  

##### 설명
현금영수증은 [발급](/api/payment.md#발급), [취소](/api/payment.md#취소), [조회](/api/payment.md#조회) 과정을 통해 관리되며 현금영수증 조회는 현금영수증 요청 건의 조회를 의미 합니다.  

- 현금영수증 발급요청 성공시 응답받은 tid `/v1/receipt/{tid}` API에 전달하는 것으로 조회 처리 됩니다.

> 국세청으로 발급처리 요청과 발급여부 조회까지의 시간간격은 영업일 기준 최대 ⏱️ D+2일 발생합니다.  


#### 샘플 코드
``` bash
curl -X GET 'https://api.nicepay.co.kr/v1/receipt/nicuntct1m04012107272036221413' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMTQ4M2...' 
```

#### 요청 명세
``` bash
GET /receipt/{tid}/cancel HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```
| Parameter     | Type   | 필수 | Byte | 설명                                                                      |
|---------------|--------|------|------|---------------------------------------------------------------------------|
| orderId       | String | O    | 64   | 상점 거래 고유번호<br> 가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br>결제된 orderId로   재호출 불가                                            |
| reason        | String | O    | 100  | 취소사유                                                                  |
| cancelAmt     | Int    | 　   | 12   | 부분)취소요청금액<br>누락이면 전액취소<br>- 부분취소시 supplyAmt,   goodsVat, taxFreeAmt, serviceAmt 필드 필수 전달 |
| ediDate       | String | 　   | -    | 전문생성일시<br>ISO 8601 형식                                                             |
| signData      | String | 　   | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(tid + ediDate +   SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.                 |
| returnCharSet | String | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                             |
| supplyAmt     | Int    | 　   | 12   | 취소금액(cancelAmt)중에서   공급가액에 해당하는 금액                      |
| goodsVat      | Int    | 　   | 12   | 취소금액(cancelAmt)중에서   부가세에 해당하는 금액                        |
| taxFreeAmt    | Int    | 　   | 12   | 취소금액(cancelAmt)중에서   면세에 해당하는 금액                          |
| serviceAmt    | Int    | 　   | 12   | 취소금액(cancelAmt)중에서   봉사료에 해당하는 금액                        |
#### 응답 명세
``` bash
GET
Content-type: application/json
```
| Parameter   | Type   | 필수 | Byte | 설명                                                                    |
|-------------|--------|------|------|-------------------------------------------------------------------------|
| resultCode  | String | O    | 4    | 결과코드<br>0000 : 성공 / 그외 실패                                                 |
| resultMsg   | String | O    | 100  | 결과메시지                                                              |
| tid         | String | O    | 30   | 취소 거래 키<br>NICEPAY 거래키 입니다.                                                  |
| orderId     | String | O    | 64   | 상점 거래 고유번호                                                      |
| cancelAmt   | Int    | O    | 12   | 취소금액<br>취소 실패일 경우 0                                                      |
| balanceAmt  | Int    | O    | 12   | 취소 가능한 잔액<br>부분취소 거래인경우, 전체금액에서   현재까지 취소된 금액을 차감한 금액. |
| cancelledAt | String | O    | -    | 취소시점<br>ISO 8601 형식<br>취소 실패일 경우 0                                                      |
| approveNo   | String | 　   | 30   | 현금영수증 국세청 취소 승인번호<br> 취소 성공시 리턴됩니다.                                                 |
| ediDate     | String | O    | 14   | 응답전문생성일시<br>ISO 8601 형식                                                           |
| signature   | String | 　   | 256  | 위변조 검증 데이터<br>- 유효한 거래건에   한하여 응답<br>- 생성규칙 :   hex(sha256(tid + orderId + ediDate+ SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.               |

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
- [거래·정산·대사](/api/reconciliation.md) 👉 [거래대사](/api/reconciliation.md#거래대사) | [정산대사](/api/reconciliation.md#정산대사) | [입금대사](/api/reconciliation.md#입금대사)
- [취소·환불·망취소](/api/cancel.md) 👉  [취소·환불](/api/cancel.md#취소환불) | [망 취소](/api/cancel.md#망취소)
- [웹훅](/api/hook.md) 👉 [웹훅](/api/hook.md#웹훅)
- [APP](/api/app.md) 👉 [iOS](/api/app-ios.md#ios) | [iOS Swift](/api/app-ios.md#ios-swift-웹뷰web-view개발-가이드) | [iOS Objective-c](/api/app-ios.md#ios-objective-c-웹뷰web-view개발-가이드) | [Android](/api/app-android.md#) | [Android java](/api/app-android.md#android-java-웹뷰web-view개발-가이드) | [Android kotlin](/api/app-android.md#android-kotlin-웹뷰web-view개발-가이드)

### ☸️ 운영
`운영`에 필요한 정보 입니다.  
- [지원환경](/management/user.md) 👉 [개발환경](/management/user.md#개발환경) | [지원 브라우저](/management/user.md#브라우저)
- [오류관리](/management/user.md#오류관리) 👉 [오류관리](/management/user.md#오류관리)
- [개발정보](/management/admin.md) 👉 [기능 요약](/management/admin.md#기능-요약) | [KEY 정보](/management/admin.md#key정보) | [ip보안(ip접근제한)](/management/admin.md#ip보안ip접근-제한) | [웹훅](/management/admin.md#웹훅) | [로그](/management/admin.md#로그)
