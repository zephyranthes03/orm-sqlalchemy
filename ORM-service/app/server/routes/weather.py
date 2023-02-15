from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from typing import List

from app.server.database import (
    add_weather,
    add_weathers,
    retrieve_weather,
    retrieve_weathers,
    delete_weather,
    # update_weather,
)
from app.server.models.weather import (
    ErrorResponseModel,
    ResponseModel,
    WeatherSchema,
    UpdateWeatherModel,
)

router = APIRouter()


@router.post("/all", response_description="Weather data added into the database")
async def add_weather_data(weather: List[WeatherSchema] = Body(...)):
    weather = jsonable_encoder(weather)
    new_weather = await add_weathers(weather)
    return ResponseModel(new_weather, "Weather added successfully.")

@router.post("/", response_description="Weather data added into the database")
async def add_weather_data(weather: WeatherSchema = Body(...)):
    weather = jsonable_encoder(weather)
    new_weather = await add_weather(weather)
    return ResponseModel(new_weather, "Weather added successfully.")


@router.get("/", response_description="Weathers retrieved")
async def get_weathers():
    weathers = await retrieve_weathers()
    if weathers:
        return ResponseModel(weathers, "Weathers data retrieved successfully")
    return ResponseModel(weathers, "Empty list returned")


@router.get("/{id}", response_description="Weather data retrieved")
async def get_weather_data(id):
    weather = await retrieve_weather(id)
    if weather:
        return ResponseModel(weather, "Weather data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Weather doesn't exist.")


# @router.put("/{id}")
# async def update_weather_data(id: str, req: UpdateWeatherModel = Body(...)):
#     req = {k: v for k, v in req.dict().items() if v is not None}
#     updated_weather = await update_weather(id, req)
#     if updated_weather:
#         return ResponseModel(
#             "Weather with ID: {} name update is successful".format(id),
#             "Weather name updated successfully",
#         )
#     return ErrorResponseModel(
#         "An error occurred",
#         404,
#         "There was an error updating the weather data.",
#     )


@router.delete("/", response_description="Weather data deleted from the database")
async def delete_weather_data():
    deleted_weather = await delete_weather()
    if deleted_weather == True:
        return ResponseModel([], "Empty list returned")
    return ErrorResponseModel(
        "An error occurred", 404, "Weather with id {0} doesn't exist".format(id)
    )