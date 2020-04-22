# DevOps

## Links
* [모든 컨테이너/이미지 삭제 커맨드](https://countryxide.tistory.com/86)
    * `docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)`
    * `docker rmi $(docker images -q)`