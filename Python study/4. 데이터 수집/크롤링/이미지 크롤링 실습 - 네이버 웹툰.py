import requests
import bs4

url = "https://comic.naver.com/webtoon/list?titleId=786537"

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,"html.parser")

rate = soup.findAll("div",{"class":"rating_type"})

star=[]
for row in rate:
    star.append(row.strong.text)

print(star)
print(soup)