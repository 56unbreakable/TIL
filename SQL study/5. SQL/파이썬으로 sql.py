import pymysql
import csv

conn, cur = None,None
sql = ""
conn = pymysql.connect(host='localhost',user = 'root', password='1111',db='mulcam',charset='utf8')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS userTable (name char(4), sex char(1), class char(1), attend char(1))")

f = open('C:/sh/study/Study Everyday/data files/data.csv')
data = csv.reader(f)
next(data)
for row in data:
    cur.execute("INSERT INTO userTable VALUES('{}','{}','{}','{}')".format(row[0],row[1],row[2],row[3]))

cur.execute("SELECT * FROM userTable")
while (True) :
    row = cur.fetchone()
    if row == None :
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%s   %s   %s   %s" % (data1, data2, data3, data4))

conn.commit()
conn.close()
