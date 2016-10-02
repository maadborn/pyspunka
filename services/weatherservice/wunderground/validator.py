class WUValidator:
    def validate(self, data):
        if 'response' in data and 'error' in data['response']:
            raise Exception('{}: {}: {}'.format('Failed to validate received data', data['response']['error']['type'], data['response']['error']['description']))
    
# Failed request:
#{
#  "response": {
#    "version": "0.1",
#    "termsofService": "http://www.wunderground.com/weather/api/d/terms.html",
#    "features": {
#      "conditions": 1
#    },
#    "error": {
#      "type": "querynotfound",
#      "description": "No cities match your search query"
#    }
#  }
#}