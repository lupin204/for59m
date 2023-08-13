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



driver.get(f"https://finance.naver.com/sise/theme.naver")


dom_theme_list_page = driver.find_elements(By.CSS_SELECTOR, 'table.Nnavi td')
# theme_list_page_cnt = len(dom_theme_list_page) - 1

theme_list = []

for page in dom_theme_list_page[:-1]:
    driver.implicitly_wait(2) # 웹 페이지가 로딩될때까지 5초 기다림
    driver.get(f"https://finance.naver.com/sise/theme.naver?&page={page}")
    
    dom_theme_a_tags = driver.find_elements(By.XPATH, "//table[1]//td[@class='col_type1']//a[@href]")
    
    for a_tag in dom_theme_a_tags:
        theme_list.append({'title': a_tag.text, 'url': a_tag.get_attribute("href")})
        

for theme in theme_list:
    driver.implicitly_wait(2)
    driver.get(theme['url'])
    dom_stock_a_tags = driver.find_elements(By.XPATH, "//table[@class='type_5']//div[@class='name_area']//a[@href]")
    
    # https://finance.naver.com/item/main.naver?code=900260
    for aa in aa_tags:
        code_arr.append
    code_arr = [aa.get_attribute("href") for aa in aa_tags]
    name_arr = [aa.text for aa in aa_tags]

    for na in code_arr:
        print(na)




driver.quit()

