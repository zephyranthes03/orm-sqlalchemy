from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.process.process import (
    statistic_weather,
    statistic_weather_by_station,
    delete_weather,
    add_weather,
    add_weathers
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
    new_weather = await add_weather(weather['location'])
    return ResponseModel(new_weather, "Weather added successfully.")

@router.post("/all", response_description="Weather data folder added into the database")
async def add_weathers_data(weather: LocationSchema = Body(...)):
    weather = jsonable_encoder(weather)
    print(weather['location'],flush=True)
    new_weather = await add_weathers(weather['location'])
    return ResponseModel(new_weather, "Weather added successfully.")


@router.get("/", response_description="Weathers retrieved")
async def get_weathers():
    weathers = await statistic_weather()
    if weathers:
        return ResponseModel(weathers, "Weathers data statistic retrieved successfully")
    return ResponseModel(weathers, "Empty list returned")

@router.get("/{id}", response_description="Weathers retrieved")
async def get_weathers(id:str):
    weathers = await statistic_weather_by_station(id)
    if weathers:
        return ResponseModel(weathers, "Weathers data statistic retrieved successfully")
    return ResponseModel(weathers, "Empty list returned")


@router.delete("/", response_description="Weather data deleted from the database")
async def delete_weather_data():
    deleted_weather = await delete_weather()
    if deleted_weather == True:
        return ResponseModel([], "Database is Deleted")
    return ErrorResponseModel(
        "An error occurred", 404, "Database deletation is failiure"
    )