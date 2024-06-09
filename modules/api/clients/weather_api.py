import requests


class WeatherApi:
    """
    A simple API client for interacting with the Weather API.
    """

    MAIN_URL = 'https://api.weatherapi.com/v1/'  # Base URL for the Weather API
    API_KEY = 'b97cfa5f31ae477e8be191208232602'  # Your API key for authenticating requests

    def get_status_code(self):
        """
        Get the status code from the Weather API for a sample request.

        This method sends a GET request to the Weather API for the current weather
        in Lviv and returns the status code of the response.

        :returns:
        int: The HTTP status code from the API response.
        """
        resp = requests.get(f"{self.MAIN_URL}current.json?key={self.API_KEY}&q=Lviv")
        return resp.status_code

    def get_current_weather(self, city):
        """
        Get the current weather for a specified city.

        This method sends a GET request to the Weather API to fetch the current weather
        data for the provided city.

        :param:
        city (str): The name of the city to get the current weather for.

        :returns:
        dict: A dictionary containing the current weather data for the specified city.
        """
        resp = requests.get(f"{self.MAIN_URL}current.json?key={self.API_KEY}&q={city}")
        return resp.json()

    def get_forecast_weather(self, city, days):
        """
        Get the weather forecast for a specified city for a given number of days.

        This method sends a GET request to the Weather API to fetch the weather forecast
        data for the provided city for the specified number of days.

        :param:
        city (str): The name of the city to get the weather forecast for.
        days (int): The number of days to get the weather forecast for.

        :returns:
        dict: A dictionary containing the weather forecast data for the specified city and days.
        """
        resp = requests.get(f"{self.MAIN_URL}forecast.json?key={self.API_KEY}&q={city}&days={days}")
        return resp.json()
