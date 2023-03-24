- [회원가입](README.md#회원가입)
- [개발정보](README.md#개발정보)
- [Key 정보](README.md#key-정보)
	- [클라이언트 키](README.md#클라이언트-키)
	- [클라이언트 키 Type](README.md#클라이언트-키-type)
	- [시크릿 키](README.md#시크릿-키)
	- [재발급](README.md#재발급)
- [방화벽 정책](README.md#방화벽-정책)
	- [IP 보안 기능(IP 접근 제한)](README.md#ip-보안-기능--ip접근-제한-)
	- [IP 보안 설정](README.md#ip-보안-설정)
	- [IP 보안 추가](README.md#ip-보안-추가)
	- [CIDR 규칙과 등록](README.md#cidr-규칙과-등록)
	- [타임아웃 정보](README.md#타임아웃-정보)
- [샌드박스](README.md#샌드박스)
	- [샌드박스(테스트 상점) 생성](README.md#샌드박스--테스트-상점--생성)
	- [샌드박스 활용](README.md#샌드박스-활용)
	- [샌드박스 장점](README.md#샌드박스-장점)
	- [샌드박스 가맹점 테스트](README.md#샌드박스-가맹점-테스트)
	- [토큰 기반 인증](README.md#토큰-기반-인증)
		- [Basic Authentication](README.md#basic-authentication)
			- [HTTP header Basic Authentication](README.md#http-header-basic-authentication-scheme)
			- [Credentials 생성 알고리즘](README.md#credentials-생성-알고리즘)
			- [Credentials 생성 방식](README.md#credentials-생성-예시)
		- [Bearer Authentication](README.md#bearer-authentication)
			- [HTTP header Bearer Authentication](README.md#http-header-bearer-authentication-scheme)
			- [Access Token 생성 API](README.md#access-token-생성-api)
			- [Bearer Token 생성 방식](README.md#bearer-token-생성-예시)
			- [Access Token API 응답 예시](README.md#access-token-api-응답-예시)
			- [HTTP header Bearer Token 사용 예시](README.md#http-header-bearer-token-셋팅)
	- [샌드박스를 통한 테스트 개발 예시](README.md#샌드박스를-통한-테스트-개발-예시)
		- [결제창 호출을 위한 JS include](README.md#결제창-호출을-위한-js-include)
		- [결제창 응답](README.md#결제창-응답)
		- [결제 요청 API 목록](README.md#결제-요청-api-목록)
		- [결제 응답 예시](README.md#결제--승인--응답-예시)
	- [로그](README.md#로그)
		- [웹 로그 디버깅](README.md#웹-로그-디버깅)
		- [주요기능](README.md#주요기능)
		- [상세보기](README.md#상세보기)
		- [로그 검색](README.md#로그-검색)
			- [단순 로그 확인](README.md#단순-로그-확인)
			- [상세 로그 확인](README.md#상세-로그-확인)
- [API·JS SDK](README.md#apijs-sdk)
	- [URI 목록](README.md#uri-목록)
	- [JS SDK](README.md#js-sdk)
		- [JS SDK 인증이란?](README.md#js-sdk-인증이란)
		- [JS SDK 인증-Server & Client 승인 모델](README.md#js-sdk-인증-server--client-승인-모델)

- [결제·발급](README.md#결제발급)
	- [Access token](README.md#access-token)
		- [Over-view](README.md#over-view)
		- [샘플 코드](README.md#샘플-코드)
		- [요청 명세](README.md#요청-명세)
		- [응답 명세 (Body)](README.md#응답-명세--body-)
	- [결제 인증 (Server 승인 모델-JS SDK)](README.md#결제-인증--server-승인-모델-js-sdk-)
		- [Over-view](README.md#over-view-1)
		- [예외처리](README.md#예외처리)
		- [샘플 코드](README.md#샘플-코드-1)
		- [요청 명세](README.md#요청-명세--server-승인-모델-)
			- [공통](README.md#공통)
			- [부가세 지정금액](README.md#부가세-지정금액)
			- [신용카드 & 간편결제](README.md#신용카드--간편결제)
			- [가상계좌](README.md#가상계좌)
			- [휴대폰](README.md#휴대폰)
			- [현금영수증](README.md#현금영수증)
			- [PC 옵션](README.md#pc-옵션)
			- [Mobile 옵션](README.md#mobile-옵션)
		- [응답 명세](README.md#응답-명세--server-승인-모델-)
	- [결제 승인](README.md#승인--결제-)
		- [Over-view](README.md#over-view-2)
		- [예외처리](README.md#예외처리-1)
		- [샘플 코드](README.md#샘플-코드-2)
		- [요청 명세](README.md#요청-명세-1)
		- [응답 명세](README.md#응답-명세)
			- [공통](README.md#공통-1)
			- [할인정보](README.md#할인정보-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey)
			- [카드](README.md#카드-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey)
			- [현금영수증](README.md#현금영수증-img-srchttpsimgshieldsiobadge-array-blueviolet-img-srchttpsimgshieldsiobadge-nullable-lightgrey)
			- [계좌이체](README.md#계좌이체-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey)
			- [가상계좌](README.md#가상계좌-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey)
	- [결제 인증 (Client 승인 모델-JS SDK)](README.md#결제-인증--client-승인-모델-)
		- [Over-view](README.md#over-view-3)
		- [예외처리](README.md#예외처리-2)
		- [샘플 코드](README.md#샘플-코드-3)
		- [요청 명세 (Client 승인 모델)](README.md#요청-명세--client-승인-모델-)
			- [공통](README.md#공통-2)
			- [부가세 지정금액](README.md#부가세-지정금액-1)
			- [신용카드 & 간편결제](README.md#신용카드--간편결제-1)
			- [가상계좌](README.md#가상계좌-1)
			- [휴대폰](README.md#휴대폰-1)
			- [현금영수증](README.md#현금영수증)
			- [PC 옵션](README.md#pc-옵션-1)
			- [Mobile 옵션](README.md#mobile-옵션-1)
		- [응답 명세 (Client 승인 모델)](README.md#응답-명세--client-승인-모델-)
	- [승인 금액 검증](README.md#승인-금액-검증)
		- [Over-view](README.md#over-view-4)
		- [샘플 코드](README.md#샘플-코드-4)
		- [요청 명세](README.md#요청-명세-2)
		- [응답 명세](README.md#응답-명세-1)
	- [빌링](README.md#빌링)
		- [빌키 발급](README.md#빌키-발급)
			- [Over-view](README.md#over-view-5)
			- [샘플 코드](README.md#샘플-코드-5)
			- [요청 명세](README.md#요청-명세--body-)
				- [encData 필드 상세정보](README.md#encdata-필드-상세정보)
		- [encData 필드 암호화 예시 (AES-128)](README.md#encdata-필드-암호화-예시--aes-128-)
		- [encData 필드 암호화 예시 (AES-256)](README.md#encdata-필드-암호화-예시--aes-256-)
			- [응답 명세](README.md#응답-명세--body--1)
		- [빌키 승인](README.md#빌키-승인)
			- [Over-view](README.md#over-view-6)
			- [샘플 코드](README.md#샘플-코드-6)
			- [요청 명세](README.md#요청-명세--body--1)
			- [응답 명세](README.md#응답-명세--body--2)
				- [할인정보](README.md#할인정보-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-1)
				- [카드](README.md#카드-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-1)
		- [빌키 삭제](README.md#빌키-삭제)
			- [Over-view](README.md#over-view-7)
			- [샘플 코드](README.md#샘플-코드-7)
			- [요청 명세](README.md#요청-명세--body--2)
			- [응답 명세](README.md#응답-명세--body--3)
	- [현금 영수증](README.md#현금영수증-1)
		- [현금영수증 발급](README.md#현금영수증-발급)
			- [Over-view](README.md#over-view-8)
			- [샘플 코드](README.md#샘플-코드-8)
			- [요청 명세](README.md#요청-명세--body--3)
			- [응답 명세](README.md#응답-명세--body--4)
		- [현금영수증 취소](README.md#현금영수증-취소)
			- [Over-view](README.md#over-view-9)
			- [샘플 코드](README.md#샘플-코드-9)
			- [요청 명세](README.md#요청-명세--body--4)
			- [응답 명세](README.md#응답-명세--body--5)
		- [현금영수증 조회](README.md#현금영수증-조회)
			- [Over-view](README.md#over-view-10)
			- [샘플 코드](README.md#샘플-코드-10)
			- [요청 명세](README.md#요청-명세--body--5)
			- [응답 명세](README.md#응답-명세--body--6)
	- [EPAY](README.md#epay)
		- [샘플 코드](README.md#샘플-코드-11)
		- [요청 명세](README.md#요청-명세--body--6)
			- [encData 필드 상세정보](README.md#encdata-필드-상세정보-1)
			- [encData 필드 암호화 정보](README.md#encdata-필드-암호화-정보)
			- [카드사별 (결제) 승인요청 전문](README.md#카드사별--결제--승인요청-전문)
		- [응답 명세](README.md#응답-명세--body--7)
			- [할인정보](README.md#할인정보-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-2)
			- [카드](README.md#카드-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-2)
	- [조회](README.md#조회)
		- [거래 조회](README.md#거래-조회)
			- [Over-view](README.md#over-view-11)
			- [샘플 코드](README.md#샘플-코드-12)
			- [요청 명세](README.md#요청-명세-3)
				- [거래조회(tid)](README.md#거래조회--with-tid-)
				- [거래조회(orderId)](README.md#거래조회--with-orderid-)
			- [응답 명세](README.md#응답-명세--body--8)
				- [공통](README.md#공통-3)
				- [할인 정보](README.md#할인정보-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-3)
				- [카드](README.md#카드-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-3)
				- [현금영수증](README.md#현금영수증-img-srchttpsimgshieldsiobadge-array-blueviolet-img-srchttpsimgshieldsiobadge-nullable-lightgrey-1)
				- [계좌이체](README.md#계좌이체-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-1)
				- [가상계좌](README.md#가상계좌-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-1)
				- [취소](README.md#취소-img-srchttpsimgshieldsiobadge-array-blueviolet-img-srchttpsimgshieldsiobadge-nullable-lightgrey)
		- [약관조회](README.md#약관조회)
			- [Over-view](README.md#over-view-12)
			- [약관 조회 종류](README.md#약관-조회-종류)
			- [샘플 코드](README.md#샘플-코드-13)
			- [요청 명세](README.md#요청-명세-4)
			- [응답 명세](README.md#응답-명세--body--9)
		- [카드 이벤트 조회](README.md#카드-이벤트-조회)
			- [Over-view](README.md#over-view-13)
			- [샘플 코드](README.md#샘플-코드-14)
			- [요청 명세](README.md#요청-명세-5)
			- [응답 명세](README.md#응답-명세--body--10)
				- [무이자 할부정보](README.md#무이자-할부정보-img-srchttpsimgshieldsiobadge-array-blueviolet)
		- [카드 무이자 조회](README.md#카드-무이자-조회)
			- [Over-view](README.md#over-view-14)
			- [샘플 코드](README.md#샘플-코드-15)
			- [요청 명세](README.md#요청-명세-6)
			- [응답 명세](README.md#응답-명세--body--11)
				- [무이자 할부정보](README.md#무이자-할부정보-img-srchttpsimgshieldsiobadge-array-blueviolet-1)
	- [취소·환불·망취소](README.md#취소환불망취소)
		- [취소·환불](README.md#취소환불)
			- [Over-view](README.md#over-view-15)
			- [결제수단 별 취소·환불](README.md#결제수단-별-취소환불)
			- [샘플 코드](README.md#샘플-코드-16)
			- [요청 명세](README.md#요청-명세-7)
			- [응답 명세](README.md#응답-명세--body--12)
				- [할인 정보](README.md#할인정보-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-4)
				- [카드](README.md#카드-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-4)
				- [현금영수증](README.md#현금영수증-img-srchttpsimgshieldsiobadge-array-blueviolet-img-srchttpsimgshieldsiobadge-nullable-lightgrey-2)
				- [계좌이체](README.md#계좌이체-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-2)
				- [가상계좌](README.md#가상계좌-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-2)
				- [취소](README.md#취소-img-srchttpsimgshieldsiobadge-array-blueviolet-img-srchttpsimgshieldsiobadge-nullable-lightgrey-1)
		- [망취소](README.md#망취소)
			- [Over-view](README.md#over-view-16)
			- [결제창 (Server 승인 모델) 의 망취소 구현](README.md#결제창--server-승인-모델--의-망취소-구현)
			- [결제창 (Client 승인 모델) 의 망취소 구현](README.md#결제창--client-승인-모델--의-망취소-구현)
			- [빌링 등 Server-side 결제의 망취소 구현](README.md#빌링-등-server-side-결제의-망취소-구현)
			- [샘플 코드](README.md#샘플-코드-17)
			- [요청 명세](README.md#요청-명세-8)
			- [응답 명세](README.md#응답-명세--body--13)
				- [할인 정보](README.md#할인정보-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-5)
				- [카드](README.md#카드-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-5)
				- [현금영수증](README.md#현금영수증-img-srchttpsimgshieldsiobadge-array-blueviolet-img-srchttpsimgshieldsiobadge-nullable-lightgrey-3)
				- [계좌이체](README.md#계좌이체-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-3)
				- [가상계좌](README.md#가상계좌-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-3)
				- [취소](README.md#취소-img-srchttpsimgshieldsiobadge-array-blueviolet-img-srchttpsimgshieldsiobadge-nullable-lightgrey-2)
	- [웹훅](README.md#웹훅)
		- [Over-view](README.md#over-view-17)
		- [웹훅 발송 흐름](README.md#웹훅-발송-흐름)
		- [웹훅 발송 시점](README.md#웹훅-발송-시점)
		- [웹훅 URL 추가](README.md#웹훅-url-추가)
		- [웹훅 개발 정보](README.md#웹훅-개발정보)
		- [웹훅 테스트 호출](README.md#웹훅-테스트-호출)
			- [웹훅 테스트 호출 처리 프로세스](README.md#웹훅-테스트-호출-처리-프로세스)
		- [웹훅 재전송](README.md#웹훅-재전송)
		- [응답 명세](README.md#응답-명세--body--14)
			- [할인 정보](README.md#할인정보-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-6)
			- [카드](README.md#카드-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-6)
			- [현금영수증](README.md#현금영수증-img-srchttpsimgshieldsiobadge-array-blueviolet-img-srchttpsimgshieldsiobadge-nullable-lightgrey-4)
			- [계좌이체](README.md#계좌이체-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-4)
			- [가상계좌](README.md#가상계좌-img-srchttpsimgshieldsiobadge-object-yellow-img-srchttpsimgshieldsiobadge-nullable-lightgrey-4)
			- [취소](README.md#취소-img-srchttpsimgshieldsiobadge-array-blueviolet-img-srchttpsimgshieldsiobadge-nullable-lightgrey-3)
		- [웹훅 로그](README.md#웹훅-로그)
- [iOS](README.md#ios)
	- [iOS 공통사항](README.md#ios-공통사항)
	- [iOS 지원환경](README.md#ios-지원환경)
		- [iOS 개발흐름](README.md#ios-개발흐름)
		- [appScheme 설정 - Client 승인 모델](README.md#appScheme-설정---client-승인-모델)
		- [appScheme 설정 - Server 승인 모델](README.md#appScheme-설정---server-승인-모델)
		- [URL Scheme 설정](README.md#url-scheme-설정)
			- [3rd party app URL Scheme 등록](README.md#3rd-party-app-url-scheme-등록)
			- [3rd URL Scheme 리스트](README.md#3rd-url-scheme-리스트)
		- [네트워크 보안 예외 설정](README.md#네트워크-보안-예외-설정)
		- [iOS-Swift 웹 뷰(web-view) 개발 가이드](README.md#ios-swift-웹-뷰--web-view--개발-가이드)
			- [결제 페이지 호출](README.md#결제-페이지-호출)
			- [URL 처리 및 3rd party app 호출](README.md#url-처리-및-3rd-party-app-호출)
			- [자바스크립트 팝업 처리](README.md#자바스크립트-팝업-처리)
		- [iOS-Objective-C 웹뷰(web-view)개발 가이드](README.md#ios-objective-c-웹-뷰--web-view--개발-가이드)
			- [결제 페이지 호출](README.md#결제-페이지-호출-1)
			- [URL 처리 및 3rd party app 호출](README.md#url-처리-및-3rd-party-app-호출-1)
			- [자바스크립트 팝업 처리](README.md#자바스크립트-팝업-처리-1)
- [Android](README.md#android)
	- [지원 환경](README.md#android-지원-환경)
	- [개발 흐름](README.md#android-개발-흐름)
	- [공통 사항](README.md#android-공통-사항)
	- [appScheme 설정 - Server 승인 모델, Client 승인 모델](README.md#appscheme-설정--server-승인-모델-client-승인-모델)
	- [권한 설정](README.md#android-권한-설정)
	- [네트워크 보안정책 설정](README.md#android-네트워크-보안정책-설정)
	- [Android-java 웹뷰(web-view)개발 가이드](README.md#android-java-웹-뷰--web-view--개발-가이드)
		- [기본 설정 및 자바스크립트 허용](README.md#android-java-기본-설정-및-자바스크립트-허용)
		- [캐시 및 쿠키 설정](README.md#android-java-캐시-및-쿠키-설정)
		- [결제 페이지 호출](README.md#android-java-결제-페이지-호출)
		- [URI 및 Intent 처리](README.md#android-java-uri-및-intent-처리)
	- [Android-kotlin 웹뷰(web-view)개발 가이드](README.md#android-kotlin-웹-뷰--web-view--개발-가이드)
		- [기본 설정 및 자바스크립트 허용](README.md#android-kotlin-기본-설정-및-자바스크립트-허용)
		- [캐시 및 쿠키 설정](README.md#android-kotlin-캐시-및-쿠키-설정)
		- [결제 페이지 호출](README.md#android-kotlin-결제-페이지-호출)
		- [URI 및 Intent 처리](README.md#android-kotlin-uri-및-intent-처리)
- [지원환경](README.md#지원환경)
- [브라우저](README.md#브라우저)
	- [PC 지원 브라우저](README.md#pc-지원-브라우저)
	- [Mobile 지원 브라우저](README.md#mobile-지원-브라우저)
- [오류관리](README.md#오류관리)
	- [시스템 오류의 대응](README.md#시스템-오류의-대응)
	- [결제고객 오류](README.md#결제고객-오류)
		- [사용자 환경 오류의 대응](README.md#사용자-환경-오류의-대응)
- [코드집](README.md#코드집)
	- [HTTP 상태코드](README.md#http-상태코드)
	- [카드 코드](README.md#카드-코드)
	- [은행 코드](README.md#은행-코드)
	- [API 응답 코드](README.md#api-응답-코드)