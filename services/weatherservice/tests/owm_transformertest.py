'''Tests OpenWeatherMapTransformer'''

import unittest
from openweathermap.owm_transformer import OpenWeatherMapTransformer

class OWMTransformTest(unittest.TestCase):
    '''Tests OpenWeatherMapTransformer'''

    def test_owm_transform(self):
        '''Tests transform_data'''
        transformer = OpenWeatherMapTransformer()
        transformed = transformer.transform_data(self.testdata_owm_transform)
        self.assertDictEqual(
            transformed,
            self.testdata_owm_transform_expected,
            "Transformed structure is not the same as expected")

    testdata_owm_transform = {
        "coord": {
            "lon": 15.63,
            "lat": 58.47
        },
        "weather": [{
            "id": 802,
            "main": "Clouds",
            "description": "scattered clouds",
            "icon": "03d"
        }],
        "base": "stations",
        "main": {
            "temp": 284.832,
            "pressure": 1003.98,
            "humidity": 71,
            "temp_min": 284.832,
            "temp_max": 284.832,
            "sea_level": 1018.73,
            "grnd_level": 1003.98
        },
        "wind": {
            "speed": 5.16,
            "deg": 256.503
        },
        "clouds": {
            "all": 32
        },
        "dt": 1475299418,
        "sys": {
            "message": 0.009,
            "country": "SE",
            "sunrise": 1475298186,
            "sunset": 1475339375
        },
        "id": 2716758,
        "name": "Ekangen",
        "cod": 200
    }

    testdata_owm_transform_expected = {
        "loccoords": {
            "lon": 15.63,
            "lat": 58.47
        },
        "weatherdescr": {
            "id": 802,
            "description": "scattered clouds",
            "icon": "03d"
        },
        "temp": 284.832,
        "pressure": 1003.98,
        "humidity": 71,
        "wind": {
            "speed": 5.16,
            "deg": 256.503
        },
        "clouds": 32,
        "time": 1475299418,
        "locid": 2716758,
        "locname": "Ekangen"
    }

if __name__ == '__main__':
    unittest.main()
