import FinanceDataReader as fdr
import firebase_admin
from firebase_admin import credentials, firestore
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager



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
service = Service(ChromeDriverManager().install())
# service = Service("D:/myprjs/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)


#브라우저 꺼짐 방지
# chrome_options.add_experimental_option("detach", True)

#불필요한 에러 메시지 없애기 
options.add_experimental_option("excludeSwitched", ["enable-logging"])



# 웹페이지 해당 주소 이동 
driver.implicitly_wait(2) # 웹 페이지가 로딩될때까지 5초 기다림
driver.maximize_window() # 브라우저 최대화





# 다운로드한 키 파일의 경로
cred = credentials.Certificate('d:/myprjs/for59m/doc/for84m2-firebase-adminsdk-j8u7b-74f6e68204.json')

# Firebase 프로젝트 초기화
firebase_admin.initialize_app(cred)

# Realtime Database의 레퍼런스 생성
db = firestore.client()
theme_arr = collection_ref = db.collection('themes').document('theme_idx').get('data')

for idx in theme_arr:
    
    # https://stockplus.com/m/investing_strategies/topics/771
    driver.get(f"https://stockplus.com/m/investing_strategies/topics/{idx}")

    driver.implicitly_wait(3) # 웹 페이지가 로딩될때까지 5초 기다림
        
    # 토픽 맥신(MXene)
    text_content = driver.find_element(By.CSS_SELECTOR, 'main div.topicTop h3 a').text
    text_topic = text_content.strip()
    
    
    if (text_topic == '토픽'):
        print(f"[{idx}]")
    else:
        theme_arr.append(idx)
        theme_list.append({'no': idx, 'title': text_topic[3:]})
        print(f"[{idx}]{text_topic[3:]}")
    
    
    # Scroll down to the end of the page
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


print(theme_arr)




# Realtime Database의 레퍼런스 생성
db = firestore.client()
collection_ref = db.collection('themes').document('theme_idx').get({"data": theme_arr})
collection_ref = db.collection('themes').document('theme_list').set({"data": theme_list})