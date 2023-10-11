import os
import requests
from utils.endpoints import FIVE_DAYS_FORECAST
from dotenv import load_dotenv
from utils.helpers.get_coordinates_by_city_name import get_coordinates

load_dotenv()

appid = os.getenv("API_KEY")


def get_five_days_forecast(city_name, lang="en", units="metric", limit=5):
    """
    :param limit: number of timestamps per day
    :param units: standard, metric and imperial
    :param lang: e.g en
    :param city_name: in any language (you can use Алматы, Алмата, алма-ата and other. Coordinates will be correct)
    """
    lat, lon = get_coordinates(city_name)

    params = {"lat": lat, "lon": lon, "appid": appid, "units": units, "lang": lang, "cnt": limit}
    response = requests.get(url=FIVE_DAYS_FORECAST, params=params)
    return response
