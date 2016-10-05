'''wu_validatortest'''

import unittest
from wunderground.wu_validator import wu_validate

class WUValidateTest(unittest.TestCase):
    '''WUValidateTest'''

    def test_wu_validate_ok(self):
        '''wu_validate_ok'''
        wu_validate(self.testdata_wu_validate_ok)
        self.assertEqual(1, 1, 'Just to have something to assert')

    def test_wu_validate_error(self):
        '''wu_validate_error'''
        with self.assertRaisesRegex(Exception, 'No cities match your search query'):
            wu_validate(self.testdata_wu_validate_error)

    testdata_wu_validate_ok = {
        "response": {
            "version": "0.1",
            "termsofService": "http://www.wunderground.com/weather/api/d/terms.html",
            "features": {
                "conditions": 1
            }
        },
        "current_observation": {
            "blabla": "bläblä",
            "foo": 123
        }
    }

    testdata_wu_validate_error = {
        "response": {
            "version": "0.2",
            "termsofService": "http://www.wunderground.com/weather/api/d/terms.html",
            "features": {
                "conditions": 1
            },
        },
        "error": {
            "type": "querynotfound",
            "description": "No cities match your search query"
        }
    }

if __name__ == '__main__':
    unittest.main()
