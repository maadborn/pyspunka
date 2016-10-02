import sys
import requests
from wsmain import serviceconfig
from utils import logger
from wunderground.transformer import WUTransformer
from wunderground.validator import WUValidator

class WUDataCollector:
    _validator = WUValidator()
    _transformer = WUTransformer()

    def collect(self, location):
        try:
            location_query = self.get_location_query(location)
            data = self.get_data(location_query)
            self._validator.validate(data)
            transformed_data = self._transformer.transform_data(data, location['_id'])
            return transformed_data;
        except Exception as err:
            logger.log_error('Failed to collect data', err)

        return None;

    def collect_default(self):
        return self.collect(serviceconfig.WU_DEFAULT_QUERY)

    def get_data(self, location_query):
        url = serviceconfig.WU_URL.format(location_query)
        response = requests.get(url)
        return response.json()

    def get_location_query(self, location):
        return '{}/{}'.format(location['state_name_wu'], location['city_wu'])
        