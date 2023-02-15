from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.process_pandas.process_pandas import (
    pandas_statistic_weather,
)


from app.server.models.weather import (
    ErrorResponseModel,
    ResponseModel,
    WeatherSchema,
    LocationSchema,
)

router = APIRouter()


@router.post("/", response_description="Weather data folder added into the database")
async def add_weather_data(weather: LocationSchema = Body(...)):
    weather = jsonable_encoder(weather)
    print(weather['location'],flush=True)
    new_weather = await pandas_statistic_weather(weather['location'])
    return ResponseModel(new_weather, "Weather added successfully.")

