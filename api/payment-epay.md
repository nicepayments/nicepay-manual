## EPAY	
[EPAY](/api/payment-epay.md#epay) | [더 알아보기](/api/payment-epay.md#더-알아보기)

### 샘플 코드
```bash
curl -X POST "https://api.nicepay.co.kr/v1/epay/" 
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
| Parameter       | Type    | 필수 | Byte | 상세 설명                                                                                                           |
|-----------------|---------|------|------|---------------------------------------------------------------------------------------------------------------------|
| orderId         | String  | O    | 64   | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br> 결제된 orderId로 재호출 불가                                                                                        |
| encData         | String  | O    | -    | 결제정보 암호화 데이터 [encData 상세정보 참고](#encdata-상세-정보)<br>결제정보 암호화 생성 규칙 [encData 암호화 정보 참고](#encdata-암호화-정보)<br>- Hex(AES(authFlag=value&cardNo=value&track2Data=value&cardExpire=value&TRID=value&CAVV=value&XID=value&ECI=value)) |
| amount          | Integer | O    | 12   | 결제 금액                                                                                                           |
| goodsName       | String  | O    | 40   | 상품명                                                                                                              |
| cardCode        | String  | O    | 2    | 카드사 코드                                                                                                         |
| cardQuota       | String  | O    | 2    | 할부개월<br>0:일시불, 2:2개월, 3:3개월 …                                                                                        |
| useShopInterest | Boolean | O    | -    | 상점분담무이자 사용여부<br>false : 유이자 / true : 무이자<br>- 사전 협의된 카드사에 한하여 무이자   결제 가능.<br>- 분담무이자 미등록된 카드사로   승인요청하면 결제 실패됩니다.                                                     |
| useCardPoint    | Boolean | 　   | -    | 카드사포인트 사용 여부<br>false:포인트 미사용(default) / true:포인트 사용<br>- 사전에 협의된 카드사에 한하여   포인트 결제 가능합니다.<br>- 포인트 미보유 시 결제   실패됩니다.(일부 카드사 결제 허용)                                                       |
| buyerName       | String  | 　   | 30   | 구매자 이름                                                                                                         |
| buyerTel        | String  | 　   | 40   | 구매자 전화번호<br>하이픈(-) 없이 숫자만 입력                                                                                          |
| buyerEmail      | String  | 　   | 60   | 구매자 이메일                                                                                                       |
| taxFreeAmt      | Integer | 　   | 12   | 면세공급가액<br>전체 거래금액(amount)중에서 면세에 해당하는 금액을 설정합니다.                                                      |
| mallReserved    | String  | 　   | 500  | 상점 정보 전달용 예비필드<br>승인응답 또는 webhook 시점에 요청 원문을 전달 합니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                                          |
| encMode         | String  | 　   | 10   | 암호화 모드<br>encData 필드의 암호화 알고리즘 정의<br>- A2 : AES256                                                                                                      |
| ediDate         | String  | 　   | -    | 전문생성일시 <br>ISO 8601 형식                                                                                                       |
| signData        | String  | 　   | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(orderId + amount +   ediDate + SecretKey)) <br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.                                                           |
| returnCharSet   | String  | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                                                                       |
<br>

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

<br>

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

<br>

#### 카드사별 (결제) 승인요청 전문
| 카드사 | AuthFlag | Track2Data(39)              | 나이스정보통신<br>인증 응답 값 승인요청전문 셋팅  | 예시                                               |
|--------|----------|-----------------------------|----------------------------------------|----------------------------------------------------|
| 비씨   | 2        | 37+REAL_CARD_NUM+=+유효기간 | TR_ID -> TRID <br>REAL_CARD_NUM -> cardNo  | authFlag=2<br>cardNo=9100123412341234<br>track2Data=379100123412341234=2502<br>cardExpire=2502<br>TRID=1000031234                                    |
| 삼성   | 0        | 37+REAL_CARD_NUM+=+0000     | CAVV -> CAVV<br>XID -> XID<br>ECI -> ECI<br>REAL_CARD_NUM -> cardNo | authFlag=0<br>cardNo=5310123412341234<br> track2Data=375310123412341234=0000<br>cardExpire=0000<br>CAVV=AAABCGkWZSAhBwIIGRZlBSAAAAA=<br> XID=MjAyMTA3MDIwNzEyNTQ2MzE5OTg=<br>ECI=05                            |
| 현대   | 0        | 37+REAL_CARD_NUM+=+0000     | CAVV -> CAVV<br>XID -> XID<br>ECI -> ECI<br>REAL_CARD_NUM -> cardNo                         | authFlag=0<br>cardNo=9490123412341234<br>track2Data=379490123412341234=0000<br>cardExpire=0000<br>CAVV=AAABCGkWZSAhBwIIGRZlBSAAAAA=<br>XID=MjAyMTA3MDIwNzEyNTQ2MzE5OTg=<br>ECI=05                                             |
| 롯데   | 0        | 37+REAL_CARD_NUM+=+9999     | CAVV -> CAVV<br>ECI('05'고정) -> ECI<br>REAL_CARD_NUM -> cardNo                           | authFlag=0<br>cardNo=5217123412341234<br>track2Data=375217123412341234=9999<br>cardExpire=9999<br>CAVV=AAABCGkWZSAhBwIIGRZlBSAAAAA=<br>ECI=05                           |
| 신한   | 2        | 37+OTC_NUM                  | OTC_NUM 중 '='앞 15~16자리 cardNo 셋팅 | authFlag=2<br>cardNo=4450123412341234<br>track2Data=374450123412341234=22011234123400100000<br>cardExpire=9999                                    |
| 하나   | 2        | 37+OTC_NUM                  | OTC_NUM 중 '='앞 15~16자리 cardNo 셋팅 | authFlag=2<br>cardNo=9417123412341234<br>track2Data=379417123412341234=22011234123400100000<br>cardExpire=9999                                    |
| 농협   | 2        | 37+OTC_NUM                  | OTC_NUM 중 '='앞 15~16자리 cardNo 셋팅 | authFlag=2<br>cardNo=5461123412341234<br>track2Data=375461123412341234=22011234123400100000<br>cardExpire=9999                                    |
| 국민   | 2        | 37+OTC_NUM+=+8911           | OTC_NUM이 21 자리 인 경우<br>앞 16자리만 cardNo 셋팅              | authFlag=2<br>cardNo=5570123412341234<br>track2Data=375570123412341234=8911<br>cardExpire=8911                                    |

<br>

### 응답 명세 (Body)
```bash
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
| payMethod         | String  | O    | 10   | 결제수단<br><br>card:신용카드,<br>vbank:가상계좌,<br>bank:계좌이체,<br>cellphone:휴대폰,<br>naverpay=네이버페이, kakaopay=카카오페이, samsungpay=삼성페이                   |
| amount            | Integer     | O    | 12   | 결제 금액                                                                                                      |
| balanceAmt        | Integer     | O    | 12   | 취소 가능 잔액<br>부분취소 거래인경우, 전체금액에서   현재까지 취소된 금액을 차감한 금액.                                        |
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

<br>

#### 할인정보 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |           | Type   | 필수 | 　Byte | 설명                   |
|-----------|-----------|--------|------|--------|------------------------|
| coupon    | 　        | Object | 　   | -      | 즉시할인 프로모션 정보 |
| 　        | couponAmt | Integer    | 　   | 12     | 즉시할인 적용된 금액   |

<br>

#### 카드 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">


| Parameter |                | Type    | 필수 | 　Byte | 설명                                                              |
|-----------|----------------|---------|------|--------|-------------------------------------------------------------------|
| card      | 　             | Object  | 　   | 　     | 신용카드 정보                                                     |
| 　        | cardCode       | String  | O    | 3      | 신용카드사별 코드                                                 |
|           | cardName       | String  | O    | 20     | 결제 카드사 이름<br>예) 비씨                                                          |
|           | cardNum        | String  | 　   | 20     | 카드번호<br>앞 6자 마지막 4자를 제외한 가운데 숫자 마스킹 처리됨<br>예) 536112******1234<br>- 카카오머니/네이버포인트/페이코포인트 전액결제 거래인경우   null |
|           | cardQuota      | String     | O    | 3      | 할부개월<br>0:일시불, 2:2개월, 3:3개월   …                                    |
|           | isInterestFree | Boolean | O    | -      | 상점분담무이자 여부<br>true:무이자,   false:일반                                         |
|           | cardType       | String  | 　   | 1      | 카드 구분<br>credit:신용,   check:체크                                         |
|           | canPartCancel  | String  | O    | -      | 부분취소 가능 여부<br>true:가능,   false:불가능                                         |
|           | acquCardCode   | String  | O    | 3      | 매입카드사코드                                                    |
|           | acquCardName   | String  | O    | 100    | 매입카드사명                                                      |


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
- [결제·발급](/api/payment.md#) 👉 [결제창](/api/payment-window-server.md) | [현금영수증](/api/payment-receipt.md) | [Access token](/api/payment-access-token.md)
- [조회](/api/status.md) 👉 [거래 조회](/api/status-transaction.md) | [약관 조회](/api/status-terms.md) | [카드 이벤트 조회](/api/status-event.md) | [카드 무이자 조회](/api/status-interest.md)
- [취소·환불·망취소](/api/cancel.md) 👉  [취소·환불](/api/cancel.md#취소환불) | [망 취소](/api/cancel.md#망취소)
- [웹훅](/api/hook.md) 👉 [웹훅](/api/hook.md#웹훅)
- [APP](/api/app.md) 👉 [iOS](/api/app-ios.md#ios) | [iOS Swift](/api/app-ios.md#ios-swift-웹뷰web-view개발-가이드) | [iOS Objective-c](/api/app-ios.md#ios-objective-c-웹뷰web-view개발-가이드) | [Android](/api/app-android.md#) | [Android java](/api/app-android.md#android-java-웹뷰web-view개발-가이드) | [Android kotlin](/api/app-android.md#android-kotlin-웹뷰web-view개발-가이드)

### ☸️ 운영
`운영`에 필요한 정보 입니다.  
- [지원환경](/management/user.md) 👉 [개발환경](/management/user.md#개발환경) | [지원 브라우저](/management/user.md#브라우저)
- [오류관리](/management/user.md#오류관리) 👉 [오류관리](/management/user.md#오류관리)
- [개발정보](/management/admin.md) 👉 [기능 요약](/management/admin.md#기능-요약) | [KEY 정보](/management/admin.md#key정보) | [ip보안(ip접근제한)](/management/admin.md#ip보안ip접근-제한) | [웹훅](/management/admin.md#웹훅) | [로그](/management/admin.md#로그)
