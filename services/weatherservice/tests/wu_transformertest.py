'''wu_transformertest'''

import unittest
from wunderground.wu_transformer import WUTransformer

class WUTransformerTest(unittest.TestCase):
    '''WUTransformerTest'''

    def test_wu_transform(self):
        '''wu_transform'''
        transformer = WUTransformer()
        location_id = '01234567abcdef'
        transformed = transformer.transform_data(self.testdata_wu_transform, location_id)
        self.assertDictEqual(transformed, self.testdata_wu_transform_expected, "Transformed structure is not the same as expected")

    testdata_wu_transform = {
        "response": {
            "version": "0.1",
            "termsofService": "http://www.wunderground.com/weather/api/d/terms.html",
            "features": {
                "conditions": 1
            }
        },
        "current_observation": {
            "image": {
                "url": "http://icons.wxug.com/graphics/wu2/logo_130x80.png",
                "title": "Weather Underground",
                "link": "http://www.wunderground.com"
            },
            "display_location": {
                "full": "Linkoping, Sweden",
                "city": "Linkoping",
                "state": "",
                "state_name": "Sweden",
                "country": "SN",
                "country_iso3166": "SE",
                "zip": "00000",
                "magic": "1",
                "wmo": "02562",
                "latitude": "58.40000153",
                "longitude": "15.52000046",
                "elevation": "93.00000000"
            },
            "observation_location": {
                "full": "Linkoping, ",
                "city": "Linkoping",
                "state": "",
                "country": "SN",
                "country_iso3166": "SE",
                "latitude": "58.39805603",
                "longitude": "15.52583313",
                "elevation": "305 ft"
            },
            "estimated": {},
            "station_id": "ESCF",
            "observation_time": "Last Updated on October 1, 3:20 PM CEST",
            "observation_time_rfc822": "Sat, 01 Oct 2016 15:20:00 +0200",
            "observation_epoch": "1475328000",
            "local_time_rfc822": "Sat, 01 Oct 2016 15:30:12 +0200",
            "local_epoch": "1475328612",
            "local_tz_short": "CEST",
            "local_tz_long": "Europe/Stockholm",
            "local_tz_offset": "+0200",
            "weather": "Mostly Cloudy",
            "temperature_string": "57 F (14 C)",
            "temp_f": 57,
            "temp_c": 14,
            "relative_humidity": "72%",
            "wind_string": "From the West at 12 MPH",
            "wind_dir": "West",
            "wind_degrees": 260,
            "wind_mph": 12,
            "wind_gust_mph": 0,
            "wind_kph": 18,
            "wind_gust_kph": 0,
            "pressure_mb": "1009",
            "pressure_in": "29.80",
            "pressure_trend": "0",
            "dewpoint_string": "48 F (9 C)",
            "dewpoint_f": 48,
            "dewpoint_c": 9,
            "heat_index_string": "NA",
            "heat_index_f": "NA",
            "heat_index_c": "NA",
            "windchill_string": "NA",
            "windchill_f": "NA",
            "windchill_c": "NA",
            "feelslike_string": "57 F (14 C)",
            "feelslike_f": "57",
            "feelslike_c": "14",
            "visibility_mi": "6.2",
            "visibility_km": "10.0",
            "solarradiation": "--",
            "UV": "1",
            "precip_1hr_string": "-9999.00 in (-9999.00 mm)",
            "precip_1hr_in": "-9999.00",
            "precip_1hr_metric": "--",
            "precip_today_string": "0.00 in (0.0 mm)",
            "precip_today_in": "0.00",
            "precip_today_metric": "0.0",
            "icon": "mostlycloudy",
            "icon_url": "http://icons.wxug.com/i/c/k/mostlycloudy.gif",
            "forecast_url": "http://www.wunderground.com/global/stations/02562.html",
            "history_url": "http://www.wunderground.com/history/airport/ESCF/2016/10/1/DailyHistory.html",
            "ob_url": "http://www.wunderground.com/cgi-bin/findweather/getForecast?query=58.39805603,15.52583313",
            "nowcast": ""
        }
    }

    testdata_wu_transform_expected = {
        'station_id':   'ESCF',
        'obs_epoch':    '1475328000',
        'weather':      'Mostly Cloudy',
        'temp':         14,
        'humidity':     72,
        'wind_degrees': 260,
        'wind_mps':     5,
        'pressure':     1009,
        'UV':           1,
        'precip_1hr':   0,
        'precip_today': 0.0,
        'icon':         'mostlycloudy',
        'icon_url':     'http://icons.wxug.com/i/c/k/mostlycloudy.gif',
        'location_id':  '01234567abcdef',
    }

if __name__ == '__main__':
    unittest.main()
