---
description: 유용한 커맨드라인들
---

# Useful Commands

## JSON 예쁘게 출력하기

```bash
curl -GET ... | python -m json.tool
```

회사에서 Kong이란 게이트웨이를 쓰는데 라우트 정보를 받으려고 curl을 치면 줄바꿈이 전혀 없는 JSON 뭉치가 나온다. 도저히 알아볼수 없는 매직아이라 정렬을 할수 없을가 생각하던 도중 쉘 스크립트는 개쩌는 파이프라는게 있기 때문에 curl 출력을 JSON 포매터에 먹여보았더니 이쁘게 포맷된 결과를 받을 수 있었다.

## 커맨드라인에서 JetBrains 계열 IDE 열기

```text
alias charm="pycharm ."
alias lion="clion ."
```

요즘 젯브레인스에서 IDE에 대한 커맨드라인 명령어를 제공한다. alias와 조합해서 쓰면 편하다.

[https://www.jetbrains.com/help/idea/working-with-the-ide-features-from-command-line.html](https://www.jetbrains.com/help/idea/working-with-the-ide-features-from-command-line.html)

## 쉽게 뭔가를 찾자, fzf

`general-purpose command-line fuzzy finder.`

파일을 찾으면서 프리뷰를 보고싶다면 다음의 명령어를 활용해보자.

```bash
fzf --preview "cat {}"
```

### fzf + cd = fd

커맨드라인에서 디렉토리를 전환할때 매번 숨쉬는것과 같이 ls 한번 치고 cd를 수행하는것이 귀찮기 때문에 fzf로 옮겨갈 디렉토리를 보고 바로 선택한 디렉토리로 옮겨가고 싶었다.

먼저 [fzf 공식 예제](https://github.com/junegunn/fzf/wiki/examples#changing-directory)에서 기본 틀을 빌렸다.

```bash
fd() {
  DIR=`find * -maxdepth 0 -type d -print 2> /dev/null | fzf-tmux` \
    && cd "$DIR"
}
```

fzf에는 프리뷰 기능도 있기때문에 프리뷰로 선택한 디렉토리 안에 무엇을 있는지도 동시에 보기 위해 tree를 활용한 프리뷰를 추가했다.

```diff
fd() {
+  DIR=`find * -maxdepth 0 -type d -print 2> /dev/null | fzf-tmux --preview "tree {} -L 3"` \
-  DIR=`find * -maxdepth 0 -type d -print 2> /dev/null | fzf-tmux` \
    && cd "$DIR"
}
```

