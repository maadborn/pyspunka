import unittest
from pprint import pprint
from openweathermap import validator

class OWMValidateTest(unittest.TestCase):
    def test_owm_validate_ok(self):
        v = validator.OpenWeatherMapDataValidator()
        v.validate(self.testdata_owm_validate_200)
        self.assertEqual(1, 1, 'Just to have something to assert')

    def test_owm_validate_404(self):
        v = validator.OpenWeatherMapDataValidator()
        with self.assertRaisesRegex(Exception, 'Not found city'):
            v.validate(self.testdata_owm_validate_404)

    testdata_owm_validate_200 = {
        "cod": 200,
        "name": "Ekangen"
    }

    testdata_owm_validate_404 = {
        "cod": 404,
        "message": "Error: Not found city"
    }

if __name__ == '__main__':
    unittest.main()