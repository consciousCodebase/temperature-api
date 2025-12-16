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

def test_celsius_to_fahrenheit_negative():
    response = client.get("/celsius-to-fahrenheit?value=-40")
    assert response.status_code == 200
    assert response.json()["fahrenheit"] == -40

def test_fahrenheit_to_celsius_decimal():
    response = client.get("/fahrenheit-to-celsius?value=98.6")
    assert response.status_code == 200
    assert round(response.json()["celsius"], 1) == 37.0