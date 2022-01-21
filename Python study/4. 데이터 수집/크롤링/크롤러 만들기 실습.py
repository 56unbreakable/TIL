import requests
from urllib.request import URLError
from urllib.request import urlopen
from urllib.request import HTTPError
import bs4


""" # request 패키지를 이용한 페이지 연결 및 다운로드
res = requests.get("https://www.naver.com")

res.raise_for_status()
print("정상입니다.")
print(len(res.text))
print(res.text) """

""" # urlopen 패키지를 이용한 페이지 연결
try :
    html = urlopen("https://www.dddsdf.com/kim.html")
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found.")
else :
    print("성공") """


# bs4 패키지를 이용한 html 문서 출력
html_str = '''
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
'''
bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
ul = bs_obj.find("ul")
li = ul.find('li')
lis = ul.findAll("li")
print(li.text)
print(lis)
print(ul.text)
print(lis[1].text)


""" # 클래스 속성을 이용해 데이터 뽑기
html_str = '''
<html>
    <body>
        <ul class = "greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        <ul class = "reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
'''
bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
ul = bs_obj.find("ul", {"class" : "reply"})
print(ul) """


""" # 속성값 뽑아내기
html_str = '''
<html>
    <body>
        <ul class = "ko">
            <li>
                <a href="https://www.naver.com">naver</a>
            </li>
            <li>
                <a href="https://www.google.com">google</a>
            </li>
        </ul>
        <ul class = "sns">
            <li>
                <a href="https://facebook.com">facebook</a>
            </li>
        </ul>
    </body>
</html>
'''
bs_obj = bs4.BeautifulSoup(html_str,"html.parser")
atag = bs_obj.find("a")
print(atag["href"]) """
