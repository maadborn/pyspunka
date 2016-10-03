'''dataserviceclient'''

import json
import requests
from wsmain import serviceconfig
from utils import logger

class DataServiceClient:
    '''DataServiceClient'''

    #logging.config.fileConfig('logging.conf')
    #logger = logging.getLogger('weatherService')

    #### OWM METHODS ####

    def send_owm(self, data):
        '''send_owm'''
        if not self.validate_unique_owm(data):
            return None

        json_dumped_data = json.dumps(data)

        try:
            headers = {'Content-type': 'application/json'}
            response = requests.post(serviceconfig.URL_DATA_SERVICE_WEATHER, headers=headers, data=json_dumped_data)
            logger.log_info(response)
        except Exception as err:
            logger.log_error('Failed to send OWM weather data', err)

    def validate_unique_owm(self, data_dict):
        '''Validates that data service doesn't already contain the OWM data'''
        try:
            filters = {'locid': data_dict['locid'], 'time': data_dict['time']}
            payload = {'where': json.dumps(filters)}
            response = requests.get(serviceconfig.URL_DATA_SERVICE_WEATHER, params=payload)

            if len(response.json()['_items']) == 0:
                return True
            else:
                logger.log_info('OWM values already stored - locid={}, time={}'.format(filters['locid'], filters['time']))

        except Exception as err:
            logger.log_error('Failed to validate unique OWM weather data', err)

        return False

    #### WU METHODS ####

    def get_wu_location(self, city_id):
        '''get_wu_location'''
        payload = {'city_id': json.dumps(city_id)}
        response = requests.get(serviceconfig.URL_DATA_SERVICE_LOCATION, params=payload)
        return response.json()['_items'][0]

    def get_wu_location_default(self):
        '''get_wu_location_default'''
        return self.get_wu_location(serviceconfig.WU_LOCATION_CITY_ID_DEFAULT)

    def send_wu(self, data):
        '''send_wu'''
        if not self.validate_unique_wu(data):
            return None

        json_dumped_data = json.dumps(data)

        try:
            headers = {'Content-type': 'application/json'}
            response = requests.post(serviceconfig.URL_DATA_SERVICE_WEATHER2, headers=headers, data=json_dumped_data)
            logger.log_info(response)
        except Exception as err:
            logger.log_error('Failed to send WU weather data', err)

    def validate_unique_wu(self, data_dict):
        '''Validates that data service doesn't already contain the WU data'''
        try:
            filters = {'location_id': data_dict['location_id'], 'obs_epoch': data_dict['obs_epoch']}
            payload = {'where': json.dumps(filters)}
            response = requests.get(serviceconfig.URL_DATA_SERVICE_WEATHER2, params=payload)

            if len(response.json()['_items']) == 0:
                return True
            else:
                logger.log_info('WU values already stored - locid={}, time={}'.format(filters['locid'], filters['time']))

        except Exception as err:
            logger.log_error('Failed to validate unique WU weather data', err)

        return False
