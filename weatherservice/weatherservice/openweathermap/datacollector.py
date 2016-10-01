import sys
import requests
import serviceconfig
from logger import log_error
from openweathermap import transformer
from openweathermap import validator

class OpenWeatherMapDataCollector:
    def collect(self, id):
        try:
            data = self.get_data(id)
            validator.OpenWeatherMapDataValidator.validate(data)
            transformed_data = transformer.OpenWeatherMapTransformer.transform_data(data)
            return transformed_data;
        except Exception as err:
            log_error('Failed to collect data', err)

    def collect_default(self):
        return self.collect(serviceconfig.LOCATION_ID_DEFAULT)

    def get_data(self, id):
        payload = {'id': id, 'appid': serviceconfig.API_KEY}
        response = requests.get(serviceconfig.OPEN_WEATHER_URL, params = payload)
        return response.json()