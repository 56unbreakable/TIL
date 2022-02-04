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
    def selectTableData(self,tablename):
        data = []
        self.useQuery("SELECT * FROM {}".format(tablename))
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

# 페이지별로 데이터를 가져오는 함수 page는 몇 페이지까지 데이터를 받아올 것인가.
def getPages(data,page,url,header):
    pagedata = []
    for i in range(page):
        pagedata.append(getPageData(data,i+1,url,header))
    return pagedata

# 특정 페이지의 주식정보를 가져오는 함수. data는 코드를 의미, page는 현재 페이지를 의미
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
