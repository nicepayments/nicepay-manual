# 빌링

[빌키발급](#빌키발급) | [빌키승인](#빌키승인) | [빌키삭제](#빌키삭제) | [더 알아보기](#더-알아보기)

<br>

## 빌키발급
### Over-view
<img src="../image/payment-subscribe-regist.svg" width="800px"> 

### 설명
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

### 샘플 코드

```bash
curl -X POST 'https://api.nicepay.co.kr/v1/subscribe/regist' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic ZWVjOGQzNTA4Y2IwNDI1ZGI5NTViMzBiZjM5...' 
-D '{
	"encData":"{암호화된 결제정보 데이터}"
	,"orderId":"{상점 거래 고유번호}"
}'
```

<br>

### 요청 명세 (Body)

```bash
POST /v1/subscribe/regist  
HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials> or Bearer <token>
Content-type: application/json;charset=utf-8
```

| Parameter     | Type   | 필수 | Byte | 설명                                                                      |
|---------------|--------|------|------|---------------------------------------------------------------------------|
| encData       | String | O    | 512  | 결제정보 암호화 데이터<br>- 암호화 알고리즘 :   AES128<br>- 암호화 상세 :   AES/CBC/PKCS5padding<br>- 암호결과 인코딩 :   Hex Encoding<br>- 암호 KEY :   SecretKey 앞 16자리<br>- IV : SecretKey 앞 16자리<br>-   Hex(AES(cardNo=value&expYear=YY&expMonth=MM&idNo=value&cardPw=value))<br>*상세 명세는 하단 참조*|
| orderId       | String | O    | 64   | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호                       |
| buyerName     | String | 　   | 30   | 구매자                                                                    |
| buyerEmail    | String | 　   | 60   | 구매자 이메일주소                                                         |
| buyerTel      | String | 　   | 20   | 구매자 전화번호<br> '-' 없이 숫자만 입력                                                      |
| encMode       | String | 　   | 10   | 암호화 모드<br>encData 필드의 암호화 알고리즘 정의<br><br> A2 : AES256<br>•암호화 알고리즘 : AES256<br>•암호화 상세 : AES/CBC/PKCS5padding <br>•암호결과 인코딩 : Hex Encoding <br> •암호 KEY : SecretKey (32byte)<br>•IV : SecretKey 앞 16자리                                                 |
| ediDate       | String | 　   | -    | 전문생성일시<br> ISO 8601 형식                                                             |
| signData      | Int    | 　   | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(orderId + ediDate +   SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.|
| returnCharSet | String | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                |

<br>

### encData 필드 상세

| Parameter | Type   | 필수       | Byte | 설명                                       |
|-----------|--------|----------|------|------------------------------------------|
| cardNo    | String | O        | 16   | 카드번호<br>숫자만 입력                           |
| expYear   | String | O        | 2    | 유효기간(년)<br>포멧 : YY                       |
| expMonth  | String | O        | 2    | 유효기간(월)<br>포멧 : MM                       |
| idNo      | String | 계약<br>옵션 | 13   | 개인 : 생년월일(6)/YYMMDD <br/> 법인 : 사업자번호(10) |
| cardPw    | String | 계약<br>옵션 | 2    | 카드 비밀번호<br>비밀번호 앞 2자리                    |

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

{
    "ResultCode":"0000"
    ,"ResultMsg":"빌키가 정상적으로 생성되었습니다."
    ,"BID":"{발급된 빌키}"
    ,"AuthDate":"20230214"
    ,"CardCode":"06"
    ,"CardName":"[신한]"
    ,"TID":"{빌키발급 거래번호}"
}

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

<br>

## 빌키승인
### Over-view
<img src="../image/payment-subscribe-billing.svg" width="800px">  

### 설명
- 빌키 승인은 발급된 bid(빌키)를 통해 💳 결제(승인) 처리를 의미 합니다. 
- 등록된 빌키를 통해 `/v1/subscribe/{bid}/payments` API를 호출하면 💳 결제(승인) 처리가 됩니다.
- 빌키 승인을 위해 [빌키 발급](#빌키발급)과정의 선행이 필요 합니다.

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
| amount          | Int     | O    | 12   | 결제 금액                                                        |
| goodsName       | String  | O    | 40   | 상품명                                                           |
| cardQuota       | Int     | O    | 2    | 할부개월<br> 0:일시불, 2:2개월, 3:3개월   …                                   |
| useShopInterest | Boolean | O    | -    | 상점분담무이자 사용여부 (현재 false만 사용 가능)<br>false : 유이자                                                   |
| buyerName       | String  | 　   | 30   | 구매자 이름                                                      |
| buyerTel        | String  | 　   | 20   | 구매자 전화번호<br>하이픈(-) 없이 숫자만   입력                                     |
| buyerEmail      | String  | 　   | 60   | 구매자 이메일                                                    |
| taxFreeAmt      | Int     | 　   | 12   | 면세공급가액<br>전체 거래금액(amount)중에서   면세에 해당하는 금액을 설정합니다. |
| mallReserved    | String  | 　   | 500  | 상점 정보 전달용 예비필드<br><br>승인응답 또는 webhook 시점에 요청 원문을 전달 합니다.<br> JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                       |
| ediDate         | String  | 　   | -    | 전문생성일시<br>ISO 8601 형식                                                    |
| signData        | String  | 　   | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(orderId + bid +   ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.        |
| returnCharSet   | String  | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                    |

<br>

### 응답 명세 (Body)
```bash
POST
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
| amount            | Int     | O    | 12   | 결제 금액                                                                                                      |
| balanceAmt        | Int     | O    | 12   | 취소 가능 잔액<br>부분취소 거래인경우, 전체금액에서   현재까지 취소된 금액을 차감한 금액.                                        |
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
| 　        | couponAmt | Int    | 　   | 12     | 즉시할인 적용된 금액   |

<br>

### 카드 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">


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
POST
Content-type: application/json

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
