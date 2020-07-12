# OS

## 커널 모드와 유저 모드

모든 응용 프로그램\(유틸리티\) 는 I/O 와 같은 작업을 위해서는 운영체제의 커널을 통해서 작업을 수행해야만 한다. 그렇지 않다면 유틸리티가 다른 유틸리티의 메모리에 접근하는 등의 문제가 발생할 수 있다.

CPU에는 이를 강제하기 위해 각 아키텍처 만의 방식으로 현재 CPU가 어떤 모드인지 나타내는 레지스터가 있다. x86의 경우에는 CS레지스터의 마지막 두 비트에 0~3까지의 현재 특권 레벨이 설정된다.

CPU는 유틸리티가 금지된 영역을 읽어오거나 명령을 수행하려고 하면 예외를 발생시킨다. \(인텔 기준으로 일반 보호 예외라고 부른다.\) 일반적인 상황에서는 유틸리티가 운영체제로 시스템 콜을 하면 운영체제가 제어권을 획득하고 CPU를 커널 모드/특권레벨 0으로 설정해 메모리를 읽어 명령을 수행한 후 유틸리티에게 결과를 돌려주며 다시 CPU를 유저모드/특권레벨 3으로 설정한다.

금지되는 명령으로는 IO 명령, CPU를 정지시키는 HLT등의 명령이나 CR 레지스터, IO 레지스터 등 일부 특별한 레지스터에 접근하는 것 등이 포함된다.

### 특권 레벨 \(보호 링\)

어떤 특권 레벨이냐에 따라 실행할 수 있는 코드가 다르다. 운영체제는 항상 링0 에서 실행되며 모든 권한을 갖는다. 우리의 프로그램\(유틸리티\) 는 항상 링3에서 동작한다.

운영체제는 항상 메모리에 상주하며 유틸리티를 로드할때마다 링3에서 동작하게 한다.

1, 2는 존재하나 사용하지 않는다. \(아마도!\)

### Links

* [리눅스 커널\(운영체제\) 강의노트 \[1\]](https://medium.com/pocs/%EB%A6%AC%EB%88%85%EC%8A%A4-%EC%BB%A4%EB%84%90-%EC%9A%B4%EC%98%81%EC%B2%B4%EC%A0%9C-%EA%B0%95%EC%9D%98%EB%85%B8%ED%8A%B8-1-d36d6c961566)
* [Privilege Level \(Ring 0, Ring 3\)](https://elfmfl.tistory.com/2)
* [Where is the mode bit?](https://stackoverflow.com/questions/13185300/where-is-the-mode-bit)
* [Kernel mode bit](https://unix.stackexchange.com/questions/406898/kernel-mode-bit)
* [Is an x86 CPU in kernel mode when the CPL value of the CS register is equal to 0?](https://stackoverflow.com/questions/55506822/is-an-x86-cpu-in-kernel-mode-when-the-cpl-value-of-the-cs-register-is-equal-to-0)
* [X86 Architecture Basics: Privilege Levels and Registers](https://sites.google.com/site/masumzh/articles/x86-architecture-basics/x86-architecture-basics)
* [CPU Rings, Privilege, and Protection](https://manybutfinite.com/post/cpu-rings-privilege-and-protection/)

