import requests
import json
from pprint import pprint
from openweathermaptransformer import transform_data

class DataServiceClient:
    DATA_SERVICE_URL = 'http://localhost:5100/weather'

    #logging.config.fileConfig('logging.conf')
    #logger = logging.getLogger('weatherService')

    def send(self, data):
        transformed_data = transform_data(data)
        
        if not self.validate_unique(transformed_data):
            return None

        json_dumped_data = json.dumps(transformed_data)
        
        try:
            headers = {'Content-type': 'application/json'}
            response = requests.post(self.DATA_SERVICE_URL, headers = headers, data = json_dumped_data)
            pprint(response)
        except Exception as err:
            print('Failed to send weather data:' + err, file = sys.stderr, flush=True)

    def validate_unique(self, data_dict):
        '''Validates that data service doesn't already contain the data'''
        try:
            filters = {'locid': data_dict['locid'], 'time': data_dict['time']}
            payload = {'where': json.dumps(filters)}
            response = requests.get(self.DATA_SERVICE_URL, params=payload)

            if len(response.json()['_items']) == 0:
                return True
            else:
                print('Values already stored - locid={}, time={}'.format(filters['locid'], filters['time']), flush=True)

        except Exception as err:
            print('Failed to validate unique weather data:' + err, file = sys.stderr, flush=True)

        return False
