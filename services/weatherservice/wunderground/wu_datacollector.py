'''datacollector'''

import requests
from wsmain import serviceconfig
from utils import logger
from wunderground.wu_transformer import WUTransformer
from wunderground.wu_validator import wu_validate
#import wunderground.wu_validator

class WUDataCollector:
    '''WUDataCollector'''

    #_validator = WUValidator()
    _transformer = WUTransformer()

    def collect(self, location):
        '''collect'''
        try:
            location_query = self.create_location_query(location)
            data = self.get_data(location_query)
            wu_validate(data)
            transformed_data = self._transformer.transform_data(data, location['_id'])
            return transformed_data
        except Exception as err:
            logger.log_error('Failed to collect WU data', err)

        return None

    def collect_default(self):
        '''collect_default'''
        return self.collect(serviceconfig.WU_DEFAULT_QUERY)

    @staticmethod
    def get_data(location_query):
        '''get_data'''
        url = serviceconfig.WU_URL.format(location_query)
        response = requests.get(url)
        return response.json()

    @staticmethod
    def create_location_query(location):
        '''create_location_query'''
        return '{}/{}'.format(location['state_name_wu'], location['city_wu'])
