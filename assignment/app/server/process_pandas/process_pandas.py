from time import process_time
import httpx
import pandas as pd

# crud operations

# Add a new weather into to the database
async def pandas_statistic_weather(filename:str) -> dict:
    t1_start = process_time()

    with open(filename, 'r') as fp:
        data = pd.read_csv(filename, header=None,sep='\t', usecols=[1,2,3])
        avg = data.mean(axis=0)
        total = data.sum(axis=0)
        average_max_temperature = float(avg[1])
        average_min_temperature = float(avg[2])
        total_precipitation = float(total[3])


        t1_stop = process_time()
        print("Elapsed time:", t1_stop, t1_start) 
        print("Elapsed time during the whole program in seconds:",
                                            t1_stop-t1_start) 

        return {
            "average_max_temperature":average_max_temperature, 
            "average_min_temperature":average_min_temperature, 
            "total_precipitation":total_precipitation
        }
    
