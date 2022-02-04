from pickletools import StackObject
import stockproject as sp
import pandas as pd



# 사용할 데이터베이스 정보.
db = 'INVESTAR'
pw = '1111'
table = 'company_info'
table2 = 'daily_price'

# 클래스 선언.
st = sp.SQLmanagement(db,pw)

# 테이블 생성
""" st.openDB()
st.useQuery('CREATE TABLE IF NOT EXISTS {} (cname char(15), ccode char(6))'.format(table)) """

# 데이터를 넣을 테이블 만들기
st.openDB()
query = "CREATE TABLE IF NOT EXISTS {} (idx int NOT NULL PRIMARY KEY,companyName CHAR(15), date char(12), cp char(7), ade CHAR(7), mp CHAR(7), hp CHAR(7), rp char(7), tv char(8));"
st.useQuery(query.format(table2))
st.closeDB()


# 테이블에 데이터 넣기
""" url = "http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13"
tables = pd.read_html(url)
data = tables[0][['회사명','종목코드']]
for i in range(len(data)):
    st.useQuery("INSERT INTO {} VALUES('{}','{}')".format(table, data.iloc[i][0], data.iloc[i][1]))
st.closeDB() """

# 데이터 읽기
st.openDB()
data = st.selectTableData(table)
st.closeDB()

# 코드 바꾸기
data = sp.codeTune(data)

# 데이터를 가져오기 위한 정보
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Whale/3.12.129.46 Safari/537.36'}
url = "https://finance.naver.com/item/sise_day.nhn?code={}&page={}"
page = 1

# 데이터 가져오고 넣기.
idx = 0
st.openDB()
for row in range(len(data)):
    stdata = sp.getPages(data[row][1],page,url,header)
    for i in range(10):
        st.useQuery("INSERT INTO {} VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
            table2, idx, data[row][0], stdata[row][i][0], stdata[row][i][1], stdata[row][i][2], stdata[row][i][3], stdata[row][i][4], stdata[row][i][5], stdata[row][i][6]))
        idx += 1
st.closeDB()

""" st.openDB()
stdata = sp.getPages(data[0][1],page,url,header)
for i in range(10):
    st.useQuery("INSERT INTO {} VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(
        table2, idx, data[0][0], stdata[0][i][0], stdata[0][i][1], stdata[0][i][2], stdata[0][i][3], stdata[0][i][4], stdata[0][i][5], stdata[0][i][6]))
    idx += 1
st.closeDB() """


""" 
stdata = sp.getPages(data[0][1],page,url,header)
for i in range(10):
    print(stdata[0][i][6])
 """
