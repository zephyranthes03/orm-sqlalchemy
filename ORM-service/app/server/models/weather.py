from typing import Optional

from pydantic import BaseModel, Field

class WeatherSchema(BaseModel):
    date: str = Field(...)
    station: str = Field(...)
    max_temperature: float = Field(...)
    min_temperature: float = Field(...)
    precipitation: float = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "date": "19850109",
                "station": "USC00332098",
                "max_temperature": -11,
                "min_temperature": -140,
                "precipitation": 191,
            }
        }


class UpdateWeatherModel(BaseModel):
    date: Optional[str]
    station: Optional[str]
    max_temperature: Optional[float]
    min_temperature: Optional[float]
    precipitation: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "date": "19850109",
                "station": "USC00332098",
                "max_temperature": -11,
                "min_temperature": -140,
                "precipitation": 191,
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