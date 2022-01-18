# day 5

## pandas

### 데이터 살펴보기

#### 데이터 요약정보 확인하기

+ 각 열의 고유값 개수

  `value_counts()` 메소드는 각 열의 고유값의 개수를 출력한다. 범주형 변수들로 이루어진 경우 각 범주의 개수를 세서 반환한다. `value_counts()` 는 시리즈를 반환한다.

  ```python
  unique = dataframe['열이름'].value_counts()
  print(uq)
  ```

#### 통계함수 적용

object 타입의 데이터는 산술정보를 계산하지 않는다. 산술데이터는 숫자형 데이터에서만 계산된다.

+ 평균값

  ```python
  df.mean()
  df['열이름'].mean()
  df.열이름.mean()
  ```

+ 중앙값

  ```python
  df.median()
  df['열이름'].medain()
  df.열이름.median()
  ```

+ 최대값

  object 타입의 경우 아스키 코드값을 기준으로 최대값을 판단한다

  ```python
  df.max()
  df['열이름'].max()
  df.열이름.max()
  ```

+ 최소값

  ```python
  df.min()
  df['열이름'].min()
  df.열이름.min()
  ```

+ 표준편차

  ```python
  df.std()
  df['열이름'].std()
  df.열이름.std()
  ```

+ 상관계수

  상관계수는 -1 ~ 1의 값을 가지며, 위의 산술정보들과 마찬가지로 열을 뽑아서 출력할 수 있지만, 서로 다른 두 개의 열을 사용해야한다. 만약 같은 열을 사용한다면 상관계수는 1이 나올 것이다.

  ```python
  df.corr()
  print(df[['열이름 1','열 이름2']].corr())
  ```

+ 상관관계

  ![image-20220118094931467](day05.assets/image-20220118094931467.png)

  위의 그림은 산점도이다. 산점도는 데이터의 분포에 따른 상관관계를 보여주는 그림이다. 데이터 분석 시 좋은 데이터를 넣어야 좋은 결과를 얻는다. 데이터 간의 상관관계를 잘 확인하고 input을 해줘야 더 좋은 output을 받을 수 있다.



## 그래프

### 판다스 내장 그래프 도구

#### plot 메소드

기본 사용법 `dataframe.plot()` .  `kind = ` 옵션을 사용하여 그래프를 변경할 수 있다.

+ 선 그래프

  `plot()` 메소드에 아무런 옵션을 지정하지 않으면 기본적으로 선 그래프가 출력된다.

  ```python
  df.plot()
  ```

+ 막대 그래프

  ```python
  df.plot(kind = 'bar')
  ```

+ 히스토그램

  ```python
  df.plot(kind = 'hist')
  ```

+ 산점도

  변수는 열을 의미한다.

  ```python
  df.plot(x = '변수 1', y = '변수 2', kind = 'scatter' )
  ```

+ 박스 플랏

  ```python
  df['변수 선택'].plot(kind = 'box')
  ```

  변수 선택은 리스트를 이용하여 여러개의 변수를 선택할 수 있다.

  `df[['a','b']].plot(kind = 'box')`

## 데이터 분석

### 공공데이터 분석

#### 기상청 기온 데이터

[기상자료 포탈](https://data.kma.go.kr)에 들어가면 기온과 관련된 공공데이터를 받을 수 있다. 통계 분석의 기온 분석 데이터를 사용하였다. 

#### csv 파일의 로드

```python
import csv
f = open('c:/sh/study/study everyday/data files/seoul.csv')
data = csv.reader(f, delimiter = ',')
print(data)
f.close
```







