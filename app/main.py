from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Temperature Conversion API"}

@app.get("/celsius-to-fahrenheit")
def celsius_to_fahrenheit(value: float):
    fahrenheit = (value * 9 / 5) + 32
    return {
        "celsius": value,
        "fahrenheit": fahrenheit
    }

@app.get("/fahrenheit-to-celsius")
def fahrenheit_to_celsius(value: float):
    celsius = (value - 32) * 5 / 9
    return {
        "fahrenheit": value,
        "celsius": celsius
    }