from time import process_time
import httpx
from typing import List

# crud operations


# Add a new weather into to the database
async def add_weather(filename:str) -> dict:
    t1_start = process_time()

    with open(filename, 'r') as fp:
        Lines = fp.readlines()
        for line in Lines:
            param = line.split()
            payload = {'date':param[0],
                        'max_temperature':float(param[1]),
                        'min_temperature':float(param[2]),
                        'precipitation':float(param[3])}
            # print(line,flush=True)
            # print(payload,flush=True)
            async with httpx.AsyncClient() as client:
                r = await client.post('http://orm-service:8001/weather/',
                                    json=payload)
    
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start) 
    print("Elapsed time during the whole program in seconds:",
                                         t1_stop-t1_start) 
    

# Add a new weather into to the database
async def add_weathers(filename:str) -> dict:
    t1_start = process_time()

    with open(filename, 'r') as fp:
        Lines = fp.readlines()
        total_payload = list()
        for line in Lines:
            param = line.split()
            payload = {'date':param[0],
                        'max_temperature':float(param[1]),
                        'min_temperature':float(param[2]),
                        'precipitation':float(param[3])}
            total_payload.append(payload)
            # print(line,flush=True)
            # print(payload,flush=True)
        async with httpx.AsyncClient() as client:
            r = await client.post('http://orm-service:8001/weather/all',
                                json=total_payload, timeout=300)
    
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start) 
    print("Elapsed time during the whole program in seconds:",
                                         t1_stop-t1_start) 
    


# Retrieve a weather with a matching ID
async def statistic_weather(): # -> dict:
    t1_start = process_time()
    total_max_temperature = 0
    total_min_temperature = 0
    total_precipitation = 0
    count_max_temperature = 0
    count_min_temperature = 0
    async with httpx.AsyncClient() as client:
        r = await client.get('http://orm-service:8001/weather/', timeout=300) 
        data = r.json()['data'][0]
        for line in data:
            # print(line,flush=True)
            if line[1] != 9999:
                count_max_temperature += 1
                total_max_temperature = total_max_temperature + line[1]
            if line[2] != 9999:
                count_min_temperature += 1
                total_min_temperature = total_min_temperature + line[2]
            if line[3] != 9999:
                total_precipitation = total_precipitation + line[3]

        average_max_temperature = total_max_temperature / count_max_temperature if count_max_temperature != 0 else 9999
        average_min_temperature = total_min_temperature / count_min_temperature if count_min_temperature != 0 else 9999

        t1_stop = process_time()
        print("Elapsed time:", t1_stop, t1_start) 
        print("Elapsed time during the whole program in seconds:",
                                            t1_stop-t1_start) 
    
    return {'average_max_temperature':average_max_temperature, 
            'average_min_temperature':average_min_temperature,
            'total_precipitation':total_precipitation
            }


# Delete a weather from the database
async def delete_weather():
    r = httpx.delete('http://orm-service:8001/weather/') 
    if r.status_code == 200:
        return True
    return False
