## 카드 이벤트

[카드 이벤트 조회](#카드-이벤트) | [더 알아보기](#더-알아보기)

<br>

## Over-view
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

## 요청 명세
```bash
POST /v1/card/event   
HTTP/1.1  
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

## 응답 명세
```bash
POST
Content-type: application/json

```
| Parameter  | Type   | 필수 | Byte | 설명                                                                 |
|------------|--------|------|------|----------------------------------------------------------------------|
| resultCode | String | O    | 4    | 결과코드<br>0000 : 성공 / 그외 실패                                              |
| resultMsg  | String | O    | 100  | 결과메시지                                                           |
| ediDate    | String |     | -    | 응답전문생성일시<br>ISO 8601 형식                                                        |
| signature  | String | 　   | 256  | 위변조 검증 데이터<br>- 유효한 거래건에   한하여 응답<br>- 생성규칙 :   hex(sha256(ediDate+ SecretKey))<br>- 데이터 유효성 검증을 위해, 가맹점 수준에서 비교하는 로직 구현 권고<br>- SecretKey는 가맹점관리자에 로그인 하여 확인 가능합니다.            |
| cardPoint  | String | 　   | 　   | 포인트 결제 지원 카드<br>-콜론(:)을 구분자로 카드코드 나열<br>-카드사포인트는 amount에 관계 없이 이용가능한 카드사정보 제공<br>ex) 01:02:04:07<br>- 설명 : BC,국민,삼성,현대 카드는 카드사포인트 사용 가능          |


### 무이자 할부정보 <img src="https://img.shields.io/badge/-Array-blueviolet"> 

| Parameter        |                 | Type   | 필수 | Byte | 설명                                  |
|------------------|-----------------|--------|------|------|---------------------------------------|
| interestFreet |                 | Array  |      | -    | 제공되는 모든 무이자 할부정보<br>- NICEPAY에서 기본제공하는 무이자와 상점무이자가 merge된 정보<br>- 카드코드별 하나의 무이자 Object가 응답됩니다.                     |
|                  | cardCode        | String | O    | 3    | 카드사 코드<br> 신용카드사별 코드|
|                  | cardName        | String | O    | 20   | 카드사 이름<br>예) 비씨                           |
|                  | freeInstallment | String | O    | 200  | 무이자 할부개월 <br>콜론(:)을 구분자로 할부개월 나열<br>ex) 02:03:04:05<br>- 설명 : 2,3,4,5개월 무이자 할부 제공    |

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
