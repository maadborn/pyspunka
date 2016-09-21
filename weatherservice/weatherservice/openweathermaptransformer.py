from boltons.iterutils import remap
from pprint import pprint

def transform_data(data):
    def move_main(data):
        main = data['main']
        data.update(main)
        return data
    
    def visit_move(path, key, value):
        if key == 'clouds':
            return key, value['all']
        if key == 'rain':
            return key, value['3h']
        if key == 'snow':
            return key, value['3h']
        if key == 'weather':
            return key, value[0]
        return True

    def visit_rename(path, key, value):
        if key == 'coord':
            return 'loccoords', value
        if key == 'dt':
            return 'time', value
        if key == 'id' and 'weather' not in path:
            return 'locid', value
        if key == 'name':
            return 'locname', value
        if key == 'weather':
            return 'weatherdescr', value
        if key == 'rain':
            return 'rain3h', value
        if key == 'snow':
            return 'snow3h', value
        return True

    def visit_remove(path, key, value):
        if key == 'base' \
        or key == 'cod' \
        or key == 'sys' \
        or key == 'main' \
        or key == 'visibility' \
        or key == 'temp_min' \
        or key == 'temp_max' \
        or key == 'grnd_level' \
        or key == 'sea_level':
            return False
        return True

    transformed_data = move_main(data)
    transformed_data = remap(transformed_data, visit = visit_move)
    transformed_data = remap(transformed_data, visit = visit_rename)
    transformed_data = remap(transformed_data, visit = visit_remove)

    return transformed_data

'''
# TEST

data = {
    "base": "stations",
    "clouds": {
        "all": 20
    },
    "cod": 200,
    "coord": {
        "lat": 58.47,
        "lon": 15.63
    },
    "dt": 1474485377,
    "id": 2716758,
    "main": {
        "grnd_level": 1022.41,
        "humidity": 77,
        "pressure": 1022.41,
        "sea_level": 1037.51,
        "temp": 285.496,
        "temp_max": 285.496,
        "temp_min": 285.496
    },
    "name": "Ekangen",
    "sys": {
        "country": "SE",
        "message": 0.1644,
        "sunrise": 1474432942,
        "sunset": 1474476998
    },
    "weather": [
        {
            "description": "few clouds",
            "icon": "02n",
            "id": 801,
            "main": "Clouds"
        }
    ],
    "wind": {
        "deg": 41.5022,
        "speed": 0.91
    }
}

#data = {
#    "base": "cmc stations",
#    "clouds": {
#        "all": 20
#    },
#    "cod": 200,
#    "coord": {
#        "lat": 58.47,
#        "lon": 15.63
#    },
#    "dt": 1472912400,
#    "id": 2716758,
#    "main": {
#        "humidity": 63,
#        "pressure": 1006,
#        "temp": 291.47,
#        "temp_max": 292.15,
#        "temp_min": 291.15
#    },
#    "name": "Ekangen",
#    "sys": {
#        "country": "SE",
#        "id": 5424,
#        "message": 0.0026,
#        "sunrise": 1472875359,
#        "sunset": 1472924935,
#        "type": 1
#    },
#    "weather": [
#        {
#            "description": "few clouds",
#            "icon": "02d",
#            "id": 801,
#            "main": "Clouds"
#        }
#    ],
#    "wind": {
#        "deg": 240,
#        "speed": 6.2
#    }
#}

result = transform_data(data)
pprint(result)
'''