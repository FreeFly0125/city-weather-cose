import openmeteo_requests
import requests_cache
from retry_requests import retry

cache_session = requests_cache.CachedSession(".cache", expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

url = "https://api.open-meteo.com/v1/forecast"


def get_current_weather(latitude, longitude):
    params = {"latitude": latitude, "longitude": longitude, "current": ["temperature_2m", "rain", "weather_code"]}

    response = openmeteo.weather_api(url=url, params=params)

    weather_info = response[0].Current().Variables

    return weather_info
