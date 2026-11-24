# 결제·발급	

### 결제창
👉 [Server 승인 모델-결제창](./payment-window-server.md#결제창-server-승인-모델) | [결제 승인](./payment-window-server.md#승인)  
대량 트래픽 예상시 결제창 개발  
<br>
👉 [Client 승인 모델-결제창](./payment-window-client.md#결제창-client-승인-모델) | [승인 금액 검증](./payment-window-client.md#승인-금액-검증)  
하루 10건 이하 트래픽 예상시 결제창 개발  

나이스페이 결제창을 통해 카드,가상계좌,에스크로 등 다양한 결제수단을 활용할때 사용됩니다. 

---

### Access token
👉 [Access token](./payment-access-token.md)  
[Bearer token](../common/api.md#bearer-token) 방식 인증을 통해 API를 호출하는 경우 활용 합니다.  

---

### 빌링  
👉 [빌링 결제창 호출](./payment-subscribe.md#빌링-결제창-호출) | [빌키확정](./payment-subscribe.md#빌키확정) | [빌키승인](./payment-subscribe.md#빌키승인) | [빌키삭제](./payment-subscribe.md#빌키삭제)  
정기,구독 결제 및 간편결제 구현이 필요한 경우 사용됩니다.  

---

### 현금영수증   
👉 [현금영수증 발급](./payment-receipt.md#현금영수증-발급) | [현금영수증 취소](./payment-receipt.md#현금영수증-취소) | [현금영수증 조회](./payment-receipt.md#현금영수증-조회)  
현금성 결제 후 현금영수증을 별도 발급하는 경우 사용됩니다.  

---

### 기타  
👉 [EPAY](./payment-epay.md) : 승인 시스템을 커스텀하게 활용하는 경우 사용됩니다.  
  
[전체 문서 목록](../README.md)
