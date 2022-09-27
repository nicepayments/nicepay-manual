# 취소·환불·망취소

[취소·환불](#취소환불) | [망 취소](#망취소) | [더 알아보기](#더-알아보기)

<br>

## 취소·환불
### Over-view
💳 결제(승인)이 완료된 거래의 취소 및 환불에 대한 가이드 입니다.  
카드와 같은 비 현금성 결제의 경우 결제(승인) 완료 시 응답된 tid를 취소 API `v1/payments/{tid}/cancel`에 POST 하는 것으로 처리가 됩니다.  
가상계좌와 같은 현금성 거래는 취소 API에 환불계좌 정보를 추가 전달 하는 것으로 처리가 됩니다.  

<br>

### 결제수단별 취소/환불 
| 결제수단              | 전체취소 | 부분취소 | 전체환불 | 부분환불 | 취소 가능 기간 |
|-----------------------|----------|----------|----------|----------|----------------|
| 카드결제              | O        | O        |          |          | 1년 내         |
| 가상계좌 (발급 후)    | O        |          |          |          | 입금 만료 전   |
| 가상계좌 (입금 후)    |          |          | O        | O        | 180일          |
| 현금영수증            | O        | O        |          |          | 발급 당해 년도 |
| 에스크로(배송등록 전) | O        |          |          |          | -              |
| 에스크로(배승등록 후) | O        |          |          |          |           -     |
| 에스크로(구매결정 후) | 불가     |   불가  |   불가  |     불가  |      -          |
| 에스크로(구매거절 후) | O        |          | O        |          |       -         |

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
| Parameter      | Type   | 필수 | Byte | 설명                                                      |
|----------------|--------|------|------|-----------------------------------------------------------|
| reason         | String | O    | 100  | 취소사유                                                  |
| orderId        | String | O    | 64   | 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br>-부분취소의 경우 중복된 orderId로 재호출 불가             |
| cancelAmt      | Int    |      | 12   | 부분)취소요청금액<br>값이 누락이면 전액취소                                    |
| mallReserved   | String |      | 500  | 상점 예약필드<br>상점 정보 전달용 예비필드                                 |
| ediDate        | String |      | -    | 전문생성일시<br>ISO 8601 형식                                             |
| signData       | String |      | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(tid + ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다. |
| returnCharSet  | String |      | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                             |
| taxFreeAmt     | Int    |      | 12   | 취소금액중 면세공급가액<br>취소금액(amount)중에서 면세에 해당하는 금액을 설정합니다. |
| refundAccount  | String |      | 16   | 환불계좌번호                                              |
| refundBankCode | String |      | 3    | 환불계좌코드                                              |
| refundHolder   | String |      | 10   | 환불계좌 예금주명                                         |

<br>

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

### 할인 정보 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

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

### 현금영수증 <img src="https://img.shields.io/badge/-Array-blueviolet"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

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

### 취소 <img src="https://img.shields.io/badge/-Array-blueviolet"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

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

## 망취소
### Over-view
결제 연동 시 네트워크 순단 혹은 `HTTP client`의 `Read-timeout`으로 결제(승인) 결과가 불확실하다면  
망취소 API를 호출하여 문제거래를 취소 해야 합니다.  
이러한 예외 처리를 통해 데이터 미 매칭의 불확실성을 해소 할 수 있습니다.  
사용 중인 결제(승인) 모델을 확인 후 예외 구간의 망취소 구현을 권장 합니다.  

<br>

### 결제창 (Server 승인 모델) 의 망취소 구현
<img src="../image/netcancel-server-authorization.svg" width="800px">   

<br>

### 결제창 (Client 승인 모델) 의 망취소 구현
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

| Parameter     | Type   | 필수 | Byte | 설명                                                      |
|---------------|--------|------|------|-----------------------------------------------------------|
| orderId       | String | O    | 64   | 취소할 상점 거래 고유번호<br>가맹점에서 관리하는 Unique한 주문번호 또는 결제번호<br>-orderId가 unique한 경우에만 정상 처리됩니다.             |
| mallReserved  | String |      | 500  | 상점 예약필드<br>상점 정보 전달용 예비필드                                 |
| ediDate       | String |      | -    | 전문생성일시<br>ISO 8601 형식                                             |
| signData      | String |      | 256  | 위변조 검증 Data<br>생성규칙 : hex(sha256(orderId + ediDate + SecretKey))<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다. |
| returnCharSet | String |      | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                             |

<br>

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

### 할인 정보 <img src="https://img.shields.io/badge/-Object-yellow"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

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

### 현금영수증 <img src="https://img.shields.io/badge/-Array-blueviolet"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

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

### 취소 <img src="https://img.shields.io/badge/-Array-blueviolet"> <img src="https://img.shields.io/badge/-nullable-lightgrey">

| Parameter |             | Type   | 필수 | 　Byte | 설명               |
|-----------|-------------|--------|------|--------|--------------------|
| cancels   | 　          | Array  | 　   | 　     | 취소/부분취소 내역 |
| 　        | tid         | String | O    | 30     | 승인 취소 거래번호 |
|           | amount      | Int    | O    | 12     | 취소금액           |
|           | cancelledAt | String | O    | -      | 취소된 시각<br>ISO 8601           |
|           | reason      | String | O    | 100    | 취소사유           |
|           | receiptUrl  | String | O    | 200    | 취소에 대한<br>매출전표 확인 URL  |
|           | couponAmt   | Int    | 　   | 12     | 쿠폰 취소금액      |

  
  
  
  
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
