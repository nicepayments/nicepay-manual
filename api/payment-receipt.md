# 현금영수증	

[현금영수증 발급](#현금영수증-발급) | [현금영수증 취소](#현금영수증-취소) | [현금영수증 조회](#현금영수증-조회) | [더 알아보기](#더-알아보기)

<br>

## 현금영수증 발급
### Over-view
<img src="../image/payment-receipt-issue.svg" width="800px">

### 설명
현금영수증은 [발급](#현금영수증-발급), [취소](#현금영수증-취소), [조회](#현금영수증-조회) 과정을 통해 관리가 가능 합니다.  
현금영수증 발급요청이 성공하면 정보는 다음날 국세청으로 전달되고 현금영수증 발급을 처리를 진행 합니다.  
국세청의 발급 처리 기간을 고려하여 현금영수증 발급 요청 성공 ⏱️ D+2일 기준으로 [현금영수증 조회](#현금영수증-조회)를 처리하면 현금영수증 발급(승인)여부를 확인 할 수 있습니다.  
현금영수증 발급 요청은 결제자 정보 및 유형을 `v1/receipt/` API로 전달 하는 것으로 완료 됩니다.  

<br>

> #### ⚠️ 중요  
> 현금영수증 발급요청 성공은 국세청으로 현금영수증 데이터 전달을 위한 요청이 완료 되었음을 의미 합니다.  
> 국세청으로 발급처리 요청과 발급여부 조회까지의 시간간격은 영업일 기준 최대 ⏱️ D+2일 발생합니다.

<br>

### 샘플 코드
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

<br>

### 요청 명세 (Body)
``` bash
POST /v1/receipt/ HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials> or Bearer <token>
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

<br>


### 응답 명세 (Body)
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

<br>

## 현금영수증 취소

### Over-view
<img src="../image/payment-receipt-cancel.svg" width="800px">

### 설명
현금영수증 취소는 현금영수증 발급 성공 건의 취소를 의미 합니다.  
현금영수증 취소 요청은 현금영수증 발급요청 성공시 응답받은 tid와 취소 금액을 `/v1/receipt/{tid}/cancel` API에 전달하는 것으로 처리 됩니다.

<br>

> #### ⚠️ 중요  
> 현금영수증 취소요청 성공은 국세청으로 현금영수증 취소 데이터 전달을 위한 요청이 완료 되었음을 의미 합니다.   
> 국세청으로 취소처리 요청과 조회까지의 시간간격은 영업일 기준 최대 ⏱️ D+2일 발생합니다.  

<br>

### 샘플 코드
``` bash
curl -X POST 'https://api.nicepay.co.kr/v1/receipt/nicuntct1m04012107272036221413/cancel' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMTQ4M2...' 
-D '{
    "orderId" : “merchant-order-id",
    "reason" : “sample-code"
}'
```

<br>

### 요청 명세 (Body)
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

<br>

### 응답 명세 (Body)
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

<br>

## 현금영수증 조회
### Over-view
<img src="../image/payment-receipt-get.svg" width="800px">  

### 설명
현금영수증 조회는 현금영수증 요청 건의 조회를 의미 합니다.  
현금영수증 발급요청 성공시 응답받은 tid `/v1/receipt/{tid}` API에 전달하는 것으로 조회 처리 됩니다.

<br>

> #### ⚠️ 중요  
> 국세청으로 발급처리 요청과 발급여부 조회까지의 시간간격은 영업일 기준 최대 ⏱️ D+2일 발생합니다.  

<br>

### 샘플 코드
``` bash
curl -X GET 'https://api.nicepay.co.kr/v1/receipt/nicuntct1m04012107272036221413' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMTQ4M2...' 
```

<br>

### 요청 명세 (Body)
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

<br>

### 응답 명세 (Body)
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
