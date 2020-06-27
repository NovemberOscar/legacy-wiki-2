# Dockerize Unifi Controller

설정이 필요할 때마다 맥북에서 켜서 사용하고 있는 유니파이 컨트롤러를 도커 내부로 옮겨서 상시 기동하게 변경했다.

## 유니파이 컨트롤러 백업하기

- Settings > Controller Settings > Backup > Download

다운로드한 .unf 파일을 새 컨트롤러 셋업 화면에서 백업에서 복구를 선택해 복구하면 된다.

## 도커 컴포즈로 유니파이 컨트롤러 띄우기

Traefik을 사용하기 때문에 Traefik 관련 설정을 추가했다.

```yaml
version: '3.3'
services:
  unifi-controller:
    image: linuxserver/unifi-controller:latest
    environment:
      PGID: '1000'
      PUID: '1000'
    ports:
     - 3478:3478/udp
     - 10001:10001/udp
     - 8080:8080
     - 8443:8443
     - 1900:1900/udp
     - 8843:8843
     - 8880:8880
     - 6789:6789
     - 5514:5514
    volumes:
     - unifi_config:/config
    networks:
     - traefik_net
    logging:
      driver: json-file
    deploy:
      labels:
        traefik.docker.network: traefik_net
        traefik.enable: 'true'
        traefik.http.routers.unifi-controller.entrypoints: web
        traefik.http.routers.unifi-controller.rule: Host(`unifi.local.swarm`)
        traefik.http.routers.unifi-controller.service: unifi-controller
        traefik.http.services.unifi-controller.loadbalancer.server.port: '8443'
networks:
  traefik_net:
    external: true
volumes:
  unifi_config:
    external: true
```

## 인증서 이슈

크롬이 자가 서명한 인증서는 허용하지 않기 때문에 어쩔 수 없이 사파리를 사용했다.

## 도커에 띄워진 컨트롤러에서 장비를 찾을 수 없을 때

USG 내부로 접속해서 컨트롤러의 위치를 변경해야 한다

```
set-inform http://<controller>:8080/inform
```

