# Assignment

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Language & Database : Python(FastAPI) & Mysql

## Problem 1 - Data Modeling

### Mysql Database : weather, Table : weather 

```
CREATE TABLE weather (
    date varchar(8) PRIMARY KEY,
    min_temperature DECIMAL(3,1),
    max_temperature DECIMAL(3,1),
    precipitation DECIMAL(3,1),
#    station varchar(32)
);
```

## Problem 2 - Ingestion

file location : `assignment/process.py'
function : add_weather - using restAPI per line by line
function : add_weathers - using restAPI for all records once.

Elapsed time printed on the logs.

** date file has PRIMARY KEY attribute, So it could have duplicate value on `date` field.


## Problem 3 - Data Analysis

file location : `assignment/process.py'
function : statistic_weather()


## Problem 4 - REST API

### orm-service : http://localhost:8001/docs

### assignment : http://localhost:8000/docs
To use assignment call It should copy `code-challenge-template` folder around assignment folder.
(default code-challenge-template location : `~/assignment/code-challenge-template`)


## Extra Credit - Deployment

```
docker-compose up 
```
or 
```
docker-compose up -d
```


file location : `assignment/process.py'
function : pandas_statistic_weather()

* Simple pandas library test version 


