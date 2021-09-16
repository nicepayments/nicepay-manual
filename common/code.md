# 코드집

[HTTP-상태코드](#http-상태코드) | [카드코드](#카드코드) | [은행코드](#은행코드) | [더 알아보기](#더-알아보기)

<!--
[HTTP-상태코드](#http-상태코드) | [카드코드](#카드코드) | [은행코드](#은행코드) | [JS SDK 응답코드](#js-sdk-응답코드) | [API 응답코드](#api-응답코드) | [더 알아보기](#더-알아보기)
-->

<br>

## HTTP 상태코드
|http status|설명|
|:---:|:--|
|200|OK, 요청이 정상 처리된 경우|
|400|Bad Request, 입력 파라미터가 없거나 유효하지않은 값일 경우|
|401|Unauthorized, SecretKey 또는 토큰 없거나 인증에 실패한 경우|
|403|Forbidden,|
|404|Not Found, 요청한 리소스가 존재하지 않는 경우|
|500|Server Error, 나이스페이먼츠 서버에 오류가 발생한 경우|

<br>
  
## 카드코드
| 코드 | 한글         | 영문         | 결제창                    | 대표 웹 사이트                   |
|:------:|:--------------|:--------------|:---------------------------:|:----------------------------------|
| 01    | 비씨         | BC           | O                         | https://www.bccard.com/          |
| 02    | KB국민       | KB Kookmin   | O                         | https://card.kbcard.com/         |
| 03    | 하나(외환)   | KEB Bank     | O                         | https://www.hanacard.co.kr/      |
| 04    | 삼성         | SAMSUNG      | O                         | https://www.samsungcard.com/     |
| 06    | 신한         | SHINHAN      | O                         | https://www.shinhancard.com/     |
| 07    | 현대         | HYUNDAI      | O                         | https://www.hyundaicard.com/     |
| 08    | 롯데         | LOTTE        | O                         | https://www.lottecard.co.kr/     |
| 11   | 씨티         | CITI         | O                         | https://www.citibank.co.kr/      |
| 12   | NH채움       | NH           | O                         | https://card.nonghyup.com/       |
| 13   | 수협         | SUHYUP       | O                         | https://www.suhyup-bank.com/     |
| 14   | 신협         | SHINHYUP     | O                         | http://www.cu.co.kr/             |
| 15   | 우리         | WOORI        | O                         | https://pc.wooricard.com/        |
| 16   | 하나         | HANA SK      | O                         | https://www.hanacard.co.kr/      |
| 21   | 광주         | KWANGJU      | O                         | https://pib.kjbank.com/          |
| 22   | 전북         | JEONBUK      | O                         | https://www.jbbank.co.kr/        |
| 23   | 제주         | JEJU         | O                         | http://tamna.jeju.go.kr/         |
| 24   | 산은캐피탈   | KDB Capital  | O                         | https://www.kdbc.co.kr/cardhome  |
| 25   | 해외비자     | VISA         | O                         | https://www.visakorea.com/       |
| 26   | 해외마스터   | MASTER       | O                         | https://www.mastercard.us/       |
| 27   | 해외다이너스 | DINERS       | O                         | https://www.dinersclub.com/      |
| 28   | 해외AMX      | AMEX         | O                         | https://www.americanexpress.com/ |
| 29   | 해외JCB      | JCB          | O                         | https://www.jcb.co.jp/           |
| 31   | SK-OKCashBag | SK-OKCashBag | |https://www.okcashbag.com |                                  
| 32   | 우체국       | Post         | O                         | https://www.epostbank.go.kr/     |
| 33   | 저축은행     | Savings Bank | O                         | http://sbcheck.bccard.com/       |
| 34   | 은련         | UnionPay     | O                         | https://www.unionpayintl.com/    |
| 35   | 새마을금고   | MG           | O                         | https://www.kfcc.co.kr/          |
| 36   | KDB산업      | KDB Bank     | O                         | https://www.kdb.co.kr/           |
| 37   | 카카오뱅크   | Kakao Bank   | O                         | https://www.kakaobank.com/       |
| 38   | 케이뱅크     | KBank        | |https://www.kbanknow.com/ |                                  
| 39   | 페이코포인트 | PAYCO        | O                         | https://www.payco.com/           |
| 40   | 카카오머니   | KAKAO        | O                         | https://www.kakaopay.com/        |
| 41   | SSG머니      | SSG          | O                         | https://www.ssgpay.com/          |
| 42   | 네이버포인트 | NAVER        | O                         | https://www.naverfincorp.com/    |

<br>

## 은행코드
| 코드 |        한글       |                                                             영문 | 가상계좌발급                 | 대표 웹 사이트                       |
|------|:-----------------:|:-----------------------------------------------------------------|:------------------------------:|:--------------------------------------|
| 001    |      한국은행     |                                                    Bank of Korea | |http://www.bok.or.kr/        |                                      
| 002    |      산업은행     |                                                         KDB Bank | |https://www.kdb.co.kr/       |                                      
| 003    |      기업은행     |                                                              IBK | O                            | https://www.ibk.co.kr/               |
| 004    | 국민은행          | Kookmin Bank                                                     | O                            | https://www.kbstar.com/              |
| 005    | 외환은행          | Korea Exchange Bank                                              | O                            | https://www.kebhana.com/             |
| 007    | 수협중앙회        | Suhyup Federation                                                | |https://www.suhyup.co.kr/    | https://www.kebhana.com/             |
| 008    | 수출입은행        | The Export-Import Bank of Korea                                  | |https://www.koreaexim.go.kr/ |                                      |
| 011   | 농협중앙회        | National Agricultural Cooperative Federation                     | O                            | https://www.nonghyup.com/            |
| 012   | 농협회원조합      | National Agricultural Cooperative Federation of Members          | |https://www.nonghyup.com/    | https://www.nonghyup.com/            |
| 020   | 우리은행          | WooriBank                                                        | O                            | https://www.wooribank.com/           |
| 023   | SC은행            | SCBank                                                           | O                            | https://www.standardchartered.co.kr/ |
| 026   | 서울은행          | Seoul Bank                                                       | |https://www.kebhana.com/     
| 027   | 한국씨티은행      | Korea city Bank                                                  | |https://www.citibank.co.kr/  |                                      
| 031   | 대구은행          | Daegu Bank                                                       | O                            | https://www.dgb.co.kr/               |
| 032   | 부산은행          | Busan Bank                                                       | O                            | https://www.busanbank.co.kr/         |
| 034   | 광주은행          | KwangjuBank                                                      | O                            | https://pib.kjbank.com/              |
| 035   | 제주은행          | Jeju Bank                                                        | |https://www.e-jejubank.com/  | 
| 037   | 전북은행          | JeonBuk Bank                                                     | |https://www.jbbank.co.kr/    |                                      
| 039   | 경남은행          | Kyongnam Bank                                                    | |https://www.knbank.co.kr/    |                                      
| 045   | 새마을금고연합회  | KFCC Federation                                                  | |https://www.kfcc.co.kr/      |                                      
| 048   | 신협중앙회        | National Credit Union Federation of Korea                        | |http://www.cu.co.kr/         |                                      
| 050   | 상호저축은행      | Mutual Savings Bank                                              | |https://www.fsb.or.kr/       |                                      
| 071   | 정보통신부 우체국 | Postal Savings for the Ministry of Information and Communication | O                            | https://www.epostbank.go.kr/         |
| 081   | 하나은행          | HanaBank                                                         | O                            | https://www.kebhana.com/             |
| 088   | 신한은행          | ShinhanBank                                                      | O                            | https://www.shinhan.com/             |
| 089   | 케이뱅크          | K Bank                                                           | O                            | https://www.kbanknow.com/            |
| 090   | 카카오뱅크        | Kakao Bank                                                       | |https://www.kakaobank.com/   | 

<br>

<!--

## JS SDK 응답코드
|구분|코드|메시지|
|:---:|:---:|:---|
|     |     |    |

<br>
  
## API 응답코드

|구분|코드|메시지|
|:---:|:---:|:---|
|     |     |    |

<br>

-->
    
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
