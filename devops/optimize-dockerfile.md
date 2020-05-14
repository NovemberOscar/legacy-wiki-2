# Optimize Dockerfile

회사에서 사용하던 파이썬-알파인을 베이스로 하던 도커 이미지의 빌드 시간이 30분을 넘어가는 등 여러모로 생산성에 악영향을 끼쳐서 속도와 용량 모두 최적화하는 방안을 찾아보았다 

최종적으로는 빌드 시간은 30분에서 1분, 최종 런타임 이미지는 100MB 정도 증가한 330MB이 되었다.

## 알파인 리눅스에서 데비안 기반 이미지로 전환

알파인 리눅스는 musl과 glibc 때문에 생기는 성능 하락도 있지만 결정적으로 알파인 리눅스에서는 모든 파이썬 휠을 다시 빌드해야 하고 휠을 빌드하기 위한 `build-base`, `gcc` 등을 설치해야 하기 때문에 패키지 자체를 설치하는 시간도 엄청나게 길어진다. 따라서 모든 빌드 의존성이 포함되어 있는 데비안 버스터 기반 파이썬 이미지로 베이스 이미지를 교체했다.

## 미러 서버를 사용하기

pypi 에서 패키지를 받아 올 때 카카오 미러를 기본으로 사용하도록 설정했다.

그리고 추가적으로 설치할 데비안 패키지는 없었지만 만약 생기게 된다면 데비안 패키지 또한 카카오 미러 서버에서 패키지를 다운로드하도록 설정하자.

## poetry install 대신 pip install 사용하기

레이어 캐싱과 설치 속도 향상를 위해 lock 된 의존성을 해시를 제외하고 requirements.txt 형태로 내보낸 후 pip 를 사용해 설치한다. 그 다음 검증을 위해 poetry install 을 수행하면 속도와 안전함 모두 얻을 수 있다.

## 멀티 스테이지 빌드

멀티 스테이지 빌드를 활용하면 최종적으로 나오는 런타임 이미지와 빌드 단계의 이미지를 분리할 수 있다. 

이를 사용해 빌드용 이미지의 베이스 이미지로는 데비안 버스터 또는 우분투 이미지를 사용해 왠만한 의존성이 깔려있는 이미지를 사용해 필요한 의존성을 모두 설치한 뒤, 경량 이미지를 베이스로 하는 런타임 이미지에 의존성을 모두 붙여넣으면 최종적으로는 불필요한 용량은 모두 제거된 이미지가 나오게 된다

후에 이미지 용량을 검사해본 결과 빌드 이미지는 1GB 를 넘어가지만 최종 런타임 이미지는 ~330MB가 된 것을 볼 수 있었다.

```
server on  dockerfile-opt [!] is 📦 v0.1.0 via 🐍 v3.6.1 on ☁️  ap-northeast-1 took 9s 
❯ docker images  
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
<none>              <none>              c4b5c1bfb10d        22 minutes ago      331MB
<none>              <none>              58f193ca60f3        23 minutes ago      1.1GB

```

그리고 파이썬 한정으로 파이썬 패키지들을 그대로 복사해 오기 위해서 가상환경에 모든 패키지를 설치한 후 런타임 이미지에서 가상환경을 그대로 복사해와 사용한다.

```Dockerfile
FROM python:3.6-buster AS build
COPY poetry.lock pyproject.toml /
RUN pip install \
    --index-url http://mirror.kakao.com/pypi/pypi/ \
    --index-url http://mirror.kakao.com/pypi/simple/ \
    --trusted-host mirror.kakao.com poetry
RUN poetry config virtualenvs.in-project true \
 && poetry export --without-hashes -f requirements.txt \
 |  poetry run pip install --upgrade \
    --index http://mirror.kakao.com/pypi/pypi \
    --index-url http://mirror.kakao.com/pypi/simple \
    --trusted-host mirror.kakao.com -r /dev/stdin \
 && poetry install --no-interaction --no-ansi --no-dev


FROM python:3.6-slim
COPY --from=build /.venv /.venv

...

ENTRYPOINT ["/.venv/bin/python"]
CMD ["<app_name>"]

```

## 참고문헌

* [파이썬 멀티 스테이지 빌드](https://pythonspeed.com/articles/multi-stage-docker-python/)
* [도커에서 venv 사용하기](https://pythonspeed.com/articles/activate-virtualenv-dockerfile/)
* [포에트리 도커 캐싱 이슈](https://github.com/python-poetry/poetry/issues/1301)
* [알파인 리눅스가 파이썬에 적합하지 않은 이유](https://pythonspeed.com/articles/alpine-docker-python/)