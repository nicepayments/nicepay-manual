# Android

### 지원 환경
- `Android 4.4` (KITKAT) 이상

<br>

### 개발 흐름
- `AndroidManifast.xml` 네트워크 🔒 보안 예외설정
- `웹뷰 자바스크립트 허용` 처리
- 캐시 및 쿠키 설정
- `URI Intent` 처리

<br>

### 공통사항
App 내 웹뷰를 통해 결제창을 연동하는 경우, 웹 환경에서 결제창을 통한 💳 결제(승인)이 가능하도록 개발이 선행 되어야 합니다.  
이 후 appScheme 값을 설정 합니다.  
카드사를 포함한 제휴사 인증 완료 후 전달된 가맹점 APP의 scheme을 확인하여 화면 focus가 이동 하게 됩니다.  

<br>

### appScheme 설정- Server 승인 모델, Client 승인 모델
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

### 패키지명 정의

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="kr.co.nicepay.nicepayappsample">

	<queries>
        <!--신용카드-->
        <package android:name="kr.co.samsungcard.mpocket" />  <!--삼성 앱카드, 삼성 앱카드 공동인증서-->
        <package android:name="com.shcard.smartpay" />  <!--신한 페이판-->
        <package android:name="com.shinhancard.smartshinhan" />  <!--신한(ARS/일반결제/Smart결제), 신한 공동인증서-->
        <package android:name="com.kbcard.cxh.appcard" />  <!--KBPay-->
        <package android:name="com.kbstar.liivbank" />  <!--LiiV(국민은행)-->
        <package android:name="com.kbstar.reboot" />  <!--new liib-->
        <package android:name="kvp.jjy.MispAndroid320" />  <!--페이북/ISP-->
        <package android:name="com.hanaskcard.paycla" />  <!--하나카드 원큐페이-->
        <package android:name="kr.co.hanamembers.hmscustomer" />  <!--하나멤버스-->
        <package android:name="com.lcacApp" />  <!--롯데 앱카드-->
        <package android:name="nh.smart.nhallonepay" />  <!--NH 올원페이, NH 올원페이 공동인증서-->
        <package android:name="com.wooricard.smartapp" />  <!--우리 WON 카드-->
        <package android:name="com.hyundaicard.appcard" />  <!--현대 앱카드-->
        <package android:name="kr.co.citibank.citimobile" />  <!--씨티카드-->

        <!--공인인증-->
        <package android:name="com.hanaskcard.rocomo.potal" />  <!--하나카드-->
        <package android:name="com.lumensoft.touchenappfree" />  <!--공동인증서-->

        <!--백신-->
        <package android:name="com.TouchEn.mVaccine.webs" />  <!--TouchEn mVaccine(신한)-->
        <package android:name="com.ahnlab.v3mobileplus" />  <!--V3(NH, 현대)-->
        <package android:name="kr.co.shiftworks.vguardweb" />  <!--V-Guard(삼성)-->

        <!--간편결제-->
        <package android:name="com.samsung.android.spay" />  <!--삼성페이(삼성, 농협, KB)-->
        <package android:name="com.samsung.android.spaylite" />  <!--삼성페이 미니(삼성, KB)-->
        <package android:name="com.kakao.talk" />  <!--카카오페이-->
        <package android:name="com.nhn.android.search" />  <!--네이버페이-->
        <package android:name="com.ssg.serviceapp.android.egiftcertificate" />  <!--SSGPay(현대)-->
        <package android:name="com.nhnent.payapp" />  <!--페이코(삼성, 농협, KB)-->
        <package android:name="com.lge.lgpay" />  <!--엘지페이(삼성, KB)-->
        <package android:name="com.lottemembers.android" />  <!--LPay-->
		<package android:name="com.tencent.mm" /> <!-- 위챗페이-->
        <package android:name="viva.republica.toss" /> <!-- 토스-->

        <!--계좌이체-->
        <package android:name="com.kftc.bankpay.android" />  <!--금결원-->

        <!--본인인증-->
        <package android:name="com.sktelecom.tauth" />  <!--SKT-->
        <package android:name="com.kt.ktauth" />  <!--KT-->
        <package android:name="com.lguplus.smartotp" />  <!--LGT-->
    </queries>
    <!-- 권한 설정 -->
    ...
    <!-- 네트워크 권한 설정 -->
    ...
</manifest>
```


### 권한 설정
- `AndroidManifast.xml` 파일에 권한 및 네트워크 🔒 보안 예외 설정을 합니다.

```bash
AndroidManifast.xml 
```
```xml
<!-- 패키지 설정 -->
...
<!-- 권한 설정 -->
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

<br>

### 네트워크 보안정책 설정
- 네트워크 TLS 기본값 변경으로 인해 일반 텍스트 사용 시 설정 (`Android 9.0` 이상)


```bash
AndroidManifast.xml 
```

```xml
<!-- 패키지 설정 -->
...
<!-- 권한 설정 -->
<uses-permission android:name="android.permission.INTERNET" />
 
<!-- 네트워크 보안 정책 --> 
<application
  android:allowBackup="true"
  android:icon="@mipmap/ic_launcher"
  android:label="@string/app_name"
  android:roundIcon="@mipmap/ic_launcher_round"
  android:supportsRtl="true"
  android:theme="@style/AppTheme"
  android:usesCleartextTraffic="true">
```

<br>

## Android-java 웹뷰(web-view)개발 가이드
### 기본 설정 및 자바스크립트 허용
- 웹뷰 커스텀 클래스를 설정하고 자바스크립트 실행 가능하도록 `enabled` 설정 합니다.

```bash
Android-java

```

```java
//setup default
mWebView.setWebViewClient(new WebViewClientClass());
 
//javascript allow
mWebView.getSettings().setJavaScriptEnabled(true);
```

<br>

### 캐시 및 쿠키 설정
- 캐시 모드는 웹뷰 기본값으로 설정 합니다.
- 쿠키 허용 설정 (`Android 5.0` 이상 시 `third-party 쿠키 허용` 추가)


```bash
Android-java

```

```java

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

<br>

> #### ⚠️ 중요
> 캐시 모드를 `WebSetting.LOAD_CACHE_ELSE_NETWORK` 으로 설정 시 일부 카드사 세션 오류가 발생 합니다.  

<br>

### 결제 페이지 호출
- 웹뷰의 `postUrl`을 통해 결제 요청 URL 호출 (가맹점 결제 요청 페이지)

```bash
Android-java
```
```bash
//load url
 mWebView.postUrl(MERCHANT_URL, null);
```

<br>

### URI 및 Intent 처리
- URI에 포함된 요청 데이터를 Intent를 통해 어플리케이션을 호출 합니다.(`startActivity`)


```bash
Android-java
```
```java
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

<br>

> #### ⚠️ 중요
> Android 하위 버전으로 개발 시 카드사 보안, 백신 프로그램 어플 등은 `intent://` 방식이 아닌 scheme 호출 방식으로 처리 될 수 있습니다.  
> 해당 문제가 발생되는 경우 scheme을 수동으로 추가해야 합니다  
> Ex) `cloudpay://~` 로 들어올 경우 `if( url.startwith("cloudpay”) 추가)` 


## Android-kotlin 웹뷰(web-view)개발 가이드

### 기본 설정 및 자바스크립트 허용
- 웹뷰 커스텀 클래스를 설정하고 자바스크립트 실행 가능하도록 `enabled` 설정 합니다.

```bash
Android-kotlin

```

```kotlin
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

<br>

### 캐시 및 쿠키 설정
- 캐시 모드는 웹뷰 기본값으로 설정 합니다.
- 쿠키 허용 설정 (`Android 5.0` 이상 시 `third-party 쿠키 허용` 추가)

<br>

```bash
Android-kotlin

```

```kotlin
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

<br>

> #### ⚠️ 중요
> 캐시 모드를 `WebSetting.LOAD_CACHE_ELSE_NETWORK` 으로 설정 시 일부 카드사 세션 오류가 발생 합니다.  

<br>

### 결제 페이지 호출
- 웹뷰의 `postUrl`을 통해 결제 요청 URL 호출 (가맹점 결제 요청 페이지)

<br>

```bash
Android-kotlin
```

```kotlin
//load url
webview.postUrl(MERCHANT_URL, null)
```

<br>

### URI 및 Intent 처리
- URI에 포함된 요청 데이터를 Intent를 통해 어플리케이션을 호출 합니다.(`startActivity`)

<br>

```bash
Android-kotlin
```

```kotlin

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

<br>

> #### ⚠️ 중요
> Android 하위 버전으로 개발 시 카드사 보안, 백신 프로그램 어플 등은 `intent://` 방식이 아닌 scheme 호출 방식으로 처리 될 수 있습니다.  
> 해당 문제가 발생되는 경우 scheme을 수동으로 추가해야 합니다  
> Ex) `cloudpay://~` 로 들어올 경우 `if( url.startwith("cloudpay”) 추가)`

[전체 문서 목록](../README.md)
