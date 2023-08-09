import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt


url = 'https://finance.naver.com/item/sise_day.nhn?code=029780&page=1'
html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text




# BeautifulSoup 생성자 첫번째 인수로 HTML/XML 페이지를 넘겨주고, 두번째 인수로 페이지를 파싱할 방식을 넘겨준다.
bs = BeautifulSoup(html, 'lxml')

# find 함수를 통해 'pgRR'인 'td'태그를 찾으면, 결과값은 'bs4.element.Tag'타입으로 pgrr 변수에 반환한다.
# pgRR = Page Right Right 맨 마지막 페이지를 의미한다.
pgrr = bs.find('td', class_='pgRR')


# 삼성카드 전체 페이지 수를 구하려면 pdRR 클래스 속성값으로 <td>하위의 <a> href 속성값을 구한다.
# pfgg.a['href']를 출력하면 href의 속성값인 item/sise.naver?code=029780&page=1 문자열을 얻을 수 있다.
s = str(pgrr.a['href']).split('=')

last_page = s[-1]  

# 빈 데이터프레임 생성
df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=029780'  

for page in range(1, int(last_page)+1):
    url = '{}&page={}'.format(sise_url, page)  
    html = requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text
    pd.concat([df, pd.read_html(html, header=0)[0]])

df = df.dropna()
print(df)



# 차트 출력을 위해 데이터프레임 가공하기
df = df.dropna()
df = df.iloc[0:30]  
df = df.sort_values(by='날짜')  

# 날짜, 종가 컬럼으로 차트 그리기
plt.title('Samsung Card (close)')
plt.xticks(rotation=45)  
plt.plot(df['날짜'], df['종가'], 'co-') 
plt.grid(color='gray', linestyle='--')
plt.show()


