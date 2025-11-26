import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Bienvenido" in response.get_data(as_text=True)

def test_predict(client):
    response = client.get('/predict')
    assert response.status_code == 200
    assert "predicción" in response.get_data(as_text=True)

