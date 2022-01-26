from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://flight.naver.com/'
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get(url)
    time.sleep(1)
    # 출발지 선택
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]').click()
    driver.find_element_by_class_name('autocomplete_input__1vVkF').send_keys("인천")
    time.sleep(1)
    driver.find_element_by_class_name('autocomplete_search_item__2WRSw').click()
    
    # 도착지 선택
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
    driver.find_element_by_class_name('autocomplete_input__1vVkF').send_keys("파리")
    time.sleep(1)
    driver.find_element_by_class_name('autocomplete_search_item__2WRSw').click()

    # 가는날 선택
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[7]/button').click()
    time.sleep(2)
    
    # 오는날 선택
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[5]/button').click()

    # 항공권 검색
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()


    WebDriverWait(driver, 50).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR , '#__next > div > div.container > div.List_content > div > div.concurrent_ConcurrentList__1EKaB > div:nth-child(1) > div')))
    # WebDriverWait(driver, 50).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'#__next > div > div.container > div.List_top > div > div.inlineFilter_FilterWrapper__1Icm4 > div')))
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 최저가 검색
    airplane = driver.find_element_by_css_selector("#__next > div > div.container > div.List_content > div > div.concurrent_ConcurrentList__1EKaB > div:nth-child(1) > div")
    #airplane = driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div[3]/div[1]')
    # selector로 선택한건 selector로 저장해야함. 즉, webdriverwait를 selector로 했으면 find도 selector로
except Exception as e:
    print(e)

finally :
    print(airplane.text)

""" while True:
    pass """

