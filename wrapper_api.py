import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

API_Key = os.environ.get('API_KEY')
lat= os.environ.get("LAT")
lon = os.environ.get("LONG")

# Vérification des variables d'environnement
if API_Key is None:
    raise ValueError("La variable d'environnement OPENWEATHER_API_KEY est manquante")
if lat is None:
    raise ValueError("La variable d'environnement LAT est manquante")
if lon is None:
    raise ValueError("La variable d'environnement LONG est manquante")


@app.get("/")
def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp'] - 273.15 # Convert Kelvin to Celsius
        return {'weather': weather, 'temperature': temperature}
    else:
        return {'error': 'Failed to retrieve weather data'}

