from typing import Optional

from pydantic import BaseModel, Field

class LocationSchema(BaseModel):
    location: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "location": "./code-challenge-template/wx_data/USC00115712.txt",
            }
        }


class WeatherSchema(BaseModel):
    process_time: float = Field(...)
    average_max_temperature: float = Field(...)
    average_min_temperature: float = Field(...)
    total_precipitation: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "average_max_temperature": -11,
                "average_min_temperature": -140,
                "total_precipitation": 191,
                "process_time": 1.000,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}