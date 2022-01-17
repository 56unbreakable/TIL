# day 4

## pandas

### 1. 시리즈

시리즈는 인덱스와 데이터 값으로 이루어져 있는 pandas 데이터 형식이다.

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

  
