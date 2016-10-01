import requests
import json
import serviceconfig
from utils import logger
from pprint import pprint

class DataServiceClient:
    #logging.config.fileConfig('logging.conf')
    #logger = logging.getLogger('weatherService')

    def send(self, data):
        if not self.validate_unique(data):
            return None

        json_dumped_data = json.dumps(data)
        
        try:
            headers = {'Content-type': 'application/json'}
            response = requests.post(serviceconfig.URL_DATA_SERVICE_WEATHER, headers = headers, data = json_dumped_data)
            logger.log_info(response)
        except Exception as err:
            logger.log_error('Failed to send weather data', err)

    def validate_unique(self, data_dict):
        '''Validates that data service doesn't already contain the data'''
        try:
            filters = {'locid': data_dict['locid'], 'time': data_dict['time']}
            payload = {'where': json.dumps(filters)}
            response = requests.get(serviceconfig.URL_DATA_SERVICE_WEATHER, params=payload)

            if len(response.json()['_items']) == 0:
                return True
            else:
                logger.log_info('Values already stored - locid={}, time={}'.format(filters['locid'], filters['time']))

        except Exception as err:
            logger.log_error('Failed to validate unique weather data', err)

        return False
