# Prepared Statement

## 개요

> 일반적으로 쿼리나 업데이트와 같은 SQL 문과 함께 사용되는 프리페어드 스테이트먼트는 템플릿의 형태를 취하며, 그 템플릿 안으로 특정한 상수값이 매 실행 때마다 대체된다.

SQL 인젝션 을 막을 수 있는 방법 중 하나이다. DBMS에 쿼리할때 일종의 프로그램인 쿼리에서 데이터를 분리함으로써 \(SQL 인젝션의 근본적인 원인은 코드와 데이터가 분리되지 않는 것에 있음\) DBMS가 실행 계획을 불필요하게 여러번 만들지 않고, 악의적인 사용자가 SQL 인젝션을 시도해도 해당 쿼리는 이미 실행 계획이 만들어져 있기 때문에 DBMS가 개발자의 의도와 다르게 SQL을 실행하는 일을 막을 수 있다

## 참고문헌

* [프리페어드 스테이트먼트 - Wikipedia](https://ko.wikipedia.org/wiki/%ED%94%84%EB%A6%AC%ED%8E%98%EC%96%B4%EB%93%9C_%EC%8A%A4%ED%85%8C%EC%9D%B4%ED%8A%B8%EB%A8%BC%ED%8A%B8)
* [How can prepared statements protect from SQL injection attacks? - Stack Overflow](https://stackoverflow.com/questions/8263371/how-can-prepared-statements-protect-from-sql-injection-attacks/8265319)
* [SQL인젝션 취약점, 쿼리바인딩, Prepared Statement](https://blog.naver.com/blogpyh/220675109307)

