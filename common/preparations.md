# 개발준비

## 회원가입
회원가입을 하고 [샌드박스](/common/test.md#샌드박스test)를 활용하면 빠르게 개발 할 수 있어요.  
[회원가입 페이지](https://start.nicepay.co.kr/merchant/login)로 이동 후 무료로 회원가입을 해보세요.  

- [회원가입](https://start.nicepay.co.kr/merchant/login)
- [샌드박스 준비](/common/test.md#샌드박스-준비)
- [샌드박스 활용](/common/test.md#샌드박스-활용)


## API KEY 확인
API KEY는 결제창과 API를 호출할 때 사용 됩니다.  
로그인을 하여 상점을 생성 후 [개발정보](/management/admin.md#개발정보)로 이동하면 확인이 가능합니다.  

### API KEY
- [클라이언트 키](/common/api.md#클라이언트-키) : 결제창 호출시 활용 됩니다.
- [시크릿 키](/common/api.md#시크릿-키) : API 호출시 암호화 키 값으로 사용 됩니다.

### API · JS SDK 인증
- [JS SDK 인증](/common/api.md#js-sdk-인증)
- [Basic auth](/common/api.md#basic-auth)
- [Bearer token](/common/api.md#bearer-token)

> 샌드박스에서 제공되는 키와 운영상점에서 제공되는 키는 다릅니다.  
> 실제 운영상점의 결제를 원하는 경우 반드시 해당 상점 KEY로 변경 해주세요.  
> 운영상점의 시크릿 키가 외부에 노출되지 않도록 주의 해주세요.  
> 만약 노출된 경우 키를 변경하여 위험을 예방할 수 있습니다.  
> ( 로그인 > 개발정보 > 키 변경 )

## 방화벽 정책
원활한 통신을 위해 서버의 HTTP 클라이언트가 `TLS 1.2`에 대응되는지 확인 해주세요.  
서버에서 결제 API호출을 위해 필요한 서비스의 IP를 방화벽에서 허용 해주세요.  

|    서비스    |    프로토콜    |    IP    |    방향    |
|:---|:---|:---|:---|
|    API    |    HTTPS    |    210.108.219.202    |    OUTBOUND    |
|    웹훅    |    HTTPS    |    210.108.219.XXX    |    INBOUND    |
|    정산·대사    |    HTTPS    |    210.108.219.XXX    |    OUTBOUND    |

  
## IP 보안 기능
나이스페이 API는 모든 IP 대역에서 호출이 가능 합니다.   
처음 상점을 생성한 후 IP 보안 기능을 통해 API 호출이 가능한 IP를 제어한다면 한 단계 높은 보안수준을 유지할 수 있습니다.  
IP 등록 규칙은 `CIDR`체계를 따르며 Class체계 대비 유연하게 IP 대역을 제한할 수 있습니다.  

### IP 보안 설정
![image](https://user-images.githubusercontent.com/86043374/128289743-abfd822e-b303-4e4a-bb94-ab6d6da77f4a.png)

- 로그인 후 [개발정보](/management/admin.md#개발정보)에 접속하면 IP 보안 등록이 가능 합니다.  
- 추가를 누른 후 설명과 CIDR 규칙을 입력 후 등록하면 등록된 IP대역만 API호출이 가능합니다.  

### CIDR 규칙과 등록
network prefix / bit (0~32) 범위 내에서 등록이 가능합니다.  
CIDR 대역이 넓은 경우 CIDR 계산기를 활용 하는 것을 권장 합니다.  

예시1.  
![image](https://user-images.githubusercontent.com/86043374/128290525-8cd72e7e-3470-47cf-8c3f-b3dce084881b.png)  
255.255.255.255 `1개` IP 범위를 CIDR 변환  
CIDR : 255.255.255.255/32    
  
  
  
예시2.  
![image](https://user-images.githubusercontent.com/86043374/128290571-100740b5-94da-4d40-aaac-f7945336a830.png)  
255.255.255.254 ~255 `2개` IP 범위를 CIDR 변환  
CIDR : 255.255.255.255/31  


## 타임아웃 정보
HTTP 클라이언트 구성 시 타임아웃 예외 처리에 대한 정보 입니다.  
Read-timeout이 발생된 경우 반드시 [망 취소](/api/cancel.md#망취소)를 요청하여 결제 정보 불일치를 방지 해주세요.  

- Connection timeout : `5s`
- Receive(Read) timeout : `30s`  
