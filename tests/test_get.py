import pytest
import allure
from utils.helpers.get_current_weather import get_current_weather
from utils.baseclasses.response import Response
from utils.schemas.current_weather import CurrentWeather
from utils.schemas.five_days import FiveDays
from utils.helpers.get_five_days_forecast import get_five_days_forecast
from utils.enums.general_enums import GeneralErrors
from utils.enums.weather_enum import Cities


@allure.story("Test current weather")
class TestCurrent:
    @pytest.mark.positive
    @pytest.mark.parametrize("city_name", Cities.VALID_POSITIVE)
    def test_get_current_positive(self, city_name):
        """Positive check for any city"""
        response = Response(get_current_weather(city_name))
        response.assert_status_code(200)
        response.validate(CurrentWeather)
        assert response.response_json["name"] == city_name, GeneralErrors.WRONG_CITY_NAME.value

    @pytest.mark.negative
    @pytest.mark.parametrize("city_name", Cities.INVALID_NEGATIVE)
    def test_get_current_negative(self, city_name):
        """Negative check for any city"""
        response = Response(get_current_weather(city_name))
        response.assert_status_code(200)
        response.validate(CurrentWeather)
        assert response.response_json["name"] == city_name, GeneralErrors.WRONG_CITY_NAME.value


@allure.feature("Get forecast for 5 days")
@pytest.mark.parametrize("city_name", ["Almaty"])
def test_get_five_days_forecast(city_name):
    """Test for 5 days forecast. number of timestamps = 5 by default."""
    response = Response(get_five_days_forecast(city_name))
    response.assert_status_code(200)
    response.validate(FiveDays)
    assert len(response.response_json["list"]) == 5, GeneralErrors.WRONG_CITY_NAME.value
