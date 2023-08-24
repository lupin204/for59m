import FinanceDataReader as fdr
import firebase_admin
from firebase_admin import credentials, firestore
import json


# 다운로드한 키 파일의 경로
cred = credentials.Certificate('d:/myprjs/for59m/doc/for84m2-firebase-adminsdk-j8u7b-74f6e68204.json')

# Firebase 프로젝트 초기화
firebase_admin.initialize_app(cred)


df_krx = fdr.StockListing("KRX")


# Convert DataFrame to JSON object
json_object = df_krx.to_json(orient='records', indent=4, force_ascii=False)
data = json.loads(json_object)

# Realtime Database의 레퍼런스 생성
db = firestore.client()
collection_ref = db.collection('stocks')


# 데이터 쓰기
for item in data:
    doc_ref = collection_ref.document(item["Code"])  # Automatically generate a new document ID
    doc_ref.set(item)  # Set the data of the document


############################################
# Realtime Database의 레퍼런스 생성
db = firestore.client()
collection_ref = db.collection('stocks-name')


# 데이터 쓰기
for item in data:
    doc_ref = collection_ref.document(item["Name"])  # Automatically generate a new document ID
    doc_ref.set(item)  # Set the data of the document

