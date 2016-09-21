from datetime import datetime

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# Skip these if your db has no auth. But it really should.
#MONGO_USERNAME = '<your username>'
#MONGO_PASSWORD = '<your password>'

MONGO_DBNAME = 'apidev'

#########################

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

#########################

X_DOMAINS = '*'

#########################

DOMAIN = {
    # Adapted from http://openweathermap.org/current#parameter
    'weather': {
        'schema': {
            'locid':   { 'type': 'integer' },
            'locname': { 'type': 'string' },
            'loccoords': {
                'type': 'dict',
                'schema': {
                    'lat': { 'type': 'number' },
                    'lon': { 'type': 'number' },
                },
            },
            'wind': {
                'type': 'dict',
                'schema': {
                    'speed': { 'type': 'number' },
                    'deg':   { 'type': 'number' },
                },
            },
            'rain3h':   { 'type': 'number' },
            'snow3h':   { 'type': 'number' },
            'clouds':   { 'type': 'number' },
            'temp':     { 'type': 'number' },
            'humidity': { 'type': 'number' },
            'pressure': { 'type': 'number' },
            'time':     { 'type': 'integer' },
            'weatherdescr': {
                # http://openweathermap.org/weather-conditions
                'type': 'dict',
                'schema': {
                    'id':   { 'type': 'integer' },
                    'main': { 'type': 'string' },
                    'description': { 'type': 'string' },
                    'icon': { 'type': 'string' },
                },
            },
        },
    },
    'dump': {
        'schema': {
            'x': { 'type': 'string' },
        },
    },
}