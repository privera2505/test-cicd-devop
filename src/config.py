from os import getenv

API_HOST = getenv("API_HOST", "0.0.0.0")
API_PORT = getenv("API_PORT", "8000")
TEST_NAME = getenv("TEST_NAME", "Api0")