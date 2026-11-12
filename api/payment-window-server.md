# 결제창 (Server 승인 모델)

[결제창 Server 승인 모델](#결제창-server-승인-모델) | [결제 승인](#승인) | [더 알아보기](#더-알아보기)

<br>

## 결제창 (Server 승인 모델-JS SDK)

### Over-view

<img src="../image/payment-window-server-sdk.svg" width="800px"> 

### 설명
결제자가 브라우저에서 `pay.nicepay.co.kr/v1/js/` JS SDK의 `AUTHNICE.requestPay()` Method 호출시 결제창이 노출 됩니다.  
결제자는 💡 결제창을 통해 카드사 및 결제 원천사에 접근하여 인증과정을 진행 하고 나이스페이는 인증 및 💳 결제(승인) 처리 후 결과를 `AUTHNICE.requestPay()`의 object value로 전달된 `returnUrl`로 `POST` 합니다.  
<br>

> #### ⚠️ 중요
> [클라이언트 키](../common/api.md#클라이언트-키)가 Server 승인 방식으로 발급 된 경우 Server승인 모델 결제창 사용이 가능 합니다.  
> [시크릿 키](../common/api.md#시크릿-키) 생성이 [Bearer token](../common/api.md#bearer-token) 방식인 경우 결제(승인)API 호출전 token 생성과정이 추가 됩니다.


<br>

### 예외처리
- `returnUrl`로 인증응답이 될때 금액, 위변조검증 `signature`, 주문번호가 응답되며 반드시 생성한 결제정보와 일치하는지 체크 후 승인(결제) API를 호출 해주세요.

<br>

### 샘플 코드
 
```html
<script src="https://pay.nicepay.co.kr/v1/js/"></script> //Client 승인 
<script>
function serverAuth() {
  AUTHNICE.requestPay({
    clientId: 'af0d116236df437f831483ee9c500bc4',
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

- 먼저 https://pay.nicepay.co.kr/v1/js/ 를 Inclue 합니다.
- clientId 필드에 [클라이언트 키](../common/api.md#클라이언트-키) 값을 셋팅 하면 준비가 완료 됩니다.
- `AUTHNICE.requestPay()` method 호출시 결제창이 노출 됩니다.
- 💳 결제(승인)결과는 `returnUrl`로 전달된 `end-point`로 post 됩니다.
- 응답된 post 데이터를 결제(승인)API로 전달하면 💳 결제(승인) 처리가 진행 됩니다.
- 샌드박스를 연동하신 내역이 있었다면 실 운영 계정의 `clientId(R1_xx or R2_xx)`로 변경바랍니다.

<br>

### 요청 명세

### 공통

|   Parameter  | type        |    필수  | byte | 설명                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:------------:|:-----------:|:--------:|:----:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| clientId      | String     | O        | 50	 | 가맹점 식별코드, NICEPAY가 발급한 가맹점 식별 값 		                                                                                                                                                                                                                                                                                                                                                                                                                                                   | 
| method      | String     | O        | 20	 | 결제수단 <br> card : 신용카드 <br> bank : 계좌이체 <br> directCard : 결제창 없이 카드사 바로 노출  <br> vbank : 가상계좌  <br> cellphone : 휴대폰 <br>naverpayCard : 네이버페이-신용카드 전액결제(포인트 이용불가) <br> kakaopay : 카카오페이(카드전액 또는 포인트전액) <br>kakaopayCard : 카카오페이-신용카드 전액결제 <br>kakaopayMoney : 카카오페이-머니 전액결제 <br>samsungpayCard : 삼성페이 카드전액 결제 <br>payco : 페이코 <br>ssgpay : SSGPAY <br>cardAndEasyPay : 신용카드와 간편결제 노출 <br>*cardAndEasyPay인 경우, 아래 파라미터와 함께 사용불가* <br>- cardCode, cardQuota, shopInterest, quotaInterest | 
| orderId      | String     | O         | 64	 | 가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br> 결제된 orderId로 재호출 불가                                                                                                                                                                                                                                                                                                                                                                                                                              | 
| amount       | Integer  	    | O         | 12	 | 결제금액 (숫자만)		                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 
| goodsName    | String     | O         | 40	 | 상품명<br> - doubleQuota(")와 pipLine(&brvbar;) 2가지 특수문자는 '-'로 대체 됩니다.                                                                                                                                                                                                                                                                                                                                                                                                                   | 
| returnUrl    | String     | O         | 500	 | 인증 처리 후 redirect 되는 url 		                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 
| mallReserved | String     |           | 500	 | 상점 정보 전상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                                                                                                                                                                                                                                                                                                               | 
| mallUserId   | String     |           | 20	 | 상점에서 관리하는 사용자 아이디 		                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 
| buyerName    | String     |           | 30	 | 구매자 이름 		                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 
| buyerTel     | String     |           | 40	 | 구매자 전화번호<br> (-) 없이 숫자만 입력 		                                                                                                                                                                                                                                                                                                                                                                                                                                                        | 
| buyerEmail   | String     |           | 60	 | 구매자 이메일 		                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 
| useEscrow    | Boolean    |           | -	 | true: 에스크로 거래 / false: 일반거래(default) 		                                                                                                                                                                                                                                                                                                                                                                                                                                              | 
| currency     | String     |           | 3	 | KRW:원화, USD:미화달러, CNY:위안화 		                                                                                                                                                                                                                                                                                                                                                                                                                                                         | 
| logoImgUrl   | String     |           | 100	 | 로고 이미지의 full URL 전달<br>  ex) https://youre.site.com/image/logo.jpg<br> *채널별 사이즈 (단위 : pixel)*<br>모바일 : width 50 X height 50<br> 웹표준 : width 94 X height 25                                                                                                                                                                                                                                                                                                                           | 
| language     | String     |           | 2	 | EN : 영문 / CN : 중문 / KO : 국문(Default)<br>NICEPAY 결제창 내 다국어를 지원<br>*sample)*<br>lang=EN -> 결제창 영문표기<br>lang=CN -> 결제창 중문표기                                                                                                                                                                                                                                                                                                                                                             | 
| returnCharSet| String     |           | 10	 | 가맹점 서버의 encoding 방식 전달<br> - utf-8(Default) / euc-kr		                                                                                                                                                                                                                                                                                                                                                                                                                               | 
| skinType     | String     |           | 10	 | 결제창 스킨 설정<br>지원 옵션 red/green/purple/gray/dark                                                                                                                                                                                                                                                                                                                                                                                                                                        | 

<br>

### 부가세 지정금액

|   Parameter  | type        |    필수  | byte |                             설명                           |
|:------------:|:-----------:|:--------:|:----:|:-----------------------------------------------------------| 
| taxFreeAmt      | Integer     |        | 12	 | 전체 거래금액(amount)중에서 면세에 해당하는 금액을 설정합니다.| 

<br>

### 신용카드 & 간편결제
|   Parameter  | type        |     필수     | byte |                             설명                           |
|:------------:|:-----------:|:------------:|:----:|:-----------------------------------------------------------| 
| cardQuota      | String     |            | 100	 |할부개월 설정<br><br>[공통]<br>선택할 수 있는 할부기간을 제한한다.<br><br>[카드일반+PAYCO+네이버페이]<br>- 단독 설정 가능<br>- ','를 구분자로 할부개월 나열<br>- 일시불은 반드시 "00"으로 설정할것<br>- 2자리의 할부기간 설정 (3개월일 경우 반드시 '03' 으로 설정)<br>Ex) cardQuota=03 <br>- 설명 : 3 개월 할부만 가능하도록 함.<br>최소금액 : 50,000원 이상<br><br>[카카오페이, 삼성페이, SSGPAY]<br> - 단독 설정 사용불가. 반드시 cardCode와 함께 설정되어야 사용가능.<br> - 할부개월 복수설정 불가| 
| cardCode      | String     |            | 100	 | 특정카드사 선택옵션<br><br>[공통]<br>이용할 수 있는 카드 리스트를 제한 (코드집-카드코드 참고)<br>- 단독 설정 가능<br><br>[카드일반]<br>- ','를 구분자로 카드코드 나열<br>Ex1) cardCode=02<br>-> 국민 카드만 이용할 수 있도록 제한<br>Ex2) cardCode=02,04<br>-> 국민,삼성 카드만 이용할 수 있도록 제한<br><br>[간편결제]<br>- 복수설정 불가<br>- 카카오페이와 PAYCO는 각 간편결제에서 카드만 이용 가능함.<br>카카오페이는 카카오Money 이용불가, PAYCO는 페이코포인트 이용불가<br>  ex) cardCode = 06 (카드사 복수설정 불가)<br><br>*간편결제별 이용가능 카드리스트<br>*- 삼성페이 : 비씨,국민,하나(외환),삼성,신한,현대,롯데,NH,하나<br>- 카카오페이: 비씨,국민,하나(외환),삼성,신한,현대,롯데,씨티,NH,하나<br>- PAYCO : 비씨,국민,하나(외환),삼성,신한,현대,롯데,씨티,NH,하나,한미,신세계한미,수협,신협,우리,광주,전북,제주,해외비자,해외마스터,해외JCB,저축은행,은련,KDB산업,카카오뱅크<br>- SSGPAY : 비씨,국민,하나(외환),삼성,신한,현대,롯데,씨티,NH,하나,전북,케이뱅크<br>- 네이버페이 : 신한, 비씨, 국민, NH, 롯데, 삼성, 씨티, 하나, 현대| 
| cardShowOpt      | String     |           | 50	 |카드사별 인증창 호출방식 옵션<br><br>카드사별 호출방식 정의하여 카드사로 전달<br>- 1:안심클릭, 2:간편결제, 3:앱카드직접 호출<br>- '&brvbar;'를 구분자로 카드코드 나열<br>- 카드코드:노출유형&brvbar;카드코드:노출유형<br>ex) CardShowOpt=08:3&brvbar;02:3<br>- 이용가능 카드사목록 : 02(국민), 04(삼성), 06(신한), 07(현대), 08(롯데), 12(NH), 15(우리)| 

<br>

### 가상계좌
| Parameter       | Type    | 필수     | Byte | 설명                                                                               |
|-----------------|---------|----------|------|------------------------------------------------------------------------------------|
| vbankHolder     | String  | O | 40   | 가상계좌 (가맹점 상호명, 사용자명) <br> *가상계좌 채번시 필수                                                 |
| vbankValidHours | Integer |          | 4    | 가상계좌 유효시간<br>- 시간단위로 입력.<br>- Default 값 D+7일<br>- vbankValidHours와 vbankExpDate가 함께 요청된경우 vbankValidHours가 우선함<br>ex) 10 을 입력하면, 가상계좌 발급후 10시간동안 해당 가상계좌를 이용할 수 있습니다.                                           |
| vbankExpDate	  | String  |          |      | 가상계좌 입금 만료일                                                            |

<br>

### 휴대폰
| Parameter | Type | 필수  | Byte | 설명            |
|-----------|------|-----|------|---------------|
|  isDigital  |  Boolean   |  휴대폰결제  |   -    | true: 컨텐츠, false: 실물  |

<br>

### 현금영수증
| Parameter         | Type   | 필수              | Byte | 설명                                                              |
|-------------------|--------|-------------------|------|-------------------------------------------------------------------|
| directReceiptType | String |                   | 20   | 현금영수증 발급 유형<br>unPublished : 미발행<br>individual : 개인 소득공제용<br>company : 사업자 지출증빙용|
| directReceiptNo   | String | 네이버페이-포인트 | 20   | 현금영수증 발행대상 식별정보<br>휴대폰번호(10 자리 또는 11 자리) 또는 사업자번호(10 자리)<br>* directReceiptType 이 individual 또는 company 인 경우 필수<br>* directReceiptType 이 individual 인경우 휴대폰번호를 입력합니다.<br>* directReceiptType 이 company 인경우 사업자번호를 입력합니다.<br> * '-'없이 숫자만 입력|

<br>

### PC 옵션
| Parameter      | Type    | 필수 | Byte | 설명                                                     |
|----------------|---------|------|------|----------------------------------------------------------|
| disableScroll  | Boolean |      | -    | 결제창 스크롤 생성여부<br><br>true : 스크롤 생성 안함(Default : true)<br>false : 스크롤 생성 </br> 결제창 사이즈 : 660*825 pixel |
| disableEdgeChk | Boolean |      | -    | Edge브라우저 가이드Alert 예외 여부<br><br>true : Edge브라우저 가이드문구 노출안함<br> false : Edge브라우저 가이드문구 노출(Default : false)|
| zIdxHigher     | Boolean |      | -    | NICEPAY Layer z-index 조정 여부<br>true : NICEPAY Layer의 최하단 z-index를 11000 으로 설정<br>false : default z-index로 9999가 설정됨(Default : false) |

<br>

### Mobile 옵션
| Parameter | Type   | 필수 | Byte | 설명                                                                |
|-----------|--------|------|------|---------------------------------------------------------------------|
| appScheme | String |      | 200  | 모바일 App Scheme 값 (APP 연동인 경우만 사용)<br>가맹점 독립 APP을 이용하여 개발시 (Webview 연동)<br>카드사를 포함한 제휴사 인증 완료 후 결과에대한 focus가 <br>가맹점 APP으로 돌아오기 위해 설정하는 가맹점 APP의 scheme 값을 설정<br>예) 가맹점 App 스킴이 nicepaysample인 경우<br>appScheme=nicepaysample://|

<br>

### 응답 명세 (Server 승인 모델)
```bash
POST
Accept: application/x-www-form-urlencoded
```
| Parameter      | Type   | 필수   | Byte | 설명                                                                 |
|----------------|--------|--------|------|----------------------------------------------------------------------|
| authResultCode | String |        | 4    | 인증결과 코드<br><br>0000 : 인증성공 / 그외 인증 실패<br>(0000인 경우에만 승인 API를 호출하여 승인요청)                       |
| authResultMsg  | String |        | 500  | 인증결과 메시지                                                      |
| tid            | String | 성공시 | 30   | 결제 인증 키<br><br>결제 승인을 위한  키값 입니다.<br>- 인증에 성공한 경우(authResultCode=0000)에만 리턴됩니다.            |
| clientId       | String |        | 50   | 가맹점 식별코드<br><br>NICEPAY가 발급한 가맹점 식별값                                       |
| orderId        | String |        | 64   | 상점 거래 고유번호<br><br>인증 요청시 전달된 orderId값이 리턴됩니다.                           |
| amount         | Integer    |        | 12   | 결제 금액                                                            |
| mallReserved   | String |        | 500  | 상점 예약필드<br><br>인증 요청시 전달된 mallReserved값이 리턴됩니다.                      |
| authToken      | String |        | 40   | 인증 TOKEN                                                           |
| signature      | String |        | 256  | 위변조 검증 데이터<br><br>- 생성규칙 : hex(sha256(authToken + clientId + amount + SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- 인증에 성공한 경우(authResultCode=0000)에만 리턴됩니다.<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.            |

<br>

> #### ⚠️ 중요
> Server 승인 모델은 `authResultCode`가 `0000`인 경우 승인 API를 호출하면 💳 결제(승인)이 발생 합니다.  
> 승인 API를 호출하지 않는 경우 💳 결제(승인)이 발생되지 않습니다.  

<br>

## 승인

### Over-view
<img src="../image/payment-server-authorization.svg" width="800px"> 

### 설명
- 결제창 [JS SDK](/api/payment.md#js-sdk) Server승인 모델에서 카드사 인증 완료 후 처리 구간의 명세 입니다.
- 결제창을 통해 결제자가 카드사 및 결제 원천사에 접근하여 인증과정을 완료하면 나이스페이는 인증결과를 `AUTHNICE.requestPay()`의 object value로 전달된 `returnUrl`로 POST 합니다.
- 가맹점은 POST 데이터의 금액 및 위변조 여부를 체크하고 응답된 tid을 승인 API로 전달 하면 💳 결제(승인)요청 처리가 완료 됩니다. 

<br>

> #### ⚠️ 중요
> [클라이언트 키](/common/api.md#클라이언트-키)가 Server 승인 방식으로 발급 된 경우 Server승인 모델 결제창 사용이 가능 합니다.  
> [시크릿 키](/common/api.md#시크릿-키) 생성이 [Bearer token](/common/api.md#bearer-token) 방식인 경우 결제(승인)API 호출전 token 생성과정이 추가 됩니다.  

<br>

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
| Parameter     | Type   | 필수 | Byte | 설명                                                       |
|---------------|--------|------|------|------------------------------------------------------------|
| amount        | Integer    | O    | 12   | 결제금액                                                   |
| ediDate       | String |      | -    | 전문생성일시<br><br>ISO 8601 형식                          |
| signData      | String |      | 256  | 위변조 검증 Data<br><br>생성규칙 : hex(sha256(tid + amount + ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.  |
| returnCharSet | String |      | 10   | 응답파라메터 인코딩 방식<br><br>가맹점 서버의 encoding 방식 전달<br>utf-8(Default) / euc-kr                                    |

<br>

### 응답 명세

### 공통
```bash
Content-type: application/json
```
| Parameter         |  Type    | 필수 | Byte | 설명                                                                                                         |
|-------------------|----------|------|------|--------------------------------------------------------------------------------------------------------------|
| resultCode        |  String  | O    | 4    | 결제결과코드<br><br>0000   : 성공 / 그외 실패                                                             |
| resultMsg         | String  | O    | 100  | 결제결과메시지                                                                                               |
| tid               | String  | O    | 30   | 결제 승인 키<br><br>최초 승인(가상계좌-채번)에 성공한   원거래의 NICEPAY 거래키 입니다.                              |
| cancelledTid      | String  | 　   | 30   | 취소 거래 키 <br><br>NICEPAY가 발행하는 취소 응답 TID (부분취소시 tid와   다른 값이 응답됨)<br>- 취소 요청건에 한하여 응답됨<br>- cancels 객체에서 현재 취소된   거래정보를 찾을 때 사용 하시면 됩니다.                                     |
| orderId           |  String  | O    | 64   | 상점 거래 고유번호                                                                                           |
| ediDate           |  String  |     | -    | 응답전문생성일시 ISO 8601 형식                                                                               |
| signature         |  String  | 　   | 256  | 위변조 검증 데이터<br><br>- 유효한 거래건에 한하여 응답<br>- 생성규칙 : hex(sha256(tid + amount +   ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>-   SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.                                                  |
| status            |  String  | O    | 20   | 결제 처리상태<br><br>paid:결제완료, ready:준비됨, failed:결제실패, cancelled:취소됨, partialCancelled:부분 취소됨, expired:만료됨<br>['paid',   'ready', 'failed', 'cancelled', 'partialCancelled', 'expired']                                    |
| paidAt            |  String  | O    | -    | 결제완료시점 ISO 8601 형식<br><br>결제완료가   아닐 경우 0                                             |
| failedAt          |  String  | O    | -    | 결제실패시점 ISO 8601 형식<br><br>결제실패가   아닐 경우 0                                                               |
| cancelledAt       |  String  | O    | -    | 결제취소시점 ISO 8601 형식<br><br>결제취소가   아닐 경우 0 <br>부분취소인경우, 가장 마지막건의 취소 시간  |
| payMethod         | String  | O    | 10   | 결제수단<br><br>card:신용카드, vbank:가상계좌,<br>naverpay=네이버페이, kakaopay=카카오페이, payco=페이코, ssgpay=SSGPAY, samsungpay=삼성페이                   |
| amount            |  Integer     | O    | 12   | 결제 금액                                                                                                    |
| balanceAmt        |Integer     | O    | 12   | 취소 가능 잔액<br><br>부분취소   거래인경우, 전체금액에서 현재까지 취소된 금액을 차감한   금액.                        |
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

<br>

### 할인정보 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">
| Parameter |             | Type   | 필수 | 　Byte | 설명                   |
|-----------|-----------|--------|------|--------|------------------------|
| coupon    | 　        | Object | 　   | -      | 즉시할인 프로모션 정보 |
|           | couponAmt | Integer    | 　   | 12     | 즉시할인 적용된 금액   |

<br>

### 카드 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">
| Parameter |                | Type    | 필수 | 　Byte | 설명                                                              |
|-----------|----------------|---------|------|--------|-------------------------------------------------------------------|
| card      | 　             | Object  | 　   | 　     | 신용카드 정보                                                     |
| 　        | cardCode       | String  | O    | 3      | 신용카드사별 코드                                                 |
|           | cardName       | String  | O    | 20     | 결제 카드사 이름<br>예) 비씨                                                          |
|           | cardNum        | String  | 　   | 20     | 카드번호<br>앞 6자 마지막 4자를 제외한 가운데 숫자 마스킹 처리됨<br>예) 536112******1234<br>- 카카오머니/네이버포인트/페이코포인트 전액결제 거래인경우   null |
|           | cardQuota      | String     | O    | 3      | 할부개월<br>0:일시불, 2:2개월, 3:3개월   …                                    |
|           | isInterestFree | Boolean | O    | -      | 상점분담무이자 여부<br>true:무이자,   false:일반                                         |
|           | cardType       | String  | 　   | 1      | 카드 구분<br> credit:신용,   check:체크                                         |
|           | canPartCancel  | String  | O    | -      | 부분취소 가능 여부<br>true:가능,   false:불가능                                         |
|           | acquCardCode   | String  | O    | 3      | 매입카드사코드                                                    |
|           | acquCardName   | String  | O    | 100    | 매입카드사명                                                      |

<br>

### 현금영수증 <img src="https://img.shields.io/badge/-Array-blueviolet"> <img src="https://img.shields.io/badge/-nullable-lightgrey">
| Parameter    |             | Type   | 필수 | Byte | 설명                                                                                             |
|--------------|-------------|--------|------|------|--------------------------------------------------------------------------------------------------|
| cashReceipts | 　          | Array  | 　   | 　   | 현금영수증 발급정보<br>-NaverPay-포인트 ,가상계좌 입금건에서 제공<br>-부분 취소시, 2건이상 존재가능 |
| 　           | receiptTid  | String | O    | 30   | 현금영수증 TID                                                                                   |
|              | orgTid      | String | O    | 30   | 연관된 원 승인/취소 거래 TID<br>부분취소시, 원 부분취소   거래건의 TID와 매핑됨<br>- 원거래를 부분취소 하면,   신규 TID가 채번되고,<br>채번된 부분취소 TID가   셋팅 됩니다.                                                             |
|              | status      | String | O    | 20   | 발급진행 상태<br><br>[발급]<br>issueRequested : 발급 접수 완료[1,3]<br>issueReqCancelled : 요청회수(국세청 발행 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>issued : 국세청 발급 완료[4]<br>issueFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10])<br><br>[취소]<br>cancelRequested : 취소 접수 완료[1,3]<br>cancelReqCancelled : 요청회수(국세청 취소 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>cancelled : 국세청 취소 완료[4]<br>cancelFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10])                               |
|              | amount      | Integer    | O    | 12   | 현금영수증 발행 총금액                                                                           |
|              | taxFreeAmt  | Integer    | O    | 12   | 현금영수증 전체 금액중에서 면세금액                                                              |
|              | receiptType | String | O    | 20   | 현금영수증 타입<br>individual : 개인 소득공제용<br>company : 사업자 지출증빙용                                          |
|              | issueNo     | String | O    | 30   | 현금영수증 국세청 발행번호                                                                       |
|              | receiptUrl  | String | O    | 200  | 현금영수증 매출전표 확인 URL                                                                     |

<br>

### 계좌이체 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">


| Parameter |          | Type   | 필수  | Byte | 설명               |
|-----------|----------|--------|-----|------|------------------|
| bank      | 　        | Object | 　   | 　    | 은행 정보            |
| 　         | bankCode | String | O   | 3    | 결제은행코드 (은행코드 참조) |
|           | bankName | String | O   | 20   | 결제은행명 (euc-kr)   |

<br>

### 가상계좌 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">


| Parameter |              | Type   | 필수 | Byte | 설명                        |
|-----------|--------------|--------|------|------|-----------------------------|
| vbank     | 　           | Object | 　   | 　   | 가상계좌 정보               |
| 　        | vbankCode    | String | O    | 3    | 입금받을 가상계좌 은행코드  |
|           | vbankName    | String | O    | 20   | 입금받을 가상계좌 은행명    |
|           | vbankNumber  | String | O    | 20   | 입금받을 가상계좌 번호      |
|           | vbankExpDate | String | O    | -    | 가상계좌 입금 만료일<br>ISO 8601                    |
|           | vbankHolder  | String | O    | 40   | 입금받을 가상계좌 예금주명  |


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
