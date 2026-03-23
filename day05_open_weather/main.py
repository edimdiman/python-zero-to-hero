import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

city = input("Enter a city: ")

# Open Weather requires Lat and Long, using their Geocoding API here
# Just pulling the first result, will consider other cities later
geo_url = "http://api.openweathermap.org/geo/1.0/direct"

geo_params = {
    "q": city,
    "limit": 5,
    "appid": API_KEY
}

geo_response = requests.get(geo_url, params=geo_params)

geo_data = geo_response.json()

city_lat = geo_data[0]["lat"]
city_lon = geo_data[0]["lon"]

# Now for the current weather, using the weather API
weather_url = "https://api.openweathermap.org/data/2.5/weather"

weather_params = {
    "lat": city_lat,
    "lon": city_lon,
    "units": "metric",
    "appid": API_KEY
}

weather_response = requests.get(weather_url, params=weather_params) 

weather_data = weather_response.json()

# All together now
print(f"It is currently {round(weather_data['main']['temp'])}°C in {city}.")

# Very basic, will make more improvements later
