---
description: println!("Hello World!");
---

# Rust

## 러스트 프로그래밍 공식 가이드
- [x] 2019-12-12 CHAPTER 1: 시작하기
    - [x] 1.1 설치하기 
    - [x] 1.2 첫 번째 러스트 프로그램 작성하기 
    - [x] 1.3 카고 알아보기

- [x] 2019-12-12 CHAPTER 2: 숫자 맞히기 게임의 구현
    - [x] 2.1 새 프로젝트 셋업하기
    - [x] 2.2 플레이어가 예측한 값 처리하기
    - [x] 2.3 난수 생성하기
    - [x] 2.4 난수와 사용자의 입력 비교하기
    - [x] 2.5 반복문을 이용해 다중 입력 지원하기

- [x] 2019-12-12 CHAPTER 3: 일반 프로그래밍 개념
    - [x] 3.1 변수와 가변성
    - [x] 3.2 데이터 타입
    - [x] 3.3 함수 
    - [x] 3.4 주석
    - [x] 3.5 흐름 제어

- [x] 2019-12-19 CHAPTER 4: 소유권
    - [x] 4.1 소유권이란?
    - [x] 4.2 참조와 대여
    - [x] 4.3 슬라이스 타입

- [x] 2020-01-02 CHAPTER 5 구조체를 활용한 관련 데이터의 구조화
    - [x] 5.1 구조체 정의와 인스턴스 생성
    - [x] 5.2 구조체를 사용하는 예제 프로그램
    - [x] 5.3 메서드 문법

- [x] 2020-01-09 CHAPTER 6: 열거자와 패턴 매칭
    - [x] 6.1 열거자 정의하기
    - [x] 6.2 match 흐름 제어 연산자
    - [x] 6.3 if let을 이용한 간결한 흐름 제어

- [x] 2020-01-16 CHAPTER 7 패키지, 크레이트, 모듈로 프로젝트 관리하기
    - [x] 7.1 패키지와 크레이트
    - [x] 7.2 모듈을 이용한 범위와 접근성 제어
    - [x] 7.3 경로를 이용해 모듈 트리의 아이템 참조하기
    - [x] 7.4 use 키워드로 경로를 범위로 가져오기
    - [x] 7.5 모듈을 다른 파일로 분리하기

- [x] 2020-01-30 CHAPTER 8 범용 컬렉션
    - [x] 8.1 벡터에 일련의 값 저장하기
    - [x] 8.2 String 타입에 UTF-8 형식의 텍스트 저장하기
    - [x] 8.3 키와 값을 저장하는 해시 맵

- [x] 2020-02-06 CHAPTER 9 에러 처리
    - [x] 9.1 panic! 매크로를 이용한 회복 불가능한 에러 처리
    - [x] 9.2 Result 타입으로 에러 처리하기
    - [x] 9.3 패닉에 빠질 것인가? 말 것인가?

- [x] 2020-03-05 CHAPTER 10 제네릭 타입, 트레이트 그리고 수명
    - [x] 10.1 함수로부터 중복 제거하기
    - [x] 10.2 제네릭 데이터 타입
    - [x] 10.3 트레이트: 공유 가능한 행위를 정의하는 방법
    - [x] 10.4 수명을 이용해 참조 유효성 검사하기
    - [x] 10.5 제네릭 타입 매개변수, 트레이트 경계, 그리고 수명

- [x] 2020-03-12 CHAPTER 11 자동화 테스트 작성하기
    - [x] 11.1 테스트의 작성
    - [x] 11.2 테스트 실행 제어하기
    - [x] 11.3 테스트의 조직화

- [x] 2020-03-19 CHAPTER 12 I/O 프로젝트: 명령줄 프로그램 작성하기
    - [x] 12.1 명령줄 인수 처리하기
    - [x] 12.2 파일 읽기
    - [x] 12.3 모듈화와 에러 처리 향상을 위한 리팩토링
    - [x] 12.4 테스트 주도 방법으로 라이브러리의 기능 개발하기
    - [x] 12.5 환경 변수 다루기
    - [x] 12.6 stderr을 이용해 에러 메시지 출력하기

- [x] 2020-04-01 CHAPTER 13 함수형 언어의 기능: 반복자와 클로저
    - [x] 13.1 클로저: 주변 환경을 캡처하는 익명 함수
    - [x] 13.2 반복자를 이용해 일련의 아이템 처리하기
    - [x] 13.3 입출력 프로젝트의 개선

- [ ] CHAPTER 14 카고와 crates.io
    - [ ] 14.1 릴리즈 프로필을 이용한 빌드 커스터마이징
    - [ ] 14.2 crates.io 사이트에 크레이트 발행하기
    - [ ] 14.3 카고 작업공간
    - [ ] 14.4 cargo install 명령을 이용해 crates.io에서 바이너리 설치하기
    - [ ] 14.5 사용자 정의 명령을 이용해 카고 확장하기

- [x] CHAPTER 15 스마트한 포인터
    - [x] 15.1 Box〈T〉를 이용해 힙 메모리의 데이터 참조하기
    - [x] 15.2 Deref 트레이트를 이용해 스마트 포인터를 참조처럼 취급하기
    - [x] 15.3 Drop 트레이트를 구현해서 메모리를 해제할 때 코드 실행하기
    - [x] 15.4 Rc〈T〉, 참조 카운터 스마트 포인터
    - [x] 15.5 RefCell〈T〉 타입과 내부 가변성 패턴
    - [x] 15.6 메모리 누수의 원인이 되는 순환 참조

- [ ] CHAPTER 16 자신 있는 동시성
    - [x] 16.1 코드를 동시에 실행하기 위한 스레드
    - [x] 16.2 공유 상태 동시성
    - [ ] 16.3 Sync와 Send 트레이트로 동시성 확장하기

- [ ] CHAPTER 17 러스트의 객체지향 프로그래밍 기능
    - [ ] 17.1 객체지향 언어의 특징
    - [ ] 17.2 다른 타입의 값을 허용하는 트레이트 객체
    - [ ] 17.3 객체지향 디자인 패턴 구현

- [ ] CHAPTER 18 패턴과 매칭
    - [ ] 18.1 패턴을 활용할 수 있는 위치
    - [ ] 18.2 부인 가능성: 패턴이 일치할 수도 있고 그렇지 않을 수도 있는 경우
    - [ ] 18.3 패턴 문법

- [ ] CHAPTER 19 러스트의 고급 기능
    - [ ] 19.1 안전하지 않은 러스트
    - [ ] 19.2 고급 트레이트
    - [ ] 19.3 고급 타입 시스템
    - [ ] 19.4 고급 함수와 클로저
    - [ ] 19.5 매크로

- [ ] CHAPTER 20 최종 프로젝트: 다중 스레드 웹서버 구축
    - [x] 20.1 단일 스레드 웹서버 구현하기
    - [ ] 20.2 다중 스레드 서버로 전환하기
    - [ ] 20.3 우아한 종료와 해제

## Links

* [https://rinthel.github.io/rust-lang-book-ko/](https://rinthel.github.io/rust-lang-book-ko/)
* [Functional Programming Jargon in Rust](https://functional.works-hub.com/learn/functional-programming-jargon-in-rust-1b555)
* [Getting Started with Rust by Building a Tiny Markdown Compiler](https://jesselawson.org/rust/getting-started-with-rust-by-building-a-tiny-markdown-compiler/)
* [Writing an OS in Rust](https://os.phil-opp.com/)
* [Rust: Dropping heavy things in another thread can make your code 10000 times faster](https://abramov.io/rust-dropping-things-in-another-thread)
* [The Rustnomicon](https://doc.rust-lang.org/stable/nomicon/)
* [The Node Experiment - Exploring Async Basics with Rust](https://cfsamson.github.io/book-exploring-async-basics/)
  * [Source Code](https://github.com/cfsamson/book-exploring-async-basics)
* [Epoll, Kqueue and IOCP Explained with Rust](https://cfsamsonbooks.gitbook.io/epoll-kqueue-iocp-explained/)
  * [Source Code](https://github.com/cfsamson/examples-minimio)
* [Green Threads Explained in 200 Lines of Rust](https://cfsamson.gitbook.io/green-threads-explained-in-200-lines-of-rust/)
  * [Source Code](https://github.com/cfsamson/example-greenthreads)