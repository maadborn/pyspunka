'''owm_validatortest'''

import unittest
from openweathermap.owm_validator import OpenWeatherMapDataValidator

class OWMValidateTest(unittest.TestCase):
    '''OWMValidateTest'''

    def test_owm_validate_ok(self):
        '''Validate OWM OK data'''
        validator = OpenWeatherMapDataValidator()
        validator.validate(self.testdata_owm_validate_200)
        self.assertEqual(1, 1, 'Just to have something to assert')

    def test_owm_validate_404(self):
        '''Validate OWM 404 data'''
        validator = OpenWeatherMapDataValidator()
        with self.assertRaisesRegex(Exception, 'Not found city'):
            validator.validate(self.testdata_owm_validate_404)

    testdata_owm_validate_200 = {
        'cod': 200,
        'name': 'Ekangen'
    }

    testdata_owm_validate_404 = {
        'cod': 404,
        'message': 'Error: Not found city'
    }

if __name__ == '__main__':
    unittest.main()
