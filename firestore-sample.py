import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# 다운로드한 키 파일의 경로
cred = credentials.Certificate('d:/myprjs/for59m/doc/for84m2-firebase-adminsdk-j8u7b-74f6e68204.json')

# Firebase 프로젝트 초기화
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://for84m2-default-rtdb.asia-southeast1.firebasedatabase.app'  # Replace with your actual database URL
})

# Realtime Database의 레퍼런스 생성
ref = db.reference('/')

# 데이터 읽기
data = ref.get()
print(data)

# 데이터 쓰기
new_data = {'name': 'John', 'age': 30}
ref.set(new_data)