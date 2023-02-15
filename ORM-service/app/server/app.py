from pydantic import BaseModel

from fastapi import FastAPI

from app.server.routes.weather import router as WeatherRouter

app = FastAPI()


app.include_router(WeatherRouter, tags=["Weather"], prefix="/weather")

@app.get("/", tags=["health_check"])
async def read_root():
    return {"message": "Welcome to health check link"}