from pydantic import BaseModel
from typing import List


class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    sea_level: int
    grnd_level: int
    humidity: int
    temp_kf: float


class Clouds(BaseModel):
    all: int


class Wind(BaseModel):
    speed: float
    deg: int
    gust: float


class Sys(BaseModel):
    pod: str


class ListItem(BaseModel):
    dt: int
    main: Main
    weather: List[Weather]
    clouds: Clouds
    wind: Wind
    visibility: int
    pop: int
    sys: Sys
    dt_txt: str


class City(BaseModel):
    id: int
    name: str
    coord: dict
    country: str
    population: int
    timezone: int
    sunrise: int
    sunset: int


class FiveDays(BaseModel):
    cod: str
    message: int
    cnt: int
    list: List[ListItem]
    city: City
