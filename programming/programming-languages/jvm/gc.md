# JVM GC

## 가비지 콜렉션이란?

더 이상 사용되지 않는 객체들을 추적해서 메모리에서 해제하는 작업. 가비지는 보통 Unreachable한 객체들을 지칭함.

## 가비자 컬렉션은 어떻게 수행되나.

GC를 매번 수행할 때 마다 전체 메모리 영역에 대해서 수행하는것은 오버헤드가 너무 크다. JVM의 GC는 weak generation hypothesis에 따라 세대를 나누어 GC를 수행해서 STW 시간을 줄인다.

### 세대

* Young
  * Eden, Survivor0/1 로 나뉨
  * 생성된지 얼마 안된 객체들이 있는 곳. Eden 에 쌓이다가 가득 차면 Minor GC가 돌면 필요없는것들은 버리고 survivor로 이동한다.
  * survivor 둘중 하나는 항상 비어 있어야 한다.
  * survivor 중에서도 여러번 GC를 거쳐도 살아남은 세대 threshold 를 넘은 객체는 오래 살아있어야 하는 것이라고 판단되어 Old 영역으로 넘어간다.
* Old\(Tenured\)
  * 길게 살아있는 객체들이 이곳에 있다.
  * 이곳이 가득차면 Major GC가 수행된다.

## Stop the World \(STW\)

메모리를 정리하려면 애플리케이션 스레드들이 정리하는 도중에 메모리를 어지르지 않도록 해야 하기 때문에 GC 중에는 애플리케이션 스레드들을 모두 멈춰야 한다. JVM GC 튜닝의 핵심은 이 시간을 줄이는 것이다.

## 가비지 컬렉션 알고리즘

* Reference Counting
  * 객체를 참조하는 숫자가 0이 되면 GC 수행
  * 순환 참조하는 메모리는 해제하지 못함
* Tracing
  * GC Root에서부터 객체 참조를 순회하면서 발견되는 객체를 제외하고는 메모리를 해제시킴. 서로간에 순환참조가 있더라도 GC Root에서 도달할 수 없으면 해제된다.
  * Mark-Copy \(Young Gen. GC 방식\)
  * Mark-Sweap
    * Mark-Sweap-Compact -&gt; 메모리 파편화 문제를 막기 위함
  * Mark-Summary-Compat
* Garbage First \(G1\)
  * 메모리를 2048개 정도의 Region으로 나누어 각 Region에 Eden, Survivor, Old 역할 부여
  * 리전 하나가 꽉 찰때마다 컬렉션을 수행하기 때문에 수행 시간 자체가 짧다.
  * 조금 더 자주 컬렉션이 일어나지만 수행시간이 짧음..?

## 사용 가능한 컬렉터의 종류

* Serial Collector
  * Young GC: Mark-Copy
  * Old GC: Mark-Sweap-and-Compact
  * 적은 메모리, 싱글코어 프로세서에 적합
* Parallel Collector
  * Young GC: Parallel Mark-Copy
  * Old GC: Parallel Mark-Sweap-Compact
  * 병렬로 GC를 수행
* CMS\(Concurrent Mark Sweap\) Collector
  * Young GC: Parallel Mark-Copy
  * Old GC: Almost Concurrent Mark-Sweap \(Remark is not concurrent\)
  * STW 시간이 적은 편
  * 조각모음을 하지 않음 -&gt; 메모리 파편화 문제 있음 -&gt; Compaction 시 STW 시간 증가
* G1 Collector
  * Garbage First

## 참조

* [JVM 메모리 구조와 GC - 기계인간 John Grib](https://johngrib.github.io/wiki/jvm-memory/)
* [\[JVM\] Garbage Collection Algorithms - Leopold Baik \(백중원\)](https://medium.com/@joongwon/jvm-garbage-collection-algorithms-3869b7b0aa6f)
* [JVM performance optimization, Part 3: Garbage collection - JAVAWORLD](https://www.javaworld.com/article/2078645/jvm-performance-optimization-part-3-garbage-collection.html)
* [Java 의 GC는 어떻게 동작하나? - J-Log](https://mirinae312.github.io/develop/2018/06/04/jvm_gc.html)
* [GC Algorithms: Implementations - Plumbr](https://plumbr.io/handbook/garbage-collection-algorithms-implementations)
* [How does Java Garbage Collection work with Circular References? - StackOverflow](https://stackoverflow.com/questions/1910194/how-does-java-garbage-collection-work-with-circular-references)
* [Java Garbage Collection - Naver D2](https://d2.naver.com/helloworld/1329)

