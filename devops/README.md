# DevOps

## Links
* [모든 컨테이너/이미지 삭제 커맨드](https://countryxide.tistory.com/86)
    * `docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)`
    * `docker rmi $(docker images -q)`
* [Real-time Service Configuration으로 Consul을 신주소 서비스에 적용한 사례](https://woowabros.github.io/tools/2018/10/08/location-service-with-rcs.html)