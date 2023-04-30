import os
import requests
from fastapi import FastAPI

app = FastAPI()

API_Key = os.environ.get('API_KEY')
lat= os.environ.get("LAT")
lon = os.environ.get("LONG")

if 'API_KEY' not in os.environ:
    print("API_KEY environment variable not defined.")
    exit(1)
if 'LAT' not in os.environ:
    print("LAT environment variable not defined.")
    exit(1)
if 'LONG' not in os.environ:
    print("LONG environment variable not defined.")
    exit(1)

@app.get("/")
async def root():
    return {"message": "Welcome to my weather API!"}

def get_weather(lat, long):     
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp'] - 273.15 # Convert Kelvin to Celsius
        return f'The weather in your location is {weather} with a temperature of {temperature:.2f}°C'
    else:
        return 'Failed to retrieve weather data'


print(get_weather(lat, lon))