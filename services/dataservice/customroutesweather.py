from flask import Blueprint, Response
from weatherdataaccess import get_weather_data_for
from bson.json_util import dumps

custom_weather_routes = Blueprint('custom_weather_routes', __name__)

@custom_weather_routes.route('/custom/weather/<int:location_id>')
def get_weather_data(location_id):
    weather_list = get_weather_data_for(location_id)
    weather_json = dumps(weather_list)
    return Response(weather_json, mimetype='application/json')
