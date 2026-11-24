# 약관 조회

## Over-view
약관 조회 API는 결제 호출 전 사용자에게 노출 해야 하는 약관정보를 응답 합니다.  
나이스페이 결제창을 활용하지 않는 결제수단의 경우 약관 정보 API를 활용하여 사용자에게 약관을 고지해야 합니다. 

<br>

### 약관 조회 API 포함 약관
- [전자금융거래 약관](https://github.com/nicepayments/nicepay-manual/blob/main/api/terms/electronicFinancialTransactions.md)
- [개인정보 수집 및 이용 약관](https://github.com/nicepayments/nicepay-manual/blob/main/api/terms/collectPersonalInfo.md)
- [개인정보 제 3자 제공약관](https://github.com/nicepayments/nicepay-manual/blob/main/api/terms/sharingPersonalInformation.md)
- [통신과금서비스 이용약관](https://github.com/nicepayments/nicepay-manual/blob/main/api/terms/telecommunicationCharging.md)

<br>

### 샘플 코드
```bash
curl -X GET 'https://api.nicepay.co.kr/v1/terms?termsType={약관유형}'
-H 'Content-Type: application/json' 
-H 'Authorization: Basic YWYwZDExNjIzNmRmNDM3ZjgzMT...'

```

<br>

## 요청 명세
```bash
GET /v1/terms?termsType={약관 유형} HTTP/1.1  
Host: api.nicepay.co.kr 
Authorization: Basic <credentials>  or Bearer <token>
Content-type: application/json;charset=utf-8
```
| Parameter     | Type   | 필수 | Byte | 설명                                                |
|---------------|--------|------|------|-----------------------------------------------------|
| termsType     | String | O    | 50   | 약관 유형<br>ElectronicFinancialTransactions:전자금융거래   약관<br>CollectPersonalInfo:개인정보 수집 및 이용 약관<br>SharingPersonalInformation:개인정보 제 3자 제공약관<br>TelecommunicationCharging:통신과금서비스 이용약관   |
| returnCharSet | String | 　   | 10   | 응답파라메터 인코딩 방식<br>가맹점 서버의 encoding 방식 전달<br>예시) utf-8(Default) / euc-kr                       |

<br>

## 응답 명세
```bash

Content-type: application/json

```
| Parameter  | Type   | 필수 | Byte  | 상세 설명               |
|------------|--------|------|-------|-------------------------|
| resultCode | String | O    | 4     | 결과코드<br>0000 : 성공 / 그외 실패 |
| resultMsg  | String | O    | 100   | 결과메시지              |
| termsTitle | String | O    | 100   | 약관제목                |
| content    | String | O    | 30000 | 약관내용                |

[전체 문서 목록](../README.md)
