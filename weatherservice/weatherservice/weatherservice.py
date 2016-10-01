import time
#import logging
from openweathermap import datacollector
from dataserviceclient import DataServiceClient
from utils import logger

class WeatherService:
    COLLECT_DATA_DELAY_SECONDS = 60 * 15
    
    weather_data_collector = datacollector.OpenWeatherMapDataCollector()
    data_service_client = DataServiceClient()

    def start(self):
        #logging.config.fileConfig('logging.conf')
        #logger = logging.getLogger('weatherService')

        while True:
            try:
                data = self.weather_data_collector.collect_default()
                if data != None:
                    self.data_service_client.send(data)
            except Exception as err:
                logger.log_error('Failed to process data in main loop', err)

            time.sleep(self.COLLECT_DATA_DELAY_SECONDS)
