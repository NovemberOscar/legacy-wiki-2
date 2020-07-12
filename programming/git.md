# Git

## Tips

* git status 필수 옵션
  * git status -s -uall
  * -uall: untracked 파일들이 디렉토리 아래에 있을 경우에 디렉토리만 보여주는것이 아닌 모든 파일을 다 보여줌
  * -s: short 포맷으로 간략하게 보여줌
  * [git-status Documentation - Git](https://git-scm.com/docs/git-status)
* git pull 필수 옵션: [자동으로 리베이스 & 스태쉬](https://cscheng.info/2017/01/26/git-tip-autostash-with-git-pull-rebase.html)

  ```bash
  git config --global pull.rebase true
  git config --global rebase.autoStash true
  ```

## Links

* [Pro GIt](https://git-scm.com/book/ko/v2)
  * 깃은 이 책 한권으로 끝난다.
* [편리한 git alias 설정하기](https://johngrib.github.io/wiki/git-alias/)
  * preview 도구를 bat으로 교체하는 등 조금 변경해 사용중.

