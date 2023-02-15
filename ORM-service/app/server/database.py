from typing import List

# import databases
import sqlalchemy
# from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


# SQLAlchemy specific code, as with any other app
DATABASE_URL = 'mysql+mysqldb://root:default@mysql/weather'
engine = sqlalchemy.create_engine(DATABASE_URL)

metadata = sqlalchemy.MetaData()

weathers = sqlalchemy.Table(
    "weather",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String(19), primary_key=True),
    sqlalchemy.Column("date", sqlalchemy.String(8)),
    sqlalchemy.Column("station", sqlalchemy.String(11)),
    sqlalchemy.Column("min_temperature", sqlalchemy.DECIMAL(5,1)),
    sqlalchemy.Column("max_temperature", sqlalchemy.DECIMAL(5,1)),
    sqlalchemy.Column("precipitation", sqlalchemy.DECIMAL(5,1)),
    # sqlalchemy.Column("date_convert", sqlalchemy.Date),
)

metadata.create_all(engine)

class Weather(BaseModel):
    id: str
    date: str
    station: str
    min_temperature: float
    max_temperature: float
    precipitation: float


# helpers

# crud operations


# Retrieve all weathers present in the database
async def retrieve_weathers() -> list:
    with engine.connect() as conn:        
        query = weathers.select()
        result_list = list()
        for row in conn.execute(query):
            result_list.append(list(row))
        return result_list


# Retrieve a weather with a matching station id
async def retrieve_weathers_by_station(id: str): # -> dict:
    with engine.connect() as conn:
        query = weathers.select().where(weathers.c.station==id)
        result_list = list()
        for row in conn.execute(query):
            result_list.append(list(row))
        return result_list


# Add a new weather into to the database
async def add_weathers(weather_data: List[Weather]) -> dict:
    count = 0
    with engine.connect() as conn:
        for weather in weather_data:
            count += 1
            query = weathers.insert().values(id=f"{weather['station']}_{weather['date']}",date=weather['date'],
                max_temperature=weather['max_temperature'], min_temperature=weather['min_temperature'], 
                precipitation=weather['precipitation'], station=weather['station'])
            last_record_id = conn.execute(query)
        conn.commit()
        return {"Total inserted record : ", count}

# Add a new weather into to the database
async def add_weather(weather_data: Weather) -> dict:
    with engine.connect() as conn:        
        query = weathers.insert().values(id=f"{weather_data['station']}_{weather_data['date']}", date=weather_data['date'], 
            max_temperature=weather_data['max_temperature'], min_temperature=weather_data['min_temperature'], 
            precipitation=weather_data['precipitation'], station=weather_data['station'])
        last_record_id = conn.execute(query)
        conn.commit()
        return {**weather_data, "id": last_record_id}


# # Update a weather with a matching ID
# async def update_weather(id: str, data: dict):
#     # Return false if an empty request body is sent.
#     if len(data) < 1:
#         return False
#     weather = await weather_collection.find_one({"_id": ObjectId(id)})
#     if weather:
#         updated_weather = await weather_collection.update_one(
#             {"_id": ObjectId(id)}, {"$set": data}
#         )
#         if updated_weather:
#             return True
#         return False


# Delete a weather from the database
async def delete_weather():
    with engine.connect() as conn:        
        query = weathers.delete()
        conn.execute(query)
        conn.commit()
        return True
    return False
