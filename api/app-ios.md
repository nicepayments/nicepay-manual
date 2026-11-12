# iOS
[iOS](#ios) | [iOS Swift](#ios-swift-웹뷰web-view개발-가이드) | [iOS Objective-c](#ios-objective-c-웹뷰web-view개발-가이드) | [더 알아보기](#더-알아보기)

<br>

## 공통사항
App 내 웹뷰를 통해 결제창을 연동하는 경우, 웹 환경에서 결제창을 통한 💳 결제(승인)이 가능하도록 개발이 선행 되어야 합니다.  
이 후 appScheme 값을 설정 합니다.  
카드사를 포함한 제휴사 인증 완료 후 전달된 가맹점 APP의 scheme을 확인하여 화면 focus가 이동 하게 됩니다.  

<br>

### 지원환경
- IOS 9.0 이상 
- Xcode 7.x 이상
- Swift 4.0 이상

<br>

### 개발흐름
결제창을 App내 에서 구현하는 경우 웹뷰(Web-view)를 통해 구현 처리가 가능 합니다.  
빠른 개발 진행을 원하는 경우 샘플코드를 검토 후 가이드 확인을 권장 합니다.  

- 결제창 호출시 appScheme 값 셋팅 
- 환경 설정
- URL Scheme 설정
- 예외처리 (java-script, 네트워크)

<br>

>#### ⚠️ 중요
>가맹점 결제 요청 페이지 로드 실패 하는 경우 가맹점 페이지가 HTTP 라면 `info.plist` 내 네트워크 🔒 보안 예외 설정을 확인(ATS) 해주세요.  
>3rd 어플리케이션 호출 불가한 경우 `info.plist` 내 `3rd URL Scheme` 설정을 확인 해주세요.  
>3rd 어플리케이션에서 인증 or 결제 완료 후 가맹점 어플리케이션으로 미전환시 `info.plist` 내 가맹점 URL Scheme 설정을 확인해 주세요.  
>결제 완료 후 웹 브라우저 호출이 되지 않는 경우 `info.plist` 내 가맹점 URL Scheme 설정 값과 결제창 JS SDK로 전달된 appScheme 값이 일치하는지 체크 해주세요.  
>팝업창 미노출 되는 경우 웹뷰의 자바스크립트 오버라이딩 함수 재정를 해주세요.  

<br>

### appScheme 설정- Server 승인 모델
```html
<script src="https://pay.nicepay.co.kr/v1/js/"></script> //Server 승인 
<script>
function serverAuth() {
  AUTHNICE.requestPay({
	clientId: 'af0d116236df437f831483ee9c500bc4',
        appScheme: `nicepaysample://`,
	method: 'vbank',
	orderId: 'your-unique-orderid',
	amount: 1004,
	goodsName: '나이스페이-상품',
	returnUrl: 'http://localhost:4567/serverAuth'
 });
}
</script>
```

<br>

### appScheme 설정 - Client 승인 모델

```html
<script src="https://pay.nicepay.co.kr/v1/js/"></script> //Client 승인 
<script>
function serverAuth() {
  AUTHNICE.requestPay({
	clientId: 'af0d116236df437f831483ee9c500bc4',
        appScheme: `nicepaysample://`,
	method: 'vbank',
	orderId: 'your-unique-orderid',
	amount: 1004,
	goodsName: '나이스페이-상품',
	returnUrl: 'http://localhost:4567/serverAuth'
 });
}
</script>
```

<br>

### URL Scheme 설정
- 가맹점 어플리케이션에 URL Scheme 을 등록합니다. (JS SDK 호출시 appScheme 필드 값으로 URL Scheme 사용)
- `Info.plist` 파일에 URL Scheme을 등록 합니다. (3rd 어플리케이션 -> 가맹점 어플리케이션 호출)
```bash
info.plist
```
```xml
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleURLName</key>
            <string>kr.co.nicepay.swift.NicepayAppSample</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <string>nicepaysample</string>
        </array>
    </dict>
</array>
```

<br>

> #### ⚠️ 중요
> `info.plist` 파일에 URL Scheme 미설정 시 특정 3rd 어플리케이션에서 인증 or 결제 완료 후 가맹점 어플리케이션으로 자동 전환이 불가 합니다.

<br>

### 3rd 어플리케이션 URL Scheme 등록
- `info.plist` 파일에 `3rd URL Scheme`을 등록 합니다. (가맹점 어플리케이션 -> 3rd 어플리케이션 호출)
- URL Scheme 미설정 시3rd 어플리케이션 연동이 불가 합니다.
```bash
info.plist
```
```xml
<key>LSApplicationQueriesSchemes</key>
<array>
    <string>kftc-bankpay</string>
    <string>ispmobile</string>
    <string>shinhan-sr-ansimclick</string>
    <string>smshinhanansimclick</string>
    <string>hdcardappcardansimclick</string>
    <string>smhyundaiansimclick</string>
    <string>mpocket.online.ansimclick</string>
    <string>scardcertiapp</string>
    <string>cloudpay</string>
    <string>nhappcardansimclick</string>
    <string>nonghyupcardansimclick</string>
    <string>kb-acp</string>
    <string>lotteappcard</string>
    <string>lottesmartpay</string>
    <string>citispay</string>
    <string>shinsegaeeasypayment</string>
    <string>kakaotalk</string>
    <string>tswansimclick</string>
    <string>nhallonepayansimclick</string>
    <string>citimobileapp</string>
    <string>payco</string>
    <string>hanaskcardmobileportal</string>
    <string>wooripay</string>
   <string>com.wooricard.wcard</string>
    <string>lpayapp</string>
    <string>hanawalletmembers</string>
    <string>tauthlink</string>
    <string>ktauthexternalcall</string>
    <string>upluscorporation</string>
    <string>liivbank</string>
   <string>kb-bankpay</string>
   <string>naversearchthirdlogin</string>
   <string>lmslpay</string>
</array>

```

<br>

### 3rd URL Scheme 리스트
| APP                       | SCHEME                       |
|---------------------------|------------------------------|
| 신한 앱카드 결제          | shinhan-sr-ansimclick://     |
| 신한카드 일반결제         | smshinhanansimclick://       |
| 현대 앱카드 결제          | hdcardappcardansimclick://   |
| 현대카드 일반결제         | smhyundaiansimclick://       |
| 삼성 앱카드 결제          | mpocket.online.ansimclick:// |
| 삼성카드 일반결제         | scardcertiapp://             |
| 하나 앱카드 결제          | cloudpay://                  |
| 농협 앱카드 결제          | nhappcardansimclick://       |
| 농협카드 일반결제         | nonghyupcardansimclick://    |
| KB 앱카드 결제(KB Pay)    | kb-acp://                    |
| 롯데 앱카드 결제          | lotteappcard://              |
| 롯데카드 스마트결제       | lottesmartpay://             |
| 롯데카드 LPAY             | lpayapp://                   |
| 시티 앱카드 결제          | citispay://                  |
| ISP 인증결제              | ispmobile://                 |
| SSG-PAY 결제              | shinsegaeeasypayment://      |
| 시럽페이                  | tswansimclick://             |
| 농협카드 올원페이 결제    | nhallonepayansimclick://     |
| 시티 앱카드 모바일 결제   | citimobileapp://             |
| 페이코                    | payco://                     |
| 카카오페이                | kakaotalk://                 |
| 하나카드 일반결제         | hanaskcardmobileportal://    |
| 우리 앱카드 결제          | wooripay://                  |
| 우리 앱카드 결제(리뉴얼)  | com.wooricard.wcard://       |
| 하나멤버스 월렛           | hanawalletmembers://         |
| SKT 본인인증(PASS) APP    | tauthlink://                 |
| KT 본인인증(PASS) APP     | ktauthexternalcall://        |
| LG U+ 본인인증(PASS)  APP | upluscorporation://          |
| 네이버페이 앱 로그인      | naversearchthirdlogin://     |
| LPAY 앱                   | lmslpay://                   |
| 뱅크페이(금융결제원)      | kftc-bankpay://              |
| KB-리브페이               | liivbank://                  |
| KB 계좌이체 APP           | kb-bankpay://                |

<br>

### 네트워크 보안 예외 설정
- HTTP 또는 유효하지 않은 인증서를 가진 HTTPS 연결 시 예외 처리입니다. 
- Apple에서는 하기와 같은 방법을 권장하지 않으며, 특정 도메인에 대해서만 예외 처리하도록 권장 합니다.

<br>

```bash
info.plist
```
```xml
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

<br>

## iOS-Swift 웹뷰(web-view)개발 가이드
### 결제 페이지 호출
- 웹뷰의 load를 통해 결제 요청 URL을 호출 합니다. 가맹점 결제 요청 웹 페이지 예시
```bash
swift
```
```swift
override func viewDidLoad() {
        super.viewDidLoad()
 
        title = "구매하기 TEST"
        
        webView = WKWebView(frame: self.view.frame)
        webView?.navigationDelegate = self
        webView?.uiDelegate = self
        self.view.addSubview(webView!)
        
        let url = URL(string: PAY_URL)
        let request = URLRequest(url: url!)
        webView?.load(request)
 }
```

<br>

### URL 처리 및 3rd 어플리케이션 호출
- URL에 포함된 App Scheme을 통해 어플리케이션 호출(openURL)
```bash
swift
```
```swift
func webView(_ webView: WKWebView, decidePolicyFor navigationAction: WKNavigationAction, decisionHandler: @escaping (WKNavigationActionPolicy) -> Void) {
        let request = navigationAction.request
        let optUrl = request.url
        let optUrlScheme = optUrl?.scheme
        
        guard let url = optUrl, let scheme = optUrlScheme
            else {
                return decisionHandler(WKNavigationActionPolicy.cancel)
        }
        
        debugPrint("url : \(url)")
       
        if( scheme != "http" && scheme != "https" ) {
            if( scheme == "ispmobile" && !UIApplication.shared.canOpenURL(url) ) {  //ISP 미설치 시
                UIApplication.shared.openURL(URL(string: "http://itunes.apple.com/kr/app/id369125087?mt=8")!)
            } else if( scheme == "kftc-bankpay" && !UIApplication.shared.canOpenURL(url) ) {    //BANKPAY 미설치 시
                UIApplication.shared.openURL(URL(string: "http://itunes.apple.com/us/app/id398456030?mt=8")!)
            } else {
                if( UIApplication.shared.canOpenURL(url) ) {
                    UIApplication.shared.openURL(url)
                } else {
                    //1. App 미설치 확인
                    //2. info.plist 내 scheme 등록 확인
                }
            }
        }
        
        decisionHandler(WKNavigationActionPolicy.allow)
    }

```

<br>

### 자바스크립트 팝업 처리
- 웹뷰의 오버라이딩 함수를 재정의 하여 팝업 처리 하면 웹뷰 처리가 완료 됩니다.

```bash
swift
```
```swift
func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping () -> Void) {
        let alert = UIAlertController(title: "", message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "확인", style: .default, handler: { (UIAlertAction) in
            completionHandler()
        }))
        
        self.present(alert, animated: true, completion: nil)
}
```

<br>

## iOS-Objective-C 웹뷰(web-view)개발 가이드

<br>

### 결제 페이지 호출
- 웹뷰의 loadRequest를 통해 결제 요청 URL을 호출 (가맹점 결제 요청 웹 페이지)
```bash
Object-C
```
```objective-c
(void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
    self.title = @"구매하기";
    
    self.webView = [[[WKWebView alloc] init] autorelease];
    self.webView.navigationDelegate = self;
    self.webView.UIDelegate = self;
    [self.view addSubview:self.webView];
    
    //nicepay 결제테스트 URL 입니다.
    //제공 된 샘플 상 payRequest 스크립트 페이지를 참고 하시여 개발 하시면 됩니다.
    [self.webView loadRequest:[NSURLRequest requestWithURL:[NSURL URLWithString:PAY_URL]]];
}
```

<br>

### URL 처리 및 3rd 어플리케이션 호출
- URL에 포함된 App Scheme을 통해 어플리케이션 호출(openURL)
```bash
Object-C
```
```objective-c
(void)webView:(WKWebView *)webView decidePolicyForNavigationAction:(WKNavigationAction *)navigationAction decisionHandler:(void (^)(WKNavigationActionPolicy))decisionHandler {
    NSURLRequest *request = navigationAction.request;
    NSURL *url = [request URL];
    NSString *urlScheme = [url scheme];
    
    NSLog(@"url : %@", url);
    
    if( ![urlScheme isEqualToString:@"http"] && ![urlScheme isEqualToString:@"https"] ) {
        if( [urlScheme isEqualToString:@"ispmobile"] && ![[UIApplication sharedApplication] canOpenURL:url] ) {
            //ISP App가 설치되어 있지 않을 경우 앱스토어로 이동
            [[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"http://itunes.apple.com/kr/app/id369125087?mt=8"]];
        } else if( [urlScheme isEqualToString:@"kftc-bankpay"] && ![[UIApplication sharedApplication] canOpenURL:url] ) {
            //BANKPAY App가 설치되어 있지 않을 경우 앱스토어로 이동
            [[UIApplication sharedApplication] openURL:[NSURL URLWithString:@"http://itunes.apple.com/us/app/id398456030?mt=8"]];
        } else {
            if( [[UIApplication sharedApplication] canOpenURL:url] ) {
                [[UIApplication sharedApplication] openURL:url];    //App 실행
            } else {
                //1. App 미설치 확인
                //2. info.plist 내 scheme 등록 확인
            }
        }
    }
    
    decisionHandler(WKNavigationActionPolicyAllow);
}

```

<br>

### 자바스크립트 팝업 처리
- 웹뷰의 오버라이딩 함수를 재정의 하여 팝업 처리

```bash
Object-C
```

``` objective-c
(void)webView:(WKWebView *)webView runJavaScriptAlertPanelWithMessage:(NSString *)message initiatedByFrame:(WKFrameInfo *)frame completionHandler:(void (^)(void))completionHandler {

    UIAlertController *alertController = [UIAlertController alertControllerWithTitle:nil
                                                                    message:message
                                                                    preferredStyle:UIAlertControllerStyleAlert];
    [alertController addAction:[UIAlertAction actionWithTitle:@"확인"
                                                                    style:UIAlertActionStyleCancel
                                                                        handler:^(UIAlertAction *action) {
                                                                        completionHandler();
                                                                    }]];
    [self presentViewController:alertController animated:YES completion:^{}];
}

```

   
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
