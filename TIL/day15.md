# day 15

## 네이버 주가정보 크롤링 프로젝트

[day 14](https://github.com/56unbreakable/TIL/blob/master/TIL/day14.md)에서 네이버의 주가정보를 가져오는 프로그램을 작성했다. 이 프로젝트의 목적은 주가정보를 가져오는것에 그치는게 아니라 가져온 데이터를 분석하여 미래의 주가를 예측하는 프로그램을 만드는 것이 최종 목적이다.

### 주가 정보 테이블

#### 기존의 방식

기존에 테이블에서 조금 더 효율적인 코드를 사용해 테이블에 데이터를 저장하고자 한다.

기존의 테이블은 인덱스를 주키로 설정하여 인덱스에 대해서 정렬하는 데이터 방식이다.

```sql
CREATE TABLE IF NOT EXISTS {} (idx int NOT NULL PRIMARY KEY,companyName VARCHAR(15), date VARCHAR(15), cp VARCHAR(15), ade VARCHAR(15), mp VARCHAR(15), hp VARCHAR(15), rp VARCHAR(15), tv VARCHAR(15));
```

이렇게 테이블을 설정하고 다음과 같은 함수를 사용해 데이터를 추가했다.

```python
for row in range(len(comp_data)):
    stdata = sp.getPages(comp_data[row][1],page,url,header) # 데이터 크롤링
    for p in range(page):
        for i in range(10):
            st.useQuery("INSERT INTO {} VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".
                format(table2, idx, comp_data[row][0], stdata[p][i][0], stdata[p][i][1], stdata[p][i][2], stdata[p][i][3], 					stdata[p][i][4], stdata[p][i][5], stdata[p][i][6]))
            idx += 1
```

이 방법의 문제점은 만약 새로운 데이터가 추가될 경우 데이터 안에 정렬이 제대로 이루어지지 않는다는 점이다. 인덱스를 기준으로 정렬이 되어있기 때문에 새로 추가되는 데이터는 회사명 혹은 날짜로 데이터가 정렬되지 않는다. 이러면 데이터를 한 번 더 정렬해야 데이터를 뽑기 수월하다는 단점이 있다.

#### 새로운 방식

따라서 새롭게 테이블을 재정의할 필요가 있다고 생각하였다. 우선 날짜를 `char` 형으로 받지 않고 `date` 형으로 받아낸다. 그러면 날짜끼리의 비교가 가능해져 파이썬으로 데이터를 불러와 정렬할 필요 없이 데이터베이스 내부에서 쿼리를 사용해 날짜와 관련된 정보를 불러올 수 있다.

그리고 `primary key` 를 인덱스로 지정하는 것이 아니라 회사명과 날짜 두개를 사용한다면 새롭게 추가되는 데이터가 있더라도 회사명, 날짜에 대해서 정렬된다.

재정의한 테이블은 다음과 같다.

```sql
CREATE TABLE IF NOT EXISTS {} (companyName VARCHAR(15), date DATE, cp VARCHAR(15), ade VARCHAR(15), mp VARCHAR(15), hp VARCHAR(15), rp VARCHAR(15), tv VARCHAR(15),PRIMARY KEY(companyName, date))
```

하지만 테이블을 이 방식으로 지정할 경우, 기존의 `insert` 문은 문제가 발생했다.

데이터를 저장하려는 페이지 수가 30일경우, 30페이지의 데이터를 갖고 있지 않는 주가 정보는 그 이전 페이지를 중복해서 입력하게된다. 그러면 `primary key` 두개가 모두 겹쳐 데이터가 입력되지 않는 현상이 발생하게된다.

따라서 `IGNORE` 구문을 이용하여 중복된 데이터가 입력되지 않게 조정하였다.

```python
for row in range(len(comp_data)):
    stdata = sp.getPages(comp_data[row][1],page,url,header) # 데이터 크롤링
    for p in range(page):
        for i in range(10):
            st.useQuery("INSERT IGNORE INTO {} VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".
                format(stockTable, comp_data[row][0], stdata[p][i][0], stdata[p][i][1], stdata[p][i][2], stdata[p][i][3], 					stdata[p][i][4], stdata[p][i][5], stdata[p][i][6]))
```



### 데이터 확인

데이터를 크롤링해서 데이터베이스에 저장을 하면 그걸로 끝이 아니다. 데이터베이스에 저장해놓은 데이터를 가져와서 읽을 수 있어야한다. MySQL을 이용해 데이터베이스 내부에서 확인할 수도 있지만 파이썬을 이용하여 데이터를 가져와 확인해볼 수 있다.

#### 데이터 확인 함수

`selectTableData` 함수를 사용해 모든 데이터를 불러오는 작업을 실행했었다.

또 다른 함수로 회사명, 시작날짜, 종료날짜를 인자로 받아 그 사이의 데이터를 받아오는 함수를 작성했다. 

```python
def selectDateData(self, tableName, companyName, startDate, endDate):
    data = []
    self.useQuery("SELECT * FROM {} WHERE companyName = '{}' and date >= '{}' AND date <= '{}'".
                  format(tableName,companyName,startDate,endDate))
    while (True) :
        row = self.cur.fetchone()
        if row == None :
            break
            data.append(row)
	return data
```

