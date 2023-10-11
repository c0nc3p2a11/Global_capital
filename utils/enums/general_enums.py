from enum import Enum


class GeneralErrors(Enum):
    WRONG_STATUS_CODE = "Status code is different than expected"
    WRONG_CITY_NAME = "City name is different than factual coordinates location"
