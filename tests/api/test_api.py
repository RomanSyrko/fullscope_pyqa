import pytest


class User:
    """
    A simple User class to represent user attributes.
    """

    def __init__(self):
        # Initialize the user with a name and a second name
        self.name = 'Roman'
        self.second_name = 'Sirko'


@pytest.fixture
def user():
    """
    A pytest fixture to create and provide a User instance.
    """
    # Create a User instance and provide it to the test
    yield User()


@pytest.mark.change
def test_remove_name(user):
    """
    Test to ensure the name can be removed.

    This test modifies the user's name attribute to an empty string
    and checks if the change is correctly applied.
    """
    user.name = ""  # Remove the user's name
    assert user.name == ""  # Assert that the name is now an empty string


@pytest.mark.check
def test_name(user):
    """
    Test to ensure the initial name is set correctly.

    This test checks if the user's initial name is 'Roman'.
    """
    assert user.name == "Roman"  # Assert that the initial name is 'Roman'


@pytest.mark.check
def test_second_name(user):
    """
    Test to ensure the initial second name is set correctly.

    This test checks if the user's initial second name is 'Sirko'.
    """
    assert user.second_name == "Sirko"  # Assert that the initial second name is 'Sirko'
