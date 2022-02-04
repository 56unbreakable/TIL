import stockproject as sp
import pandas as pd

# 사용할 데이터베이스 정보.
db = 'INVESTAR'
pw = '1111'
table = 'company_info'
table2 = 'daily_price'

# 클래스 선언과 동시에 db생성
st = sp.SQLmanagement(db,pw)

# 상장사 데이터를 넣을 테이블 만들기
st.openDB()
st.useQuery('CREATE TABLE IF NOT EXISTS {} (cname char(15), ccode char(6))'.format(table))
st.closeDB()

# 주가 데이터를 넣을 테이블 만들기
st.openDB()
query = "CREATE TABLE IF NOT EXISTS {} (idx int NOT NULL PRIMARY KEY,companyName VARCHAR(15), date VARCHAR(15), cp VARCHAR(15), ade VARCHAR(15), mp VARCHAR(15), hp VARCHAR(15), rp VARCHAR(15), tv VARCHAR(15));"
st.useQuery(query.format(table2))
st.closeDB()


# 테이블에 데이터 넣기
st.openDB()
url = "http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13"
tables = pd.read_html(url)
comp_data = tables[0][['회사명','종목코드']]
for i in range(len(comp_data)):
    st.useQuery("INSERT INTO {} VALUES('{}','{}')".format(table, comp_data.iloc[i][0], comp_data.iloc[i][1]))
st.closeDB()

# 데이터 크롤링해서 저장
# 데이터 읽기
st.openDB()
comp_data = st.selectTableData(table)
st.closeDB()

# 코드 바꾸기
comp_data = sp.codeTune(comp_data)

# 데이터를 가져오기 위한 정보
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Whale/3.12.129.46 Safari/537.36'}
url = "https://finance.naver.com/item/sise_day.nhn?code={}&page={}"
page = 3

# 데이터 가져오고 넣기.
st.openDB()
idx = 0
for row in range(len(comp_data)):
    stdata = sp.getPages(comp_data[row][1],page,url,header) # 데이터 크롤링
    for p in range(page):
        for i in range(10):
            st.useQuery("INSERT INTO {} VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".
                format(table2, idx, comp_data[row][0], stdata[p][i][0], stdata[p][i][1], stdata[p][i][2], stdata[p][i][3], stdata[p][i][4], stdata[p][i][5], stdata[p][i][6]))
            idx += 1
st.closeDB()
