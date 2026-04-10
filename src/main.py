import uvicorn
from os import getenv

API_HOST = getenv("API_HOST", "0.0.0.0")
API_PORT = getenv("API_PORT", "8000")
TEST_NAME = getenv("TEST_NAME", "Api1.1")

if __name__ == "__main__":
    uvicorn.run("api:app", host=API_HOST, port=int(API_PORT))