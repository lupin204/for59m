import FinanceDataReader as fdr
import firebase_admin
from firebase_admin import credentials, firestore
import json
from datetime import datetime, timedelta
import exchange_calendars as ecals


# 다운로드한 키 파일의 경로
cred = credentials.Certificate('d:/myprjs/for59m/doc/for84m2-firebase-adminsdk-j8u7b-74f6e68204.json')

# Firebase 프로젝트 초기화
firebase_admin.initialize_app(cred)
db = firestore.client()


########################################################################################
# yyyy-mm-dd
today = datetime.today().strftime('%Y-%m-%d')
# 어제 days = 1
# today = (datetime.today() - timedelta(days = 1)).strftime('%Y-%m-%d')

# 오늘은 개장일인지 확인
is_today_session = ecals.get_calendar("XKRX").is_session(today)


########################################################################################
# fdr 종목정보
print(f"finance-data start")

df_kospi = fdr.StockListing("KOSPI")
df_kosdaq = fdr.StockListing("KOSDAQ")

# columns, index, records, values, split
kospi_json_str = df_kospi.to_json(orient='records', indent=0, force_ascii=False)
kosdaq_json_str = df_kosdaq.to_json(orient='records', indent=0, force_ascii=False)

kospi_json_arr = json.loads(kospi_json_str)
kosdaq_json_arr = json.loads(kosdaq_json_str)

# [{'Code': '308700', 'ISU_CD': 'KR7308700004', 'Name': '테크엔', 'Market': 'KONEX', 'Dept': '일반기업부', 'Close': '265', 
# 'ChangeCode': '4', 'Changes': 34, 'ChagesRatio': 14.72, 'Open': 265, 'High': 265, 'Low': 201, 'Volume': 2251, 'Amount': 596451, 
# 'Marcap': 1060000000, 'Stocks': 4000000, 'MarketId': 'KNX'}, ... ]
krx_json_arr = kospi_json_arr + kosdaq_json_arr

# {'005930': {'Code': '005930', 'ISU_CD': 'KR7005930003', 'Name': '삼성전자', 'Market': 'KOSPI', 'Dept': '', 'Close': '67100', 
# 'ChangeCode': '2', 'Changes': -1100, 'ChagesRatio': -1.61, 'Open': 67100, 'High': 67400, 'Low': 66900, 'Volume': 7032462, 
# 'Amount': 471934306900, 'Marcap': 400572409105000, 'Stocks': 5969782550, 'MarketId': 'STK'}, ... }
krx_dict = { el["Code"]: el for el in krx_json_arr }
meta_dict = {}
print(f"finance-data end")


########################################################################################
# Realtime Database의 레퍼런스 생성 - 종목코드 6자리
collection_ref = db.collection('stocks')

print(f"firestore stocks start")
# 데이터 쓰기 - 개장일 인 경우만 firestore 적재
if (is_today_session):
    for item in krx_dict:
        # item = 005930'
        doc_dict = collection_ref.document(item).get().to_dict()
        # { '삼성전자': 005930 }
        meta_dict[krx_dict[item]['Name']] = item
        
        if (doc_dict):
            # 종목코드 있으면 금일 날짜 추가
            collection_ref.document(item).update({ today: krx_dict[item] })
        else:
            # 신규 종목코드면 새 document(종목) 추가
            collection_ref.document(item).set({ today: krx_dict[item] })
            
        # 특정 조건이면 bot 알림
        # 거래금액 1000억 :: 100000000000
        # trade_amount = doc_dict["Amount"] * doc_dict["Volume"]
        # if (trade_amount > 100000000000):
        #     print(item)
    
        

print(f"firestore stocks end")


########################################################################################
# Realtime Database의 메타정보
print(f"firestore meta start")
if (is_today_session):
    meta_collection_ref = db.collection('stocks-meta')
    meta_collection_ref.document('by-name').set(meta_dict)

print(f"firestore meta end")













