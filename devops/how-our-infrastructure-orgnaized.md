# How our infrastructure organized

## AWS 상식 for FE/BE

### Our Infrastructure

- VPC
    - Public Subnet
        - ALB
    - Private subnet
        - ECS
        - Aurora
        - ES
        - EC
        - Lambda
- CF, S3, DynamoDB, SQS/SNS, CW, lambda, X-Ray

### VPC

private vs public?
- public -> internet gateway 붙어있음 외부 접근 O
- private -> VPC 내부에서만 접근가능, 외부 연결하려면 NAT 필요

사용자 정보가 있는 DB는 VPC 내부에 두는게 안전 -> 포트스캐닝 이슈

### Bastion

프라이빗 서브넷은 VPC로만 접근 가능하기 때문에 퍼블릭 서브넷으로 접속가능한 EC2 인스턴스를 만들어야 함

세큐리티 그룹으로 Bastion 인스턴스의 인바운드 포트와 아이피를 지정할 수 있다 (오피스에서만 접근 가능한 식으로)

DB는 EC2 인스턴스의 세큐리티 그룹 사용

### ACL 

- ingress
- egress

### VPN1 (MMT -> AWS)

MMT Network와 VPC 가 IPSec tunnel을 통해서 커넥션 수립. -> MMT 오피스 안에서는 Bastion 안쓰고 프라이빗 서브넷 접근 가능

현재는 서울리전만 이렇고 나중에는 버지니아도 이렇게 연결하는것이 좋다.

### VPN2 (Home -> MMT)

집에서 MMT 네트워크랑 터널링 뚫어서 MMT로컬 환경에 있는 젠킨스 접속 가능

### VPC peering

VPC 끼리 통신하는 용도. beta/prod 로그를 람다로 보낼때 관리용 VPC와 피어링이 되어있어서 가능한것

- Q. VPC 꼭 이렇게 나눠야만 했나?
    - 목적별로 나누는건 필요 두 환경이 접근 가능한 영역대가 다름 + 대역폭 이슈 있음

### 우리가 AWS에 접근하는법

#### 개인
1. AWS 어카운트 만들어주고 MFA 설정, access key id와 secret key 부여
2. policy에 따라 접근

#### 앱
1. 인스턴스에 role 을 부여해서 키를 직접 가지지 않는 형태로 외부 서비스에 접근
    - 앱이 직접 Access key ID와 secret access key를 안 건드리는게 best practice

## AWS에 올라와있는 서비스를 접속하면 무슨 일이 일어날까?

### Internet -> CF
- Route53이라는 DNS이 CF 엔드포인트를 가르킴
- TLS 과정에서 aws cert manager 에서 만들어진 cert 사용 -> server authentication

### CF -> (ECS / Lambda / S3)
- CF에 behavior가 정해져 있어서 path에 따라 라우팅, 정해진거 못찾으면 디폴트로 라우팅
- API는 ECS/Lambda
- 서버사이드렌더링도 ECS안에 있고
- SPA + 기타 잡다한거는 S3에 있음

#### Cloudfront?
- edge location
    - 한국에 있는 유저가 버니지아 MMT에 접근할때 매번 미국까지 RTT 하는것보단 엣지 로케이션에 캐시해놓고 가까운 엣지 로케이션에서 가져올 수 있게 한다.
- 캐시컨트롤로 브라우저상에서 캐시하게도 할 수 있다.
- 새로 뭔가 업데이트할때 cloudfront invalidation 하면 엣지의 캐시를 날릴 수 있다.


##### Lambda @edge

CF에는 엣지에 람다를 설정할 수 있다. (제약사항 더 있음)

- 설정할 수 있는 곳
    - viewer req/res
    - origin req/res
- 유즈케이스
    -  CSR 할 때 open graph tag를 캠페인 페이지별로 생성해서 response 할 수 있도록 lambda edge 사용 (편법으로)
    - 예전 shorturl 만들어줄 때도 람다 엣지에서 DB에 접근해서 리다이렉트시켜주는 형식
    - 이미지 섬네일

##### CSR? SSR?
- CSR
    - CF -> S3
- SSR
    - CF -> ECS(Next.JS) for FE
    - 왜?: 기기별로 JS가 편파적인 경우도 있다. + 느림 + SEO
    - 서버에서 대충 만들어주고 브라우저에서 마무리짓는 방식

### 더 자세히

1. First Contact (CSR)
    - Intenet -> CF -> ALB -> FE ECS(Next.JS) -> BE ECS

2. After CSR (SSR)
    - Intenet(SSR App) -> CF -> ALB -> BE ECS

#### WAF

- 일종의 방화벽 
    - user-agent 헤더로 보고 뭐는 거부, 어디서 오는 ip만 접근 가능, 뭐는 뭐로 등등등

### 진짜 결론

Intenet -> (Route53 | WAF | Cert) -> (CF + Lambda @edge) -> (ECS(FE, BE) | Lambda | S3)

## 배포

### deployment 방식

- blue/green
    - 돌아가는 환경이 4개 컨테이너리면 새 배포도 4개의 컨테이너 동일한 환경 설정
    - 멀쩡하면 트래픽 넘겨서 스왑
    - FE는 코드디플로이 이용해 트래픽 스왑 전에 훅 걸어서 캐시 무효화
- rolling
    - healthcheck required
    - maximumPercent / minimumPercent 지정해서 이전 버전이 minimumPercent를 만족하는 한에서 새로운 컨테이너 띄움
    - 새로 전부 health running이 되어야 스위치됨
- canaray
    - 몇분/시간동안 트래픽 일부만 전달했을때 오류가 나지 않으면 환경 스왑

### Sigterm

graceful exit을 위해서 30sec wait -> sigkill

그동안 커넥션 끊고 태스크 처리하고

## 아아아아주 작은 이슈들

- ES sunjeon plugin
- ES logging queue issue
- DynamoDB exponential backoff retry
    - DynamoDB 특성상 분산시스템이라 retry 몇번하면 다 성공할것
- Redis full search  (keys)
    - scan과 namespace를 사용
- Aurora high cpu utilization
    - index issue -> explain query, do CQRS

## MSA의 아쉬움

- 한번에 바꾸지 말고 천천히 때어 나갔으면 얼만 좋았을까...
- do DDD/CA, no NDD