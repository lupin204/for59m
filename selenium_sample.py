from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from bs4 import BeautifulSoup

# 크롬드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip


#브라우저 꺼짐 방지
chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)

#불필요한 에러 메시지 없애기 
#chrome_options.add_experimental_option("excludeSwitched", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동 
driver.implicitly_wait(5) # 웹 페이지가 로딩될때까지 5초 기다림
driver.maximize_window() # 브라우저 최대화
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")


#page_source = driver.page_source
#soup = BeautifulSoup(page_source, 'html.parser')
#elements = soup.select('your-selector')

div_type = driver.find_elements(By.CSS_SELECTOR, ".box_type_l")[0]
div_grid = driver.find_elements(By.CSS_SELECTOR, ".box_type_l")[1]


stock_list = div_grid.find_elements(By.CSS_SELECTOR, "table > tbody > tr")
for stock in stock_list:
    item_list = stock.find_elements(By.CSS_SELECTOR, "td")
    
    item_link = item_list[0].find_element(By.CSS_SELECTOR, "a").get_attribute("href")
    #print(item_link)
    item_no = item_link.split("=")[1]
    item_name = item_list[0].find_element(By.CSS_SELECTOR, "a").text
    현재가 = item_list[2].text.replace(',', '')
    
    if 'red02' in item_list[3].find_element('span').get_attribute('class').split():
        # 상승
        전일비 = item_list[3].find_element('span').text
    else:
        # 하락
        전일비 = "-" + item_list[3].find_element('span').text
    #if 'nv01' in item_list[3].find_element('span').get_attribute('class').split():

    


# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
#id.send_keys("lupin204")
pyperclip.copy('lupin204')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
#pw.send_keys("")
pyperclip.copy('password')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, "#log\.login")
login_btn.click()






