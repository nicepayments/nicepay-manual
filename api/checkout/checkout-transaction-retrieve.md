# 체크아웃

## 체크아웃 거래 조회

체크아웃 서비스는 1transaction 서비스를 보다 쉽게 사용할 수 있도록 제공하기 위해 만들어진 서비스 입니다.
체크아웃 서비스는 결제창 호출 및 승인 관련 API들이 존재합니다.

| 설명             | HttpMethod | URI                                                |
|:---------------|:----------:|:---------------------------------------------------|
| 체크아웃 발급        |    POST    | /v1/checkout                                       |
| 체크아웃 승인        |    POST    | /v1/checkout/pay/{encodeMerchantToken}/{sessionId} |
| 체크아웃 만료        |    POST    | /v1/checkout/{sessionId}/expire                    |
| 체크아웃 조회        |    GET     | /v1/checkout/{sessionId}                           |
| **체크아웃 거래 조회** |    GET     | **/v1/payments/checkout/{sessionId}**              |
| 체크아웃 거래 취소     |    POST    | /v1/payments/checkout/{sessionId}/cancel           |

### 설명

체크아웃 거래 조회는 sessionId로 거래조회 할 수 있는 서비스입니다.
sessionId로 결제가 발생한 거래 건에 대해서, tid, orderId로 거래조회 서비스처럼 거래건을 조회할 수 있는 서비스입니다.

#### ⚠️ 중요

해당 서비스는 1transaction 서비스로 key 발급 시 `client 승인 & basic 인증`으로 발급 받으셔야 합니다.

### 요청 명세

```bash
curl -X GET 'https://api.nicepay.co.kr/v1/payments/checkout/{sessionId}'
-H 'Content-type: application/json'
-H 'Authorization: Basic ZWVjOGQzNTA4Y2IwNDI1ZGI5NTViMzBiZjM5...'
```

#### 공통

|      구분      |    필드     |   타입   | 필수 | 길이  | 설명     | 상세설명                              |
|:------------:|:---------:|:------:|:--:|:---:|:-------|:----------------------------------|
| PathVariable | sessionId | String | O  | 64	 | 결제정보 키 | 가맹점이 요청한 sessionId                | 

<br>

### 응답 명세

#### 공통

|        필드         |   타입    | 필수 | 길이  | 설명                 | 상세설명                                                                                                                                                                               |
|:-----------------:|:-------:|:--:|:---:|:-------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    resultCode     | String  | O  |  4  | 처리결과코드             | 0000 : 성공 / 그외 실패                                                                                                                                                                  |
|     resultMsg     | String  | O  | 100 | 처리결과메시지            | "정상 처리되었습니다."                                                                                                                                                                      |
|        tid        | String  | O  | 30  | 결제 승인 키            | **[승인 결과]** <br/> 인증성공후 승인이 시도된 경우 리턴됩니다. <br>승인(가상계좌-채번)에 사용된 NICEPAY 거래키 입니다.                                                                                                    |
|   cancelledTid    | String  |    | 30  | 취소 거래 키            | **[취소 결과]** <br/> - NICEPAY가 발행하는 취소 응답 TID (부분취소시 tid와 다른 값이 응답됨) <br>- 취소 요청건에 한하여 응답 <br/> - cancels 객체에서 현재 취소된 거래정보를 추적하기 위한 용도                                               |
|      orderId      | String  | O  | 64  | 상점 거래 고유번호         |                                                                                                                                                                                    |
|      ediDate      | String  |    |  -  | 응답전문생성일시           | ISO8601                                                                                                                                                                            |
|     signature     | String  |    | 256 | 위변조 검증 데이터         | **[주의사항]** <br/> - 승인 성공된 거래시 응답 <br> - 생성규칙 : hex(sha256(tid + amount + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다. |
|      status       | String  | O  | 20  | 결제 처리상태            | **[상태 정보]** <br/> - paid:결제완료 <br/> - ready:준비됨(가상계좌 채번) <br/> - failed:결제실패 <br/> - cancelled:취소됨<br/> - partialCancelled:부분 취소됨<br/> - expired:만료됨                               |
|      paidAt       | String  | O  |  -  | 결제완료시점             | ISO 8601 형식<br> 결제완료가 아닐 경우 0                                                                                                                                                      |
|     failedAt      | String  | O  |  -  | 결제실패시점             | ISO 8601 형식<br> 결제완료가 아닐 경우 0                                                                                                                                                      |
|    cancelledAt    | String  | O  |  -  | 결제취소시점             | ISO 8601 형식<br> 결제완료가 아닐 경우 0                                                                                                                                                      |
|     payMethod     | String  | O  | 10  | 결제수단               | **[결제처리된 결제수단]** <br/> card:신용카드, vbank:가상계좌,<br>naverpay=네이버페이, kakaopay=카카오페이, payco=페이코, ssgpay=SSGPAY, samsungpay=삼성페이                                                         |
|      amount       | Integer | O  | 12  | 결제 금액              |                                                                                                                                                                                    |
|    balanceAmt     | Integer | O  | 12  | 취소 가능 잔액           | 부분취소 거래인 경우, 전체금액에서 현재까지 취소된 금액을 차감한 금액                                                                                                                                            |
|     goodsName     | String  | O  | 40  | 상품명                | 상품이름 <br/> (", * 특수문자 이용불가)                                                                                                                                                        |
|   mallReserved    | String  |    | 500 | 상점 예약필드            | 상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                    |
|     useEscrow     | Boolean |    | -	  | 에스크로 사용여부 <br/> 		 | true: 에스크로 거래 / false: 일반거래(default)                                                                                                                                               | 
|     currency      | String  |    | 3	  | 통화설정  		           | KRW:원화, USD:미화달러, CNY:위안화                                                                                                                                                          |
|      channel      | String  | O  | 10  | 결제 디바이스 정보         | pc:PC결제, mobile:모바일결제                                                                                                                                                              |
|     approveNo     | String  |    | 30  | 제휴사 승인 번호          | 신용카드, 계좌이체, 휴대폰                                                                                                                                                                    |
|     buyerName     | String  |    | 30	 | 구매자 이름 		          |                                                                                                                                                                                    | 
|     buyerTel      | String  |    | 40	 | 구매자 전화번호<br>  		   | (-) 없이 숫자만 입력                                                                                                                                                                      | 
|    buyerEmail     | String  |    | 60	 | 구매자 이메일 		         |                                                                                                                                                                                    |
|    receiptUrl     | String  |    | 200 | 매출전표 확인 URL        |                                                                                                                                                                                    |
|    mallUserId     | String  |    | 20  | 상점 사용자 아이디         | 상점에서 관리하는 사용자 아이디                                                                                                                                                                  |
| issuedCashReceipt | Boolean |    |  -  | 현금영수증 발급여부         | **[발급 타입]** <br/> - true:발행 <br/> - false:미발행                                                                                                                                      |
|     sessionId     | String  | O  | 64	 | 체크아웃 발급 키          | 가맹점 결제정보 식별 키                                                                                                                                                                      |
|   messageSource   | String  | O  | 10	 | 메시지 출처             | nicepay: 응답 결과의 출처가 NICEPAY <br/> external: 응답 결과의 출처가 제휴사                                                                                                                         |

#### 쿠폰

|  오브젝트  |    필드     |   타입    | 필수 | 길이 | 설명           | 상세설명 |
|:------:|:---------:|:-------:|:--:|:--:|:-------------|:-----|
| coupon |           | Object  |    |    | 즉시할인 프로모션 정보 |      |
|        | couponAmt | Integer |    | 12 | 즉시할인 적용된 금액  |      |

#### 카드

| 오브젝트 |       필드       |   타입    | 필수 | 길이  | 설명          | 상세설명                                                                                                             |
|:----:|:--------------:|:-------:|:--:|:---:|:------------|:-----------------------------------------------------------------------------------------------------------------|
| card |                | Object  |    |     | 신용카드 정보     |                                                                                                                  |
|      |    cardCode    | String  | O  |  2  | 즉시할인 적용된 금액 |                                                                                                                  |
|      |    cardName    | String  | O  | 20  | 결제 카드사 이름   | ex) 비씨                                                                                                           |
|      |    cardNum     | String  |    | 20  | 카드번호        | PCI-DSS 정책에 따라 앞 6자리, 마지막 4자리를 제외한 가운데 숫자 마스킹 처리 <br/> ex) 536112******1234 <br>- 카카오머니/네이버포인트/페이코포인트 전액결제 거래인경우 |
|      |   cardQuota    | String  | O  |  3  | 할부개월 수      | 0: 일시불, 2: 2개월, 3: 3개월..                                                                                         |
|      | isInterestFree | Boolean | O  |  -  | 상점분담무이자 여부  | true: 무이자 <br/> false: 일반                                                                                        |
|      |    cardType    | String  |    |  6  | 카드 구분       | credit: 신용카드 <br/> check: 체크카드                                                                                   |
|      | canPartCancel  | Boolean | O  |  -  | 부분취소 가능 여부  | true: 가능 <br/> false: 불가능                                                                                        |
|      |  acquCardCode  | String  | O  |  3  | 매입카드사코드     | ex) 06                                                                                                           |
|      |  acquCardName  | String  | O  | 100 | 매입카드사명      | ex) 신한                                                                                                           |


#### 가상계좌


| 오브젝트  | 필드           | 타입     | 필수 | 길이 | 설명             | 상세설명     |
|-------|--------------|--------|----|----|----------------|:---------|
| vbank | 　            | Object | 　  | 　  | 가상계좌 정보        |          |
| 　     | vbankCode    | String | O  | 3  | 입금받을 가상계좌 은행코드 |          |
|       | vbankName    | String | O  | 20 | 입금받을 가상계좌 은행명  |          |
|       | vbankNumber  | String | O  | 20 | 입금받을 가상계좌 번호   |          |
|       | vbankExpDate | String | O  | -  | 가상계좌 입금 만료일    | ISO 8601 |
|       | vbankHolder  | String | O  | 40 | 입금받을 가상계좌 예금주명 |          |


#### 취소

|   오브젝트    | 필드           |   타입    |  필수  |  　길이  | 설명          | 상세설명        |
|:---------:|:-------------|:-------:|:----:|:-----:|:------------|:------------|
|  cancels  | 　            |  Array  |  　   |   　   | 취소/부분취소 내역  |             |
|     　     | tid          | String  |  O   |  30   | 승인 취소 거래번호  |             |
|           | amount       | Integer |  O   |  12   | 취소금액        |             |
|           | cancelledAt  | String  |  O   |   -   | 취소된 시각      | ISO8601     |
|           | reason       | String  |  O   |  100  | 취소사유        |             |
|           | receiptUrl   | String  |  O   |  200  | 취소에 대한      | 매출전표 확인 URL |
|           | couponAmt    | Integer |  　   |  12   | 쿠폰 취소금액     |             |

#### 현금영수증

|     오브젝트     | 필드          |   타입    | 필수 | 길이  | 설명                  | 상세설명                                                                                                                                                                                                                                                                                                                                                                                                   |
|:------------:|:------------|:-------:|:--:|:---:|:--------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cashReceipts | 　           |  Array  | 　  |  　  | 현금영수증 발급정보          | -NaverPay-포인트 ,가상계좌 입금건에서 제공<br>-부분 취소시, 2건이상 존재가능                                                                                                                                                                                                                                                                                                                                                     |
|      　       | receiptTid  | String  | O  | 30  | 현금영수증 TID           |                                                                                                                                                                                                                                                                                                                                                                                                        |
|              | orgTid      | String  | O  | 30  | 연관된 원 승인/취소 거래 TID  | 부분취소시, 원 부분취소   거래건의 TID와 매핑됨<br>- 원거래를 부분취소 하면,   신규 TID가 채번되고,<br>채번된 부분취소 TID가   셋팅 됩니다.                                                                                                                                                                                                                                                                                                            |
|              | status      | String  | O  | 20  | 발급진행 상태             | **[발급]** <br/>issueRequested : 발급 접수 완료[1,3]<br/>issueReqCancelled : 요청회수(국세청 발행 접수전 거래의 발급취소(배치 형태의 거래에서 발생[2])<br/>issued : 국세청 발급 완료[4]<br/>issueFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10])<br/>**[취소]**<br/>cancelRequested : 취소 접수 완료[1,3]<br/>cancelReqCancelled : 요청회수(국세청 취소 접수전 거래의 발급취소(배치 형태의 거래에서 발생[2])<br/>cancelled : 국세청 취소 완료[4]<br/>cancelFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10]) |
|              | amount      | Integer | O  | 12  | 현금영수증 발행 총금액        |                                                                                                                                                                                                                                                                                                                                                                                                        |
|              | taxFreeAmt  | Integer | O  | 12  | 현금영수증 전체 금액중에서 면세금액 |                                                                                                                                                                                                                                                                                                                                                                                                        |
|              | receiptType | String  | O  | 20  | 현금영수증 타입            | <br>individual : 개인 소득공제용<br>company : 사업자 지출증빙용                                                                                                                                                                                                                                                                                                                                                       |
|              | issueNo     | String  | O  | 30  | 현금영수증 국세청 발행번호      |                                                                                                                                                                                                                                                                                                                                                                                                        |
|              | receiptUrl  | String  | O  | 200 | 현금영수증 매출전표 확인 URL   |                                                                                                                                                                                                                                                                                                                                                                                                        |


#### 계좌이체

| 오브젝트  | 필드        |    타입    |  필수  |  길이  | 설명                | 상세설명        |
|:-----:|:----------|:--------:|:----:|:----:|:------------------|:------------|
| bank  | 　         |  Object  |  　   |  　   | 은행 정보             |             |
|   　   | bankCode  |  String  |  O   |  3   | 결제은행코드 (은행코드 참조)  |             |
|       | bankName  |  String  |  O   |  20  | 결제은행명 (euc-kr)    |             |
