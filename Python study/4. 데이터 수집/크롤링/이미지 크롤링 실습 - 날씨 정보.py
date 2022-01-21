import requests
import bs4

url = 'http://www.cgs.or.kr/business/esg_tab04.jsp?pg=1&pp=10&skey=&svalue=&sfyear=2020&styear=2020&sgtype=TOTAL&sgrade=A%EF%BC%8B#ui_contents'

res = requests.get(url)
res.raise_for_status()

bs_obj = bs4.BeautifulSoup(res.text,"html.parser")

table = bs_obj.find("table")
headline = table.find("thead")
print(headline.text)