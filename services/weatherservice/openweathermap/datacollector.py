import sys
import requests
from wsmain import serviceconfig
from utils import logger
from openweathermap import transformer
from openweathermap import validator

class OpenWeatherMapDataCollector:
    _validator = validator.OpenWeatherMapDataValidator()
    _transformer = transformer.OpenWeatherMapTransformer()

    def collect(self, id):
        try:
            data = self.get_data(id)
            self._validator.validate(data)
            transformed_data = self._transformer.transform_data(data)
            return transformed_data;
        except Exception as err:
            logger.log_error('Failed to collect data:', err)

        return None;

    def collect_default(self):
        return self.collect(serviceconfig.OWM_LOCATION_ID_DEFAULT)

    def get_data(self, id):
        payload = {'id': id, 'appid': serviceconfig.OWM_API_KEY}
        response = requests.get(serviceconfig.OWM_URL, params = payload)
        return response.json()