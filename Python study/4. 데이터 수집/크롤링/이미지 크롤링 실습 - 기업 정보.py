import requests
import bs4

url = 'http://www.cgs.or.kr/business/esg_tab04.jsp?pg=1&pp=10&skey=&svalue=&sfyear=2020&styear=2020&sgtype=TOTAL&sgrade=A%EF%BC%8B#ui_contents'

res = requests.get(url)
res.raise_for_status()

bs_obj = bs4.BeautifulSoup(res.text,"html.parser")

tbody = bs_obj.find("tbody")
tr = tbody.findAll("tr")

data = [[] for i in range(len(tr))]

for i in range(len(tr)):
    td = tr[i].findAll("td")
    for s in range(len(td)):
        data[i].append(td[s].text.strip())

for i in range(len(data)):
    print(data[i])
    