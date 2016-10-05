'''OpenWeatherMapDataCollector'''
import requests
from wsmain import serviceconfig
from utils import logger
from openweathermap.owm_transformer import OpenWeatherMapTransformer
from openweathermap.owm_validator   import OpenWeatherMapDataValidator

class OpenWeatherMapDataCollector:
    '''OpenWeatherMapDataCollector'''
    _validator = OpenWeatherMapDataValidator()
    _transformer = OpenWeatherMapTransformer()

    def collect(self, location_id):
        '''Collects transformed data from OpenWeatherMap'''
        try:
            data = self.get_data(location_id)
            self._validator.validate(data)
            transformed_data = self._transformer.transform_data(data)
            return transformed_data
        except Exception as err:
            logger.log_error('Failed to collect OWM data:', err)
        return None

    def collect_default(self):
        '''Collects transformed data from OpenWeatherMap for default location'''
        return self.collect(serviceconfig.OWM_LOCATION_ID_DEFAULT)

    @staticmethod
    def get_data(location_id):
        '''Fetches data from OpenWeatherMap'''
        payload = {'id': location_id, 'appid': serviceconfig.OWM_API_KEY}
        response = requests.get(serviceconfig.OWM_URL, params=payload)
        return response.json()
