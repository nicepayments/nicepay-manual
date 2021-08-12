# App
## iOS
결제창을 App내 에서 구현하는 경우 웹뷰(Web-view)를 통해 구현 처리가 가능 합니다.  
빠른 개발 진행을 원하는 경우 샘플코드를 검토 후 가이드 확인을 권장 합니다.  

### 지원환경
- IOS 9.0 이상 
- Xcode 7.x 이상
- Swift 4.0 이상

### 개발흐름
- 결제창 호출시 appScheme 값 셋팅 
- 환경 설정
- URL Scheme 설정
- 예외처리 (java-script, 네트워크)


>가맹점 결제 요청 페이지 로드 실패 하는 경우 가맹점 페이지가 HTTP 일 경우 info.plist 내 네트워크 보안 예외 설정을 확인(ATS) 해주세요.  
>3rd 어플리케이션 호출 불가한 경우 info.plist 내 3rd URL Scheme 설정을 확인 해주세요.  
>3rd 어플리케이션에서 인증 or 결제 완료 후 가맹점 어플리케이션으로 미전환시 info.plist 내 가맹점 URL Scheme 설정을 확인해 주세요.  
>결제 완료 후 웹 브라우저 호출이 되지 않는 경우 info.plist 내 가맹점 URL Scheme 설정 값과 결제창 JS SDK로 전달된 appScheme 값이 일치하는지 체크 해주세요.  
>팝업창 미노출 되는 경우 웹뷰의 자바스크립트 오버라이딩 함수 재정를 해주세요.  

### 공통사항
App 내 웹뷰를 통해 결제창을 연동하는 경우, 웹 환경에서 결제창을 통한 결제(승인)이 가능하도록 개발이 선행 되어야 합니다.  
이 후 appScheme 값을 설정 합니다.  
카드사를 포함한 제휴사 인증 완료 후 전달된 가맹점 APP의 scheme을 확인하여 화면 focus가 이동 하게 됩니다.  

### appScheme 설정- Server 승인 모델
```javascript
<script src="https://pay.nicepay.co.kr/v1/js/"></script> //Server 승인 
<script>
function serverAuth() {
  AUTHNICE.requestPay({
	clientId: ‘af0d116236df437f831483ee9c500bc4’,
              appScheme: ‘nicepaysample://’,
	method: ‘vbank’,
	orderId: ‘your-unique-orderid’,
	amount: 1004,
	goodsName: ‘나이스페이-상품’,
	returnUrl: ‘http://localhost:4567/serverAuth’
 });
}
</script>
```
### appScheme 설정 - Client 승인 모델

```javascript
<script src="https://pay.nicepay.co.kr/v1/js/pay/"></script> //Client 승인 
<script>
function serverAuth() {
  PAYNICE.requestPay({
	clientId: ‘af0d116236df437f831483ee9c500bc4’,
              appScheme: ‘nicepaysample://’,
	method: ‘vbank’,
	orderId: ‘your-unique-orderid’,
	amount: 1004,
	goodsName: ‘나이스페이-상품’,
	returnUrl: ‘http://localhost:4567/serverAuth’
 });
}
</script>
```

### URL Scheme 설정
- 가맹점 어플리케이션에 URL Scheme 을 등록합니다. (JS SDK 호출시 appScheme 필드 값으로 URL Scheme 사용)
- Info.plist 파일에 URL Scheme을 등록 합니다. (3rd 어플리케이션 -> 가맹점 어플리케이션 호출)
```bash
info.plist
```
```bash
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

> info.plist 파일에 URL Scheme 미설정 시 특정 3rd 어플리케이션에서 인증 or 결제 완료 후 가맹점 어플리케이션으로 자동 전환이 불가 합니다.

### 3rd 어플리케이션 URL Scheme 등록
- info.plist 파일에 3rd URL Scheme을 등록 합니다. (가맹점 어플리케이션 -> 3rd 어플리케이션 호출)
- URL Scheme 미설정 시3rd 어플리케이션 연동이 불가 합니다.
```bash
info.plist
```
```bash
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

### 네트워크 보안 예외 설정
- HTTP 또는 유효하지 않은 인증서를 가진 HTTPS 연결 시 예외 처리입니다. 
- Apple에서는 하기와 같은 방법을 권장하지 않으며, 특정 도메인에 대해서만 예외 처리하도록 권장 합니다.
```bash
info.plist
```
```bash
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <true/>
</dict>
```

### iOS-Swift 웹뷰(web-view)개발 가이드
#### 결제 페이지 호출
- 웹뷰의 load를 통해 결제 요청 URL을 호출 합니다. 가맹점 결제 요청 웹 페이지 예시
```bash
swift
```
```bash
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

#### URL 처리 및 3rd 어플리케이션 호출
- URL에 포함된 App Scheme을 통해 어플리케이션 호출(openURL)
```bash
swift
```
```bash
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
#### 자바스크립트 팝업 처리
- 웹뷰의 오버라이딩 함수를 재정의 하여 팝업 처리 하면 웹뷰 처리가 완료 됩니다.

```bash
swift
```
```bash
func webView(_ webView: WKWebView, runJavaScriptAlertPanelWithMessage message: String, initiatedByFrame frame: WKFrameInfo, completionHandler: @escaping () -> Void) {
        let alert = UIAlertController(title: "", message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "확인", style: .default, handler: { (UIAlertAction) in
            completionHandler()
        }))
        
        self.present(alert, animated: true, completion: nil)
}
```

### iOS-Objective-C 웹뷰(web-view)개발 가이드
#### 결제 페이지 호출
- 웹뷰의 loadRequest를 통해 결제 요청 URL을 호출 (가맹점 결제 요청 웹 페이지)
```bash
Object-C
```
```bash
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
#### URL 처리 및 3rd 어플리케이션 호출
- URL에 포함된 App Scheme을 통해 어플리케이션 호출(openURL)
```bash
Object-C
```
```bash
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
#### 자바스크립트 팝업 처리
- 웹뷰의 오버라이딩 함수를 재정의 하여 팝업 처리

```bash
Object-C
```

``` bash
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

## Android
결제창을 App내 에서 구현하는 경우 웹뷰(Web-view)를 통해 구현 처리가 가능 합니다.  
빠른 개발 진행을 원하는 경우 샘플코드를 검토 후 가이드 확인을 권장 합니다.  

### 지원 환경
- Android 4.4 (KITKAT) 이상

### 개발 흐름
- AndroidManifast.xml 네트워크 보안 예외설정
- 웹뷰 자바스크립트 허용 처리
- 캐시 및 쿠키 설정
- URI Intent 처리

### Android-공통설정
#### 권한 설정
- AndroidManifast.xml 파일에 권한 및 네트워크 보안 예외 설정을 합니다.

```bash
AndroidManifast.xml 
```
```bash
<uses-permission android:name="android.permission.INTERNET" />
 
    <application
        android:allowBackup="true"
    android:icon="@mipmap/ic_launcher"
    android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme"
        android:usesCleartextTraffic="true">
```

#### 네트워크 보안정책 설정
- 네트워크 TLS 기본값 변경으로 인해 일반 텍스트 사용 시 설정 (Android 9.0 이상)


```bash
AndroidManifast.xml 
```

``` bash
<uses-permission android:name="android.permission.INTERNET" />
 
    <application
        android:allowBackup="true"
    android:icon="@mipmap/ic_launcher"
    android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme"
        android:usesCleartextTraffic="true">
```

### 웹뷰(web-view)개발 가이드
#### 기본 설정 및 자바스크립트 허용
- 웹뷰 커스텀 클래스를 설정하고 자바스크립트 실행 가능하도록 enabled 설정 합니다.

```bash
Android-java

```

```bash
//setup default
mWebView.setWebViewClient(new WebViewClientClass());
 
//javascript allow
mWebView.getSettings().setJavaScriptEnabled(true);
```


```bash
Android-kotlin

```

```bash
class WebViewActivity : AppCompatActivity() {
    companion object {
        const val MERCHANT_URL = "https://web.nicepay.co.kr/demo/v3/mobileReq.jsp"
    }
 
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_webview)
 
        webview.webViewClient = WebViewClientClass()
 
        val settings = webview.settings
        settings.javaScriptEnabled = true
```

#### 캐시 및 쿠키 설정
- 캐시 모드는 웹뷰 기본값으로 설정 합니다.
- 쿠키 허용 설정 (Android 5.0 이상 시 third-party 쿠키 허용 추가)


```bash
Android-java

```

```bash

//setup cache
/*
 * WebView에서 캐시사용 관련 Default 설정은 WebSettings.LOAD_DEFAULT 입니다.
 * ex) mWebView.getSettings().setCacheMode(WebSettings.LOAD_DEFAULT);
 * 가급적 캐시 사용 설정을 변경하지 않을것을 권고 드립니다.
 * @중요 : 'WebSettings.LOAD_CACHE_ELSE_NETWORK' 로 변경금지.
 * @중요 : Do not change the setting to 'WebSettings.LOAD_CACHE_ELSE_NETWORK'
 */
 mWebView.getSettings().setCacheMode(WebSettings.LOAD_DEFAULT);
 
 //setup cookie
 if( android.os.Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP ) {    //Android 5.0 이상
        mWebView.getSettings().setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);
        CookieManager cookieManager = CookieManager.getInstance();
        cookieManager.setAcceptCookie(true);
        cookieManager.setAcceptThirdPartyCookies(mWebView, true);
  } else {
       CookieManager cookieManager = CookieManager.getInstance();
  }

```

```bash
Android-kotlin

```

```bash
//setup cache
/*
* WebView에서 캐시사용 관련 Default 설정은 WebSettings.LOAD_DEFAULT 입니다.
* ex) settings.cacheMode = WebSettings.LOAD_DEFAULT
* 가급적 캐시 사용 설정을 변경하지 않을것을 권고 드립니다.
* @중요 : 'WebSettings.LOAD_CACHE_ELSE_NETWORK' 로 변경금지.
* @중요 : Do not change the setting to 'WebSettings.LOAD_CACHE_ELSE_NETWORK'
*/
settings.cacheMode = WebSettings.LOAD_DEFAULT
 
if( android.os.Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP ) {    //Android 5.0 이상
    settings.setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW)
    CookieManager.getInstance().setAcceptCookie(true)
    CookieManager.getInstance().setAcceptThirdPartyCookies(webview, true)
} else {
    CookieManager.getInstance().setAcceptCookie(true)
}
```

> 캐시 모드를 WebSetting.LOAD_CACHE_ELSE_NETWORK 으로 설정 시 일부 카드사 세션 오류가 발생 합니다.  

#### 결제 페이지 호출
- 웹뷰의 postUrl을 통해 결제 요청 URL 호출 (가맹점 결제 요청 페이지)

```bash
Android-java
```
```bash
//load url
 mWebView.postUrl(MERCHANT_URL, null);
```


```bash
Android-kotlin
```

```bash
//load url
webview.postUrl(MERCHANT_URL, null)
```

#### URI 및 Intent 처리
- URI에 포함된 요청 데이터를 Intent를 통해 어플리케이션을 호출 합니다.(startActivity)


```bash
Android-java
```
```bash
private class WebViewClientClass extends WebViewClient {
    @Override
    public boolean shouldOverrideUrlLoading(WebView view, String url) {
        Log.i(TAG, "url : " + url); 
        try {
            if (url != null && (url.startsWith("intent:") ||
                    url.contains("market://") ||
                    url.contains("vguard") ||
                    url.contains("droidxantivirus") ||
                    url.contains("v3mobile") ||
                    url.contains(".apk") ||
                    url.contains("mvaccine") ||
                    url.contains("smartwall://") ||
                    url.contains("nidlogin://") ||
                    url.contains("http://m.ahnlab.com/kr/site/download"))) {
                Intent intent = null;
                
                try {
                    intent = Intent.parseUri(url, Intent.URI_INTENT_SCHEME);
                } catch (URISyntaxException ex) {
                    Log.e(TAG, "[error] Bad request uri format : [" + url + "] =" + ex.getMessage());
                    return false;
                }
                
                if (Build.VERSION.SDK_INT < Build.VERSION_CODES.R) {
                    if (getPackageManager().resolveActivity(intent, 0) == null) {
                        String pkgName = intent.getPackage();
                        if (pkgName != null) {
                            Uri uri = Uri.parse("market://search?q=pname:" + pkgName);
                            intent = new Intent(Intent.ACTION_VIEW, uri);
                            startActivity(intent);
                        }
                    } else {
                        Uri uri = Uri.parse(intent.getDataString());
                        intent = new Intent(Intent.ACTION_VIEW, uri);
                        startActivity(intent);
                    }
                } else {
                    try {
                        startActivity(intent);
                    } catch (ActivityNotFoundException e) {
                        Uri uri = Uri.parse("market://search?q=pname:" + intent.getPackage());
                        intent = new Intent(Intent.ACTION_VIEW, uri);
                        startActivity(intent);
                    }
                }
                
            } else {
                view.loadUrl(url);
            }
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
        return true;
    }
}
```

```bash
Android-kotlin
```

```bash



private class WebViewClientClass : WebViewClient() {
        override fun shouldOverrideUrlLoading(view: WebView?, url: String?): Boolean {
            println("url : " + url)
 
            try {
                if( url != null && (url.startsWith("intent:")
                            || url.contains("market://")
                            || url.contains("vguard")
                            || url.contains("droidxantivirus")
                            || url.contains("v3mobile")
                            || url.contains(".apk")
                            || url.contains("mvaccine")
                            || url.contains("smartwall://")
                            || url.contains("nidlogin://")
                            || url.contains("http://m.ahnlab.com/kr/site/download")) ) {
 
                    var intent: Intent? = null
 
                    try {
                        intent = Intent.parseUri(url, Intent.URI_INTENT_SCHEME)
                    } catch (e: URISyntaxException) {
                        println("error : " + e.printStackTrace())
                    }
 
                    if( Build.VERSION.SDK_INT < Build.VERSION_CODES.R ) {
                        if( view?.context?.packageManager?.resolveActivity(intent!!, 0) == null ) {
                            val pkgName = intent?.`package`
                            if( pkgName != null ) {
                                val uri = Uri.parse("market://search?q=pname:" + pkgName)
                                intent = Intent(Intent.ACTION_VIEW, uri)
                                view?.context?.startActivity(intent)
                            }
                        } else {
                            val uri = Uri.parse(intent?.dataString)
                            intent = Intent(Intent.ACTION_VIEW, uri)
                            view?.context?.startActivity(intent)
                        }
                    } else {
                        try {
                            view?.context?.startActivity(intent)
                        } catch (e: ActivityNotFoundException) {
                            val pkgName = intent?.`package`
                            if( pkgName != null ) {
                                val uri = Uri.parse("market://search?q=pname:" + pkgName)
                                intent = Intent(Intent.ACTION_VIEW, uri)
                                view?.context?.startActivity(intent)
                            }
                        }
                    }
                } else {
                    view?.loadUrl(url)
                }
            } catch (e: Exception) {
                println("error : " + e.printStackTrace())
                return false
            }
            return true
        }
    }
```
> Android 하위 버전으로 개발 시 카드사 보안, 백신 프로그램 어플 등은 intent:// 방식이 아닌 scheme 호출 방식으로 처리 될 수 있습니다.  
> 해당 문제가 발생되는 경우 scheme을 수동으로 추가해야 합니다  
> Ex) cloudpay://~ 로 들어올 경우 if( url.startwith(“cloudpay”) 추가)  
