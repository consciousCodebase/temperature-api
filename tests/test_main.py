from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Temperature Conversion API"}

def test_celsius_to_fahrenheit():
    response = client.get("/celsius-to-fahrenheit?value=0")
    assert response.status_code == 200
    data = response.json()

    assert data["celsius"] == 0
    assert data["fahrenheit"] == 32

def test_fahrenheit_to_celsius():
    response = client.get("/fahrenheit-to-celsius?value=32")
    assert response.status_code == 200
    data = response.json()

    assert data["fahrenheit"] == 32
    assert data["celsius"] == 0