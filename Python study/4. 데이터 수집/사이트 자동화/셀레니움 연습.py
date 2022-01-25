from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
import time


# 인기영화 검색
""" url = "https://www.daum.net"
driver = webdriver.Chrome("C:/sh/study/Study Everyday/chromedriver.exe")

driver.get(url)

element = driver.find_element_by_id("q")
element.send_keys("인기영화")
# element.send_keys(Keys.ENTER)
# 클릭으로 해결.
element = driver.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
element.click() """


# 로그인화면창 클릭하기
"""url = "https://www.daum.net"
driver = webdriver.Chrome("C:/sh/study/Study Everyday/chromedriver.exe")

driver.get(url)

element = driver.find_element_by_class_name("link_login")
element.click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.back()
time.sleep(2) """


#자동 로그인
""" url = 'https://www.naver.com'
driver = webdriver.Chrome("C:/sh/study/Study Everyday/chromedriver.exe")

try:
    driver.get(url)
    # 로그인 버튼 클릭
    element = driver.find_element_by_class_name("link_login")
    element.click()
    # 로그인 하기
    driver.find_element_by_id("id").send_keys("아이디")
    driver.find_element_by_id("pw").send_keys("비밀번호")
    driver.find_element_by_id("log.login").click()
except Exception as e:
    print(e) """


# 자동로그인 우회
url = 'https://www.naver.com'
driver = webdriver.Chrome("C:/sh/study/Study Everyday/chromedriver.exe")

try:
    driver.get(url)
    element = element = driver.find_element_by_class_name("link_login")
    element.click()

    pyperclip.copy("tmdghks3044")
    driver.find_element_by_id("id").send_keys(Keys.CONTROL,"v")
    pyperclip.copy("zero3847")
    driver.find_element_by_id("pw").send_keys(Keys.CONTROL,"v")
    driver.find_element_by_id("log.login").click()

except Exception as e:
    print(e)
finally:
    print("success")


# 브라우저가 꺼지는걸 원하지 않으면 실행
while True:
    pass
