import FinanceDataReader as fdr
import firebase_admin
from firebase_admin import credentials, firestore
import json

# 다운로드한 키 파일의 경로
cred = credentials.Certificate('./for84m2-firebase-adminsdk-j8u7b-74f6e68204.json')

# Firebase 프로젝트 초기화
firebase_admin.initialize_app(cred)



def my_function():
    return "Hello, World!"

my_variable = 42

if __name__ == "__main__":
    # This code will run only if this script is executed directly, not when it's imported as a module
    print("This is the main module")
