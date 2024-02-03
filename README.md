# Matrix demo site Back server

# 1. 환경
- Ubuntu 20.04.6 LTS
- python 3.10.9

# 2. 실행
- conda create -n demo_back python=3.10
- conda activate demo_back
- pip install -r reqiurements.txt
- python app.py

# 3. 파일 구조

## 1) 루트 경로 파일
- app.log
- app.py : 다른 FastAPI 애플리케이션에 요청을 보내는 중개자 역할, CORS 미들웨어를 통해 특정 origin에서의 요청을 허용
- package-lock.json
- package.json
- README.md
- requirements.txt