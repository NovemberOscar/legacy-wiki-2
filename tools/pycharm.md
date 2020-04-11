# PyCharm

## 팁

Help &gt; Change Memory Settings.에서 [힙 메모리 한도](https://www.jetbrains.com/help/idea/increasing-memory-heap.html)를 4GB\(4096MB\) 까지는 늘려주자.

## 확장 설치

주로 룩앤필에 관련되서만 설치하는것같다. 프로페셔널 버전을 사용하니 왠만한 기능이 포함되어있어 편리하다.

* Material UI Theme
* Nyan Progress

## 폰트 & 컬러 스킴

* Fira Code를 사용하다 JetBrains Mono로 갈아탔다.
* pytest 에서 데코레이터가 많으면 \(4줄 초과\) 현란해서 가독성이 너무 떨어진다. 데코레이터는 어두운 색으로 지정해서 밝은 함수 시그니처와 구분되게 한다.
* 타입 힌트도 기본 하얀색이면 너무 더럽다. 회색으로 변경하면 조금 나은 편.

## File Watcher 설정

코드를 저장할때마다 포맷할수 있다. 다만 오토 세이브에도 포맷이 돌면 작성중에 파일이 이상하게 바뀌어버리는 경우가 있기 때문에 Ctrl+S를 눌렀을때만 포맷되게 하는것이 정신건강에 이롭다.

기본적으로 isort와 black을 사용한다.

