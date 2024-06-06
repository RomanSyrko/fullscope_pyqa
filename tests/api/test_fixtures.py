import pytest


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
    """
    A pytest fixture to create and provide a User instance with initialized data.
    """
    user = User()
    user.create()  # Set up the user data

    # Everything written before this yield will be executed before the test
    yield user
    # Everything after it will be executed after the test

    user.remove()  # Clean up the user data after the test


@pytest.mark.check
def test_change_name(user):
    """
    Test to ensure the user's name is correctly set.

    This test checks if the user's name is 'Roman' after creation.
    """
    assert user.name == "Roman"  # Assert that the user's name is 'Roman'


@pytest.mark.check
def test_change_second_name(user):
    """
    Test to ensure the user's second name is correctly set.

    This test checks if the user's second name is 'Sirko' after creation.
    """
    assert user.second_name == "Sirko"  # Assert that the user's second name is 'Sirko'
