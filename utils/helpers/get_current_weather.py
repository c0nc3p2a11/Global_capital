import os
import requests
import allure
from utils.endpoints import CURRENT_WEATHER
from dotenv import load_dotenv
from utils.helpers.get_coordinates_by_city_name import get_coordinates

load_dotenv()

appid = os.getenv("API_KEY")


def get_current_weather(city_name, lang="en", units="metric"):
    """
    :param units: standard, metric and imperial
    :param lang: e.g en
    :param city_name: in any language (you can use Алматы, Алмата, алма-ата and other. Coordinates will be correct)
    """
    with allure.step("Sending request"):
        lat, lon = get_coordinates(city_name)

        params = {"lat": lat, "lon": lon, "appid": appid, "units": units, "lang": lang}
        response = requests.get(url=CURRENT_WEATHER, params=params)
    return response
