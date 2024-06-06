import pytest


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
