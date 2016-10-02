from app import app
#from dataservicejsonencoder import DataServiceJSONEncoder
from customroutesweather import custom_weather_routes
from flask_cors import CORS

#app.json_encoder = DataServiceJSONEncoder

app.register_blueprint(custom_weather_routes)

CORS(app)   # Adds CORS '*' to all routes