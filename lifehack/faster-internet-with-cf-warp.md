# Faster internet with Cloudflare WARP

## 개요

모바일 인터넷이 최적화된 UDP 기반 프로토콜을 중심으로 기기에서 가장 가까운 클라우드플레어 서버까지 암호화한 통신을 보낸 후 클라우드플레어 서버에서 목적지까지의 통신을 대신 하는 방식으로 (유료 플랜인 워프 플러스는 아르고 스마트 라우팅을 통해 목적지 근처까지 클라우드플레어 망을 통하는 등 라우팅 최적화가 추가로 들어간다.) 최적화된 인터넷 성능을 제공하는 서비스.

기술적으로 와이어가드 VPN을 사용해 만들어져 있다.

한국 한정으로 통신사 해외망 속도와 차원이 다른 속도를 제공한다. 집에서 테스트해봤을때는 기본 KT망을 사용했을경우 샌프란시스코까지 1.08mbps가 나왔지만 WARP+ 를 사용했을 경우 148mbps를 뽑아줬다. (거의 인터넷에 붙어있다시피 하기 때문에 한달에 5달러정도를 투자할 가치가 있다고 여겨서 WARP+를 사용중이다.)

https://blog.cloudflare.com/1111-warp-better-vpn/

## Mobile

플레이 스토어나 앱스토어에서 1.1.1.1 을 다운로드 하자.

## MacOS

아직까지는 공식 클라이언트가 없기때문에 와이어가드를 사용해 직접 연결을 구성해야 한다. 맥 앱스토어에서 [와이어가드](https://apps.apple.com/kr/app/wireguard/id1451685025?l=en&mt=12)를 설치하고 [wgcf](https://github.com/ViRb3/wgcf)를 다운로드받아서 원하는 디렉토리(나는 홈 디렉토리에 추가했다)에 옮기자.

```bash
$ sudo chmod +x wgcf
$ <PATH에 wgcf 추가>
$ wgcf register
$ wgcf generate
```

홈 다렉토리 안에 만들어진 `wgcf-profile.conf` 파일을 와이어가드에서 불러와서 VPN을 구성하고, 원하는 이름으로 바꾼 후 활성화하면 맥에서 WARP 를 사용할 수 있다.

### WARP+ 사용하기

모바일 앱에서 키를 복사한 후 wgcf를 업데이트하자

```bash
$ WGCF_LICENSE_KEY=<YOUR KEY> wgcf update
```