from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

url = 'https://flight.naver.com/'
driver = webdriver.Chrome("C:/sh/study/Study Everyday/chromedriver.exe")

try:
    driver.get(url)
    time.sleep(1)
    # 출발지 선택
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]').click()
    driver.find_element_by_class_name('autocomplete_input__1vVkF').send_keys("인천")
    time.sleep(2)
    driver.find_element_by_class_name('autocomplete_search_item__2WRSw').click()
    time.sleep(2)
    
    # 도착지 선택
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
    driver.find_element_by_class_name('autocomplete_input__1vVkF').send_keys("파리")
    time.sleep(2)
    driver.find_element_by_class_name('autocomplete_search_item__2WRSw').click()
    time.sleep(2)

    # 가는날 선택
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[7]/button').click()
    time.sleep(2)
    
    # 오는날 선택
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[5]/button').click()
    time.sleep(2)

    # 항공권 검색
    driver.find_element_by_class_name('searchBox_search__2KFn3').click()
    time.sleep(20)
    

    # 최저가 검색

except Exception as e:
    print(e)

while True:
    pass

"""     driver.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]").click()
    driver.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/button[1]").click()
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/div/button[2]').click()
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
 """