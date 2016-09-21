import time
import sys
#import logging
from weatherdatacollector import WeatherDataCollector
from dataserviceclient import DataServiceClient

class WeatherService:
    COLLECT_DATA_DELAY_SECONDS = 60 * 15
    #COLLECT_DATA_DELAY_SECONDS = 60 * 60

    weather_data_collector = WeatherDataCollector()
    data_service_client = DataServiceClient()

    def start(self):
        #logging.config.fileConfig('logging.conf')
        #logger = logging.getLogger('weatherService')

        while True:
            try:
                data = self.weather_data_collector.collect_default()
                self.data_service_client.send(data)
            except Exception as err:
                print('Failed to process data in main loop' + err, file=sys.stderr, flush=True)

            time.sleep(self.COLLECT_DATA_DELAY_SECONDS)
