import pytest
from fastapi.testclient import TestClient
from api import app

@pytest.fixture
def client():
    """Crea un cliente de prueba"""
    return TestClient(app)   

def test_heath(client):
    """test unique"""
    assert True == True
