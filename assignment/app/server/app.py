from pydantic import BaseModel

from fastapi import FastAPI

from app.server.routes.weather import router as WeatherRouter
from app.server.routes.weather_pandas import router as WeatherPandasRouter

app = FastAPI()

app.include_router(WeatherRouter, tags=["Weather"], prefix="/weather")
app.include_router(WeatherPandasRouter, tags=["Weather"], prefix="/weather_pandas")

@app.get("/", tags=["health_check"])
async def read_root():
    return {"message": "Welcome to health check link"}