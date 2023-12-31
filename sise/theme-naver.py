from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
options.add_argument('ignore-certificate-errors')
options.add_argument('user-agent=' + user_agent)
options.add_argument("lang=ko_KR")
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("--no-sandbox")

# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

# 드라이버 위치 경로 입력
# service = Service(ChromeDriverManager().install())
service = Service("D:/myprjs/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)


#브라우저 꺼짐 방지
# chrome_options.add_experimental_option("detach", True)

#불필요한 에러 메시지 없애기 
options.add_experimental_option("excludeSwitched", ["enable-logging"])



# 웹페이지 해당 주소 이동 
driver.implicitly_wait(2) # 웹 페이지가 로딩될때까지 5초 기다림
driver.maximize_window() # 브라우저 최대화

list = {"537"}

driver.get(f"https://finance.naver.com/sise/sise_group_detail.naver?type=theme&no=537")


div_type = driver.find_elements(By.CSS_SELECTOR, ".box_type_l")[0]
div_grid = driver.find_elements(By.CSS_SELECTOR, ".box_type_l")[1]


stock_list = div_grid.find_elements(By.CSS_SELECTOR, "table > tbody > tr")
for stock in stock_list[:-2]:
    # print(stock.text)
    item_list = stock.find_elements(By.CSS_SELECTOR, "td")
    
    item_link = item_list[0].find_element(By.CSS_SELECTOR, "a").get_attribute("href")
    print(item_link)
    item_no = item_link.split("=")[1]
    item_name = item_list[0].find_element(By.CSS_SELECTOR, "a").text
    현재가 = item_list[2].text.replace(',', '')
    print(현재가)
    # if 'red02' in item_list[3].find_element('span').get_attribute('class').split():
        # 상승
        # 전일비 = item_list[3].find_element('span').text
    # else:
        # 하락
        # 전일비 = "-" + item_list[3].find_element('span').text
    #if 'nv01' in item_list[3].find_element('span').get_attribute('class').split():



driver.quit()

