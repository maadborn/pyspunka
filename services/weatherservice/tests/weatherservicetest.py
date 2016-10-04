'''weatherservicetest'''

import unittest
from wsmain.weatherservice import WeatherService

class WeatherServiceTest(unittest.TestCase):
    '''WeatherServiceTest'''

    def test_get_initial_sleep_time(self):
        '''test_get_initial_sleep_time'''

        WeatherService.get_initial_sleep_time()

if __name__ == '__main__':
    unittest.main()
