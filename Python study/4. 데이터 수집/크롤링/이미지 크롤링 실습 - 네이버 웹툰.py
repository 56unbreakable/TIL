import requests
import bs4

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,"html.parser")

""" # <title>의 텍스트만 불러오기
print(soup.title.text)

# 처음으로 나오는 <a> 불러오그
print(soup.a)

# <a> 태그에서 사용하는 속성값 불러오기
print(soup.a.attrs)
 """

""" r1 = soup.find("li",{"class":"rank01"})
print(r1.a.text)
r2 = r1.next_sibling.next_sibling
print(r2.a.text)
r3 = r2.next_sibling.next_sibling
print(r3.a.text)

print(r1.parent) """

r1 = soup.find("li",{"class":"rank01"})
print(r1.a.get_text())
r2 = r1.find_next_sibling("li")
print(r2.a.get_text())