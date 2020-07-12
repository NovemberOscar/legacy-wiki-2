# JVM memory structure

## JVM 메모리 구조

크게 힙 영역과 네이티브 영역으로 나뉨

힙 영역에는 객체등이 저장된다. GC가 관리하며 GC를 위해 세대가 나누어져 있다. OS가 관리하는 네이티브 영역에는 메타스페이스, 코드 캐시, 스레드 스택등이 올라간다.

### 힙 메모리 구조

보통은 Generational GC를 위해 크게 Young과 Tenured\(Old\) 로 나뉨. JDK 버전 7까지는 힙 내부에 Perm 영역이 있었지만 OOM 이슈가 발생하기 쉬운 문제 등으로 OS가 관리하는 네이티브 메모리 영역의 Metaspace로 옮겨졌다 자세한 건 [기계인간님의 글](https://johngrib.github.io/wiki/java8-why-permgen-removed/)을 참고하자.

GC와 관련된 내용은 [GC 문서](gc.md)를 참고하자

#### Young Gen.

마이너 GC를 수행하는 영역

Eden과 Eden을 정리할때 살아남은 객체들이 들어있는 Survivor 0/1 로 나뉜다.

#### Tenured Gen.

Major GC를 수행하는 영역

Young에서 넘어온다.

#### Region..?

CMS\(Concurrent Mark-Swep\) Collector, Parreral Collector, Serial Collector 등을 사용하면 메모리 영역이 Eden, Survivor 0/1, Old 등으로 딱딱 나뉘지만 G1 Collector를 사용할 경우에는 전체 메모리를 Region으로 나눈 후 각 리전에 역할을 부여하는 방식이기 때문에 경계가 명확하지 않다.

## 참조

* [Java Memory 간단히 살펴보기 - J-Log](https://mirinae312.github.io/develop/2018/06/04/jvm_memory.html)
* [Visualizing memory management in JVM\(Java, Kotlin, Scala, Groovy, Clojure\) - Deepu K Sasidharan](https://deepu.tech/memory-management-in-jvm/)
* [JVM 메모리 구조와 GC - 기계인간 John Grib](https://johngrib.github.io/wiki/jvm-memory/)

