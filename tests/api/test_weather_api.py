import pytest


@pytest.mark.weather_api
def test_status_code_weather_api(weather_api):
    """
    Test to check the status code returned by the Weather API.

    This test verifies that the Weather API returns a status code of 200,
    indicating a successful request.
    """
    resp = weather_api.get_status_code()  # Get the status code from the API

    assert resp == 200  # Assert that the status code is 200


@pytest.mark.weather_api
def test_get_current_weather(weather_api):
    """
    Test to check the current weather data for a specified city.

    This test verifies that the Weather API returns the correct location
    details for the specified city (Lviv) in the current weather data.
    """
    resp = weather_api.get_current_weather('Lviv')  # Get the current weather for Lviv

    assert resp['location']['name'] == 'Lviv'  # Assert that the location name is 'Lviv'
    assert resp['location']['country'] == 'Ukraine'  # Assert that the country is 'Ukraine'


@pytest.mark.weather_api
def test_get_forecast_weather(weather_api):
    """
    Test to check the weather forecast data for a specified city.

    This test verifies that the Weather API returns the correct number
    of forecast days for the specified city (Lviv) and number of days (3).
    """
    resp = weather_api.get_forecast_weather('Lviv', 3)  # Get the weather forecast for Lviv for 3 days

    assert len(resp['forecast']['forecastday']) == 3  # Assert that the number of forecast days is 3
