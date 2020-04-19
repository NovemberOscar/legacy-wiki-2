# Dos & Don'ts

Source: [Learning F# - Dos and Don'ts](https://fsharpforfunandprofit.com/learning-fsharp/#dos-and-donts)

## Don't

* `mutable`키워드를 떡칠하지 말자. 가변 상태 없이 복잡한 함수를 짜는 것은 함수형을 이해하는데 도움이 된다.
* `for` 그리고 `if-then-else` 를 쓰지 말자. 패턴 매칭과 재귀를 써라.
* `dot notation`을 사용하지 말자. `"hello".Length` 보단 `String.length "hello"` 를 쓰도록 하자. 고차 함수를 사용할때는 이 방식이 필수적이다.
* 클래스 대신 가급적 튜플, 레코드, 유니언같은 순수한 타입만 사용하자. 
* 디버거는 도움이 안된다. 컴파일러 에러 잡는 가장 좋은 방법은 머리를 쓰는 것이다.

## Do

* 타입(특히 유니언)을 많이 만들어라. 가볍고 쉽우며 도메인 모델을 표현하기도 좋다.
* `list`,  `seq`, 그리고 연관 라이브러리들을 이해해라. 폴드나 맵은 강력한 도구다. + 고차 함수를 이해하는데도 도움이 된다.
* 콜렉션 모듈을 이해하면 재귀를 피하자. 올바른 꼬리 재귀를 만드는건 힘들다. 컬렉션 모듈의 폴드를 사용하면 쉽개 해결된다.
* 파이프와 합성을 최대한 사용하자. 함수 호출을 중첩하는것보다 훨씬 F#적인 방법이다.
* Do understand how partial application works, and try to become comfortable with point-free (tacit) style.
    * partial을 이해하고 포인트-프리 스타일에 익숙해지자. 
* 인터렉티브 모드에서 코드를 자주 테스트하면서 코드를 만들어라. 막 짜다가 컴파일 터지면 고치기 힘들다.