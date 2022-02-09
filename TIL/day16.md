# day 16

## 네이버 주가정보 크롤링 프로젝트 3

크롤링 프로젝트의 마지막 과정으로 자동으로 매 시간이 되면 크롤러가 크롤링을 하는 파일을 생성하려고 한다. 그에 앞서 몇 가지 코드의 개선사항이 생겼다.

### 개선사항

#### 파일 구조

프로젝트의 파일 구조를 변경하였다.

`stockproject.py` : 크롤링 함수를 만들어놓은 모듈

`dbcrawler.py` : 최초 1회 대량의 데이터를 크롤링 하는 파일

`dbupdater.py` : 일정 시간마다 자동으로 데이터를 크롤링 하는 파일

#### stockproject.py

기존의 `getPageData` `getPage` 함수를 클래스 `DBmanagement` 의 함수로 이동하였다.

데이터를 데이터베이스에 입력하는 `insertStockData` 함수를 생성하였다. 이 함수는 주가정보를 데이터베이스에 입력한다.

```python
def insertStockData(self,data,page,url,header,table):
    for row in range(len(data)):
        companyCode = self.codeTune(data[row][1])
        stdata = self.getPages(companyCode,page,url,header) # 데이터 크롤링
        for p in range(page):
            for i in range(10):
                self.useQuery("INSERT IGNORE INTO {} VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".
                              format(table, data[row][0], stdata[p][i][0], stdata[p][i][1], stdata[p][i][2], stdata[p][i][3], 								stdata[p][i][4], stdata[p][i][5], stdata[p][i][6]))
```

#### dbcrawler.py

데이터베이스를 여러번 열고 닫는 문제점을 해결하였다. `openDB` , `closeDB` 함수를 맨 처음 시작과 맨 마지막 끝에만 배치하였다.

데이터베이스에 주가정보를 입력하는 코드를 `isertStockData` 함수로 대체하였다.

#### dbupdater.py

매일 17시마다 1페이지의 주가정보를 크롤링하는 파일이다.



### 최종 구조

#### stockproject.py

+ `class DBmanagement`
  + `init(db,pw)` : 데이터베이스 생성
  + `openDB` : 데이터베이스 연결
  + `closeDB` : 데이터베이스 연결 종료
  + `useQuery` : 쿼리문 사용
  + `selectTableData` : 테이블 전체 정보 불러오기
    + `useQuery`
  + `selectDateData` : 시작날짜와 끝날짜 사이의 데이터 불러오기
    + `useQuery`
  + `codeTune` : 기업 코드를 6자리로 튜닝
  + `getPages` : 여러 페이지의 데이터를 가져옴
    + `getPageData`
  + `getPageData` : 한 페이지 안의 주가정보를 긁어옴
  + `insertStockData` : 데이터베이스에 긁어온 주가정보를 입력함.
    + `getPages`
      + `getPageData`

```python
import requests
import bs4
import pymysql

# 클래스 선언
class DBmanagement :
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

    # 주가 코드가 6자리가 아닐경우 6자리로 만들기 위한 코드.
    def codeTune(self,data):
        if len(data) == 3:
            code = '000' + data
        elif len(data) == 4:
            code = '00' + data
        elif len(data) == 5:
            code = '0' + data
        else :
            code = data
        return code

    # 페이지별로 데이터를 크롤링하는 함수 page는 몇 페이지까지 데이터를 받아올 것인가.
    def getPages(self,data,page,url,header):
        pagedata = []
        for i in range(page):
            pagedata.append(self.getPageData(data,i+1,url,header))
        return pagedata

    # 특정 페이지의 주식정보를 크롤링하는 함수. data는 코드를 의미, page는 현재 페이지를 의미
    def getPageData(self,data,page,url,header):
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

        # 데이터 입력
    def insertStockData(self,data,page,url,header,table):
        for row in range(len(data)):
            companyCode = self.codeTune(data[row][1])
            stdata = self.getPages(companyCode,page,url,header) # 데이터 크롤링
            for p in range(page):
                for i in range(10):
                    self.useQuery("INSERT IGNORE INTO {} VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".
                        format(table, data[row][0], stdata[p][i][0], stdata[p][i][1], stdata[p][i][2], stdata[p][i][3], 							stdata[p][i][4], stdata[p][i][5], stdata[p][i][6]))
```

#### dbcrawler.py

+ 데이터베이스 정보 입력
+ 데이터를 가져오기 위한 정보 입력
+ 클래스 생성
+ db 연결
+ 테이블 생성
+ 상장사 데이터 긁어오기
+ 주가 데이터 긁어오기

```python
import stockproject as sp
import pandas as pd

# 사용할 데이터베이스 정보. pw는 각자 데이터베이스에 맞는 pw 사용
db = 'INVESTAR'
pw = '1111'
companyTable = 'company_info'
stockTable = 'daily_price'

# 데이터를 가져오기 위한 정보. header는 각자 컴퓨터에 맞는 header 사용
header = {'User-Agent':''}
url = "https://finance.naver.com/item/sise_day.nhn?code={}&page={}"
page = 30

# 클래스 선언과 동시에 db생성
st = sp.DBmanagement(db,pw)

# DB 연결
st.openDB()

# 상장사 데이터를 넣을 테이블 만들기
st.useQuery('CREATE TABLE IF NOT EXISTS {} (cname char(15), ccode char(6))'.format(companyTable))

# 주가 데이터를 넣을 테이블 만들기
query = "CREATE TABLE IF NOT EXISTS {} (companyName VARCHAR(15), date DATE, cp VARCHAR(15), ade VARCHAR(15), mp VARCHAR(15), hp VARCHAR(15), rp VARCHAR(15), tv VARCHAR(15),PRIMARY KEY(companyName, date));"
st.useQuery(query.format(stockTable))

# 테이블에 상장사 데이터 넣기
url3 = "http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13"
tables = pd.read_html(url3)
comp_data = tables[0][['회사명','종목코드']]
for i in range(len(comp_data)):
    st.useQuery("INSERT INTO {} VALUES('{}','{}')".format(companyTable, comp_data.iloc[i][0], comp_data.iloc[i][1]))

# 상장사 데이터 불러오기
comp_data = st.selectTableData(companyTable)

# 상장사 데이터를 이용해 주가정보 가져오기
st.insertStockData(comp_data,page,url,header,stockTable)

# DB 연결 종료
st.closeDB()
```

#### dbupdater.py

+ 데이터베이스 정보 입력
+ 데이터를 가져오기 위한 정보 입력
+ 클래스 생성
+ db 연결
+ 상장사 데이터 불러오기
+ 매 17시마다 크롤링
  + `schedule` 패키지를 사용하면 원하는 시간에 크롤러 함수를 실행할 수 있다.

```python
import stockproject as sp
import schedule

# 사용할 데이터베이스 정보. pw는 각자 데이터베이스에 맞는 pw 사용
db = 'INVESTAR'
pw = '1111'
companyTable = 'company_info'
stockTable = 'daily_price'

# 데이터를 가져오기 위한 정보. header는 각자 컴퓨터에 맞는 header 사용
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Whale/3.12.129.46 Safari/537.36'}
url = "https://finance.naver.com/item/sise_day.nhn?code={}&page={}"
page = 1

# 클래스 선언과 동시에 db생성
st = sp.DBmanagement(db,pw)

st.openDB()
comp_data = st.selectTableData(companyTable)
st.closeDB()

st.openDB()
schedule.every().day.at("17:00").do(st.insertStockData,comp_data,page,url,header,stockTable)
st.closeDB()

# 계속해서 파일을 실행시키는 함수.
"""
while True
	pass
"""
```

