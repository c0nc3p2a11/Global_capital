import os
import requests
from utils.endpoints import GEOCODING_URL
from dotenv import load_dotenv

load_dotenv()

appid = os.getenv("API_KEY")


def get_coordinates(city_name):
    """
    :param city_name: in any language (you can use Алматы, Алмата, алма-ата and other. Coordinates will be correct)
    :return: tuple(lattitude, longtitude)
    """
    params = {"q": city_name, "limit": 1, "appid": appid}
    response = requests.get(url=GEOCODING_URL, params=params).json()
    res = (response[0]["lat"], response[0]["lon"])
    return res
