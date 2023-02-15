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
    sqlalchemy.Column("date", sqlalchemy.String(8), primary_key=True),
    sqlalchemy.Column("min_temperature", sqlalchemy.DECIMAL(3,1)),
    sqlalchemy.Column("max_temperature", sqlalchemy.DECIMAL(3,1)),
    sqlalchemy.Column("precipitation", sqlalchemy.DECIMAL(3,1)),
    # sqlalchemy.Column("date_convert", sqlalchemy.Date),
)

# engine = sqlalchemy.create_engine(
#     DATABASE_URL, connect_args={"check_same_thread": False}
# )
metadata.create_all(engine)

class Weather(BaseModel):
    date: str
    min_temperature: float
    max_temperature: float
    precipitation: float


# helpers

# crud operations


# Retrieve all weathers present in the database
async def retrieve_weathers() -> list:
    with engine.connect() as conn:        
        query = weathers.select()
        # print(query, flush=True)
        # return conn.execute(query).all()
        result_list = list()
        for row in conn.execute(query):
            result_list.append(list(row))
        return result_list


# Add a new weather into to the database
async def add_weathers(weather_data: List[Weather]) -> dict:
    # database = engine.connect()
    count = 0
    with engine.connect() as conn:
        for weather in weather_data:
            count += 1
            query = weathers.insert().values(date=weather['date'], max_temperature=weather['max_temperature'],
                min_temperature=weather['min_temperature'], precipitation=weather['precipitation'])
            last_record_id = conn.execute(query)
        conn.commit()
        return {"Total inserted record : ", count}

# Add a new weather into to the database
async def add_weather(weather_data: Weather) -> dict:
    # database = engine.connect()
    with engine.connect() as conn:        
        query = weathers.insert().values(date=weather_data['date'], max_temperature=weather_data['max_temperature'],
            min_temperature=weather_data['min_temperature'], precipitation=weather_data['precipitation'])
        last_record_id = conn.execute(query)
        conn.commit()
        return {**weather_data, "id": last_record_id}

# Retrieve a weather with a matching ID
async def retrieve_weather(id: str): # -> dict:
    with engine.connect() as conn:
        query = weathers.select().where(weathers.c.date==id)
        # query = weathers.select().where(Weather.date==id)
        print(query, flush=True)
        # return conn.execute(query).all()
        result_list = list()
        for row in conn.execute(query):
            result_list.append(list(row))
        return result_list


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
