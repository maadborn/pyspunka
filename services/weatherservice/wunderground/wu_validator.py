'''validate'''

def wu_validate(data):
    '''wu_validate'''
    if 'error' in data:
        raise Exception('{}: {}: {}'.format('Failed to validate received data', data['error']['type'], data['error']['description']))

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
