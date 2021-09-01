# 조회
[거래조회](#거래) | [약관조회](#약관) | [카드 이벤트 조회](#카드-이벤트) | [카드 무이자 조회](#카드-무이자) | [더 알아보기](#더-알아보기)

<br>

## 거래	
### Over-view
거래 조회는 결제(승인)요청 성공 혹은 실패에 따른 정보확인이 필요한 경우 활용 할 수 있습니다.

<br>

#### 거래 조회 API가 필요한 경우
- 결제(승인) API를 호출 후 Http-client의 [timeout](/common/preparations.md#타임아웃-정보)이 발생하여 [결제취소](/api/cancel.md#취소환불-1) 혹은 [망 취소](/api/cancel.md#망취소)를 고려해야하는 경우
- 특정 결제(승인) 건의 데이터가 일부 유실되어 조회가 필요한 경우
- 결제(승인) 건의 데이터 위변조가 의심되어 원본 데이터 정보 체크가 필요한 경우

<br>

### 샘플 코드
```bash
curl -X GET 'https://api.nicepay.co.kr/v1/payments/nicuntct1m0101210727200125A056' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMT...'

```

<br>

### 요청 명세
### 거래조회(tid 활용)
```bash
POST /v1/payments/{tid} HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```
| Parameter     | Type | 필수 | 크기 | 설명                                                      |
|---------------|------|------|------|-----------------------------------------------------------|
| ediDate       | S    | 　   | -    | 전문생성일시<br>ISO 8601 형식                                             |
| signData      | S    | 　   | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(tid + ediDate +   SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다. |
| returnCharSet | S    | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                             |

<br>

### 거래조회(orderId 활용)
```bash
POST /v1/payments/find/{orderId} HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
![image](https://user-images.githubusercontent.com/86043374/128659182-20b04881-49b6-49d2-9326-5059c1e1088e.png)
```
| Parameter     | Type | 필수 | 크기 | 설명                                                      |
|---------------|------|------|------|-----------------------------------------------------------|
| orderDate     | S    | O    | 8    | 주문일자<br>YYYYMMDD                                                  |
| ediDate       | S    | 　   | -    | 전문생성일시<br> ISO 8601 형식                                             |
| signData      | S    | 　   | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(tid + ediDate +   SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다. |
| returnCharSet | S    | 　   | 10   | 응답파라메터 인코딩 방식<br> 가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                             |

<br>

### 응답 명세 (공통)
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
| signature         | String  | 　   | 256  | 위변조 검증 데이터<br>- 유효한 거래건에 한하여 응답<br>- 생성규칙 :   hex(sha256(tid + amount + ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.                                                      |
| status            | String  | O    | 20   | 결제 처리상태<br>paid:결제완료,   ready:준비됨, failed:결제실패, cancelled:취소됨, partialCancelled:부분 취소됨, expired:만료됨<br>['paid', 'ready', 'failed', 'cancelled', 'partialCancelled',   'expired']                                      |
| paidAt            | String  | O    | -    | 결제완료시점 ISO 8601 형식<br>결제완료가 아닐 경우 0                                                                                         |
| failedAt          | String  | O    | -    | 결제실패시점 ISO 8601 형식<br>결제실패가 아닐 경우 0                                                                                         |
| cancelledAt       | String  | O    | -    | 결제취소시점 ISO 8601 형식<br>결제취소가 아닐 경우 0<br>부분취소인경우, 가장   마지막건의 취소 시간                                                                    |
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
| receiptUrl        | String  | 　   | 200  | 　매출전표 확인 URL                                                                                            |
| mallUserId        | String  | 　   | 20   | 상점에서 관리하는 사용자 아이디                                                                                |

<br>

### 할인 정보
| Parameter |           | Type   | 필수 | 　Byte | 설명                   |
|-----------|-----------|--------|------|--------|------------------------|
| coupon    | 　        | Object | 　   | -      | 즉시할인 프로모션 정보 |
| 　        | couponAmt | Int    | 　   | 12     | 즉시할인 적용된 금액   |

<br>

### 카드
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

### 현금영수증
| Parameter    |             | Type   | 필수 | Byte | 설명                                                                                             |
|--------------|-------------|--------|------|------|--------------------------------------------------------------------------------------------------|
| cashReceipts | 　          | Array  | 　   | 　   | 현금영수증 발급정보<br>-NaverPay-포인트 ,가상계좌 입금건에서 제공<br>-부분 취소시, 2건이상 존재가능                                                                   |
| 　           | receiptTid  | String | O    | 30   | 현금영수증 TID                                                                                   |
|              | orgTid      | String | O    | 30   | 연관된 원 승인/취소 거래 TID<br>부분취소시, 원 부분취소   거래건의 TID와 매핑됨<br>- 원거래를 부분취소 하면,   신규 TID가 채번되고,<br>채번된 부분취소 TID가   셋팅 됩니다.                                                             |
|              | status      | String | O    | 20   | 발급진행 상태<br>[발급]<br>issueRequested : 발급 접수 완료[1,3]<br>issueReqCancelled : 요청회수(국세청 발행 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>issued : 국세청 발급 완료[4]<br>issueFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10])<br>[취소]<br>cancelRequested : 취소 접수 완료[1,3]<br>cancelReqCancelled : 요청회수(국세청 취소 접수전   거래의 발급취소(배치 형태의 거래에서 발생[2])<br>cancelled : 국세청 취소 완료[4]<br>cancelFailed : 발급실패(제휴사(더빌) 실패[9] 또는 국세청 실패[10])                               |
|              | amount      | Int    | O    | 12   | 현금영수증 발행 총금액                                                                           |
|              | taxFreeAmt  | Int    | O    | 12   | 현금영수증 전체 금액중에서 면세금액                                                              |
|              | receiptType | String | O    | 20   | 현금영수증 타입<br>individual : 개인 소득공제용<br>company : 사업자 지출증빙용                                                                      |
|              | issueNo     | String | O    | 30   | 현금영수증 국세청 발행번호                                                                       |
|              | receiptUrl  | String | O    | 200  | 현금영수증 매출전표 확인 URL                                                                     |

<br>

### 가상계좌
| Parameter |              | Type   | 필수 | Byte | 설명                        |
|-----------|--------------|--------|------|------|-----------------------------|
| vbank     | 　           | Object | 　   | 　   | 가상계좌 정보               |
| 　        | vbankCode    | String | O    | 3    | 입금받을 가상계좌 은행코드  |
|           | vbankName    | String | O    | 20   | 입금받을 가상계좌 은행명    |
|           | vbankNumber  | String | O    | 20   | 입금받을 가상계좌 번호      |
|           | vbankExpDate | String | O    | -    | 가상계좌 입금 만료일<br>ISO 8601                    |
|           | vbankHolder  | String | O    | 40   | 입금받을 가상계좌 예금주명  |

<br>

### 취소
| Parameter |             | Type   | 필수 | 　Byte | 설명               |
|-----------|-------------|--------|------|--------|--------------------|
| cancels   | 　          | Array  | 　   | 　     | 취소/부분취소 내역 |
| 　        | tid         | String | O    | 30     | 승인 취소 거래번호 |
|           | amount      | Int    | O    | 12     | 취소금액           |
|           | cancelledAt | String | O    | -      | 취소된 시각<br>ISO 8601           |
|           | reason      | String | O    | 100    | 취소사유           |
|           | receiptUrl  | String | O    | 200    | 취소에 대한<br>매출전표 확인 URL  |
|           | couponAmt   | Int    | 　   | 12     | 쿠폰 취소금액      |

<br>

## 약관	
### Over-view
약관 조회 API는 결제 호출 전 사용자에게 노출 해야 하는 약관정보를 응답 합니다.  
나이스페이 결제창을 활용하지 않는 결제수단의 경우 약관 정보 API를 활용하여 사용자에게 약관을 고지해야 합니다. 

<br>

### 약관 조회 API 포함 약관
- 전자금융거래 약관
- 개인정보 수집 및 이용 약관
- 개인정보 제 3자 제공약관
- 통신과금서비스 이용약관

<br>

### 샘플 코드
```bash
curl -X GET 'https://api.nicepay.co.kr/v1/payments/nicuntct1m0101210727200125A056' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMT...'

```

<br>

### 요청 명세
```bash
POST /v1/terms HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```
| Parameter     | Type   | 필수 | Byte | 설명                                                |
|---------------|--------|------|------|-----------------------------------------------------|
| termsType     | String | O    | 50   | 약관 유형<br>ElectronicFinancialTransactions:전자금융거래   약관<br>CollectPersonalInfo:개인정보 수집 및 이용 약관<br>SharingPersonalInformation:개인정보 제 3자 제공약관<br>TelecommunicationCharging:통신과금서비스 이용약관   |
| returnCharSet | String | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                       |

<br>

### 응답 명세
```bash
POST
Content-type: application/json
```
| Parameter  | Type   | 필수 | Byte  | 상세 설명               |
|------------|--------|------|-------|-------------------------|
| resultCode | String | O    | 4     | 결과코드<br>0000 : 성공 / 그외 실패 |
| resultMsg  | String | O    | 100   | 결과메시지              |
| termsTitle | String | O    | 100   | 약관제목                |
| content    | String | O    | 30000 | 약관내용                |

<br>

## 카드 이벤트	
### Over-view
카드 이벤트 조회 API는 요청된 기준금액에 해당되는 카드사별 이벤트 정보를 응답 합니다.  
이벤트 정보를 결제자에게 전달하여 카드사 선택을 위한 정보를 편리하게 제공할 수 있습니다. 

> 기준금액이 5만원 이하 인 경우 무이자는 미제공하는 것으로 응답 됩니다. 

<br>

### 샘플 코드
```bash
curl -X GET 'https://api.nicepay.co.kr/v1/payments/nicuntct1m0101210727200125A056' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMT...'
```

<br>

### 요청 명세
```bash
POST /v1/card/event HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```
| Parameter     | Type | 필수 | 크기 | 설명                                                                                                      |
|---------------|------|------|------|-----------------------------------------------------------------------------------------------------------|
| amount        | N    | O    | 12   | 기준금액<br>기준금액에 해당하는 카드 이벤트 정보를 제공합니다.                                                        |
| useAuth       | B    | O    | -    | 인증 거래 여부<br>true : 인증 /   false : 비인증(빌링)                                                                      |
| ediDate       | S    | O    | -    | 전문생성일시<br>ISO 8601 형식                                                                                             |
| mid           | S    | 　   | 10   | 상점 MID<br>일반적으로 사용하지 않지만, mid가 요청된 경우, 최우선하여 제공.<br>(요청된 clientId하위 가맹점여부 검증 필수) |
| signData      | S    | 　   | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(ediDate + SecretKey))<br> - SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.                                                 |
| returnCharSet | S    | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                                                                             |

<br>

### 응답 명세
```bash
POST
Content-type: application/json

```
| Parameter  | Type   | 필수 | Byte | 설명                                                                 |
|------------|--------|------|------|----------------------------------------------------------------------|
| resultCode | String | O    | 4    | 결과코드<br>0000 : 성공 / 그외 실패                                              |
| resultMsg  | String | O    | 100  | 결과메시지                                                           |
| ediDate    | String | O    | -    | 응답전문생성일시<br>ISO 8601 형식                                                        |
| signature  | String | 　   | 256  | 위변조 검증 데이터<br>- 유효한 거래건에   한하여 응답<br>- 생성규칙 :   hex(sha256(ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.            |
| cardPoint  | String | 　   | 　   | 포인트 결제 지원 카드<br>-콜론(:)을 구분자로 카드코드 나열<br>-카드사포인트는 amount에 관계 없이 이용가능한 카드사정보 제공<br>ex) 01:02:04:07<br>- 설명 : BC,국민,삼성,현대 카드는 카드사포인트 사용 가능          |

<br>

### 무이자 할부정보
| Parameter        |                 | Type   | 필수 | Byte | 설명                                      |
|------------------|-----------------|--------|------|------|-------------------------------------------|
| interestFreeList | 　              | Array  | 　   | -    | 무이자 할부정보                           |
| 　               | cardCode        | String | O    | 3    | 카드사 코드<br>신용카드사별 코드                         |
|                  | cardName        | String | O    | 20   | 카드사 이름<br>예) 비씨                                  |
|                  | freeInstallment | String | O    | 200  | 무이자 할부개월<br>콜론(:)을 구분자로   할부개월 나열<br>ex) 02:03:04:05<br>- 설명 : 2,3,4,5개월 무이자 할부 제공 |

<br>

## 카드 무이자	
### Over-view
카드 무이자 조회 API는 카드사 무이자 정보를 응답 합니다.  
무이자 조회 API를 통해 무이자 결제가 가능한 카드사와 금액구간 정보를 확인 할 수 있습니다.  

<br>

### 샘플 코드
```bash

curl -X GET 'https://api.nicepay.co.kr/v1/payments/nicuntct1m0101210727200125A056' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMT...'

```

<br>

### 요청 명세
```bash
POST /v1/card/interest-free HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8

```
| Parameter     | Type    | 필수 | Byte | 설명                                                                                                      |
|---------------|---------|------|------|-----------------------------------------------------------------------------------------------------------|
| useAuth       | Boolean | O    | -    | 인증 거래 여부<br>true : 인증 /   false : 비인증(빌링)                                                                      |
| ediDate       | String  | O    | -    | 전문생성일시<br>ISO 8601 형식                                                                                             |
| mid           | String  | 　   | 10   | 상점 MID<br>일반적으로 사용하지 않지만, mid가 요청된 경우, 최우선하여 제공.(요청된 clientId하위 가맹점여부 검증 필수) |
| signData      | String  | 　   | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.|
| returnCharSet | String  | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr|

<br>

### 응답 명세
```bash
POST
Content-type: application/json

```
| Parameter  | Type   | 필수 | Byte | 설명                                                                 |
|------------|--------|------|------|----------------------------------------------------------------------|
| resultCode | String | O    | 4    | 결과코드<br>0000 : 성공 / 그외 실패                                              |
| resultMsg  | String | O    | 100  | 결과메시지                                                           |
| ediDate    | String | O    | -    | 응답전문생성일시<br>ISO 8601 형식                                                        |
| signature  | String | 　   | 256  | 위변조 검증 데이터<br>- 유효한 거래건에   한하여 응답<br>- 생성규칙 :   hex(sha256(ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.            |

#### 무이자 할부정보
| Parameter        |                 |             | Type   | 필수 | Byte | 설명                                  |
|------------------|-----------------|-------------|--------|------|------|---------------------------------------|
| interestFreeList |                 |             | Array  |      | -    | 무이자 할부정보                       |
|                  | cardCode        |             | String | O    | 3    | 카드사 코드<br>신용카드사별 코드                     |
|                  | cardName        |             | String | O    | 20   | 카드사 이름<br>예) 비씨                              |
|                  | freeInstallment |             | Array  | O    | -    | 무이자 할부 상세 정보                 |
|                  |                 | minAmt      | Int    | O    | 12   | 이벤트 적용 최소 금액<br>ex) 50000                             |
|                  |                 | maxAmt      | Int    | O    | 14   | 이벤트 적용 최대 금액<br>ex) 99999999999999                    |
|                  |                 | installment | String | O    | 100  | 무이자 할부개월<br>콜론(:)을 구분자로 할부개월 나열<br>ex) 02:03:04:05<br>- 설명 : 2,3,4,5개월 무이자 할부 제공 |
|                  |                 | eventToDate | String | O    | -    | 이벤트 제공 기한<br>ISO 8601 형식                         |


<br>

## 더 알아보기
결제 개발을 위해 더 상세한 정보가 필요하다면 `공통` 탭의 정보를 활용하고,  
API 개발을 위한 각 인터페이스의 개발 명세가 필요하다면 `문서` 탭의 자료를 확인 해주세요.  
개발이 완료되어 운영에 필요한 정보와 Tip은 `운영` 탭의 정보를 통해 확인이 가능 합니다. 

### 📌 공통
개발 전 필요한 `공통`적인 가이드 입니다.  
[개발 준비](../common/preparations.md) | [API·JS SDK](../common/api.md) | [TEST·샘플코드](../common/test.md) | [코드집](../common/code.md)
  
### 📚 문서
`API 명세`와 `코드`가 포함된 기술문서 입니다.  
[결제·발급](./payment.md) | [조회](./status.md) | [정산·대사](./reconciliation.md) | [취소·환불](./cancel.md) | [웹훅](./api/hook.md) | [APP](./api/app.md)

### ☸️ 운영
`운영`에 필요한 정보 입니다.  
[지원환경](../management/user.md) | [오류관리](../management/user.md) | [개발정보](../management/admin.md)
