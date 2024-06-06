import pytest
from modules.api.clients.github import GitHub

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
