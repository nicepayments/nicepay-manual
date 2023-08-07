# 체크아웃

## 체크아웃 결제창 & 승인

체크아웃 서비스는 1transaction 서비스를 보다 쉽게 사용할 수 있도록 제공하기 위해 만들어진 서비스 입니다.
체크아웃 서비스는 결제창 호출 및 승인 관련 API들이 존재합니다.

| 설명          | HttpMethod | URI                                                    |
|:------------|:----------:|:-------------------------------------------------------|
| 체크아웃 발급     |    POST    | /v1/checkout                                           |
| **체크아웃 승인** |    POST    | **/v1/checkout/pay/{encodeMerchantToken}/{sessionId}** |
| 체크아웃 만료     |    POST    | /v1/checkout/{sessionId}/expire                        |
| 체크아웃 조회     |    GET     | /v1/checkout/{sessionId}                               |
| 체크아웃 거래 조회  |    GET     | /v1/payments/checkout/{sessionId}                      |
| 체크아웃 거래 취소  |    POST    | /v1/payments/checkout/{sessionId}/cancel               |

### 설명

체크아웃 발급 후 url을 호출할 때의 내용으로 가맹점은 결제창을 고객에게 제공할 수 있는 기능입니다.
해당 기능은 1transaction으로 인증 & 승인이 한번에 처리되어 가맹점은 응답을 받지 못할 수도 있는 감안하여 웹훅 및 승인금액검증으로 후처리 작업을 진행하여야 합니다.

** 가맹점의 네트워크 서비스 환경으로 인하여 Read Timeout이 발생할 수 있음을 고려해야 합니다. 

#### ⚠️ 중요

해당 서비스는 1transaction 서비스로 key 발급 시 `client 승인 & basic 인증`으로 발급 받으셔야 합니다.

### 요청 링크

```text
link: https://pay.nicepay.co.kr/v1/checkout/pay/{token}/{sessionId}
```

|    필드     |   타입   | 필수 | 길이  | 설명     | 상세설명                              |
|:---------:|:------:|:--:|:---:|:-------|:----------------------------------|
|   token   | String | O  |     | 가맹점 키  | NICEPAY에서 관리하는 encoding 된 가맹점 GID |
| sessionId | String | O  | 64	 | 결제정보 키 | 가맹점이 요청한 sessionId                |

<br>

### 응답 명세

|        필드         |   타입    | 필수 | 길이  | 설명             | 상세설명                                                                                                                                                                               |
|:-----------------:|:-------:|:--:|:---:|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|      success      | Boolean | O  |     | 결제 성공 여부       | true: 결제성공 또는 가상계좌 채번 성공 <br/> false: 결제실패 또는 인증실패                                                                                                                                 |
|     authToken     | String  | O  | 40  | 인증 TOKEN       | 인증 구간의 유니크한 값 <br>- 인증 구간 내에 프로세스를 추적 할 수 있는 정보                                                                                                                                    |
|        tid        | String  |    | 30  | 결제 승인 키        | **[승인 결과]** <br/> 인증성공후 승인이 시도된 경우 리턴됩니다. <br>승인(가상계좌-채번)에 사용된 NICEPAY 거래키 입니다.                                                                                                    |
|      orderId      | String  | O  | 64  | 상점 거래 고유번호     |                                                                                                                                                                                    |
|     clientId      | String  | O  | 50  | 가맹점 식별코드       | NICEPAY가 발급한 가맹점 식별값                                                                                                                                                               |
|   mallReserved    | String  |    | 500 | 상점 예약필드        | 상점 정보 전달용 예비필드<br>returnUrl로 redirect되는 시점에 반환 됩니다.<br>JSON string format으로 이용하시기를 권고 드립니다.<br>단, 큰따옴표(")는 이용불가                                                                    |
|    resultCode     | String  | O  |  4  | 처리결과코드         | 0000 : 성공 / 그외 실패                                                                                                                                                                  |
|     resultMsg     | String  | O  | 100 | 처리결과메시지        |                                                                                                                                                                                    |
|      amount       | Integer | O  | 12  | 결제 금액          |                                                                                                                                                                                    |
|     goodsName     | String  | O  | 40  | 상품명            | 상품이름 <br/> (", * 특수문자 이용불가)                                                                                                                                                        |
|      channel      | String  | O  | 10  | 결제 디바이스 정보     | pc:PC결제, mobile:모바일결제                                                                                                                                                              |
|     sessionId     | String  | O  | 64	 | 체크아웃 발급 키 | 가맹점 결제정보 식별 키                                                                                                                                                                      |
|      status       | String  |    | 20  | 결제 처리상태        | **[상태 정보]** <br/> - paid:결제완료 <br/> - ready:준비됨(가상계좌 채번) <br/> - failed:결제실패 <br/> - cancelled:취소됨<br/> - partialCancelled:부분 취소됨<br/> - expired:만료됨                               |
|      ediDate      | String  |    |  -  | 응답전문생성일시       | ISO 8601 형식 <br/> 참고 - [ISO8601](https://ko.wikipedia.org/wiki/ISO_8601)                                                                                                           |
|     signature     | String  |    | 256 | 위변조 검증 데이터     | **[주의사항]** <br/> - 승인 성공된 거래시 응답 <br> - 생성규칙 : hex(sha256(tid + amount + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다. |
|      paidAt       | String  |    |  -  | 결제완료시점         | ISO 8601 형식<br> 결제완료가 아닐 경우 0                                                                                                                                                      |
|     failedAt      | String  |    |  -  | 결제실패시점         | ISO 8601 형식<br> 결제완료가 아닐 경우 0                                                                                                                                                      |
|     payMethod     | String  | O  | 10  | 결제수단           | **[결제처리된 결제수단]** <br/> card:신용카드, vbank:가상계좌,<br>naverpay=네이버페이, kakaopay=카카오페이, payco=페이코, ssgpay=SSGPAY, samsungpay=삼성페이                                                         |
|     useEscrow     | Boolean |    |  -  | 에스크로 거래 여부     | **[에스크로 결제 타입]** <br/> - false:일반거래 <br/> - true:에스크로 거래                                                                                                                           |
|     currency      | String  |    |  3  | 결제승인화폐단위       | KRW:원화, USD:미화달러, CNY:위안화                                                                                                                                                          |
|     approveNo     | String  |    | 30  | 제휴사 승인 번호      | 신용카드, 계좌이체, 휴대폰                                                                                                                                                                    |
|        bid        | String  |    | 30  | 빌키             | NICEPAY가 발급하는 빌링 아이디                                                                                                                                                               |
|     couponAmt     | Integer |    | 12  | 즉시할인 적용된 금액    |                                                                                                                                                                                    |
|     buyerName     | String  |    | 30  | 구매자 명          |                                                                                                                                                                                    |
|     buyerTel      | String  |    | 40  | 구매자 전화번호       |                                                                                                                                                                                    |
|    buyerEmail     | String  |    | 60  | 구매자 이메일        |                                                                                                                                                                                    |
| issuedCashReceipt | Boolean |    |  -  | 현금영수증 발급여부     | **[발급 타입]** <br/> - true:발행 <br/> - false:미발행                                                                                                                                      |
|    receiptUrl     | String  |    | 200 | 매출전표 확인 URL    |                                                                                                                                                                                    |
|    mallUserId     | String  |    | 20  | 상점 사용자 아이디     | 상점에서 관리하는 사용자 아이디                                                                                                                                                                  |
|     cardCode      | String  |    |  3  | 결제 카드사 코드      |                                                                                                                                                                                    |
|     cardName      | String  |    | 20  | 결제 카드사 이름      |                                                                                                                                                                                    |
|     cardQuota     | Integer |    |  3  | 할부개월           | 0:일시불, 2:2개월, 3:3개월 …                                                                                                                                                              |
|  isInterestFree   | Boolean |    |  -  | 상점분담무이자 여부     |                                                                                                                                                                                    |
|     cardType      | String  |    |  1  | 카드 구분          |                                                                                                                                                                                    |
|   canPartCancel   | String  |    |  -  | 부분취소 가능 여부     |                                                                                                                                                                                    |
|   acquCardCode    | String  |    |  3  | 매입카드사코드        |                                                                                                                                                                                    |
|   acquCardName    | String  |    | 100 | 매입카드사명         |                                                                                                                                                                                    |
|     vbankCode     | String  |    |  3  | 입금받을 가상계좌 은행코드 |                                                                                                                                                                                    |
|     vbankName     | String  |    | 20  | 입금받을 가상계좌 은행명  |                                                                                                                                                                                    |
|    vbankNumber    | String  |    | 20  | 입금받을 가상계좌 번호   |                                                                                                                                                                                    |
|   vbankExpDate    | String  |    |  -  | 가상계좌 입금 만료일    | ISO 8601 형식                                                                                                                                                                        |
|    vbankHolder    | String  |    | 40  | 입금받을 가상계좌 예금주명 |                                                                                                                                                                                    |
|     bankCode      | String  | O  |  3  | 결제은행코드         | **[은행코드 참조]** - 은행 코드                                                                                                                                                              |
|     bankName      | String  | O  | 20  | 결제은행명          |                                                                                                                                                                                    |

<br>
