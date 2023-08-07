# 지원환경

[개발환경](#개발환경) | [지원 브라우저](#브라우저) | [오류관리](#오류관리) | [더 알아보기](#더-알아보기)

<br>

## 개발환경	
나이스페이는 API를 활용하기 위해 HTTP 클라이언트는 `TLS 1.2` 대응이 가능해야 하며,  
모던한 개발환경 지원을 위해 다양한 옵션과 편의성을 제공 하고 있습니다.  

- 다양한 개발언어 지원
- node.js, python, ruby, jsp, php, classic asp, .net
- REST API
- HTTP Status code
- JS SDK를 통한 결제창 승인방식 옵션 👉[JS SDK 바로가기](/api/payment.md#js-sdk)
- 원천사 응답코드 👉[API 응답코드 바로가기](/common/code.md#api-응답코드)
- HTTP 클라이언트 `TLS 1.2`
- [웹훅](/management/admin.md#기능설명-2)
- [웹 로그를 통한 디버깅](/management/admin.md#기능설명-3)
- 샌드박스를 활요한 TEST 및 리포팅 👉[개발정보 활용 바로가기](/management/admin.md#활용)

<br>

## 브라우저	
나이스페이 결제창은 `HTML5` 기반 PC/Mobile 브라우저에서 활용이 가능하도록 개발 되었습니다.  
또한 가맹점의 결제창 연동시 활용되는 JS SDK가 브라우저를 판단하여 결제창을 노출 하기 때문에  
한번의 개발로 PC/Mobile 대응이 가능한 장점이 있습니다.  

<br>

### PC 지원 브라우저
|            | Chrome | Firefox | IE 9 이상 | Opera | Whale | Edge | Safari |
|------------|--------|---------|-----------|-------|-------|------|--------|
| Windows XP | O      | O       | O         | *     | *     | *    | *      |
| Windows 7  | O      | O       | O         | O     | O     | *    | *      |
| Windows 8  | O      | O       | O         | O     | O     | *    | *      |
| Windows 10 | O      | O       | O         | O     | O     | O    | *      |
| Windows 11 | O      | O       | O         | O     | O     | O    | *      |
| Mac-OSX    | O      | O       | *         | O     | O     | O    | O      |

&ast;OS가 지원하지 않음  

<br>

### Mobile 지원 브라우저
| App      | 분류     | 앱 이름      | 지원여부 |
|----------|----------|--------------|----------|
| naver    | 브라우저 | naver        | O        |
| daum     | 브라우저 | daum         | O        |
| google   | 브라우저 | google       | O        |
| telegram | 메신저   | 텔레그램     | O        |
| naver    | 메신저   | 밴드         | O        |
| naver    | 메신저   | line         | O        |
| kakao    | 메신저   | 카카오톡     | O        |
| kakao    | SNS      | 카카오스토리 | O        |
| facebook | SNS      | 페이스북     | O        |

<br>

# 오류관리


## 시스템 오류의 대응
나이스페이 시스템 혹은 원천사 시스템의 문제에 의해 결제오류가 발견되는 사항으로,  
대부분 모니터링 시스템에 의해 오류 확인 즉시 대응 되며 가맹점이 별도 대응을 하지 않아도 무관합니다.  
대응 방식은 💡 결제창의 공지, 해당 결제수단의 노출 제한을 통한 다른 결제방식 유도, 가맹점 공지 등이 있습니다.  

<br>

## 결제고객 오류
나이스페이 모니터링 팀은 시스템과 결제고객의 오류를 감지하고 대응하기 위해 ⏱️ 24/7 365일 운영이 가능한 관제시스템을 유지하고 있습니다.  
결제고객이 결제를 진행 하는 과정에서 발생 가능한 오류는 크게 시스템적인 오류(나이스페이의 시스템 혹은 원천사의 시스템)와  
사용자 환경 오류(기기, 브라우저, 결제수단의 제약)으로 나누어 분류 할 수 있습니다.  

<br>

### 사용자 환경 오류의 대응
대부분 결제고객의 오류는 환경적인 요인에 의해 발생되며 각 인터페이스에서 대응이 가능한 오류코드와 메시지를 응답 하고 있습니다.  
상세한 대응은 [FAQ](https://start.nicepay.co.kr/homepage/fnq.do)를 통해 확인이 가능 합니다.  

<br>

> #### 결제창 호출이 되지 않는 경우
> JS SDK Include가 정상인지 Include를 위한 도메인에 접근이 가능한 네크워크 환경 구성인지 체크가 필요하며,  
> 결제자의 브라우저에서 java-script 허용, 쿠키 허용으로 옵션이 적용되어 있는지 체크가 필요 합니다.  

<br>
  
> #### 결제창 호출 후 버튼 동작이 정상적이지 않은 경우
> JS SDK을 iframe에서 호출되는 경우 문제가 발생할 수 있으며 [JS SDK 옵션](/api/payment.md#js-sdk)을 통해 문제를 검토 합니다.  

<br>

> #### 결제창 호출 후 카드사 인증을 완료 했으나 결제(승인)이 발생되지 않은 경우
> 결제자가 결제창을 통해 원천사 접근 후 인증과정 진행 과정에서 문제가 발생된 경우로  
> 해당 결제수단의 원천사를 통한 지원이 필요한 경우가 있습니다.  
> 또한 Server승인 모델 결제창을 사용하는 경우 승인 API가 정상적으로 호출 되었는지 체크 해주세요.

<br>
   
> #### 결제(승인)은 완료 했으나 오류가 발생된 경우
> 결과 코드와 메시지를 통해 대부분 사유 확인이 가능하며 대응이 어려운 경우 거래 tid와 함께 1:1문의를 남겨주세요.  


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
