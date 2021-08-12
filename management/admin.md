## 개발정보

### 활용	
로그인 후 상점을 생성하면 개발에 필요한 정보를 ‘개발정보‘ 탭에서 확인 할 수 있습니다.  
개발정보의 기능을 통해 연동에 필요한 KEY관리, IP보안, 웹훅과 로그 확인을 할 수 있습니다.    

![image](https://user-images.githubusercontent.com/86043374/128664778-73f6915a-f131-44a5-98a6-b76eccf4ed2d.png)  

### 기능 요약
#### KEY 정보
JS SDK 인증을 위한 Client-key API호출을 위한 Secret-key 발급 및 관리  
- [기능설명](/management/admin.md#기능설명)
- [재발급](/management/admin.md#재발급)

#### IP보안
API호출 IP제한 정책을 통한 API보안 관리
- [기능설명](/management/admin.md#기능설명-1)
- [추가](/management/admin.md#추가)

#### 웹훅
웹훅의 셋팅, TEST, 실패 웹훅의 재전송
- [기능설명](/management/admin.md#기능설명-2)
- [추가](/management/admin.md#추가-1)
- [TEST 호출](/management/admin.md#test호출)
- [재전송](/management/admin.md#재전송)
- [로그](/management/admin.md#로그-1)

#### 로그
API, 웹훅의 요청 응답 로그를 통해 빠른 디버깅
- [기능설명](/management/admin.md#기능설명-3)
- [상세보기](/management/admin.md#상세보기)

## KEY정보	
### 기능설명
개발정보 탭의 KEY 정보는 결제창 승인 모델의 선택과 API인증 방식을 선택하여 KEY를 발급 및 삭제 할 수 있습니다.  
  
![image](https://user-images.githubusercontent.com/86043374/128665135-7e576957-c6bc-4540-94b5-df99eef0a6e5.png)

#### 결제창 승인방식 [결제창 JS SDK 검토하기] (/api/payment.md#js-sdk) 
선택된 결제창 승인 방식은 클라이언트 키 항목에 표기 됩니다 
- Server승인 모델 :  결제창 인증(카드사 및 원천사)과 승인(결제) API 호출이 분리된 모델
- Client승인 모델 :  결제창의 인증과 승인이 동시에 처리되어 응답 모델 Client승인 모델이 제공됩니다. 

#### API 인가방식
선택된 API 인가방식은 시크릿 키 항목에 표기 됩니다.
- [Basic 인증](/common/api.md#basic-auth)  
- [Token 인증](/common/api.md#bearer-token) 

### 재발급
개발정보 > KEY정보 > 재발급 버튼을 클릭하면 KEY 발급이 가능 합니다.  
최대 5개의 KEY생성이 가능하며 KEY를 변경하는 경우 TEST가 필요한 경우 생성하여 활용 할 수 있습니다.  
   
![image](https://user-images.githubusercontent.com/86043374/128665322-0b1497a8-a56c-4eef-82a1-54ae39794142.png)


> 시크릿키는 외부에 노출이 되지 않도록 주의가 필요하며 외부 유출시 반드시 KEY를 재발급하여 변경 해야 합니다.  
> 클라이언트 키와 시크릿 키가 삭제되는 경우 복구되지 않으며 삭제된 키를 통해 결제가 발생되지 않아 변경 작업 시 주의가 필요 합니다.   

## IP보안(IP접근 제한)
### 기능설명
IP보안 상점이 사용하는 API의 접근 가능한 IP를 제한 하여 보안을 강화 할 수 있는 기능 합니다.  
CIDR 규칙을 통해 제한 범위를 설정할 수 있고, 등록 후 ‘IP TEST’ 버튼을 클릭 하여 등록된 규칙에 이상이 없는지 반드시 체크 해주세요.  
  
![image](https://user-images.githubusercontent.com/86043374/128665366-aa74e7e2-b667-4a76-be05-8fae851e15b4.png)


### 추가
개발정보 > IP보안 > 추가 버튼을 클릭하면 IP제한 규칙 등록을 위한 팝업이 노출 됩니다.  
설명과 IP제한 규칙을 등록하면 IP보안을 위한 준비가 완료 됩니다.  


![image](https://user-images.githubusercontent.com/86043374/128665418-caa1390f-18ce-4925-bad2-0c890e80301a.png)

> IP제한 규칙을 추가하는 경우 등록된 CIDR 범위에서만 결제가 진행 됩니다.  
> 서비스 운영 중 IP제한 규칙을 추가하는 경우 주의 해주세요.

## 웹훅
### 기능설명
웹훅은 API의 이벤트를 Server-side로 응답 받아 추가적인 비즈니스 로직을 구현 할 수 있는 기능으로  
가상계좌 처럼 계좌 생성과 입금시점 차이가 발생하는 결제 수단을 사용하는 경우 반드시 구현이 필요 합니다.  
개발정보 탭 에서 제공되는 웹훅은 추가/삭제관리, TEST 호출, 재전송, 로그 체크 기능을 제공 합니다.      

![image](https://user-images.githubusercontent.com/86043374/128665498-39293a3d-d1c0-4dc9-9502-d2b223d81597.png)


#### 기능요약
- [추가](/management/admin.md#추가-1) : 결제수단을 선택하여 웹훅을 추가 하는 기능
- [TEST 호출](/management/admin.md#test호출) : 웹훅 등록 후 등록된 End-point로 Test 전문을 전달하는 기능
- [재전송](/management/admin.md#재전송) : 웹훅 전송 실패시 처리 가이드
- [로그](/management/admin.md#로그-1) : 전달된 웹훅의 로그 확인 가이드

#### 웹훅 발송 시점
- 결제(승인) 되었을 때(모든 지불수단)
- 가상계좌가 발급(채번) 되었을 때
- 가상계좌에 결제금액이 입금 되었을 때
- 결제가 취소 처리되었을 때 (API 또는 가맹점관리자 취소)

### 추가
![image](https://user-images.githubusercontent.com/86043374/128665650-59e1c404-383c-45a8-958d-e97dfcf8f5bc.png)  
웹훅을 전달 받을 End-point와 결제수단을 선택하고 등록하면 웹훅 등록이 완료 됩니다.  
유효한 도메인을 등록해야 하며 등록 후 TEST호출 버튼을 통해 웹훅 전문이 정상적으로 응답되는지 반드시 확인 해 주세요.  

### TEST호출
#### Test 호출 처리 프로세스
![image](https://user-images.githubusercontent.com/86043374/128665697-d63165a4-0da7-4499-bb67-6d683c036f3a.png)  
웹훅 등록 후 TEST호출 버튼을 클릭하면 등록된 End-point로 test웹훅 전문이 전달 됩니다.  
또한 등록된 End-point에서 웹훅 처리가 성공적으로 되었는지 체크가 가능 합니다.  

#### 개발정보-웹훅
![image](https://user-images.githubusercontent.com/86043374/128665763-ce74dccf-d672-4670-ad9c-5ce2a4e5e108.png)

### 재전송

웹훅 재전송은 네트워크 이슈 등의 문제로 인해 웹훅 처리의 문제가 발생 하여  
재전송이 필요한 경우 활용 할 수 있습니다.  
웹훅 재전송은 다음과 같은 흐름으로 진행 됩니다.  

- 로그인 > 개발정보 > 로그 상세보기 > 웹훅 탭 클릭
- 주문번호를 통해 재전송이 필요한 웹훅 검색
- 검색이 완료된 경우 거래를 선택하여 오른쪽 상단 재전송 버튼 클릭 

> 웹훅 재전송이 반복적으로 실패 하는 경우 다음과 같은 확인이 필요 합니다.
> - [방화벽 정책](/preparations.md#방화벽-정책) 확인 후 웹훅 Test버튼 클릭하여 정상인지 체크
> - [웹훅 매뉴얼](/api/hook.md#over-view)을 통해 연동이 정상인지 체크


### 로그
가맹점 디버깅 편의를 위해 웹훅 로그를 제공하고 있습니다.  
응답된 웹훅과 정보 비교가 필요하거나 재전송이 기능이 필요한 경우 활용 할 수 있습니다.  
웹훅 로그를 통해 다음과 같은 정보를 확인 할 수 있습니다.  

- 웹훅이 전달된 시간과 정보
- 웹훅 전달시 body 정보
- 웹훅 재전송을 위한 버튼 

## 로그
### 기능설명
나이스페이는 개발과 디버깅의 편의성을 위해 웹로그를 제공하고 있습니다.  
local 개발 환경의 로그와 API호출시 처리된 웹로그를 비교 한다면 효과적으로 디버깅이 가능 합니다.  

로그인 > 개발정보 하단에서 표기되는 단순 이벤트성 로그를 통해 최근 호출된 인터페이스 로그 확인이 가능하며  
로그 list를 클릭하면 선택된 로그의 상세 정보 확인이 가능 합니다.  

#### 주요기능
- 로그 : 결과코드, 주문번호, 시간등이 표기된 단순 이벤트성 로그  
- 상세로그 : 조회 및 검색 기능과 Request / Response body 상세 정보를 제공하는 기능  

### 상세보기
로그 ‘상세보기’는 요청된 인터페이스의 로그를 검색하여  
상세한 Request / Response body 정보를 제공하는 기능 입니다.  
상세보기는 다음과 같은 기능을 제공 합니다.  

#### 로그의 검색
- 선택된 로그의 상세 Request / Response body 제공
- 선택된 거래와 연관된 거래의 Timeline
- 웹훅과 일반 로그의 분리
