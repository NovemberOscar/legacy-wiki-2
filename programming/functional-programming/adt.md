# ADT

## ADT

프로그래밍, 특히 함수형 프로그래밍과 타입 이론에서 ADT는 여러가지 원시 타입의 조합힌 합성 타입의 일종이다. 크게 곱\(Product\) 타입과 합\(Sum\) 타입으로 나누어진다.

ADT의 값들은 패턴 매칭을 통해 분석된다.

## 곱 타입

흔히 튜플, 레코드, 구조체 타입 등으로 불리는 타입이다.

곱 타입은 각 타입이 가질수 있는 값의 개수들을 곱한 만큼의 인스턴스를 가질 수 있다.

다음의 튜플은 int 집합 \* int 집합 만큼의 인스턴스를 가질 수 있다.

```fsharp
type intAndInt = int * int
```

## 합 타입

태그드 유니언, 열거형 등으로 불리는 타입이다.

다음의 `Option` 타입은 `Some<T>` **또는** `Empty`라는 것을 나타낸다. 따라서 다음의 유니온이 가질 수 있는 인스턴스의 개수는 `Some<T>` + `None` 만큼이다.

```fsharp
type Option<'a> =
   | Some of 'a
   | None
```

### References

* [https://fsharpforfunandprofit.com/posts/tuples/](https://fsharpforfunandprofit.com/posts/tuples/)
* [https://fsharpforfunandprofit.com/posts/discriminated-unions/](https://fsharpforfunandprofit.com/posts/discriminated-unions/)
* [https://en.wikipedia.org/wiki/Algebraic\_data\_type](https://en.wikipedia.org/wiki/Algebraic_data_type)

