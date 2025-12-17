#---------------------------
# Project:
# Temperature Conversion API
# using Python APIs
#
# Joy Williams Morales
# Date: 14 December 2025
#
# Filename: main.py
#----------------------------

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import logging
from fastapi import FastAPI, Request

from fastapi import HTTPException, Query
import math

from app.models import (
    TemperatureRequest,
    CelsiusToFahrenheitResponse,
    FahrenheitToCelsiusResponse,
)

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
app.mount("/static", StaticFiles(directory="static"), name="static")


#-------
# Routes
#-------

@app.get("/")
def root():
    logger.info("Serving frontend")
    return FileResponse("static/index.html")

@app.post("/celsius-to-fahrenheit",
         response_model=CelsiusToFahrenheitResponse)

def celsius_to_fahrenheit(payload: TemperatureRequest):
    try:
        value = payload.value
        logger.info(f"Converting Celsius to Fahrenheit: value={value}")

        if not math.isfinite(value):
            logger.warning("Invalid Celsius value received")
            raise HTTPException(
                status_code=400,
                detail="Value must be a finite number"
            )
        
        fahrenheit = (value * 9 / 5) + 32

        logger.info(
            f"Conversion result: {value}C -> {fahrenheit}F"
        )

        return CelsiusToFahrenheitResponse(
            celsius=value,
            fahrenheit=fahrenheit
        )
    
    except HTTPException:
        raise

    except Exception as e:
        logger.error("Conversion failed", exc_info=True)
        raise

@app.post("/fahrenheit-to-celsius",
         response_model=FahrenheitToCelsiusResponse)

def fahrenheit_to_celsius(payload: TemperatureRequest):
    try:
        value = payload.value
        logger.info(f"Converting Fahrenheit to Celsius: value={value}")

        if not math.isfinite(value):
            logger.warning("Invalid Fahrenheit value received")
            raise HTTPException(
                status_code=400,
                detail="Value must be a finite number"
            )

        celsius = (value - 32) * 5 / 9

        logger.info(
            f"Conversion result: {value}F -> {celsius}C"
        )

        return FahrenheitToCelsiusResponse(
            fahrenheit=value,
            celsius=celsius
        )
    
    except HTTPException:
        raise

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