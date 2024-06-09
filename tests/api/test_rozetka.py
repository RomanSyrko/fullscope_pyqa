import pytest


@pytest.mark.rozetka
def test_rozetka(rozetka_api):
    """
    Test the Rozetka API for status code and unauthorized access error.

    This test checks if the Rozetka API returns a 200 status code and verifies
    that the response contains an error message indicating unauthorized access.

    Parameters:
    rozetka_api (Rozetka): An instance of the Rozetka class for API interaction.
    """

    status_code = rozetka_api.get_status_code()  # Getting the status code from the Rozetka API
    assert status_code == 200  # Asserting that the status code is 200 (OK)

    resp = rozetka_api.find_products()  # Fetching the products from the Rozetka API
    # Asserting that the error message indicates unauthorized access
    assert resp['errors']['description'] == 'Спроба неавторизованого доступу до методів, які вимагають авторизації'