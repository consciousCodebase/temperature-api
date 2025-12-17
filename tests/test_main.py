#---------------------------
# Project:
# Temperature Conversion API
# using Python APIs
#
# Joy Williams Morales
# Date: 14 December 2025
#
# Filename: test_main.py
#----------------------------

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200

def test_celsius_to_fahrenheit_valid():
    response = client.post(
        "/celsius-to-fahrenheit",
        json={"value":0}
    )
    assert response.status_code == 200
    data = response.json()

    assert data["celsius"] == 0
    assert data["fahrenheit"] == 32

def test_fahrenheit_to_celsius_valid():
    response = client.post(
        "/fahrenheit-to-celsius",
        json={"value":32}
        )
    
    assert response.status_code == 200
    data = response.json()

    assert data["fahrenheit"] == 32
    assert data["celsius"] == 0

def test_celsius_to_fahrenheit_negative_valid():
    response = client.post(
        "/celsius-to-fahrenheit",
        json={"value":-40}
        )
    assert response.status_code == 200
    assert response.json()["fahrenheit"] == -40

def test_fahrenheit_to_celsius_decimal_valid():
    response = client.post(
        "/fahrenheit-to-celsius",
        json={"value":98.6}
        )
    assert response.status_code == 200
    assert round(response.json()["celsius"], 1) == 37.0

def test_celsius_to_fahrenheit_missing_value():
    response = client.post("/celsius-to-fahrenheit", json={})
    assert response.status_code == 422

def test_fahrenheit_to_celsius_missing_value():
    response = client.post("/fahrenheit-to-celsius", json={})
    assert response.status_code == 422

def test_celsius_to_fahrenheit_nan():
    response = client.post(
        "/celsius-to-fahrenheit",
        json={"value": "nan"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Value must be a finite number"

def test_fahrenheit_to_celsius_nan():
    response = client.post(
        "/fahrenheit-to-celsius",
        json={"value": "nan"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Value must be a finite number"

def test_celsius_to_fahrenheit_infinity():
    response = client.post(
        "/celsius-to-fahrenheit",
        json={"value": "inf"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Value must be a finite number"

def test_fahrenheit_to_celsius_infinity():
    response = client.post(
        "/fahrenheit-to-celsius",
        json={"value": "inf"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Value must be a finite number"

def test_celsius_to_fahrenheit_non_numeric():
    response = client.post(
        "/celsius-to-fahrenheit",
        params={"value": "abc"}
    )
    assert response.status_code == 422

def test_fahrenheit_to_celsius_non_numeric():
    response = client.post(
        "/fahrenheit-to-celsius",
        params={"value": "abc"}
    )
    assert response.status_code == 422