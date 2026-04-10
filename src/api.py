from fastapi import FastAPI, Request
from main import TEST_NAME

app = FastAPI()

@app.get("/api2/test1")
async def payment_webhook(request: Request):
    return f"Test micro 124 {TEST_NAME}"

@app.get("/api2/test2")
async def payment_webhook(request: Request):
    return f"Test micro 124 {TEST_NAME}"

@app.get("/api2/health")
async def payment_webhook(request: Request):
    return 200