'''weatherservice'''

import datetime
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

        sleep_time = WeatherService.get_initial_sleep_time()
        logger.log_info('Sleeping for {} seconds'.format(sleep_time))
        time.sleep(sleep_time)

        wu_location = self.data_service_client.get_wu_location_default()
        if wu_location is None:
            raise Exception('Default location for WU not found')

        while True:
            self.run_owm_collect()
            self.run_wu_collect(wu_location)
            time.sleep(serviceconfig.UPDATE_INTERVAL)

    def run_owm_collect(self):
        try:
            owm_data = self.owm_data_collector.collect_default()
            if owm_data is not None:
                self.data_service_client.send_owm(owm_data)
            #owm_data = None
        except Exception as err:
            logger.log_error('Failed to process OpenWeatherMap data in main loop', err)

    def run_wu_collect(self, wu_location):
        try:
            if wu_location is not None:
                wu_data = self.wu_data_collector.collect(wu_location)
            if wu_data is not None:
                self.data_service_client.send_wu(wu_data)
            #wu_data = None
        except Exception as err:
            logger.log_error('Failed to process WeatherUnderground data in main loop', err)

    def get_initial_sleep_time():
        time_now = datetime.datetime.now()
        logger.log_info('Time now: {}'.format(time_now))
        sleep_time = (60 - time_now.minute) * 60 - (time_now.second)
        logger.log_info('Time until until next hour starts: {} seconds'.format(sleep_time))
        return sleep_time
