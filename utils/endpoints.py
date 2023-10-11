import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("URL")

GEOCODING_URL = f"{BASE_URL}/geo/1.0/direct"
CURRENT_WEATHER = f"{BASE_URL}/data/2.5/weather"
FIVE_DAYS_FORECAST = f"{BASE_URL}/data/2.5/forecast"
