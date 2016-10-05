'''OpenWeatherMapDataValidator'''

class OpenWeatherMapDataValidator:
    '''OpenWeatherMapDataValidator'''

    @staticmethod
    def validate(data):
        '''Validates OpenWeatherMap data'''
        if data is None:
            raise Exception('Failed to validate received data: data missing')
        if str(data['cod']) != '200':
            raise Exception(
                '{}: {}: {}'.format(
                    'Failed to validate received data',
                    data['cod'],
                    data['message']))

# Failed request:
#{
#  "cod": "404",
#  "message": "Error: Not found city"
#}
