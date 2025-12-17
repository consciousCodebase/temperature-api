#---------------------------
# Project:
# Temperature Conversion API
# using Python APIs
#
# Joy Williams Morales
# Date: 14 December 2025
#
# Filename: models.py
#----------------------------

from pydantic import BaseModel, Field
import math

#---------
# Requests
#---------

class TemperatureRequest(BaseModel):
    value: float
    
#----------
# Responses
#----------

class CelsiusToFahrenheitResponse(BaseModel):
    celsius: float = Field(..., description="Temperature in Celsius")
    fahrenheit: float = Field(..., description="Temperature in Fahrenheit")

class FahrenheitToCelsiusResponse(BaseModel):
    fahrenheit: float = Field(..., description="Temperature in Fahrenheit")
    celsius: float = Field(..., description="Temperature in Celsius")