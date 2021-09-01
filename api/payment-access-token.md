


## Access token

### Over-view
<img src="../image/payment-token.svg" width="800px">

### 활용
[Bearer token](../common/api.md#bearer-token)방식 authorization을 활용하여 API를 호출하는 경우 활용 합니다.

<br>

> #### ⚠️ 중요  
> [시크릿 키](../common/api.md#시크릿-키)를 [Basic auth](,,/common/api.md#basic-auth) 방식으로 생성한 경우 API 호출시 token 관리는 생략 할 수 있습니다.

<br>

### 샘플 코드
```bash
curl -X POST "https://api.nicepay.co.kr/v1/access-token" 
-H "Content-Type: application/json" 
-H "Authorization: Basic YWYwZDExNjIzNmRm..."
```

<br>

### 요청 명세 (Body)
```bash
POST /v1/access-token HTTP/1.1
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```
|   Parameter  | type        |    필수    | byte |                             설명                           |
|:------------:|:-----------:|:----------:|:----:|:-----------------------------------------------------------| 
| returnCharSet|  String     |            |   10 | 응답 파라메터 인코딩 방식<br> 값: utf-8/euc-kr <br> Default:utf-7  |

<br>

### 응답 명세 (Body)
```bash
POST
Content-type: application/json
```
|   Parameter  | type        |    필수    | byte |                             설명                           |
|:------------:|:-----------:|:----------:|:----:|:-----------------------------------------------------------| 
| resultCode  |  String     |     O      |   4  | 결과코드<br>0000: 성공/그외 실패  |
| resultMsg   |  String     |     O      |   100 | 결과 메시지 |
| accessToken |  String     |     O      |   40  | access token  |
| tokenType   |  String     |     O      |   10  | 인증 스킴 유형<br> Bearer 고정  |
| expiredAt   |  String     |     O      |       | Token 만료 시각<br>ISO 8601 형식  |
| now         |  String     |     O      |       | 현재 시각<br> ISO 8601 형식  |
  
  
  
  
  
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
