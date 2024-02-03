from fastapi import FastAPI, HTTPException
import requests
import uvicorn
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="백엔드 서버")
root_path = os.path.abspath(".")

# CORSMiddleware를 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.0.32:8406"],
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)


class RequestModelType(BaseModel):
    category: str = "Detection"
    sub_category: str = "보호장비 착용 식별 모델"


class RequestInference(BaseModel):
    category: str = "Detection"
    sub_category: str = "보호장비 착용 식별 모델"
    data_list: List[str] = []
    port: int = 8403  # 기본 포트 설정


# 기본 AI 서버 URL
base_first_app_url = "http://192.168.0.32:8403"


@app.get("/getCategory")
async def Get_Category():
    # 첫 번째 FastAPI 애플리케이션의 /getCategory 엔드포인트 호출
    response = requests.get(f"{base_first_app_url}/getCategory")

    if response.status_code == 200:
        data = response.json()
        return {"data_from_first_app": data}
    else:
        return {"error": response.status_code}


@app.get("/sampleImg")
async def Sample_Img():
    # 첫 번째 FastAPI 애플리케이션의 /sampleImg 엔드포인트 호출
    response = requests.get(f"{base_first_app_url}/sampleImg")

    if response.status_code == 200:
        data = response.json()
        return {"data_from_first_app": data}
    else:
        return {"error": response.status_code}


@app.get("/modelCategory")
async def Model_Category():
    # 첫 번째 FastAPI 애플리케이션의 /modelCategory 엔드포인트 호출
    response = requests.get(f"{base_first_app_url}/modelCategory")

    if response.status_code == 200:
        data = response.json()
        return {"data_from_first_app": data}
    else:
        return {"error": response.status_code}


@app.post("/modelType", status_code=200)
async def request_model_type(req: RequestModelType):
    # 요청 데이터 설정
    request_data = req.dict()

    # 첫 번째 FastAPI 애플리케이션의 /modelType 엔드포인트로 POST 요청 보내기
    response = requests.post(f"{base_first_app_url}/modelType", json=request_data)

    if response.status_code == 200:
        data = response.json()
        return {"data_from_first_app": data}
    else:
        raise HTTPException(status_code=response.status_code, detail="Request failed")


@app.post("/inference", status_code=200)
async def request_inference(
    req: RequestInference,
):
    # 요청 데이터 설정
    request_data = {
        "category": req.category,
        "sub_category": req.sub_category,
        "data_list": req.data_list,
    }
    # print(req.sub_category)

    # 포트 번호를 기반으로 AI 서버 URL을 동적으로 구성
    dynamic_first_app_url = f"http://192.168.0.32:{req.port}"

    # 동적으로 결정된 AI 서버 URL로 요청 보내기
    response = requests.post(f"{dynamic_first_app_url}/inference", json=request_data)

    # print("응답 데이터:", response.text)

    if response.status_code == 200:
        data = response.json()
        return {"data_from_first_app": data}
    else:
        return {"error": response.status_code}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=int(8402), reload=True)
