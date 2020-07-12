# Refactoring .zshrc

zshrc 에 너무나 많은 alias와 환경변수, 그리고 각종 편의를 위한 함수들로 설정파일이 계속 길어지는 중이었다. 또한 수많은 플러그인들이 원인들로 의심되는 시작시간 지연이 굉장히 짜증났었다. 

설정들을 묶어 다른 파일로 보내고 그 파일들을 소싱 하는 방식으로 설정을 깔끔하게 만들 수 있기 때문에 Zshrc에 대한 리팩토링을 결정했다.

## Lazy Loading 적용하기

* nvm
  * 이미 nvm 깃헙에 관련 [이슈](https://github.com/nvm-sh/nvm/issues/730)가 등록되어 있었다. nvm은 다음 플러그인을 설치하고 `NVM_LAZY_LOAD`로 레이지로딩을 활성화하면 된다
* pyenv
  * 구글에 검색했더니 누가 이미 만들어 놨다. 이 [플러그인](https://github.com/davidparsson/zsh-pyenv-lazy)을 설치하고 `ZSH_PYENV_LAZY_VIRTUALENV` 로 레이지로딩을 활성화하면 된다

## alias 분리하기

가장 많은 양을 차지하는 것은 alias였기때문에 가장 최우선적으로 분리를 결정했다.

dotfiles에 zalias 파일을 만들고 `~/.zalias` 로 링크를 걸은 후 zshrc에서 `source $HOME/.zalias` 로 로딩하게 변경했다.

## 민감한 정보 분리하기

회사에서 사용하는 커맨드라인 툴은 다양한 토큰 및 정보를 요구하는데 이 토큰을 퍼블릭한 저장소에 올릴수 없어서 민감한 환경변수 템플릿을 만든 후 dotfiles의 메이크파일을 사용해 대화형으로 템플릿을 채운 후 `~/.zsecrets` 로 복사하고 zshrc에서 `source $HOME/.zsecrets` 로 로딩하게 변경했다.

## ZSH 스타일의 PATH 사용하기

기본적인 PATH 환경변수 설정방법은 `export PATH="<P1>:<P2>:<Pn..>"` 일 것이다. 문제는 콜론으로 구분하는것이 양이 많아지면 상당히 더럽다. zsh는 플러그인처럼 [array를 사용해 PATH를 설정](https://unix.stackexchange.com/a/73635)할수 있기 때문에 array를 사용하는 방식으로 변경했다.

```text
path=(
  $path
  $PYENV_ROOT/bin
  $HOME/.cargo/bin
  $HOME/.poetry/bin
  $HOME/.toolbox
)
```

콜론으로 분리하는 방식보다 훨씬 깔끔하게 보이는걸 알 수 있다.

## 함수들을 분리하기

함수 여러개가 zshrc에 인라인으로 들어가있는 형식에서 zfunc 에 함수를 저장해놓고 autoload를 하는 방식으로 변경해서 실행속도 또한 개선했다.

```text
fpath=(
  $fpath
  $HOME/.zfunc
)

...

autoload -Uz ~/.zfunc/**/*
```

```text
~/.zfunc
├── _cargo
├── _rustup
└── fd -> ~/Documents/GitHub/dotfiles/fd
```

