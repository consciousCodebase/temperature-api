from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Temperature Conversion API"}

@app.get("/celsius-to-fahrenheit")
def celcius_to_fahrenheit(value: float):
    fahrenheit = (value * 9 / 5) + 32
    return {
        "celcius": value,
        "fahrenheit": fahrenheit
    }

@app.get("/fahrenheit-to-celsius")
def fahrenheit_to_celcius(value: float):
    celcius = (value - 32) * 5 / 9
    return {
        "fahrenheit": value,
        "celsius": celcius
    }