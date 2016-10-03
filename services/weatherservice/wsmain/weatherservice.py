'''weatherservice'''

import time
#import logging
from openweathermap.owm_datacollector import OpenWeatherMapDataCollector
from wunderground.wu_datacollector import WUDataCollector
from wsmain.dataserviceclient import DataServiceClient, serviceconfig
from utils import logger

class WeatherService:
    '''WeatherService'''

    owm_data_collector = OpenWeatherMapDataCollector()
    wu_data_collector = WUDataCollector()
    data_service_client = DataServiceClient()

    def start(self):
        '''start'''

        wu_location = self.data_service_client.get_wu_location_default()
        if wu_location is None:
            raise Exception('Default location for WU not found')

        while True:
            try:
                owm_data = self.owm_data_collector.collect_default()
                if owm_data is not None:
                    self.data_service_client.send_owm(owm_data)
                owm_data = None
            except Exception as err:
                logger.log_error('Failed to process OpenWeatherMap data in main loop', err)

            try:
                if wu_location is not None:
                    wu_data = self.wu_data_collector.collect(wu_location)
                if wu_data is not None:
                    self.data_service_client.send_wu(wu_data)
                wu_data = None
            except Exception as err:
                logger.log_error('Failed to process WeatherUnderground data in main loop', err)

            time.sleep(serviceconfig.UPDATE_INTERVAL)
