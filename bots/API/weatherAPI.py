# API de OpenWeatherMap
from pyowm import OWM
import os

def getClima(ciudad):

    API_KEY = os.getenv('API_KEY')

    # Se proporciona la clave de la API
    # Se cera un objeto de tipo OWM
    owm = OWM(API_KEY)

    # Se crea un objeto de tipo WeatherManager
    wm = owm.weather_manager()

    # Se busca el clima de una ciudad
    obs = wm.weather_at_place(ciudad)

    # Se obtiene informacion del clima de la ciudad
    clima = obs.weather
    localidad = obs.location

    temperatura = clima.temperature('celsius')['temp']
    humedad = clima.humidity
    viento = clima.wind()
    nubes = clima.status

    clima = (
        f"Localidad: {localidad.name} \nTemperatura: {temperatura} °C\nHumedad: {humedad}%\nViento: {viento['speed']} km/h\nNubes: {nubes}")

    return clima
