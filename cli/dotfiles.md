---
description: 'https://github.com/NovemberOscar/dotfiles'
---

# dotfiles

dotfiles는 `.`으로 시작하는 설정이나 설치 정보를 담는 파일들의 모음을 말한다. 간단히 말해 테라폼을 사용하는것처럼 내 컴퓨터 설정도 코드로 관리한다고 보면 편하다. \(물론 테라폼만큼 편하진 않다.\)

일단 대부분의 dotfiles의 구조는 dotfiles로 설정하고자 하는 디렉토리들과 그걸 인스톨하는 쉘/메이크 스크립트로 이루어져있다. 많은 dotfiles의 예시가 있지만 개인적인 컴퓨터 설정인 만큼 각양각색이다. 그러므로 "Best practice"를 찾기보다는 여러가지를 찾아보고 좋은점만을 취사선택하기로 결정했다.

참고한 자료는 다음과 같다

* [dotfiles 만들기 - Appkr.memo\(new Story\)](https://blog.appkr.dev/work-n-play/dotfiles/): 가장 먼저 나오는 자료. 하지만 outdated된 자료가 많아서 중간에 닫았다.
* [Your unofficial guide to dotfiles on GitHub](https://dotfiles.github.io/)
* [jongmin92/dev-settings](https://github.com/jongmin92/dev-settings)
* [mrsakkaro/dotfiles](https://github.com/mrsakkaro/dotfiles)
* [johngrib/dotfiles](https://github.com/johngrib/dotfiles)
* [holman/dotfiles](https://github.com/holman/dotfiles)

## 무엇을 백업해야 하는가?

일단 가장 널리 관리하는것들은 macOS 설정들, gitconfig, 쉘, 그리고 Homebrew 설정이다.

일단은 그 중에서 gitconfig, Homebrew, 그리고 쉘 설정만 우선적으로 백업하기로 결정했다. 추후에는 IDE와 macOS 설정도 추가해볼 생각이다.

또한 인스톨 스크립트는 쉘 스크립트 대신 일단 익숙한 Makefile을 사용한다. 추후에는 [dotbot](https://github.com/anishathalye/dotbot)이라는 것을 사용해볼수도 있을것같다.

### Homebrew

일단 Brewfile을 만들어 현재 깔려있는 패키지들을 모았다.

```bash
brew tap homebrew/bundle
brew bundle dump
```

Homebrew에 대해 조사하다가 `mas`라는 툴로 맥 앱스토어 앱도 한곳에서 관리할수 있다는 것을 알아내서 사용하기 위해 설치했다. account 명령어로 현재 로그인된 어카운트를 확인할 수 있고 list 명령어로 설치된 프로그램의 목록들도 가져올 수 있다.

```bash
brew install mas
mas account
mas list
```

이후 Brewfile의 가독성을 조금 수정한 이후 홈 디렉토리의 Brewfile을 dotfiles 내부로 옮긴 후 홈 디렉토리에 symlink를 걸었다.

```text
ln -snf Brewfile ~/Brewfile
```

### .gitconfig

회사 동료분 스크립트에서 많은 부분을 가져와서 유저네임과 이메일, 그리고 서명 키를 대화형으로 완성할수 있도록 구성했다.

```properties
[user]
	name = {{GIT_NAME}}
	email = {{GIT_EMAIL}}
    signingkey = {{GIT_SIGN_KEY}}
```

이 템플릿을 이런 Makefile을 사용해서 완성할 수 있다.

```makefile
.PHONY: git
git: ## Install git configs.
	ln -sfn $(CURDIR)/gitalias $(HOME)/.gitalias
	@cp $(CURDIR)/gitconfig $(HOME)/.gitconfig
	@read -p "Enter your name: " git_name; \
		sed -i -e "s/{{GIT_NAME}}/$$git_name/g" $(HOME)/.gitconfig
	@read -p "Enter your e-mail: " git_email; \
		sed -i -e "s/{{GIT_EMAIL}}/$$git_email/g" $(HOME)/.gitconfig
	@read -p "Enter your GPG key ID: " git_sign_key; \
		sed -i -e "s/{{GIT_SIGN_KEY}}/$$git_sign_key/g" $(HOME)/.gitconfig
```

~~약간의 문제로 이런식으로 사용하면 symlink가 아니기 때문에 한쪽에서 alias를 수정한다 해도 다른쪽에는 반영되지 않는 문제가 있다. aliass는 include로 사용할수 있도록 개선할 필요가 있다.~~

gitconfig 분문은 카피한 후 alias는 링크를 걸고 gitconfig가 인클루드해서 사용하도록 변경했다.

### .zshrc

현재 있는 .zshrc 파일을 dotfiles 아래로 복사하고 있던 파일을 지운다음 symlink를 걸었다.

~~alias 들을 추후에 분리할 필요가 있을것 같다고 느낀다.~~

```makefile
.PHONY: zsh 
zsh: ## Install the zsh related dotfiles.
	@echo "Starting zsh Setup..."
	mkdir -p ~/.zfunc
	@cp $(CURDIR)/zsecrets $(HOME)/.zsecrets
	@read -p "Enter your GitHub token: " github_token; \
		sed -i -e "s/{{GITHUB_TOKEN}}/$$github_token/g" $(HOME)/.zsecrets
	ln -sfn $(CURDIR)/zshrc $(HOME)/.zshrc
	ln -sfn $(CURDIR)/fd $(HOME)/.zfunc/fd
	git clone https://github.com/davidparsson/zsh-pyenv-lazy.git $(HOME)/.oh-my-zsh/custom/plugins/pyenv-lazy 2>/dev/null ||:
	git clone https://github.com/lukechilds/zsh-nvm $(HOME)/.oh-my-zsh/custom/plugins/zsh-nvm 2>/dev/null ||:
	@echo "Done! (zsh)\n"
```

zfunc로 함수들을 옮긴 후 로딩해서 사용하고 aws 키나 깃허브 토큰같은 민감한 정보들은 git과 동일한 방식으로 설정하도록 바꾸었다. 실행시간을 줄이기 위해 lazy-loading을 위한 플러그인을 설치하는 명령어도 추가했다.

### iTerm2 설정

```text
iTerm2 > Preferences > General > Preferences > Load preferences from a custom folder or URL
```

을 클릭해 dotfiles 내부로 지정하면 자동으로 com.googlecode.iterm2.plist 파일이 생성된다. 새로 설정을 돌려놓을 때도 똑같이 하면 이미 있는 파일을 읽어들인다.

### Rust, Poetry 설치 스크립트

pyenv는 brew를 통해 설치되기 때문에 python 설치 스크립트는 따로 존재하지 않는다.

#### Rust

rustup이 깔려있지않다면 설치하고 자동완성과 프로파일을 설치한다.

```makefile
RUST := $(HOME))/.cargo/bin/rustup

.PHONY: rust
rust: | $(RUST)
    rustup update
    rustup set profile complete
    rustup completions zsh > ~/.zfunc/_rustup
    rustup completions zsh cargo > ~/.zfunc/_cargo

$(RUST):
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

#### Poetry

Poetry도 비슷한 과정으로 설치 가능하다.

```makefile
POETRY := $(HOME)/.poetry/bin/poetry

.PHONY: poetry
poetry: | $(POETRY)
    poetry self update
    mkdir -p $(ZSH)/plugins/poetry
    poetry completions zsh > $(ZSH)/plugins/poetry/_poetry

$(POETRY):
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

기타 툴체인도 유사한 방법으로 설치 가능하다.

## 내 dotfiles

내 dotfiles는 깃허브로 관리중이다.

[NovemberOscar/dotfiles](https://github.com/NovemberOscar/dotfiles)

