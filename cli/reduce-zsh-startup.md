# Reduce zsh startup time

## 문제의 근원

* pyenv
* nvm
* CPPFLAGS & LDFLAGS

## pyenv & nvm

* nvm
    * 이미 nvm 깃헙에 관련 [이슈](https://github.com/nvm-sh/nvm/issues/730)가 등록되어 있었다. nvm은 다음 플러그인을 설치하고 `NVM_LAZY_LOAD`로 레이지로딩을 활성화하면 된다
* pyenv
    * 구글에 검색했더니 누가 이미 만들어 놨다. 이 [플러그인](https://github.com/davidparsson/zsh-pyenv-lazy)을 설치하고 `ZSH_PYENV_LAZY_VIRTUALENV` 로 레이지로딩을 활성화하면 된다

## CPPFLAGS & LDFLAGS

* 왜 넣어뒀는지 이유를 알수 없어서 일단 그냥 삭제했다.

## 개선 결과

### From
```
dotfiles on  master [!]
❯ for i in $(seq 1 10); do /usr/bin/time zsh -i -c exit; done

        5.33 real         3.23 user         1.82 sys
        4.50 real         2.81 user         1.56 sys
        4.60 real         2.84 user         1.63 sys
        4.73 real         2.92 user         1.67 sys
        4.55 real         2.80 user         1.60 sys
        4.56 real         2.84 user         1.59 sys
        4.91 real         2.98 user         1.76 sys
        4.86 real         2.98 user         1.72 sys
        4.70 real         2.88 user         1.66 sys
        4.45 real         2.77 user         1.55 sys
```

### To

```
dotfiles on  master [!] 
❯ for i in $(seq 1 10); do /usr/bin/time zsh -i -c exit; done

        1.18 real         0.67 user         0.34 sys
        0.55 real         0.37 user         0.20 sys
        0.61 real         0.38 user         0.23 sys
        0.57 real         0.38 user         0.22 sys
        0.53 real         0.36 user         0.19 sys
        0.53 real         0.36 user         0.19 sys
        0.53 real         0.36 user         0.19 sys
        0.56 real         0.37 user         0.20 sys
        0.56 real         0.37 user         0.20 sys
        0.54 real         0.36 user         0.19 sys
```
