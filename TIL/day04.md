# day 4

## numpy

#### array

+ array 생성

  ```python
  import numpy as np
  np.array([1,4,2,5])
  ```

  `dtype` 을 사용해 원하는 자료형으로 바꿀 수 있다

  ```python
  np.array([1,4,2.4,5],dtype=int)
  ```

  서로 다른 자료형이 묶여있을 경우 더 상위 자료형으로 선언된다

  ```python
  np.array([1,'a',3,4.5]) 
  ```

  이중으로 선언 가능하다

  ```python
  np.array([[1,2,3],[4,5,6],[7,8,9,]])
  ```

#### 난수

+ 난수 발생.

  ```python
  np.random.random(10)
  # 범위 지정해서 난수 발생
  np.random.normal(10000,2000,(3,3))
  # normal함수는 평균(0), 표준편차(1)인 난수를 발생시킴. 괄호안은 지정값.
  np.random.normal(0,1,10)
  # 1~37까지 랜덤하게 정수뽑기
  np.random.randint(1,37,(4,3))
  ```

  

## pandas

### 시리즈

시리즈는 인덱스와 데이터 값으로 이루어져 있는 pandas 데이터 형식이다.

#### 데이터를 시리즈로 변환

+ 딕셔너리 -> 시리즈 변환

  딕셔너리의 key가 시리즈의 인덱스로, value는 데이터값으로 들어가게 된다.

  ``` python
  import pandas as pd
  dict_data = {'a':1,'b':2,'c':3}
  sr=pd.Series(data)
  ```

+ 리스트 -> 시리즈 변환

  ```python
  import pandas as pd
  list_data = ['2019-01-02',3.14,'ABC',100,True]
  sr = pd.Series(list_data)
  ```

+ 튜플 -> 시리즈 변환

  index 함수를 이용해서 튜플 데이터의 인덱스를 지정해 줄 수 있다.

  ```python
  import pandas as pd
  tup_data = ('민수','2017-04-08','du',True)
  sr = pd.Series(tup_data, index = ['이름','생년월일','성별','학생여부'])
  ```


#### 시리즈의 연산

시리즈의 연산은 시리즈vs시리즈 간에도 가능하고 시리즈vs숫자 간에도 가능하다. 시리즈 vs 시리즈 연산의 경우, 각각의 시리즈가 서로 다른 인덱스의 순서를 가지고 있더라도 같은 인덱스끼리 연산이된다.

+ 사칙연산

  시리즈는 시리즈 끼리 사칙연산의 수행이 가능하다. 만약 `NaN`값이 있을 경우 사칙연산의 결과값은 `NaN` 값이 나온다.

  ```python
  student1 = pd.Series({'국어':100,'영어':80,'수학':90})
  student2 = pd.Series({'수학':80,'국어':75,'영어':85})
  
  addiction = student1 + student2
  subtraction = student1 - student2
  multiplication = student1 * student2
  division = student1 / student2
  ```

+ 시리즈의 연산메소드

  시리즈의 연산메소드를 사용해서 사칙연산을 사용할 수 있다. 이때, `NaN`값을 `fill_value` 를 사용하여 바꿔줄 수 있다. 

  `series1.함수(series2)` -> series 1과 series 2를 특정 메소드로 연산한다.

  ```python
  sr_add = student1.add(student2,fill_value = 0)
  sr_sub = student1.sub(student2,fill_value = 0)
  sr_mul = student1.mul(student2,fill_value = 0)
  sr_div = student1.div(student2,fill_value = 0)
  ```

  

### 데이터 프레임

데이터 프레임은 2차원 형태의 pandas 데이터 형식이다.

#### 데이터를 데이터 프레임으로 변환

+ 리스트 -> 데이터프레임 변환

  데이터 프레임으로 변환할때는 index 이름을 설정해주어야한다. 만약 index를 설정해주지 않으면 0, 1, 2.. 와 같이 숫자가 인덱스로 들어가게 된다. 

  ```python
  import pandas as pd
  df = pd.DataFrame([[15,'남','덕명중'],[17,'여','수리중']], index=['준서','예은'],columns=['나이','성별','학교'])
  ```

  데이터 프레임의 인덱스만을 따로 바꿔줄 수 있다. `index` 함수는 데이터 프레임의 row의 인덱스를 변경해주고 `columns` 는 column 인덱스를 변경해준다.

  ```python
  df.index = ['st1','st2']
  df.columns = ['연령','남녀','소속']
  ```

  `rename` 함수를 사용하여 데이터프레임의 인덱스를 변경해줄 수 있다. 마찬가지로 `index` 는 row index를, `columns` 는 column index를 변경해준다.

  ```python
  df.rename(columns={'age' : '연령', 'sex' : '남녀', 'school': '소속'},inplace=True)
  df.rename(index={'junseo':'student 1', 'yeun':'student 2'},inplace=True)
  ```

  서로 다른 두 개의 리스트를 병합하여 데이터프레임을 만들 수 있다.

  ```python
  import pandas as pd
  x = [1,2,3]
  y = [4,5,6]
  df = pd.DataFrame(x ,y)
  ```

+ 딕셔너리 -> 데이터프레임 변환

  딕셔너리 형태의 데이터를 데이터프레임으로 변환하면 딕셔너리의 key가 column index로 들어가게 된다.

  ```python
  import pandas as pd
  df_data = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9],'d':[10,11,12]}
  dff = pd.DataFrame(df_data)
  ```

  딕셔너리를 데이터 프레임으로 변환한 다음에도 row index를 설정해줄 수 있다.

  ```python 
  df = pd.DataFrame(data, index = ['서준','우현','인아'])
  ```

#### 데이터 프레임의 삭제

다음과 같은 데이터 프레임을 만들었다고 가정하자

``` python
import pandas as pd
data = {'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
df = pd.DataFrame(data, index = ['서준','우현','인아'])
```

결과는 다음과 같다.

​	    수학  영어   음악   체육 

서준  90     98      85     100

우현  80     89      95     90 

인아  70     95     100    90

+  데이터프레임의 행 삭제

  axis = 0, inplace = True 를 설정해줘야 한다. axis = 0 이라는 의미는 행을 선택한다는 의미이다. 만약 선택한 인덱스가 row index가 아닐 경우 에러가 발생하게 된다. inplace = False 인 경우 변경사항이 데이터 프레임에 반영되지 않는다.

  ```python
  df.drop('우현',axis = 0, inplace=True)
  ```

+ 데이터프레임 열 삭제

  axis = 1로 설정을 해주면 column index를 삭제한다.

  ``` python
  df4.drop('수학',axis=1,inplace=True)
  ```

#### 데이터 프레임의 선택

앞선 데이터 프레임을 계속해서 사용한다고 가정한다.

데이터 프레임의 행과 열을 선택할 경우에는 `loc` 함수와 `iloc` 함수를 사용할 수 있다. `loc` 함수는 인덱스의 이름을 이용하여 선택하는 방법이고 `iloc` 함수는 인덱스의 정수형 위치, 즉 0, 1, 2... 와 같은 숫자를 이용하여 선택하는 방법이다. 각각의 방법은 문제를 해결해야하는 방법에 따라 다양하게 사용될 수 있다.

`loc` 함수는 범위를 슬라이싱으로 지정할 때 범위의 끝 부분을 포함한다. `iloc` 함수는 반대로 범위의 끝을 제외한다. 

+ 행 선택

  행 선택은 다음과 같이 사용할 수 있다.

  ```python
  label1 = df.loc['서준']	# 데이터 프레임의 '서준' 행 선택
  print(label1)			 # '서준' 행 출력
  
  position1 = df.iloc[0]   # 데이터 프레임의 '0'번째 행 선택
  print(position1)		 # '0'번째 행 출력
  ```

  `loc` 함수와 `iloc` 함수 [ ] 를 이용하여 리스트를 만들어 사용할 수 있다. 리스트 안에 지정된 행을 모두 출력한다.

  ```python
  label2 = df.loc[['서준','우현']]
  position2 = df.iloc[[0,1]]
  ```

  마찬가지로 슬라이싱을 활용하여 사용할 수 있다. 이때 `iloc` 함수는 `0:1` 일 경우 0번째 행만 선택된다. 만약 `0:3` 일 경우 0, 1, 2번째 행이 선택된다. 범위의 끝은 제외한다. 반대로 `loc` 함수는 범위의 끝을 포함한다.

  ```python
  label3 = df.loc['서준':'우현']
  position3 = df.iloc[0:1]
  ```

+ 열 선택

  열 선택은 다음과 같이 사용할 수 있다.

  ``` python
  math1 = df['수학']   # '수학' 열 선택
  print(math1)		# '수학' 열 출력
  
  print(df.수학)	   # '수학' 열 선택 후 출력
  
  mg = df[['음악','체육']] # 여려 열 선택 후 출력
  print(mg)
  ```

+ 인덱스 슬라이싱

  `iloc` 함수를 이용해 인덱스를 슬라이싱하여 추출할 수 있다. `[0 : 2 : 1]` 은 0부터 2까지 1씩 증가하면서 선택하는 것이다. 이 때 범위의 끝은 제외한다. 세번째 요소를 음수로 지정하면 역순으로 출력한다. 이때 `iloc` 함수는 행을 지정하여 출력한다.

  ```python
  print(df.iloc[ 0: 2: 1])
  print(df.iloc[ : : -1])
  ```

+ 원소 선택

  원소를 선택할 때에는 `loc` 함수와 `iloc` 함수를 모두 사용할 수 있다. 

  `데이터프레임객체.loc[행 이름, 열 이름]` `데이터프레임객체.iloc[행 인덱스, 열 인덱스]` 형태로 사용할 수 있다.

  ```python
  a = df.loc['서준','음악']   # '서준' 행, '음악' 열 선택
  b = df.iloc[0,2]		   # 0번째 행, 2번째 열 선택
  ```

  특정 원소를 2개 이상 선택할 수 있다. 여러개의 행과 열을 선택하려면 리스트로 묶어서 출력하면 된다.

  ```python
  c = df.loc['서준',['음악','국어']]
  d = df.iloc[0,[1,2]]
  ```

  슬라이싱을 사용하여 출력할 수 있다. 

  ```python
  e = df.loc['서준','음악':'국어']
  f = df.iloc[0,1:2]
  ```

#### 데이터프레임에 데이터 추가

+ 열 추가

  열 추가는 인덱스 이름을 지정하고 들어갈 값을 지정해주면 된다. 행의 길이와 같은 길이를 가진 리스트를 넣어서 각각의 값을 다르게 추가해줄 수 있다. 만약 하나의 값으로 추가를 하지 않고 리스트를 사용해서 값을 추가할 경우, 행의 길이와 리스트의 길이가 다르면 에러가 발생한다.

  ```python
  df['국어'] = 80
  df['과학'] = [77,88,99]
  ```

+ 행 추가

  행 추가는 `loc` 함수를 사용해 추가한다. `dataframe.loc[행이름] = 추가할 값` 형식으로 사용한다. 리스트를 사용해 열의 길이와 리스트의 길이가 같으면 서로 다른 값을 추가해줄 수 있다.

  ```python
  df.loc['우성'] = 90
  df.loc[3]=0
  df.loc[4] = ['동규',90,80,70,60]
  ```

#### 데이터 프레임의 조작

+ 원소값 변경

  원소값 변경은 `loc` 함수와 `iloc` 함수를 사용해 변경할 수 있다.

  ```python
  # 한 개의 원소 변경
  df.iloc[0,3] = 80
  df.iloc[0][3] = 80
  df.loc['서준']['체육'] = 90
  df.loc['서준','체육'] = 100 
  
  # 여러개의 원소 변경
  df.loc['서준',['음악','체육']] = 50
  df.loc['서준',['음악','체육']] = 70 ,100
  df.loc['서준']['음악','체육'] = 70 ,100
  ```

+ 행, 열의 위치 바꾸기

  ```python
  df = df.transpose()
  ```

+ 데이터 프레임의 특정 열을 새로운 행 인덱스로 지정

  하나의 열을 새로운 행 인덱스로 지정할 수 있다. 

  두 개 이상의 열을 새로운 행 인덱스로 지정할 수 있다. 이때 두 개의 행 인덱스 중 1개만을 선택할 경우 나머지 하나의 행 인덱스와 그 행의 값들이 출력된다. 두 개의 행 인덱스를 모두 선택할 경우 행의 값들만 출력된다.

  ```python
  df.set_index('이름',inplace= True)
  df = df.set_index(['음악','수학'])
  ```

+ 행 인덱스 재배열

  행 인덱스를 `reindex` 함수를 이용하여 재배열 할 경우 인덱스 정보가 바뀌게 된다.

  ```python
  # 데이터 프레임 정의
  dict_data = {'c0' : [1,2,3], 'c1' : [4,5,6], 'c2' : [7,8,9], 'c4' : [10,11,12]}
  df = pd.DataFrame(dict_data,index=['r0','r1','r2'])
  
  # 인덱스를 재지정
  new_index = ['r0','r1','r2','r3','r4']
  ndf = df.reindex(new_index)
  ```

  인덱스 정보가 바뀌면서 `NaN`(비어있는 값)이 발생할 경우 `reindex` 함수의 `fill_value` 를 지정하여 해결할 수 있다. `fii_value = 0 ` 으로 지정하면 인덱스를 재지정하면서 발생하는 `NaN`값을 0으로 채워넣는다. 이 때 0의 데이터형식인 `int` 형식으로 모든 데이터를 처리한다. 만약 0.0으로 하게 된다면 0.0의 데이터 형식인 `float` 형식으로 모든 데이터값이 지정된다. 만약 `fill_value` 를 지정하지 않으면 디폴트 형식은 `float` 이다.

  ```python
  ndf = df.reindex(new_index,fill_value=0)
  ndf = df.reindex(new_index,fill_value=0.0)
  ```

+ 행 인덱스를 정수형으로 초기화

  ```python
  ndf = df.reset_index()
  ```

+ 데이터 프레임 정렬

  행 인덱스를 기준으로 정렬

  ``` python
  ndf = df.sort_index(ascending=False)
  ```

  특정 열을 기준으로 정렬

  ```python
  ndf = df.sort_values(by='c1',ascending=False)
  ```

#### 데이터 프레임 연산

데이터 프레임은 숫자와 데이터 프레임 간의 연산이 가능하다.

+ 데이터 프레임과 숫자 연산

  ``` python
  df + 10
  ```

+ 데이터 프레임 vs 데이터 프레임 연산

  ```python
  df1 + df2
  ```



### 데이터 입출력

#### 외부 파일 읽어오기

+ csv 파일 읽어오기

  ```python
  file_path = '파일 경로/파일이름.csv'
  df1 = pd.read_csv(file_path)
  ```

  `header = None` 이면 첫줄까지 데이터로 상정하여 읽어온다

  ```python
  df2 = pd.read_csv(file_path,header=None)
  ```

  `index_col` 을 이용해 row index를 조작할 수 있다.

  ```python
  # row index에 대한 정보를 가지고오지 않는다.
  df3 = pd.read_csv(file_path,index_col=None)
  
  # index_col = 'c0'로 설정하면 row index에 대한 정보를 c0의 정보로 대체한다.
  df4 = pd.read_csv(file_path,index_col='c0')
  ```

+ excel 파일 읽어오기

  ```python
  df1 = pd.read_excel('파일경로/파일이름.xlsx')
  df2 = pd.read_excel('파일경로/파일이름.xlsx',header= None)
  ```

+ 웹에서 파일 가져오기

  ```python
  tables = pd.read_html('url')
  ```

+ json 파일

  ```python
  df = pd.read_json('파일경로/파일이름.json')
  ```



### 데이터 살펴보기

#### 데이터 요약정보 확인하기

+ 앞부분 미리보기. n은 출력할 행의 개수를 의미한다.

  ```python
  print(df.head(n))
  ```

+ 뒤부분 미리보기.

  ```python
  print(df.tail(n))
  ```

+ 데이터 프레임의 크기

  ```python
  print(df.shape)
  ```

  결과값으로 (행, 열) 의 개수 정보가 튜플로 반환된다.

+ 데이터 프레임의 기본 정보

  데이터의 행에 대한 정보, 개수 각 열의 자료형확인. r의 str과 동일하다.

  ```python
  print(df.info())
  ```

+ 각 열의 자료형 확인

  ```python
  # 각 열의 자료형 확인. 특정 열만 선택하는 것도 가능
  print(df.dtypes)
  print(df.mpg.dtypes)
  ```

+ 데이터 프레임의 기술통계 정보 요약

  ```python
  print(df.describe())
  print(df.describe(include='all'))
  ```

  include = 'all'로 설정할 경우 NaN값이 모두 출력된다. NaN값은 유효한 기술통계 정보가 없을 경우 출력된다. 그냥 출력할 경우 NaN값이 있는 row는 출력되지 않는다.

+ 각 열의 데이터 개수 출력

  ```python
  print(df.count())
  print(type(df.count()))
  ```
