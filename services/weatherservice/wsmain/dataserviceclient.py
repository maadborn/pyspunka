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

    @staticmethod
    def send_owm(data):
        '''send_owm'''

        # Skipping unique validation, let's always save the data
        #if not self.validate_unique_owm(data):
        #    return None

        dump = json.dumps(data)

        try:
            hdrs = {'Content-type': 'application/json'}
            response = requests.post(
                serviceconfig.URL_DATA_SERVICE_WEATHER,
                headers=hdrs,
                data=dump)
            logger.log_info(response)
        except Exception as err:
            logger.log_error('Failed to send OWM weather data', err)

    @staticmethod
    def validate_unique_owm(data_dict):
        '''Validates that data service doesn't already contain the OWM data'''
        try:
            filters = {'locid': data_dict['locid'], 'time': data_dict['time']}
            payload = {'where': json.dumps(filters)}
            response = requests.get(serviceconfig.URL_DATA_SERVICE_WEATHER, params=payload)

            if len(response.json()['_items']) == 0:
                return True
            else:
                logger.log_info(
                    'OWM values already stored - locid={}, time={}'.format(
                        filters['locid'],
                        filters['time']))

        except Exception as err:
            logger.log_error('Failed to validate unique OWM weather data', err)

        return False

    #### WU METHODS ####

    @staticmethod
    def get_wu_location(city_id):
        '''get_wu_location'''
        payload = {'city_id': json.dumps(city_id)}
        response = requests.get(serviceconfig.URL_DATA_SERVICE_LOCATION, params=payload)
        return response.json()['_items'][0]

    def get_wu_location_default(self):
        '''get_wu_location_default'''
        return self.get_wu_location(serviceconfig.WU_LOCATION_CITY_ID_DEFAULT)

    @staticmethod
    def send_wu(data):
        '''send_wu'''
        # Skipping unique validation, let's always save the data
        #if not self.validate_unique_wu(data):
        #    return None

        dump = json.dumps(data)

        try:
            hdrs = {'Content-type': 'application/json'}
            response = requests.post(
                serviceconfig.URL_DATA_SERVICE_WEATHER2,
                headers=hdrs,
                data=dump)
            logger.log_info(response)
        except Exception as err:
            logger.log_error('Failed to send WU weather data', err)

    @staticmethod
    def validate_unique_wu(data_dict):
        '''Validates that data service doesn't already contain the WU data'''
        try:
            filters = {'location_id': data_dict['location_id'], 'obs_epoch': data_dict['obs_epoch']}
            payload = {'where': json.dumps(filters)}
            response = requests.get(serviceconfig.URL_DATA_SERVICE_WEATHER2, params=payload)

            if len(response.json()['_items']) == 0:
                return True
            else:
                logger.log_info(
                    'WU values already stored - locid={}, time={}'.format(
                        filters['locid'],
                        filters['time']))

        except Exception as err:
            logger.log_error('Failed to validate unique WU weather data', err)

        return False
