import sys
import requests
import serviceconfig

class WeatherDataCollector:
    # http://api.openweathermap.org/data/2.5/weather?id=2716758&appid=f0db5dccac9fb038bf628776d6709f06
    
    def collect(self, id):
        try:
            payload = {'id': id, 'appid': serviceconfig.API_KEY}
            response = requests.get(serviceconfig.OPEN_WEATHER_URL, params = payload)
            return response.json()
        except Exception as err:
            print('Failed to collect data', file=sys.stderr, flush=True)

    def collect_default(self):
        return self.collect(serviceconfig.LOCATION_ID_DEFAULT)