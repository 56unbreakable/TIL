# 데이터 모델링의 이해

## 데이터 모델링

### 데이터 모델링의 이해

#### 데이터 모델링

1. 현실 세계를 데이터 베이스로 표현하기 위해 추상화
2. 고객의 업무 프로세스를 이해해야함
3. 모델링 표기법을 사용해 모델링
4. 복잡하지 않게 모델링
5. 분석, 설계하면서 더 상세해짐
6. 비즈니스 프로세스를 이해하고  규칙을 정의하여 데이터모델로 표현

#### 데이터 모델링의 특징

추상화 : 공통적인 특징을 찾고 간략하게 표현

단순화 : 누구나 이해할 수 있게 표현

명확함 : 의미적 해석이 모호하지 않고 명확하게 해석되어야함

#### 데이터 모델링 단계

1. 개념적 모델링

   복잡하게 표현하지 않고 중요한 부분을 위주로 모델링, 기술적인 용어는 가급적 사용 안함.

   엔터티와 속성 도출, 개념적 ERD 작성

   추상화 수준이 가장 높다.

2. 논리적 모델링

   개념적 모델링을 논리적 모델링으로 변환, 식별자 도출, 릴레이션 정의, 정규화수행

   재사용성을 높인다

3. 물리적 모델링

   실제로 데이터베이스 구축. 테이블, 인덱스, 함수 등 생성

   성능, 보안, 가용성 등을 고려하여 데이터베이스 구축

+ 데이터 모델링 관점
  1. 데이터 : 비즈니스 프로세스에서 사용되는 데이터를 의미
  2. 프로세스 : 비즈니스 프로세스에서 수행하는 작업을 의미
  3. 데이터와 프로세스 : 프로세스와 데이터 간의 관계를 의미

#### ERD

+ ERD 작성절차

  1. 엔터티를 도출하고 그린다
  2. 엔터티를 배치한다
  3. 엔터티 간의 관계를 설정한다
  4. 관계명을 서술한다. 엔터티 간의 어떤 행위나 존재가 있는지 표현한다.
  5. 관계 참여도를 표현한다. 관계참여도는 한 개의 엔터티와 다른 엔터티 간의 참여하는 관계 수를 의미한다.
  6. 관계의 필수여부를 표현한다.

+ 고려사항

  중요한 엔터티를 가급적 왼쪽 상단에 배치한다.

  ERD는 이해가 쉬워야하고 복잡하지 않아야한다.

#### 데이터 모델링 고려사항

1. 데이터 모델의 독립성 : 정규화를 통해 데이터 중복 제가
2. 고객 요구사항의 표현 
3. 데이터 품질 확보



### 3층 스키마

#### 3층 스키마

사용자, 설계자, 개발자가 데이터베이스를 보는 관점에 따라 데이터베이스를 기술하고 이들간의 관꼐를 정의한 ANSI표준

3층 스키마는 데이터베이스의 독립성을 확보하기 위한 방법이다. 독립성을 확보하면 데이터 복잡도 감소, 데이터 중복 제거, 사용자 요구사항 변경에 따른 대응력 향상, 관리 및 유지보수 비용 절감

3단계 계층으로 분리, 각 계층을 뷰`View` 라고 함.

+ 논리적 독립성 : 개념 스키마가 변경되더라도 외부 스키마가 영향을 받지 않는 것
+ 물리적 독립성 : 내부 스키마가 변경되더라도 개념 스키마가 영향을 받지 않는 것

#### 3층 스키마 구조

외부단계 -> 개념단계 -> 내부단계

+ 외부 스키마 : 사용자 관점, 응용 프로그램이 접근하는 데이터베이스 정의, 사용자 관점에서 업무상 관련이 있는 데이터 접근.
+ 개념 스키마 : 설계자 관점, 사용자 전체 집단의 데이터베이스 구조. 전체 데이터베이스 내의 규칙과 구조를 표현, 통합 데이터베이스구조
+ 내부 스키마 : 개발자 관점, 데이터베이스의 물리적 저장 구조. 데이터저장구조, 레코드구조, 필드정의, 인덱스 등등의미.



### 엔터티

#### 엔터티

업무에서 관리해야 하는 데이터집합을 의미. 저장되고 관리되어야 하는 데이터.

엔터티는 개념, 사건, 장소등의 명사.

#### 엔터티 도출

고객의 비즈니스 프로세스에서 관리되어야 하는 정보를 추출.

#### 엔터티 특징

1. 식별자 : 엔터티는 유일한 식별자가 있어야함
2. 인스턴스 집합 : 2개 이상의 인스턴스가 있어야함
3. 속성 : 반드시 속성을 가지고 있음
4. 관계 : 다른 엔터티와 최소 한 개 이상의 관계를 가져야함
5. 업무 : 업무에서 관리되어야 하는 집합.

+ 릴레이션과 테이블, 인스턴스

  릴레이션과 테이블은 같은의미, 릴레이션에 기본키 및 제약조건을 설정하면 테이블.

  단, 릴레이션쉽은 릴레이션간의 관계를 의미

  인스턴스는 릴레이션이 가질 수 있는 값을 의미.

#### 엔터티 종류

+ 유형과 무형에 따른 엔터티 종류
  1. 유형 엔터티 : 업무에서 도출되어 지속적으로 사용되는 엔터티
  2. 개념 엔터티 : 물리적 형태가 없음. 개념적으로 사용되는 엔터티
  3. 사건 엔터티 : 비즈니스 프로세스를 실행하면서 생성되는 엔터티
+ 발생 시점에 따른 엔터티 종류
  1. 기본 엔터티 : 키 엔터티, 다른 엔터티로부터 영향을 받지 않고 독립적으로 생성되는 엔터티
  2. 중심 엔터티 : 기본 엔터티로부터 발생되고 행위 엔터티를 생성하는 것
  3. 행위 엔터티 : 2개 이상의 엔터티로부터 발생된다.



### 속성

#### 속성

속성이라는 것은 업무에서 필요한 정보인 엔터티가 가지는 항목이다.

속성은 더 이상 분리되지 않는 단위로, 업무에 필요한 데이터를 저장할 수 있다.

인스턴스의 구성요소이고, 의미적으로 더 이상 분해되지 않는다.

+ 엔터티
  + 속성
    + 데이터 저장

#### 속성의 특징과 종류

1. 특징 : 업무에서 관리되는 정보, 하나의 값만 가짐, 주 식별자에게 함수적으로 종속, 즉 기본키가 변경되면 속성의 값도 변경됨
2. 종류 
   + 분해 여부에 따른 속성의 종류
     1. 단일 속성 : 하나의 의미로 구성된 것
     2. 복합 속성 : 여러개의 의미가 있는 것, ex) 주소
     3. 다중값 속성 : 여러개의 값을 가질 수 있는 것. 다중값 속성은 엔터티로 분해된다.
   + 특성에 따른 속성의 종류
     1. 기본 속성 : 비즈니스 프로세스에서 도출되는 본래의 속성
     2. 설계 속성 : 데이터 모델링 과정에서 발생되는 속성, 유일한 값 부여
     3. 파생 속성 : 다른 속성에 의해서 만들어지는 속성
3. 도메인 : 속성이 가질 수 있는 값의 범위.



### 관계

#### 관계 (Relationship)

관계는 에터티 간의 관련성을 의미하며 존재관계와 행위관계로 분류됨.

존재관계는 두 개의 엔터티가 존재 여부의 관계가 있는 것이고, 행위 관계는 두 개의 엔터티가 어떤 행위에 의한 관련성이 있는 것.

#### 관계의 종류

1. 존재 관계 : 엔터티간의 상태를 의미. 고객이 은행에 회원가입을 하면, 관리점이 할당되고, 그 할당괸 관리점에서 고객 관리
2. 행위 관계 : 어떤 행위가 엔터티간에 있는 것,

#### 관계 차수

관계 차수는 두 개의 엔터티 간에 관계에 참여하는 수를 의미.

(관계 차수에 관한 그림은 책 74p 참고)

1. 1대1 관계 

   + 완전 1대1 관계 : 하나의 엔터티에 관계되는 엔터티의 관계가 하나인 경우로 반드시 존재
   + 선택적 1대1 관계 : 하나의 엔터티에 관계되는 엔터티의 관계가 하나이거나 없을수도 있음.

2. 1대N 관계 : 엔터티의 행이 하나 있을 때 다른 엔터티의 값이 여러 개 있는 관계. ex) 고객은 계좌를 여러개를 가질 수 있다.

3. M대N 관계 : 두 개의 엔터티가 서로 여러개의 관계를 가지고 있는 것. 1대N, N대1 로 해소해야 한다.

4. 필수적 관계와 선택적 관계.

   필수적 관계는 `|`로 표현되고, 반드시 하나가 있어야 하는 관계이다.

    선택적 관계는 `O` 로 표현되고, 없을수도 있는 관계이다.

   `고객 -|-------O- 계좌`

   `고객`은 `계좌`가 있어도 되고 없어도 되기 때문에 `계좌`는 `O` 로 표현한다. 하지만 `계좌`는 무조건 `고객`이 있어야한다. 따라서 `고객`은 `|` 로 표현한다.

   필수적으로 있어야 하는 쪽에 `|` 를 쓰고 선택적으로 있어야 하는 쪽에 `O` 를 쓴다.

#### 식별 관계와 비식별 관계

1. 식별 관계 

   강한 개체는 다른 엔터티에게 의존하지 않고 독립적으로 존재한다. 강한 개체가 다른 엔터티와 관계를 가질 떄 다른 엔터티에게 기본키를 공유한다. 강한 개체는 식별 관계로 표현된다. 식별관계란 강한 개체의 기본키를 다른 엔터티의 기본키 하나로 공유하는 것이다. 강한 개체의 기본키 값이 변경되면 식별 관계에 있는 엔터티의 값도 변경된다. 실선으로 표현한다.

   `고객 -|------------O- 계좌` 와 같은 관계가 있을 때, 강한 개체는 `고객` 이다. `고객` 은 계좌 없이도 독립적인 존재가 가능하다.

   `고객`의 기본키를 `계좌`가 공유할 때, `고객`의 기본키가 변경되면 `계좌`의 기본키도 변경된다.

2. 비식별 관계

   비식별 관계는 강한 개체의 기본키를 다른 엔터티의 기본키가 아닌 일반 칼럼으로 관계를 가지는 것이다.

   비식별 관계는점선으로 표현한다.

   `부서 -|- - - - - - - O - 사원`

3. 강한개체와 약한개체

   강한 개체는 누구에게도 지배되지 않고 독립적인 개체

   약한 개체는 개체의 존재가 다른 개체의 존재에 달려있는 개체이다.

#### 엔터티 식별자

식별자는 엔터티를 대표할 수 있는 유일성을 만족하는 속성.

1. 주 식별자

   주 식별자는 다음과 같은 속성을 가져야 한다.

   + 최소성
   + 대표성 : 엔터티를 대표할 수 있어야 하는 것
   + 유일성 : 유일하게 인스턴스를 식별
   + 불변성 : 자주 변경되지 않아야함

2. 키의 종류

   + 기본키 : 엔터티를 대표하는 키
   + 후보키 : 유일성과 최소성을 만족하는 키
   + 슈퍼키 : 유일성은 만족하지만 최소성을 만족하지 않는 키
   + 대체키 : 여러개의 후보키 중에서 기본키를 선정하고 남은 키
   + 외래키 : 하나 혹은 다수의 다른 테이블의 기본 키 필드를 가리키는 것으로 참조 무결성을 확인하기 위해서 사용되는 키. 허용된 값만 데이터베이스에 저장하기 위해서 사용

3. 식별자의 종류

   1. 식별자의 대표성 에 따른 종류 
      + 주 식별자 : 엔터티를 대표할 수 있는 식별자이며 다른 엔터티와 참조관계로 연결될 수 있다.
      + 보조 식별자 : 유일성과 최소성은 만족하지만 대표성을 만족하지 못하는 식별자
   2. 생성 여부에 따른 식별자 종류
      + 내부 식별자 : 엔터티 내부에서 스스로 생성되는 식별자. (주문번호, 종목코드 등등)
      + 외부 식별자 : 다른 엔터티와의 관계로 인하여 만들어지는 식별자
   3. 속성의 수에 따른 종류
      + 단일 식별자 : 하나의 속성으로 구성됨
      + 복합 식별자 : 두 개 이상의 속성으로 구성됨
   4. 대체 여부에 따른 종류
      + 본질 식별자 : 비즈니스 프로세스에서 만들어지는 식별자
      + 인조 식별자 : 인위적으로 만들어지는 식별자. 후보 식별자 중에서 주식별자로 선정할 것이 없거나 주 식별자가 너무 많은 칼럼으로 되어 있는 경우에 사용한다. 순서번호를 사용해서 식별자 생성.



## 데이터 모델과 성능

### 정규화

#### 정규화

정규화는 데이터의 일관성, 최소한의 데이터 중복, 최대한의 데이터 유연성을 위한 방법. 데이터를 분해하는 과정.

데이터 중복을 제거하고 모델의 독립성을 확보하기 위한 방법.

비즈니스에 변화가 발생하여도 데이터 모델의 변경 최소화 가능

제1정규화부터 제5 정규화까지 있으나, 실질적으로는 제 3 정규화까지만 수행.

정규화된 모델은 테이블이 분해된다. 테이블이 분해되면 `join` 을 수행하여 합집합으로 만들 수 있다.

#### 함수적 종속성

1. 제 1 정규화

   + 정규화는 __함수적 종속성__을 근거로 한다. 함수적 종속성이란 `X->Y` 이면 `y`는  `x` 에 함수적으로 종속된다고 말한다.
   + `x` 가 변화하면 `y` 도 변화할 경우, 함수적으로 종속된다고 말한다.
   + `x` 는 기본키가 된다. 기본키가 바뀌면 다른 속성 `y` 가 바뀐다.
   + 제 1 정규화는 기본 키를 잡는것이다. 기본키를 바탕으로 다른 속성들을 함수적으로 종속시킨다.

2. 제 2 정규화

   + 기본키가 1개일 경우 제 2 정규화는 생략한다.

   + 기본키가 2개 이상일 경우 제 2 정규화를 시행한다. 제 2 정규화는 __부분 함수 종속성__을 제거한다.

   + 부분함수 종속성 : 기본키가 2개 이상인 경우, 하나의 기본 키가 바뀌었을 때 (`x`) 다른 속성이 바뀌는 것이 있다면(`y`) 그것을 부분 함수 종속성이라 말한다. 부분함수 종속성이 발생하면 분해를 해야한다.

     예를 들어 `X` 가 계좌번호, 회원ID 이고, Y가 계좌명, 예수금, 이름, 관리점일 때, 회원ID가 바뀌면 이름이 바뀐다. 따라서

     `x(계좌번호, 회원ID) -> y(계좌명, 예수금, 관리점)` & `x(회원ID) -> y(이름)` 

     위와 같이 새로운 테이블을 만들어낸다.

3. 제 3 정규화

   + 제 3 정규화는 __이행 함수 종속성__을 제거한다. 기본키를 제외하고 칼럼간에 종속성이 발생하는 것이다.

   + 제 3 정규화는 제1, 2 정규화를 수행한 다음 해야한다.

   + `y` 칼럼간의 종속성이 발생하면 이를 해소해주어야한다.

     예를들어 `x(계좌번호, 회원ID) -> y(계좌명, 예수금, 관리점코드, 관리점)` 일때, 관리점 코드와 관리점 사이에는 종속성이 발생한다. 관리점 코드가 바뀌면 관리점이 바뀐다. 따라서

     `x(계좌번호, 회원ID) -> y(계좌명, 예수금, 관리점코드)` & `x(관리점 코드) -> y(관리점)` 

     위와같이 새로운 테이블을 만들어낸다.

#### 정규화 정리

1. 한 개의 속성의 기본키로는 유일성을 만족할 수 없을 경우 2개의 조합으로 유일성이 만족되는지 확인한다. 이렇게 기본 키를 찾는 과정이 제 1 정규화이다.

2. 기본키가 2개 이상일 경우 제 2 정규화 대상이다. 하나의 기본키에서 중복이 발생하는지 확인해야한다.

   즉, 회원ID 와 이름은 같은데 계좌번호,계좌명,예수금,관리점이 다른 경우가 발생할 수 있다. 이 경우 회원ID와 이름을 분해하여 새로운 테이블을 생성한다.

   다른 예로, 제품번호(기본키), 제품명, 재고수량이 같지만, 주문번호(기본키)가 다른 제품이 존재할 수 있다. 이 경우 제품번호를 기본키로하고 제품명, 재고수량을 칼럼으로 가지는 새로운 테이블을 생성한다.

   이렇게 기본키가 2개 이상인 경우 중복을 가지는 칼럼이 존재하게될 수 있는데, 이걸 제거하는 것이 제 2 정규화이다.



### 정규화와 성능

#### 정규화의 문제점

정규화는 테이블을 분해해서 데이터 중복을 제거하기 때문에 데이터 모델의 유연성을 높인다. 하지만 정규화는 데이터 조회시에 `join` 을 유발하기 떄문에 cpu와 메모리를 많이 사용한다. 이때 중첩된 루프를 사용하는데, 성능저하가 발생하게 된다. 이를 해결하기 위해 반 정규화가 사용된다.

하지만 성능 향상을 위한 반 정규화는 데이터를 중복시키기 때문에 또 다른 문제가 발생할 수도 있다. 데이터의 칼럼을 증가시키면 `join`이 적어지지만, 블록 사이즈를 넘어설 경우 여러개의 블록을 읽게 되고 이는 성능저하로 이어진다.

정규화는 입출력 데이터의 양을 줄여서 성능을 향상시키는 것이 낫다.



### 반정규화

#### 반정규화

데이터베이스의 성능 향상을 위하여 데이터 중복을 허용하고 조인을 줄이는 데이터베이스 성능 향상 방법이다. 

반정규화는 조회 속도를 향상하지만 데이터 모델의 유연성은 낮아진다.

#### 반정규화를 수행하는 경우

1. 정규화에 충실하면 종속성, 활용성은 향상되나 수행 속도가 느려지는 경우
2. 다량의 범위를 자주 처리해야 하는 경우
3. 특정 범위의 데이터만 자주 처리하는 경우
4. 요약/집계 정보가 자주 요구되는 경우

+ 절차
  1. 대상 조사 및 검토
  2. 다른 방법 검토 : 반정규화를 수행하기 전 다른 방법이 있는지 검토
  3. 반정규화 수행

#### 반정규화 기법

1. 계산된 칼럼 추가.

   배치 프로그램으로 총액, 평균과 같은 정보를 미리 계산하고 그 결과를 특정 칼럼에 추가

2. 테이블 수직 분할

   하나의 테이블을 두 개 이상의 테이블로 분할, 칼럼을 분할하여 새로운 테이블 생성

   `key - c1, c2, c3, c4` -> `key - c1, c2` & `key - c3, c4`

3. 테이블 수평 분할

   하나의 테이블에 있는 값을 기준으로 테이블을 분할한다.

   ex) 2020~2000 년도까지의 데이터를 가진 테이블 1개, 1999~1980 년도까지의 데이터를 가진 테이블 1개, 총 2개의 테이블로 나눔

   ​	기존 테이블은 2020~1980 데이터를 가졌지만 2개로 나눔

   + 파티션 기법

     데이터베이스의 파티션을 사용하여 테이블을 분할할 수 있다. 파티션을 사용하면 논리적으로는 하나의 테이블이지만 여러개의 데이터 파일에 분산되어서 저장된다.

     1. range partition : 데이터 값의 범위를 기준으로 파티셔닝
     2. list partition : 특정 값을 지정하여 파티셔닝
     3. hash partition : 해시 함수를 적용하여 파티셔닝
     4. composition partition : 범위와 해시를 복합적으로 사용하여 파티셔닝

     장점 : 성능향상, 각 테이블의 독립적 백업 및 복구

4. 테이블 병합

   1대1 관계의 테이블을 하나의 테이블로 병합하여 성능 향상.

   1대N 관계의 테이블을 하나의 테이블로 병합하여 성능 향상도 가능하지만 많은양의 데이터 중복이 발생할 수 있다.

   + 슈퍼타입과 서브타입

     데이터를 통합하여 성능 향상이 가능하다.

     ex) 고객 엔터티의 개인고객과 법인고객. 고객 엔터티가 슈퍼타입이고 개인고객과 법인고객이 서브타입. 배타적 관계는 개인고객이거나 법인고객인 경우, 포괄적 관계는 개인고객일 수도 있고 법인 고객일 수도 있는것.

     1. OneToOne 타입 : 슈퍼타입과 서브타입을 개별 테이블로 도출, 테이블이 많아 조인이 많고 관리가 어려움
     2. Plus 타입 : 슈퍼타입과 서브타입 테이블로 도출, 조인이 발생하고 관리가 어려움
     3. Single 타입 : 슈퍼타입과 서브타입을 하나의 테이블로 도출, 조인성능이 좋고 편리하지만 입출력 성능이 나쁨.



### 분산 데이터베이스

#### 분산데이터베이스

중앙 집중형 데이터베이스 : 데이터베이스 시스템 구축 시에 한 대의 물리적 시스템에 데이터 베이스 관리 시스템을 설치하고 여러명의 사용자가 데이터베이스 관리 시스템에 접속하여 사용하는 구조

분산데이터베이스 : 물리적으로 떨어진 데이터베이스에 네트워크로 연결하여 단일 데이터베이스 이미지를 보여주고 분산된 작업 처리 수행

+ 분산데이터베이스 투명성

  투명성은 중요한 요소. 분산DB 는 투명성을 제공해야한다.

  1. 분할 투명성 : 고객은 여러 시스템에 저장되어있는걸 느낄 필요가 없다
  2. 위치 투명성 : 고객이 사용하려는 데이터의 저장 장소를 명시할 필요가 없다
  3. 지역 사상 투명성 : 각 지역 시스템 이름과 무관한 이름이 사용 가능
  4. 중복 투명성 : 데이터베이스 객체가 여러 시스템에 중복되어 존재해도 고객과는 무관하게 일관성이 유지됨
  5. 장애 투명성 : 각 지역의 시스템이나 통신망의 이상이 생겨도 데이터의 무결성 보장
  6. 병행 투명성 : 여러 고객이 동시에 트랜잭션을 수행해도 결과에 이상이 없어야함

#### 설계 방식

1. 상향식 설계 방식 : 지역 스키마 작성 후 전역 스키마를 작성하여 분산 데이터베이스 구축

   지역별로 데이터베이스 구축한 후 전역 스키마로 통합

2. 하향식 설계 방식 : 전역 스키마 작성 후 해당 지역 사상 스키마를 작성하여 분산 데이터베이스 구축

   기업 전체의 전사 데이터 모델을 수렴하여 전역 스키마를 생성하여 각 지역별로 스키마 생성

+ 장점 
  1. 신뢰성과 가용성이 높다
  2. 빠른 응답이 가능하다
  3. 용량 확장이 쉽다
+ 단점
  1. 관리와 통제가 어렵다
  2. 보안관리가 어렵다
  3. 데이터 무결성 관리가 어렵다
  4. 데이터베이스 설계가 복잡하다.



# SQL 기본 및 활용

## SQL 기본

### 관계형 데이터베이스

#### 관계형 데이터베이스

1. 데이터베이스와 데이터베이스 관리 시스템의 차이점
   + 데이터베이스는 데이터를 어떠한 형태의 자료구조로 사용하느냐에 따라서 나누어진다.
   + 종류 
     1. 계층형 : 트리 형태의 자료구조에 데이터를 저장하고 관리. 1대N관계
     2. 네트워크 : 오너,멤버 형태로 데이터 저장. 1대N과 M대N 표현 가능
     3. 관계형 : 릴레이션에 데이터를 저장하고 관리. 집합연산과 관계연산 가능
   + 데이터베이스 관리 시스템(DBMS)는 데이터베이스를 관리하기 위한 소프트웨어
   + Oracle, MS-SQL, MySQL등이 있음
2. 관계형 데이터베이스의 집합연산과 관계연산
   + 집합연산
     1. 합집합 : 두 개의 릴레이션을 하나로 합하는 것, 중복행은 한번만 조회
     2. 차집합 : 본래 릴레이션에는 존재하고 다른 릴레이션에는 존재하지 않는 것을 조회
     3. 교집합 : 두 릴레이션의 공통된 행을 조회
     4. 곱집합 : 각 릴레이션에 존재하는 모든 데이터를 조합하여 연산
   + 관계연산
     1. 선택 연산 : 조건에 맞는 행만 조회
     2. 투영연산 : 릴레이션에서 조건에맞는 속성만을 조회
     3. 결합연산 : 공통된 속성을 사용해서 새로운 릴레이션 생성
     4. 나누기연산 : 기존 릴레이션에서 나누는 릴레이션이 가진 속성과 동일한 값을 가지는 행을 추출하고 나누는 릴레이션의 속성을 삭제한 뒤 중복행 제거

#### 테이블 구조

관계형 데이터베이스는 릴레이션에 데이터를 저장, 릴레이션을 사용해 집합 연산 및 관계연산 지원. -> 다양한 형태로 데이터 조회

릴레이션은 최종적으로 테이블로 만들어짐

+ 테이블 구성요소
  1. 튜플 : 테이블의 행
  2. 속성 : 테이블의 열
  3. 기본키 : 하나의 테이블에서 유일성, 최소성, `Not Null` 을 만족하는 열.
  4. 외래키 : 다른 테이블의 기본키를 참조하는 칼럼. 결합연산(`join`)을 위해서 사용



### SQL 종류

#### SQL

+ `sql` 은 관계형 데이터베이스에 대해서 데이터의 구조정의, 조작, 제어를 할 수 있는 절차형 언어.
+ ANIS/ISO 표준을 준수한다. (책 110페이지 참조)

#### SQL 종류

1. 종류

   + DDL(Data Definition Language) : 구조를 정의하는 언어. `CREATE` `ALTER` `DROP` `RENAME`
   + DML(Data Manipulate Language) : 데이터를 입력 수정 삭제 조회. `INSERT` `UPDATE` `DELETE` `SELECT` 
   + DCL(Data Control Language) : 데이터베이스 사용자에게 권한을 부여하거나 회수. `GRANT` `REVOKE` `TRUNCATE`
   + TCL(Transation Control Language) : 트랜잭션을 제어하는 명령어. `COMMIT` `ROLLBACK` `SAVEPOINT`

2. 트랜잭션

   트랜잭션은 데이터베이스의 작업을 처리하는 단위. 다음과 같은 특성을 가진다.

   + 원자성 : 연산의 전부가 실행되거나 전혀 실행되지 않아야한다. 처리가 완전히 끝나지 않으면 아예 실행하지 않은것과 동일
   + 일관성 : 데이터베이스의 상태가 트랜잭션 전후로 일관성이 유지되어야함. 모순되면안됨
   + 고립성 : 트랜잭션 실행중의 연산 중간결과는 다른 트랜잭션이 접근할 수 없음. 부분적인 실행결과 볼 수 없음
   + 영속성 : 트랜잭션이 실행을 완료하면 영구적인 보장이 되어야함.

#### SQL문의 실행 순서

SQL 문은 3단계를 걸쳐서 실행된다.

1. 파싱 : 문법을 확인하고 구문분석, 캐시에 저장
2. 실행 : 옵티마이저가 수립한 실행계획에 따라 실행
3. 인출 : 데이터를 읽어서 전송



### DDL - Data Definition Language

#### 테이블 생성

데이터베이스를 사용하기 위해서는 테이블을 먼저 생성해야한다.

+ 테이블 관리 SQL

  + `CREATE TABLE` : 새로운 테이블 생성. 기본키, 외래키, 제약사항 등 설정 가능
  + `ALTER TABLE` : 생성된 테이블 변경. 칼럼의 추가,변경,삭제 가능. 기본키, 외래키 설정가능
  + `DROP TABLE` : 테이블 삭제. 구조와 저장된 데이터 모두 삭제.

+ 기본적인 테이블 생성.

  ```sql
  CREATE TABLE 테이블이름(
  	칼럼1 number(10) PRIMARY KEY,
      칼럼2 varchar2(20),
      칼럼3 char(6)
  );
  ```

  1. `CREATE TABLE` 다음에 테이블 이름을 정함으로서 테이블을 생성한다.
  2. 괄호 안에 칼럼을 설정할 수 있다. `칼럼이름 데이터타임` 과 같이 선언한다. 
  3. `PRIMARY KEY` 는 기본키 설정이다.

+ 제약조건 사용

  기본키, 외래키, 기본값, `NOT NULL` 등은 테이블을 생성할 때 지정할 수 있다.

  ```sql
  CREATE TALBE EMP(
  	EMPNO number(10),
      SAL varchar2(20) default 0,
      DEPTNO number(10) NOT NULL,
      CREATEDATE date default sysdate,
      constraint emppk PRIMARY KEY(EMPNO)    
  );
  ```

  1. `constraint` 명령어를 사용하여 기본키와 기본키의 이름을 지정한다. 두 개의 기본키를 지정하고자 하면 `constraint emppk PRIMARY KEY(EMPNO,SAL)` 과 같은 형식으로 지정하면 된다.
  2. `default` 명령어로 기본값을 입력할 수 있다. `sysdate` 는 시스템상 시간을 의미한다.
  3. `NOT NULL` 명령어는 빈 값을 허용하지 않는다는 뜻이다.

+ CASCADE

  테이블 생성 시 참조관계(기본키와 외래키 관계)가 있을 경우 참조되는 데이터를 자동으로 반영한다.

  테이블 생성시 다음과 같은 명령어를 사용한다

  ```sql
  CREATE TALBE EMP(
  	EMPNO number(10),
      SAL varchar2(20) default 0,
      constraint emppk PRIMARY KEY(EMPNO)  # 기본키 설정
      constraint deptk FOREIGN KEY(DEPTNO) # 외래키 설정, CASCADE 옵션
      	references DEPT(DEPTNO)
      	ON DELETE CASCADE
  );
  ```

  `ON DELETE CASCADE` 옵션을 설정하여 참조무결성을 준수할 수 있다. `EMP` 테이블에서 데이터가 삭제되면, 참조하고있는 `DEPT` 테이블의 데이터가 자동으로 삭제되는 옵션이다.

#### 테이블 변경

기본적으로 `ALTER TABLE 이름 ~` 과 같은 명령어로 구문을 사용할 수 있다.

1. 테이블명 변경

   `RENAME` 명령어를 통해 새로은 이름으로 변경할 수 있다.

   ```sql
   ALTER TABLE EMP
   	RENAME TO NEW_EMP;
   ```

2. 칼럼 추가

   `ADD` 명령어로 칼럼을 추가할 수 있다.

   ```sql
   ALTER TALBE EMP
   	ADD(age number(2) default 1);
   ```

3. 칼럼 변경

   `MODFIY` 명령어로 칼럼을 변경할 수 있다. 이때, 데이터 타입을 변경하거나 길이를 변경할 수 있다. 제약조건의 설정도 가능하다.

   만약에 변경할 테이블의 기존 데이터의 데이터타입과 변경하는 데이터 타입이 다른 경우 에러가 발생한다.

   ```sql
   ALTER TABLE EMP
   	MODIFY(ename varchar2(20) not null);
   ```

4. 칼럼 삭제

   `DROP COLUMN` 으로 삭제한다.

   ```sql
   ALTER TABLE EMP
   	DROP COLUMN age;
   ```

5. 칼럼명 변경

   ```sql
   ALTER TABLE EMP
   	RENAME COLUMN enmae to new_ename
   ```

#### 테이블 삭제

테이블 삭제는 `DROP TABLE 테이블이름` 을 사용해 삭제한다.

테이블 삭제시에도 `CASCADE` 옵션을 사용 가능하다. `DROP TABLE EMP CASCADE CONSTRAINT` 명령어로 해당 테이블을 참조한 관련 제약사항을 모두 삭제한다.

#### 뷰 생성과 삭제

뷰는 테이블로부터 유도된 가상 테이블이다. 실제 데이터는 가지고 있지 않고 테이블을 참조해서 원하는 칼럼만을 조회한다. 딕셔너리에 SQL문 형태로 저장되며 실행시 참조된다.

뷰를 생성할 때 `CREATE VIEW` 를 사용한다. 참조할 테이블은 `SELECT` 로 지정한다.

```SQL
CREATE VIEW T AS
	SELECT * FROM EMP;
```

뷰의 조회는 일반 테이블과 같다.

```SQL
SELECT * FROM T;
```

뷰의 삭제는 `DROP VIEW 뷰이름` 구문을 사용한다. 참조했던 테이블은 삭제되지 않는다.

+ 장점
  1. 특정 칼럼만 조회할 수 있어 보안성이 높다
  2. 데이터 관리가 간단하다
  3. `SELECT` 문이 간결해진다.
  4. 하나의 테이블에 여러개의 뷰를 생성할 수 있다.
+ 단점
  1. 독자적인 인덱스를 만들 수 없다.
  2. 수정 삭제 연산이 제약된다.
  3. 데이터 구조를 변경할 수 없다.



### DML - Data Manipulate Language

#### INSERT

테이블에 데이터를 입력하는 명령어다.

`INSERT INTO 테이블이름(칼럼명...) VALUES(입력할값...)` 과 같은 형태로 사용한다.

문자열 입력시에는 작은따옴표를 사용한다. 모든 칼럼에 대해 데이터를 입력할떄는 칼럼명을 생략할 수 있다. 

최종적으로 `COMMIT` 을 실행해야 저장되지만, `AUTO COMMIT` 일 경우 자동으로 저장된다.

+ SELECT 로 입력

  데이터를 조회해서 특정 테이블에 바로 삽입할 수 있다. 단 입력되는 테이블은 사전에 생성되어있어야 한다.

  ```SQL
  INSERT INTO A     # 테이블 A를 미리 만들어둬야한다.
  	SELECT * FROM B;
  ```

+ NOLOGGIN 사용

  데이터베이스에 데이터를 입력하면 로그파일에 그 정보를 기록한다. `NOLOGGIN` 옵션은 로그파일의 기록을 최소화시킨다.

  ```SQL
  INSERT INTO A NOLOGGIN;
  ```

#### UPDATE

입력된 데이터의 값을 수정할 수 있다. 해당되는 행을 수정한다.

```SQL
UPDATE A
	SET ANAME = '조조'
	WHERE ANUM = 100;
```

테이블 A의 `ANAME` 이라는 칼럼의 값을 `조조` 로 변경하는데, `ANUM = 100` 인 행만 적용한다.

만약 조건절을 붙이지 않으면 모든 데이터가 변경된다.

#### DELETE

원하는 조건을 검색해서 해당되는 행을 삭제한다. 만약 조건이 없으면 모든 데이터를 삭제한다.

```SQL
DELETE FROM A
	WHERE ANUM = 100;
```

`TRUNCATE` 옵션을 사용해서 용량을 초기화할 수 있다. `DELETE` 문을 사용해 데이터를 지운다 해도 용량은 감소하지 않는다.

`TRUNCATE DELETE FROM A` 구문을 사용하면 A테이블의 모든 데이터를 삭제함과 동시에 용량도 초기화한다.

#### SELECT

1. SELECT문 사용

   `*` 은 모든 데이터를 의미한다. `SELECT 원하는칼럼 FROM 조회를원하는테이블` 형식으로 사용한다. 조건절을 사용할 시 조건문에 있는 행만 조회한다.

   ```SQL
   SELECT * FROM EMP
   	WHERE 사원번호 = 100;
   ```

   칼럼 지정. `|| "원하는문자"` 형식은 정보 뒤에 원하는 문자를 붙여 출력한다.

   ```SQL
   SELECT ENAME || "님" FROM EMP;
   ```

2. ORDER BY를 사용한 정렬

   `SELECT` 를 사용시 정렬할 수 있다. 오름차순(기본지정) 혹은 내림차순(`DESC` 로 설정)으로 정렬한다. 정렬은 메모리 소모가 커서 성능저하가 발생할 수 있다.

   ```SQL
   SELECT * FROM EMP
   	ORDER BY ENAME, SAL DESC;
   ```

   `ENAME` `SAL` 을 내림차순으로 정렬한다는 코드

3. INDEX를 이용한 정렬회피.

   ```SQL
   SELECT /*+ INDEX_DESC(A)*/
   FROM EMP A;
   ```

   기본키를 이용하면 위 코드를 사용해 정렬을 한 상태로 조회하여 `order by` 를 회피할 수 있다.
   
4. distinct 와 alias

   + distinct

     칼럼명 앞에 지정하여 중복데이터를 한번만 조회하게 한다

     ```sql
     SELECT DISTINCT * FROM A;
     ```

   + alias(별칭)

     테이블명이나 칼럼이 너무 길어서 간략하게 할 떄 사용한다.

     ```sql
     SELECT ENAME AS "이름" FROM EMP A
     ```

     `ENAME` 대신에 `이름` 을 사용, `EMP` 대신에 `A` 사용



### WHERE

1. 비교연산자 : >, <, <=, >= ,=
2. 부정비교연산자 : !=, ^= <>, NOT 칼럼명 =(여기까지는 같지 않은 것), NOT 칼럼명 >(크지 않은 것)
3. 논리연산자 `AND` `OR` `NOT` 
4. SQL 연산자 `LIKE %비교문자열%` `BETWEEN A AND B`(A와 B값 사이) `IN`(OR을 의미하며 하나만 일치해도 조회) `IS NULL`(NULL값 조회)

#### LIKE문

`TEST` 로 시작하는 모든 데이터 조회

```SQL
SELECT * FORM A
WHERE E LIKE 'TEST%';
```

1로 끝난 ㄴ모든 데이터 조회

```SQL
SELECT * FORM A
WHERE E LIKE '%1';
```

중간에 `EST`가 있는 모든 데이터 조회

```SQL
SELECT * FORM A
WHERE E LIKE '%EST%';
```

#### BETWEEN문

1000이상 2000이하 조회

```SQL
SELECT * FROM A
WHERE SAL BETWEEM 1000 AND 2000;
```

1000미만 2000초과 조회

```SQL
SELECT * FROM A
WHERE SAL NOT BETWEEM 1000 AND 2000;
```

#### IN문

여러개의 칼럼에 대한 조건 지정

`(JOB, ENAME)` 이`('CLERK','TEST1')` 이거나 `('MANAGER','TEST4')` 인 칼럼을 찾는 것.

```SQL
SELECT * FROM A
WHERE (JOB, ENAME)
IN (('CLERK','TEST1'),('MANAGER','TEST4'))
```

#### NULL값 조회

1. NULL의 특징 : 모르는값, 값의부재. `NULL` 과 연산을하면 `NULL`. 비교시 알 수 없음이 반환
2. `NULL` 조회시 `IS NULL` 사용, 아닌값을 조회시 `IS NOT NULL` 사용
3. 관련함수
   + NVL : `NULL` 이면 다른 값으로 바꾸는 함수. `NVL(MGR,0)` 는 `MGR` 이 `NULL` 이면 0으로 변환한다는 뜻
   + NVL2 : `NVL2(MGR,1,0)` 은 `NULL` 이 아니면 1, `NULL` 이면 0 반환
   + NULLIF : 두 값이 같으면 `NULL`, 다르면 첫 번째 값 반환. `NULLIF(EXP1, EXP2)` 일때 `EXP1` 과 `EXP2` 가 같으면 `NULL` 을 반환, 아니면 `EXP1` 반환
   + COALESCE : `NULL` 이 아닌 최초의 인자값을 반환. `COALESCE(A, B, C)` 면 `A` 가`NULL` 이 아니면 `A` 를 반환. 만약 `A` 가 `NULL` 이고 `B` 가 `NULL`이 아니면 `B` 반환.



### GROUP 연산

#### GROUP BY

+ 테이블에서 소규모 행을 그룹화하여 계산.
+ `HAVING`구에 조건문 사용
+ `ORDER BY` 를 사용해 정렬.

`A` 로 그룹을 만들어 `B` 의 값을 합산하는 코드. `A` 로 그룹지어진 그룹마다 연산 실행. `A` 별 `B` 의 합계가 출력된다.

```SQL
SELECT A, SUM(B)
	FROM EMP
GROUP BY (A);
```

+ 부서별, 관리자별 급여평균 계산하고 급여평균이 1000 이상인 행 조회

  ```SQL
  SELECT DEPTNO, MGR, AVG(SAL) FROM EMP
  GROUP BY DEPTNO, MGR
  HAVING AVG(SAL) > 1000;
  ```

#### HAVING

`GROUP BY` 에 조건절을 사용하려면 `HAVING` 을 사용해야한다. 만약 `WHERE` 를 사용하면 조건문을 충족하지 못하는 데이터는 `GROUP BY` 대상에서 제외된다.

`A` 로 그룹을 지어서 그룹별 `B` 의 합계를 구한다. 이때, `B` 의 합계가 1000이상인 절을 출력한다.

```SQL
SELECT A,SUM(B) FROM E
GROUP BY A
HAVING SUM(B) > 1000;
```

#### 집계함수 종류

+ COUNT : 행 수를 조회한다. `COUNT(*)` 은 `NULL` 값을 포함한 모든 행을 계산한다. `COUNT(칼럼명)` 은 `NULL` 값을 제외한 행 수를 계산한다.
+ SUM : 합계를 계산한다.
+ AVG : 평균을 계산한다.
+ MAX, MIN : 최대, 최소값 계산
+ STDDEV : 표준편차 계산
+ VARIAN : 분산 계산



### SELECT 문 실행 순서

조회된 데이터를 이해하는데 아주 중요한 요소이다.

실행순서 (FWGHSOB)

1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY



### 명시적 형 변환과 암시적 형 변환

#### 형변환

두 개의 데이터의 데이터 타입이 일치하도록 변환하는 것.

숫자와 문자열, 문자열과 날짜형의 비교와 같이 데이터 타입이 불일치할 떄 발생

#### 명시적 형 변환

형 변환 함수를 사용해서 데이터 타입을 일치시키는 것으로 형변환 함수를 사용

1. TO_NUMBER(문자열) : 문자열을 숫자로 변환
2. TO_CHAR(숫자 혹은 날짜, [FORMAT]) : 숫자 혹은 날짜를 지정된 FORMAT의 문자로 변환
3. TO_DATE(문자열, FORMAT) : 문자열을 지정된 FORMAT의 날짜형으로 변환한다.

#### 암시적 형변환

개발자가 형 변환을 하지 않은 경우 데이터베이스 관리 시스템이 자동으로 형변환 하는 것을 의미한다.

__인덱스 칼럼에 형변환을 수행하면 인덱스를 사용하지 못한다__

인덱스는 변형이 발생하면 기본적으로 사용하지 못한다. 형변환이 이루어지면 사용할 수 없다.



### 내장형 함수

모든 DB에는 `SQL` 에서 사용할 수 있는 내장형 함수를 가지고있다.

내장형 함수는 데이터베이스 관리 시스템 밴더별로 약간의 차이가 있지만 거의 비슷하다.

#### DUAL 테이블

`DUAL 테이블` 은 오라클 DB에 의해 자동으로 생성되는 테이블.

#### 내장형 함수

+ 문자열 함수
  + ASCII(문자) : 문자 혹은 숫자를 `ASCII` 코드값으로 변환
  + CHAR(ASCII 코드값) : `ASCII` 코드값을 문자로 변환
  + SUBSTR(문자열, M, N) : 문자열의 M번째 위치부터 N개를 자른다.
  + CONCAT(문자열1, 문자열2) : `문자열1` 과 `문자열2` 를 결합한다.
  + LOWER(문자열) : 영문자를 소문자로 변환한다. `UPPER` 는 대문자로 변환한다.
  + LEN(문자열) : 문자열의 길이를 알려준다.
  + LTRIM(문자열, 지정문자) : 왼쪽에서 지정문자를 삭제한다. 지정된 문자를 삭제하면 공백을 삭제한다.
  + RTRIM(문자열, 지정문자) : 오른쪽에서 지정문자를 삭제한다. 지정된 문자를 삭제하면 공백을 삭제한다.
  + TRIM(문자열, 지정문자) : 지정문자를 삭제한다. 지정된 문자를 삭제하면 공백을 삭제한다.
+ 날짜형 함수
  + SYSDATE : 오늘의 날짜를 날짜 타입으로 알려준다.
  + EXTRACT('YEAR' | 'MONTH' | 'DAY FROM DUAL') : 날짜에서 년, 월, 일을 조회한다.
+ 숫자형 함수
  + ABS(숫자) : 절대값을 돌려준다
  + SIGN(숫자) : 양수, 음수, 0을 구별한다.
  + MOD(숫자1, 숫자2) : `숫자1` 을 `숫자2` 로 나누어 나머지를 계산한다. %도 사용 가능하다.
  + CEIL(숫자) : 숫자보다 크거나 같은 최소의 정수를 돌려준다.
  + FLOOR(숫자) : 숫자보다 작거나 같은 최대의 정수를 돌려준다.
  + ROUND(숫자, M) : 소수점 `M` 번째 자리에서 반올림한다. 기본값은 0이다
  + TRUNC(숫자, M) : 소수점  `M` 자리에서 절삭한다. 기본값은 0이다.



### DECODE, CASE

#### DECODE

IF문을 구현할 수 있다. 특정 조건이 참이면 A, 거짓이면 B로 응답한다.

`A = 1000` 이면 `TRUE` 아니면 `FALSE`

```SQL
DECODE(A,1000,'TRUE','FALSE')
```

#### CASE

조건을 `WHEN` 구에 사용하고 `THEN` 구는 해당 조건이 참이면 실행되고 거짓이면 `ELSE` 구가 실행된다.

```SQL
CASE[A]
	WHEN B = 100 THEN RESULT1
	WHEN B = 200 THEN RESULT2
	WHEN B = 300 THEN RESULT3
	ELSE RESULT4
END
```



### ROWNUM, ROWID

#### ROWNUM

데이터베이스의 `SELECT` 결과에 대해서 논리적인 일련번호를 부여한다. 조회되는 행 수를 제한할 때 사용된다. 

만약 페이지 단위 출력을 하기 위해서는 인라인 뷰를 사용해야한다.

+ 인라인 뷰 : `SELECT` 문에서 `FROM` 절에 사용되는 서브쿼리를 의미한다.

  ```SQL
  SELECT * FROM # MAIN QUERY
  (SELECT * FROM EMP) A; # SUB QUERY(인라인 뷰)
  ```

한 행을 조회할 경우

```SQL
SELECT * FROM A
WHERE ROWNUM <= 1;
```

인라인 뷰 사용. `ROWNUM` 에 별칭 `LIST` 를 사용하여 `LIST` 로 행 조회수를 제한한다.

```SQL
SELECT *
FROM (SELECT ROWNUM LIST, ENAME FROM EMP)
WHERE LIST <= 5;
```

웹페이지 형식처럼 특정 구간 조회도 가능하다.

```SQL
SELECT *
FROM (SELECT ROWNUM LIST, ENAME FROM EMP)
WHERE LIST BETWEEN 5 AND 10;
```

#### ROWID

데이터베이스 내에서 데이터를 구분할 수 있는 유일한 값이다. `ROWID` 를 통해 데이터가 어떤 데이터파일, 블록에 저장되어 있는지 알 수 있다.



### WITH

서브쿼리를 사용해서 임시 테이블이나 뷰처럼 사용할 수 있는 구문이다.

서브쿼리 블록에 별칭을 지정할 수 있다. 옵티마이저는 SQL을 인라인 뷰나 임시테이블로 판단한다.

서브쿼리를 사용해서 임시테이블을 만든다.

```SQL
WITH VIEWDATA AS(
SELECT * FROM EMP
	UNION ALL
SELECT * FROM EMP
)
SELECT * FROM VIEWDATA WHERE EMPNO = 1000;
```



### DCL(Data Control Language)

#### GRANT

데이터베이스 사용자에게 권한을 부여한다.

```SQL
GRANT 권한 ON 테이블명 TO USER;
```

+ 권한
  + SELECT : 해당 명령어에 대한 권한 부여
  + INSERT :해당 명령어에 대한 권한 부여
  + UPDATE : 해당 명령어에 대한 권한 부여
  + DELETE : 해당 명령어에 대한 권한 부여
  + REFERENCES : 테이블을 참조하는 제약조건을 생성하는 권한 부여
  + ALTER : 테이블 수정 권한 부여
  + INDEX : 인덱스 생성 권한 부여
  + ALL : 모든 권한 부여
+ WITH GRANT OPTION : 특정 사용자에게 권한을 부여할 수 있는 권한을 준다. A사용자가  B사용자에게 권한을 주고, B가 C에게 권한을 줬을 때, A가 B에게서 권한을 뺏으면 C의 권한도 회수된다.
+ WITH ADMIN OPTION : 테이블에 대한 모든 권한을 부여한다. A가 B에게 권한을 주고, B가 C에게 권한을 줬을 때, A가 B에게서 권한을 취소하면 B의 권한만 사라지고 C의 권한은 사라지지 않는다.

#### REVOKE

데이터베이스 사용자에게 부여된 권한을 회수한다.

```SQL 
REVOKE 권한 ON 테이블명 FROM USER;
```



### TCL (Transation Control Language)

#### COMMIT

변경한 데이터를 데이터베이스에 반영한다. 변경 이전 데이터는 잃어버린다. A -> B 이면 A는 사라진다.

`COMMIT` 이 완료되면 데이터베이스 변경으로 인한 잠금이 해제된다. 다른 모든 사용자는 변경된 데이터를 조작할 수 있다.

`COMMIT` 은 하나의 트랜잭션 과정을 종료한다.

---

`INSERT` `UPDATE` `DELETE` 가 트랜잭션 ------ `COMMIT` -----> 변경 후 데이터를 데이터베이스에 저장

---

`AUTO COMMIT` 은 프로그램을 정상적으로 종료하는경우 자동으로 `COMMIT` 을 실행한다.

#### ROLLBACK

변경 사용을 모두 취소하고 트랜잭션을 종료한다.

다만 `COMMIT` 한 곳까지만 복구한다.

`ROLLBACK` 을 실행하면 잠금이 해제되고 다른 사용자도 데이터베이스 행을 조작할 수 있다.

#### SAVEPOINT

트랜잭션을 작게 분할하여 관리하는 것으로 지정된 위치 이후의 트랜잭션만  `ROLLBACK` 이 가능하다.

지정된 `SAVEPOINT` 까지 데이터 변경을 취소하고 싶다면 `ROLLBACK TO SAVEPOIT이름` 으로 실행한다.

그냥 `ROLLBACK` 을 사용하면 `SAVEPOIT` 와 관계없이 데이터의 모든 변경사항을 저장하지 않는다.



## SQL 활용

### join

#### 등가 조인

+ 등가 조인

1. 조인은 여러개의 릴레이션을 사용해 새로운 릴레이션을 만드는 과정이다. 가장 기본은 교집합을 만든 것.
2. 등가 조인은 두 개의 테이블에서 일치하는 것을 조인한다.

```sql
SELECT * FROM A, B
WHERE A.name = B.name;
```

`A` 와 `B` 의 같은 내용을 가지는 테이블을 사용해 `=` 을 가지고 연결한다.

+ INNER JOIN

  두 개의 테이블 간에 교집합만을 조회한다.

  ```SQL
  SELECT * FROM EMP INNER JOIN DEPT
  ON EMP.DEPTNO = DEPT.DEPTNO
  AND EMP.ENAME = 100
  ORDER BY ENAME;
  ```

  `INNER JOIN DEPT` 를 사용해 조인을 실행할 테이블을 지정하고, `ON` 을 조건으로 사용해 연결한다.

  `AND` 를 사용해 조인조건을 추가로 서술할 수 있다.

+ 해시조인

  먼저 선행 테이블을 결정하고 그 다음 후행 테이블을 결정하는 조인 방법이다. 해시함수를 사용하여 메인메모리에 해시 테이블을 생성한다.

+ INTERSECT 연산

  두 개의 테이블에서 교집합을 조회한다. 두 개 테이블에서 공통된 값을 조회한다.

  ```SQL
  SELECT DEPTNO FROM ENP
  INTERSECT
  SELECT DEPTNO FROM DEPT;
  ```

  이 경우 `EMP` 와  `DEPT` 에 모두 존재하는 `DEPTNO` 이 조회된다.

#### 비 등가 조인

두 개의 테이블 간에 조인하는 경우 `=` 를 사용하지 않고 부등호를 사용하는 조인이다. 정확하게 일치하지 않는것을 조인한다,

#### OUTER JOIN

두 개의 테이블 간에 교집합을 조회하고 한쪽 테이블에만 있는 데이터도 포함시켜서 조회한다.

이때 왼쪽 테이블에 있는 행만 포함하면 `LEFT OUTER JOIN` , 오른쪽 테이블의 행만 포함시키면  `RIGHT OUTER JION` 이라 한다.

둘 다 포함시키면 `FULL OUTER JOIN` 이라 한다.

```SQL
SELECT * FROM A LEFT OUTER JOIN B
ON B.NAME = A.NAME;

SELECT * FROM A RIGHT OUTER JOIN B
ON B.NAME = A.NAME;

SELECT * FROM A FULL OUTER JOIN B
ON B.NAME = A.NAME;
```

`NAME` 이 가지고있는 모든 행을 조회한다. `INNER JOIN` 은 둘 다 가지고 있는 행만 조회되지만, `OUTER JOIN` 은 모든 행이 조회된다.

예를 들어 `A.NAEM` 에는 `1,2,3,4` 이고 `B.NAME` 에는 `1,2,3,5` 이 있을 경우

+ LEFT OUTER JOIN : 1,2,3,4 조회
+ RIGHT OUTER JOIN : 1,2,3,5 조회
+ FULL OUTER JOIN : 1,2,3,4,5 조회

#### CROSS JOIN

조인 조건구 없이 2개의 테이블을 하나로 조인한다. 카테시안곱이 발생한다. `A` 와 `B` 를 CROSS JOIN 하면 `A` 의 행 수 * `B` 의 행 수 만큼의 행 수가 출력된다.

`A` 가 14, `B` 가 4일 경우 56개의 행이 나온다.

#### UNION

1. `UNION` 연산은 두 개의 테이블을 하나로 만드는 연산이다. 즉, 2개의 테이블을 하나로 합치는 것이다. 주의사항은 두개의 테이블의 칼럼수, 칼럼의 데이터 형식 모두가 일치해야한다. 만약 다르면 오류가 발생한다.
2. 유니온 연산은 중복된 데이터를 제거한다. 따라서 정렬과정을 발생시킨다.
3. `UNION ALL` : 두 개의 테이블을 하나로 만들지만 중복을 제거하거나 정렬을 유발하지 않는다.

#### MINUS

마이너스 연산은 두 개의 테이블에서 차집합을 조회한다. 먼저 쓴 SELECT에는 있고 뒤에 쓴 SELECT에는 없는 집합을 조회한다.

```SQL
SELECT NAME FROM A
MINUS
SELECT NAME FROM B
```

`A` 에는 있고 `B` 에는 없는 `NAME` 을 출력한다.



### 계층형 조회

트리 형태의 구조를 위에서 아래로 탐색하면서 조회한다. 역방향도 가능하다.

#### CONNECT BY

트리 형태의 구조로 질의를 수행하는 것으로, `START WITH`는 시작 조건을 의미하고 `CONNECT BY PRIOR` 는 조인조건이다.

`LEVEL` 은 계층값이다.

```SQL 
SELECT MAX(LEVEL) FROM A
START WITH MGR IS NULL
CONNECT BY PRIOR ANO = MGR;
```

`MGR` 이 `NULL`  값인 것 부터 시작한다. `ANO` 과 `MGR` 이 같은 것을 연결해서 트리를 형성한다.



### 서브쿼리

#### 메인쿼리와 서브쿼리

서브쿼리는 `SELECT` 문 안에 다시 `SELECT` 문을 사용하는 것이다.

#### 단일 행 서브쿼리와 다중 행 서브쿼리

반환하는 행 수가 한개인 것을 단일 행 서브쿼리라고 한다. 비교 연산자를 사용한다.

반환하는 행 수가 여러개인 것을 다중 행 서브쿼리라 한다. `IN` `ANY` `ALL` `EXISTS` 를 사용해야 한다.

#### IN

반환되는 여러 행 중 하나만 참이어도 참이 되는 연산이다.

```SQL
SELECT * FROM A,B
WHERE A.NAME = B.NAME
AND A.EMPNO
IN(SELECT EMPNO FROM A
  WHERE SAL > 2000);
```

위 SQL은 `SAL > 2000` 인 `EMPNO` 을 반환 하고 반환된 `EMPNO` 과 메인쿼리에 있는 `EMPNO` 과 같은 것을 조회한다.

#### ALL

서브쿼리와 메인쿼리의 결과가 모두 동일하면 참이된다.

#### EXISTS

어떤 데이터의 존재여부를 확인하는 것이다. 결과는 참과 거짓이 된다.

#### 스칼라 서브쿼리

스칼라 서브쿼리는 반드시 한 행과 한 칼럼만 반환한다. 만약 여러행이 반환되면 오류가 발생한다.

#### 연관 서브쿼리

서브쿼리 내에서 메인쿼리 내의 칼럼을 사용하는 것을 말한다.



### 그룹함수

#### ROLLUP

`GROUP BY` 칼럼에 대해서 서브토탈을 만들어준다. 

```SQL
SELECT DECODE(DEPTNO,NULL,'전체합계',DEPTNO), SUM(SAL) # DEPTNO = NULL이면 전체합계 문자를 출력한다. 아니면 DEPTNO을 출력한다.
	FROM EMP
	GROUP BY ROLLUP(DEPTNO, JOB)
```

`DEPTNO` 과 `JOB` 에 따라서 합계를 구한다. `DEPTNO` 이 10, 20, 30이고 `JOB` 이 A, B일 경우

10	A	합계

10	B	합계

10		  합계

20	A	합계

20	B	합계

20			합계

30	A	합계

30	B	합계

30			합계

와 같이 `DEPTNO` 과` JOB` 에 대해서 그룹을 지어 합계를 산출한다.

#### GROUPING 함수

GROUPING 함수는 ROLLUP, CUBE, GROUPING SETS에서 생성되는 합계값을 구분하기 위해 만들어진 함수이다.

소계, 합계등이 계산되면 GROUPING은 1을 반환하고 아닐경우 0을 반환하여 합계값을 식별할 수 있다.

GROUPING 반환값을 DECODE 혹은 CASE문으로 식별하여 소계와 합계를 구분한다.

#### GROUPING SETS 함수

`GROUP BY` 에 나오는 칼럼의 순서와 관계없이 다양한 소계를 만들 수 있다. 모두 개별적으로 처리한다.

```SQL 
SELECT * FROM A
GROUP BY GROUPING SETS(NAME, JOB)
```

`NAME` 과 `JOB` 을 각각의 그룹으로 합계를 계산한다. 즉, 서로 관계를 가지지 않는다.

#### CUBE 함수

결합 가능한 모든 집계를 계산한다.

다차원 집계를 제공하여 다양한 데이터를 분석할 수 있다.

예를들어 부서와 직업을 CUBE로 사용하면 부서별 합계, 직업별 합계, 부서별 직업별 합계, 전체 합계가 조회된다.

즉, 조합할 수 있는 모든 경우의 수가 조합된다.



### 윈도우 함수

#### 윈도우 함수

윈도우 함수는 행과 행 간의 관계를 정의하기 위해서 제공되는 함수이다. 순위, 합계, 평균, 행 위치 등을 조작할 수 있다.

+ WINDOWING
  + ROWS : 부분집합인 윈도우 크기를 물리적 단위로 행의 집합을 지정한다.
  + RANGE : 논리적인 주소에 의해 행 집합을 지정한다.
  + BETWEEN ~ AND ~ : 윈도우의 시작과 끝의 위치를 지정한다.
  + UNBOUNDED PRECENDING : 윈도우의 시작 위치가 첫번째 행임을 의미한다.
  + UNBOUNDED FOLLOWING : 윈도우 마지막 위치가 마지막 행임을 의미한다.
  + CURRENT ROW : 윈도우 시작 위치가 현재 행임을 의미한다.

```SQL
SELECT EMPNO, ENAME, SAL, SUM(SAL) OVER(ORDER BY SAL
                                       ROWS BETWEEN CURRENT ROW
                                       AND UNBOUNDED FOLLOWING) TOTAL
                                       FROM EMP;
```

`TOTAL` 컬럼은 현재 행부터 마지막 행까지의 합계로 나오고, 이 순서로 정렬한다.

즉, 2번째 행의 `TOTAL` 은 2번째행부터 마지막 행까지의 합꼐이다.

`OVER` 는 윈도우 함수뒤에 조건을 사용하는 방법이다.

#### 순위함수

특정 항목과 파티션에 대해서 순위를 계산할 수 있다.

+ 순위 관련 윈도우 함수

  만약 1, 2, 2, 3, 4, 5, 5, 5, 6 과 같이 있을 경우 순서

  + RANK : 특정 항목 및 파티션에 순위를 계산한다. 동일한 순위는 동일한 값이 부여된다.

     -> 1 2 2 4 5 6 6 6 9 순서, 동일한 순위인 2가 2개있으므로 3은 없다. 2 2 다음은 4

  + DENSE_RANK : 동일한 순위를 하나의 건수로 계산한다.

     -> 1 2 2 3 4 5 5 5 6순서, 2 2 다음은 2의 개수와 상관없이 3

  + ROW_NUMBER : 동일한 순위에 대해서 고유의 순위를 부여한다.

     -> 1 2 3 4 5 6 7 8 9 순서. 2 2여도 고유의 순서를 부여해 2 3 으로 표기

#### 집계함수

`SUM` `AVG` `COUNT` `MAX` `MIN`

#### 행 순서 관련 함수

행 순서 관련 함수는 상위 행의 값을 하위에 출력하거나 하위 행의 값을 상위 행에 출력할 수 있다.

+ 행 순서 관련 윈도우 함수
  + FIRST_VALUE : 가장 처음에 나오는 값을 구한다.
  + LAST_VALUE : 가장 마지막에 나오는 값을 구한다.
  + LAG : 이전 행을 가지고 온다
  + LEAD : 특정 위치의 행을 가지고 온다.



### 테이블 파티션

#### 파티션 기능

파티션은 대용량의 테이블을 여러개의 데이터 파일에 분리해서 저장한다.

테이블의 데이터가 물리적으로 분리된 데이터 파일에 저장되면 입력 수정 삭제 조회 성능이 향상된다.

#### RANGE PARTITION

테이블의 칼럼 중에서 값의 범위를 기준으로 여러개의 파티션으로 데이터를 나누어 저장하는 것이다.

#### LIST PARTITION

특정 값을 기준으로 분할하는 방법이다.

#### HASH PARTITION

데이터베이스 관리 시스템이 내부적으로 해시 함수를 사용해서 데이터를 분할한다. 즉, 데이터베이스 관리 시스템이 알아서 분할하고 관리한다.





## SQL 최적화 원리

### 옵티마이저

#### 옵티마이저

sql개발자가 sql을 작성하여 실행할 때, 옵티마이저는 어떻게 실행할 것인지 계획하게된다. 즉, 실행계획을 수립하고 sql을 실행한다.

동일한 결과가 나오는 sql도 어떻게 실행하느냐에 따라서 성능이 달라진다.

+ 특징 

  오브젝트 통계, 시스템 통계등의 정보를 사용해 예상되는 비용을 산정한다.

  이중 최저비용을 가진 계획을 선택해 실행한다.

+ 필요성

  sql은 어떻게 실행하느냐에 따라 성능이 달라진다.

  만약 옵티마이저가 비효율적으로 실행계획을 수립하면, sql개발자는 sql을 개선해야한다. 이때, 옵티마이저에게 실행계획을 변경하도록 요청할 수 있다.

  이때는 힌트(HINT) 를 사용해야한다.

+ 실행계획 확인

  옵티마이저는 실행계획을 `PLAN_TABLE` 에 저장한다. 이를 조회하여 확인할 수 있다.

  가장 편리하게 실행계획을 확인하는 방법은 `TOAD` 에서 `Execution Plan Current SQL` 메뉴를 클릭한다.

#### 종류

1. 실행방법
   + sql을 실행하면 파싱을 하여 문법 검사 및 구문분석을 수행한다.
   + 구문 분석이 완료되면 규칙기반 혹은 비용기반으로 실행계획을 수립한다. 기본적으로는 비용기반으로 수립한다.
   + 실행계획이 수립되면 최종적으로 sql을 실행하고 실행이 완료되면 데이터를 인출한다.
2. 옵티마이저 엔진
   + 15개의 우선순위를 기준으로 실행계획을 수립한다.
   + `/*+ RULE +*/` 구문을 사용해 규칙기반으로 실행할 수 있다.



### 인덱스

#### 인덱스

인덱스는 데이터를 빠르게 검색할 수 있는 방법을 제공한다.

인덱스의 구조는  `root block`(인덱스 트리에서 가장 상위에 있는 노드) `branch block`(다음 단계의 주소를 가지고 있는 포인터) `leaf block`(인덱스 키와 ROWID로 구성되고 인덱스 키는 정렬되어 저장) 으로 구성된다.

#### 인덱스 생성

`CREATE INDEX` 문을 사용해 생성한다. 기본적으로 오름차순 정렬이며, `DESC` 옵션으로 내림차순 정렬도 가능하다.

```SQL
CREATE INDEX 인덱스이름 EMP ON
	EMP (ENAME ASC, SAL DESC) # ENAME은 오름차순으로, SAL은 내림차순으로 인덱스를 생성한다.
```

`ASC` 옵션은 생략 가능하다.

#### 인덱스 스캔

1. 인덱스 유일 스캔
   + 인덱스의 키 값이 중복되지 않는 경우, 해당 인덱스를 사용할 때 발생된다.
   + 예를 들어 사원번호가 중복되지 않는 경우 하나의 사우너번호를 조회한다.
2. 인덱스 범위 스캔
   + 특정 범위를 조회하는 `WHERE` 문을 사용할 경우 발생한다.
3. 인덱스 전체 스캔
   + 인덱스에서 검색되는 인덱스 키가 많은 경우에 처음부터 끝까지 `Leaf Block` 을 읽어온다.



### 옵티마이저 조인

#### Nested Loop Join

하나의 테이블을 먼저 찾고 그 다음 테이블을 조인하는 방식으로 실행된다.

먼저 조회되는 테이블을 `outer table` 이라 하고 그 다음에 조회되는 테이블을 `inner table` 이라한다.

선행 테이블의 크기가 작은 것을 먼저 찾는게 중요한데, 그래야 데이터가 스캔되는 범위를 줄일 수 있다.

`nested loop join` 은 `RANDOM ACCESS` 가 발생한다. 이는 성능지연을 발생시킨다. 즉  `RANDOM ACCESS` 의 양을 줄여야 성능이 향상된다.

#### Sort Merge Join

두 개의 테이블을 메모리 공간에 모두 로딩하고 정렬을 수행한다. 정렬이 완료되면 두 개의 테이블을 병합한다.

`sort merge join` 은 정렬이 발생하기 때문에 데이터양이 너무 많아지면 성능이 떨어진다. 정렬 데이터 양이 너무 많으면 정렬은 임시영역에서 수행된다. 임시영역은 디스크에 있기 떄문에 성능이 급격히 떨어진다.

#### Hash Join

두 개의 테이블 중에서 작은 테이블을 `HASH` 메모리에 로딩하고 두 개의 테이블의 조인 키를 사용해서 해시테이블을 생성한다.

cpu연산이 많다.





