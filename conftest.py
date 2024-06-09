import pytest
from modules.api.clients.github import GitHub
from modules.api.clients.rozetka import Rozetka
from modules.api.clients.weather_api import WeatherApi
from modules.common.database import Database
from modules.api.clients.jsonplaceholder import JSONPlaceHolder

"""
This file used to configure the test environment, shared fixtures, and to organize the test structure.
"""


class User:
    """
    A simple User class to represent user attributes and provide methods
    for creating and removing user data.
    """

    def __init__(self):
        # Initialize the user with no name and second name
        self.name = None
        self.second_name = None

    def create(self):
        """
        Method to set the user's name and second name.
        """
        self.name = "Roman"
        self.second_name = "Sirko"

    def remove(self):
        """
        Method to clear the user's name and second name.
        """
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    """ A pytest fixture to create and provide a User instance with initialized data. """
    user = User()  # Create a User instance and provide it to the test
    user.create()  # Set up the user data

    # Everything written before this yield will be executed before the test
    yield user
    # Everything after it will be executed after the test

    user.remove()  # Clean up the user data after the test


@pytest.fixture
def github_api():
    """
    A pytest fixture to create and provide a GitHub instance with initialized data.
    And using this fixture in the test_github_api.py.
    """
    api = GitHub()  # Create a User instance and provide it to the test
    yield api


@pytest.fixture
def db_fixture():
    """
    Fixture to set up a database connection for testing
    And using this fixture in the test_database.py.
    """
    db = Database()
    yield db


@pytest.fixture
def json_placeholder():
    """
    Using this fixture in the test_jsonplaceholder.py.
    """
    json_placeholder = JSONPlaceHolder()
    yield json_placeholder


@pytest.fixture
def rozetka_api():
    """
    Using this fixture in the https://api-seller.rozetka.com.ua/
    """
    rozetka = Rozetka()
    yield rozetka


@pytest.fixture
def weather_api():
    """
    Using this fixture in the https://api.weatherapi.com/v1/
    """
    weather = WeatherApi()
    yield weather
