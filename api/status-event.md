## 카드 이벤트

## Over-view
카드 이벤트 조회 API는 요청된 기준금액에 해당되는 카드사별 이벤트 정보를 응답 합니다.  
이벤트 정보를 결제자에게 전달하여 카드사 선택을 위한 정보를 편리하게 제공할 수 있습니다. 

> 기준금액이 5만원 이하 인 경우 무이자는 미제공하는 것으로 응답 됩니다. 

<br>

### 샘플 코드
```bash
curl -X GET 'https://api.nicepay.co.kr/v1/card/event?amount={금액}&useAuth=false&ediDate={ISO 8601 형식}&...' 
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMT...'
```

<br>

## 요청 명세
```bash
GET /v1/card/event?amount={금액}&useAuth=false&ediDate={ISO 8601 형식}&...   HTTP/1.1  
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

| Parameter       |                 | Type   | 필수 | Byte | 설명                                  |
|-----------------|-----------------|--------|------|------|---------------------------------------|
| interestFree |                 | Array  |      | -    | 제공되는 모든 무이자 할부정보<br>- NICEPAY에서 기본제공하는 무이자와 상점무이자가 merge된 정보<br>- 카드코드별 하나의 무이자 Object가 응답됩니다.                     |
|                 | cardCode        | String | O    | 3    | 카드사 코드<br> 신용카드사별 코드|
|                 | cardName        | String | O    | 20   | 카드사 이름<br>예) 비씨                           |
|                 | freeInstallment | String | O    | 200  | 무이자 할부개월 <br>콜론(:)을 구분자로 할부개월 나열<br>ex) 02:03:04:05<br>- 설명 : 2,3,4,5개월 무이자 할부 제공    |

[전체 문서 목록](../README.md)
