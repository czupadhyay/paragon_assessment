import logging, datetime, sys, os
from main.models import Weather, Yield, AVGWeather

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", 
                    handlers=[logging.FileHandler(os.path.dirname(os.path.dirname(os.getcwd()))+"/answers/ouput.log"),logging.StreamHandler(sys.stdout)])
logger = logging.getLogger(__name__)

def import_weather():
    '''
    This function is used to import & save wx_data into the Database
    '''
    path = os.path.dirname(os.path.dirname(os.getcwd()))+'/wx_data'
    os.chdir(path)
    start_time = datetime.datetime.now()
    weather = []
    logger.info("Weather Data insertion Start")
    try:
        for file in os.listdir():
            if file.endswith(".txt"):
                fpath = f"{path}/{file}"
                with open(fpath, "r") as data:
                    lines = [line.rstrip() for line in data]
                    for line in lines:
                        temp = line.split('\t')
                        w = Weather()
                        w.station = file[:-4]
                        w.date = int(temp[0])
                        w.max_temp = int(temp[1])
                        w.min_temp = int(temp[2])
                        w.ppt = int(temp[3])
                        weather.append(w)
        
        Weather.objects.bulk_create(weather, 5000)
        end_time = datetime.datetime.now()
        logger.info("Weather Data inserted Successfully")
        logger.info(f"Time taken: {(end_time-start_time).total_seconds()}\t Number of rows inserted: {len(weather)}")
    except Exception as err:
        logger.error(f"{err}")
        
def import_yield():
    '''
    This function is used to import & save yld_data into the Database
    '''
    path = (os.path.dirname(os.getcwd()))+'/yld_data'
    os.chdir(path)
    logger.info("Weather Data insertion Start")
    start_time = datetime.datetime.now()
    yieldList = []
    try:
        for file in os.listdir():
            if file.endswith(".txt"):
                fpath = f"{path}/{file}"
                with open(fpath, "r") as data:
                    lines = [line.rstrip() for line in data]
                    for line in lines:
                        temp = line.split('\t')
                        y = Yield()
                        y.year = int(temp[0])
                        y.yield_value = int(temp[1])
                        yieldList.append(y)
        Yield.objects.bulk_create(yieldList, 5000)
        end_time = datetime.datetime.now()
        logger.info("Yield Data inserted Successfully")
        logger.info(f"Time taken: {(end_time-start_time).total_seconds()}\t Number of rows inserted: {len(yieldList)}")
    except Exception as err:
        print(f"{err}")
    

def Get_all_data_info():
    '''
    This function is used to calculate the 
    * Average maximum temperature 
    * Average minimum temperature 
    * Total accumulated precipitation
    for every year, for every station and saving into the Database
    '''
    results = Weather.objects.raw("select id, station,date, avg(max_temp) as max_temp,avg(min_temp),\
                                    sum(ppt) from (select * from main_weather\
                                   where max_temp!=-9999 and min_temp!=-9999 and ppt!=-9999) t group by station , substring(date,1,4) ")
    for res in results:
        AVGWeather.objects.get_or_create(
            station = res.station,
            date = res.date,
            avg_max_temp = res.max_temp,
            avg_min_temp =res.min_temp,
            total_ppt = res.ppt
            )
    print("query ran succesfully")