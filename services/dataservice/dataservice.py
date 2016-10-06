from app import app
from customroutesweather import custom_weather_routes
from flask_cors import CORS

CORS(app)   # Adds CORS '*' to all routes

app.register_blueprint(custom_weather_routes)
