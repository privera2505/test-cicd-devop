import pytest
from fastapi.testclient import TestClient
from src.api import app

@pytest.fixture
def client():
    """Crea un cliente de prueba"""
    return TestClient(app)   

def test_heath(client):
    """test unique"""
    assert True == False