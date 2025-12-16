import logging
from fastapi import FastAPI, Request

#-----------------------
# Logging Configuration
#-----------------------
logging.basicConfig(
    level = logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger("temperature-api")

#-------------------
# App Initialization
#-------------------
app = FastAPI()

#-------
# Routes
#-------

@app.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {"message": "Temperature Conversion API"}

@app.get("/celsius-to-fahrenheit")
def celsius_to_fahrenheit(value: float):
    try:
        logger.info(f"Converting Celsius to Fahrenheit: value={value}")

        fahrenheit = (value * 9 / 5) + 32

        logger.info(
            f"Conversion result: {value}C -> {fahrenheit}F"
        )

        return {
            "celsius": value,
            "fahrenheit": fahrenheit
        }
    except Exception as e:
        logger.error("Conversion failed", exc_info=True)
        raise

@app.get("/fahrenheit-to-celsius")
def fahrenheit_to_celsius(value: float):
    try:
        logger.info(f"Converting Fahrenheit to Celsius: value={value}")

        celsius = (value - 32) * 5 / 9

        logger.info(
            f"Conversion result: {value}F -> {celsius}C"
        )

        return {
            "fahrenheit": value,
            "celsius": celsius
        }
    except Exception as e:
        logger.error("Conversion failed", exc_info=True)

#-----------
# Middleware
#-----------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response Status: {response.status_code}")
    return response