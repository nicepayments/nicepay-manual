# 웹훅 URL

## 웹훅 URL 수정

웹훅 URL 서비스는 가맹점 관리자 페이지에서 웹훅 URL 사용 하던 것을 API를 통해 사용할 수 있도록 한 서비스 입니다.
웹훅 **등록** 및 **수정** 시에 해당 결제수단의 나이스페이먼츠에서 더미 데이터를 발송하여 가맹점은 웹훅 응답을 확인해볼 수 있습니다.

|                                                   설명                                                    | HttpMethod | URI                             |
|:-------------------------------------------------------------------------------------------------------:|:----------:|:--------------------------------|
|   [웹훅 URL 등록](https://github.com/nicepayments/nicepay-manual/blob/main/api/webhook/webhook-create.md)   |    POST    | /v1/webhook                     |
|  [웹훅 URL 조회](https://github.com/nicepayments/nicepay-manual/blob/main/api/webhook/webhook-retrieve.md)  |    GET     | /v1/webhook                     |
| **[웹훅 URL 수정](https://github.com/nicepayments/nicepay-manual/blob/main/api/webhook/webhook-update.md)** |    POST    | **/v1/webhook/{method}/update** |
|   [웹훅 URL 삭제](https://github.com/nicepayments/nicepay-manual/blob/main/api/webhook/webhook-delete.md)   |    POST    | /v1/webhook/{method}/delete     |



### 설명

웹훅 URL 수정 서비스는 특정 결제수단의 웹훅 URL 정보를 수정할 수 있는 서비스입니다.

웹훅 URL 수정 시에 웹훅 응답 샘플 데이터를 받아보실 수 있으며, 응답 값으로 "OK" 값을 반환하여야 합니다. 

#### ⚠️ 웹훅 URL 서비스의 중요사항

웹훅 URL 등록 및 수정시 웹훅 URL에 대한 검증을 진행하게 됩니다.

웹훅 URL 검증은 위 두 기능을 호출할 때 나이스페이먼츠에서 등록하려는 URL로 샘플 결제통보 응답을 전송하고, 
웹훅 통보용으로 등록하기 위한 URL인지 확인하기 위해 "OK" 라는 응답 값을 확인 합니다.

따라서, 웹훅 URL로 사용하려는 URL의 응답 값으로 "OK" 라는 문자열을 반환하도록 구현이 되어 있어야 합니다.

정리하면,

> 1. 웹훅 URL 등록 및 수정 시, 등록하시려는 URL로 웹훅(결제수단 별 샘플 결제통보)을 전송
> 2. 웹훅(결제통보)에 대한 응답으로 "OK"라는 문자열 값을 확인 
> 3. "OK"라는 문자열까지 확인이 되면 웹훅 URL 등록 및 수정에 대한 정상처리로 등록된 웹훅 URL 리스트를 반환



### 요청 명세

```bash
curl -X POST 'https://api.nicepay.co.kr/v1/webhook/{method}/update'
-H 'Content-type: application/json'
-H 'Authorization: Basic ZWVjOGQzNTA4Y2IwNDI1ZGI5NTViMzBiZjM5...'
-d '{
  "url": "웹훅 통보 URL",
  "managerEmail": "가맹점 관리자 이메일",
}'
```

#### 공통

|      구분      |      필드      |   타입   | 필수 | 길이  | 설명          | 상세설명                                                                        |
|:------------:|:------------:|:------:|:--:|:---:|:------------|-----------------------------------------------------------------------------|
| PathVariable |    method    | String | O  | 10  | 결제수단        | card: 신용카드 <br/> bank: 계좌이체 <br/> vbank: 가상계좌 <br/> cellphone: 휴대폰          |
| RequestBody  |     url      | String | O  | 200 | 가맹점 웹훅 URL  | 결제 통보를 받기 위한 URL <br/> **[주의사항]** <br/> 수신에 대한 응답 값으로 "OK" 문자열을 응답하도록 구현 필요 |
|              | managerEmail | String |    | 255 | 가맹점 관리자 이메일 | 가맹점 관리자 이메일                                                                 |

<br>

### 응답 명세

#### 공통

|      필드       |   타입   | 필수 | 길이  | 설명       | 상세설명                                                                                                            |
|:-------------:|:------:|:--:|:---:|:---------|-----------------------------------------------------------------------------------------------------------------|
|  resultCode   | String | O  |  4  | 결제결과 코드  | 0000: 성공 / 그 외 실패                                                                                               |
|   resultMsg   | String | O  | 100 | 결제결과 메시지 | ex) "정상 처리되었습니다."                                                                                               |
| messageSource | String | O  | 10  | 메시지 출처   | **[출처 리스트]** <br/> 메시지 응답 값에 대한 출처를 나타내기 위한 필드 <br/> nicepay: 응답 결과의 출처는 나이스페이먼츠 <br/> external: 응답 결과의 출처는 제휴사 |

#### 등록된 웹훅 URL 리스트

| 오브젝트 |      필드      |   타입   | 필수 | 길이  | 설명          | 상세설명                                                                        |
|:----:|:------------:|:------:|:--:|:---:|:------------|-----------------------------------------------------------------------------|
| urls |              |        |    |     | 등록된 웹훅 URL  |                                                                             |
|      |    method    | String | O  | 10  | 결제수단        | card: 신용카드 <br/> bank: 계좌이체 <br/> vbank: 가상계좌 <br/> cellphone: 휴대폰          |
|      |     url      | String | O  | 200 | 가맹점 웹훅 URL  | 결제 통보를 받기 위한 URL <br/> **[주의사항]** <br/> 수신에 대한 응답 값으로 "OK" 문자열을 응답하도록 구현 필요 |
|      | managerEmail | String | O  | 255 | 가맹점 관리자 이메일 | 가맹점 관리자 이메일                                                                 |

<br>
