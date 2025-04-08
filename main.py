from fastapi import FastAPI
from sklearn.linear_model import LinearRegression
import numpy as np
from prometheus_client import Counter, start_http_server

app = FastAPI()

request_counter = Counter("http_requests_total", "Total HTTP Requests", ["endpoint"])

# 더미 ML 모델 초기화
model = LinearRegression()
x_train = np.array([[1], [2], [3], [4]])
y_train = np.array([2, 4, 6, 8])
model.fit(x_train, y_train)

# Prometheus 매트릭 엔드포인트
start_http_server(8001)

@app.get("/")
async def root():
    return {"message": "Hello, MLOps Project!"}

@app.get("/predict")
async def predict(x: float):
    prediction = model.predict(np.array([[x]]))[0]
    return {"input": x, "prediction": prediction}