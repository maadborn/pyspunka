'''Configuration for the Weather Service project'''

UPDATE_INTERVAL = 60 * 60   # 60 minutes

# http://api.openweathermap.org/data/2.5/weather?id=2716758&appid=f0db5dccac9fb038bf628776d6709f06
OWM_API_KEY = 'f0db5dccac9fb038bf628776d6709f06'
OWM_URL = 'http://api.openweathermap.org/data/2.5/weather'
OWM_LOCATION_ID_DEFAULT = 2716758

# http://api.wunderground.com/api/023fbd9f0734365c/conditions/q/sweden/linkoping.json
WU_API_KEY = '023fbd9f0734365c'
WU_URL = 'http://api.wunderground.com/api/023fbd9f0734365c/conditions/q/{}.json'
WU_DEFAULT_QUERY = 'sweden/linkoping'
WU_LOCATION_CITY_ID_DEFAULT = 1

URL_DATA_SERVICE_WEATHER = 'http://localhost:5100/weather'
URL_DATA_SERVICE_WEATHER2 = 'http://localhost:5100/weather2'
URL_DATA_SERVICE_LOCATION = 'http://localhost:5100/location'
