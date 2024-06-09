import pytest


@pytest.mark.change
def test_remove_name(user):
    """
    Test to ensure the name can be removed.

    This test modifies the user's name attribute to an empty string
    and checks if the change is correctly applied.
    """
    user.name = ""  # Remove the user's name
    assert user.name == ""  # Assert that the name is now an empty string
    assert user.name is not True


@pytest.mark.check
def test_name(user):
    """
    Test to ensure the initial name is set correctly.

    This test checks if the user's initial name is 'Roman'.
    """
    assert user.name == "Roman"  # Assert that the initial name is 'Roman'
    assert user.name != ''


@pytest.mark.check
def test_second_name(user):
    """
    Test to ensure the initial second name is set correctly.

    This test checks if the user's initial second name is 'Sirko'.
    """
    assert user.second_name == "Sirko"  # Assert that the initial second name is 'Sirko'
    assert user.second_name != ''
