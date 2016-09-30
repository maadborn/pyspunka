from flask import jsonify
from app import app
from pprint import pprint

mongoclient = app.data.driver

def get_weather_data_for(location_id):
    data = mongoclient.db.weather.find({
            'locid': location_id
        }, {
            'time': 1, 
            'temp': 1, 
            'pressure': 1, 
            'humidity': 1
        })
    return list(data)