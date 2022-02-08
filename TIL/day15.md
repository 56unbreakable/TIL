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



### 최종 코드

#### 모듈 : stockproject.py

```python
from dataclasses import replace
import requests
import bs4
import pymysql

################
#클래스 부분
################

# 클래스 선언
class SQLmanagement :
    # 클래스 선언시 데이터베이스 이름과 패스워드가 필요하며, 데이터베이스가 없을 시 생성한다.
    def __init__(self,dbname,passwords):
        self.password = passwords
        self.dbname = dbname
        conn, cur = None,None
        conn = pymysql.connect(host='localhost',user = 'root', password=self.password ,charset='utf8')
        cur = conn.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS {}".format(self.dbname))
        conn.commit()
        conn.close()

    # 데이터베이스와 연결하는 함수. useQuery(), dataLoad() 함수를 쓰기전 사용해야함.
    def openDB(self):
        self.conn = None
        self.cur = None
        self.conn = pymysql.connect(host='localhost',user = 'root', password=self.password ,db = self.dbname,charset='utf8')
        self.cur = self.conn.cursor()

    # opneDB()를 사용하고 난 이후에 꼭 사용해야함. DB를 닫아줘야 에러가 나지 않음.
    def closeDB(self):
        self.conn.commit()
        self.conn.close()

    # 함수 안에 쿼리문을 작성하면 실행시켜주는 함수.
    def useQuery(self,queries):
        self.query = queries
        self.cur.execute(self.query)

    # 테이블 안에 모든 데이터를 불러오는 함수. 리스트를 반환한다.
    def selectTableData(self,tableName):
        data = []
        self.useQuery("SELECT * FROM {}".format(tableName))
        while (True) :
            row = self.cur.fetchone()
            if row == None :
                break
            data.append(row)
        return data

    # 주가 정보가 들어있는 테이블에서 회사이름, 시작날짜, 종료날짜를 설정하면 해당 기간의 주가정보를 보여주는 함수
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


################
#함수 부분
################

# 주가 코드가 6자리가 아닐경우 6자리로 만들기 위한 코드.
def codeTune(data):
    stockdata = []
    for i in range(len(data)):
        if len(data[i][1]) == 3:
            code = '000' + data[i][1]
        elif len(data[i][1]) == 4:
            code = '00' + data[i][1]
        elif len(data[i][1]) == 5:
            code = '0' + data[i][1]
        else :
            code = data[i][1]
        stockdata.append([data[i][0],code])
    return stockdata

# 페이지별로 데이터를 크롤링하는 함수 page는 몇 페이지까지 데이터를 받아올 것인가.
def getPages(data,page,url,header):
    pagedata = []
    for i in range(page):
        pagedata.append(getPageData(data,i+1,url,header))
    return pagedata

# 특정 페이지의 주식정보를 크롤링하는 함수. data는 코드를 의미, page는 현재 페이지를 의미
def getPageData(data,page,url,header):
    url2 = url.format(data,page)
    res = requests.get(url2,headers=header)
    res.raise_for_status() 

    # 객체 생성
    bs = bs4.BeautifulSoup(res.text,"html.parser")

    # 주가정보 긁어오기
    table = bs.find("table",{"class":"type2"})
    tr = table.findAll("tr",{"onmouseover":"mouseOver(this)"})

    # tr의 길이만큼의 이중 지능리스트 생성
    data = [ [] for i in range(len(tr))]

    # 모든 텍스트 정보 가져오기
    for i in range(len(tr)):
        td = tr[i].findAll("td")
        for s in range(len(td)):
            data[i].append(td[s].text.strip())
    return data
```

#### 크롤링 : 주가정보크롤링.py

```python
import stockproject as sp
import pandas as pd


#########################################################################
# 데이터를 크롤링하는 파일. 데이터베이스에 데이터를 최초로 넣을 때만 실행 #
#########################################################################


# 사용할 데이터베이스 정보. pw는 각자 데이터베이스에 맞는 pw 사용
db = 'INVESTAR'
pw = '1111'
companyTable = 'company_info'
stockTable = 'daily_price'

# 데이터를 가져오기 위한 정보. header는 각자 컴퓨터에 맞는 header 사용
header = {'User-Agent':'user agent 정보'}
url = "https://finance.naver.com/item/sise_day.nhn?code={}&page={}"
page = 30

# 클래스 선언과 동시에 db생성
st = sp.SQLmanagement(db,pw)

# 상장사 데이터를 넣을 테이블 만들기
st.openDB()
st.useQuery('CREATE TABLE IF NOT EXISTS {} (cname char(15), ccode char(6))'.format(companyTable))
st.closeDB()

# 주가 데이터를 넣을 테이블 만들기
st.openDB()
query = "CREATE TABLE IF NOT EXISTS {} (companyName VARCHAR(15), date DATE, cp VARCHAR(15), ade VARCHAR(15), mp VARCHAR(15), hp VARCHAR(15), rp VARCHAR(15), tv VARCHAR(15),PRIMARY KEY(companyName, date));"
st.useQuery(query.format(stockTable))
st.closeDB()

# 테이블에 상장사 데이터 넣기
st.openDB()
url3 = "http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13"
tables = pd.read_html(url3)
comp_data = tables[0][['회사명','종목코드']]
for i in range(len(comp_data)):
    st.useQuery("INSERT INTO {} VALUES('{}','{}')".format(companyTable, comp_data.iloc[i][0], comp_data.iloc[i][1]))
st.closeDB()

# 상장사 데이터 불러오기
st.openDB()
comp_data = st.selectTableData(companyTable)
st.closeDB()

# 데이터 튜닝
comp_data = sp.codeTune(comp_data)

# 상장사 데이터를 이용해 주가정보 가져오기
st.openDB()
for row in range(len(comp_data)):
    stdata = sp.getPages(comp_data[row][1],page,url,header) # 데이터 크롤링
    for p in range(page):
        for i in range(10):
            st.useQuery("INSERT IGNORE INTO {} VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".
                format(stockTable, comp_data[row][0], stdata[p][i][0], stdata[p][i][1], stdata[p][i][2], stdata[p][i][3], stdata[p][i][4], stdata[p][i][5], stdata[p][i][6]))
st.closeDB()
```

#### 데이터 확인

```python
from pymysql import DataError
from sklearn.exceptions import DataDimensionalityWarning
import stockproject as sp

# 사용할 데이터베이스 정보. pw는 각자 데이터베이스에 맞는 pw 사용
db = 'INVESTAR'
pw = '1111'
companyTable = 'company_info'
stockTable = 'daily_price2'

# 데이터를 가져오기 위한 정보. header는 각자 컴퓨터에 맞는 header 사용
header = {'User-Agent':'user agent 정보'}
url = "https://finance.naver.com/item/sise_day.nhn?code={}&page={}"

# 클래스 선언과 동시에 db생성
st = sp.SQLmanagement(db,pw)

# 원하는 회사의 원하는 날짜 데이터 뽑기
st.openDB()
datedata = st.selectDateData(stockTable,"DL","2022-01-14","2022-02-03")
st.closeDB() 

for i in range(len(datedata)):
    print(datedata[i])
```

