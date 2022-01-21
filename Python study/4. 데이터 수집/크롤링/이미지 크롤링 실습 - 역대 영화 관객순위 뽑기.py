import requests
from urllib.request import URLError
from urllib.request import urlopen
from urllib.request import HTTPError
import bs4
from sympy import source

for i in range(5):
    year = 2021 - i 
    url = 'https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'.format(year)
    res = requests.get(url)
    res.raise_for_status()

    bs_obj = bs4.BeautifulSoup(res.text,"html.parser")
    imgs = bs_obj.find_all("img", {"class" : "thumb_img"})

    for idx, imgs in enumerate(imgs):
        img_url = imgs["src"]
        if img_url.startswith("//"):
            img_url = "https:" + img_url
    
        img_res = requests.get(img_url)
        img_res.raise_for_status()

        with open("C:/sh/study/Study Everyday/Python study/4. 데이터 수집/이미지크롤링실습 이미지폴더/movie{} {}.jpg".format(year,idx+1),"wb") as f:
            f.write(img_res.content)

        if idx >=4:
            break 

