from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/api2/test1")
async def payment_webhook(request: Request):
    return "Test micro 123"

@app.get("/api2/test2")
async def payment_webhook(request: Request):
    return "Test micro 123"

@app.get("/api2/health")
async def payment_webhook(request: Request):
    return 200