import uvicorn
from os import getenv

API_HOST = getenv("API_HOST", "0.0.0.0")
PORT = getenv("PORT", "8000")
TEST_NAME = getenv("TEST_NAME", "Api1.1")

if __name__ == "__main__":
    uvicorn.run("api:app", host=API_HOST, port=int(PORT))