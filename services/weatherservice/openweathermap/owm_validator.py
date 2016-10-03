'''OpenWeatherMapDataValidator'''

class OpenWeatherMapDataValidator:
    '''OpenWeatherMapDataValidator'''

    def validate(self, data):
        '''Validates OpenWeatherMap data'''
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
