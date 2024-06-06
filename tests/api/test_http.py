import pytest
import requests


@pytest.mark.http
def test_first_http_request():
    """
    Test to perform a simple HTTP GET request to the GitHub Zen API.

    This test sends a GET request to the endpoint and asserts that the response
    is not None and the status code is 200.
    """
    r = requests.get('https://api.github.com/zen')  # Send a GET request

    # Perform assertions
    assert r is not None  # Assert that the response is not None
    assert r.status_code == 200  # Assert that the status code is 200


@pytest.mark.http
def test_second_http_response():
    """
    Test to perform an HTTP GET request to retrieve user information from GitHub.

    This test sends a GET request to the endpoint and asserts the status code is 200.
    It also checks that the user's name and the server header are correct.
    """
    r = requests.get('https://api.github.com/users/defunkt')  # Send a GET request
    body = r.json()  # Parse the response body as JSON
    headers = r.headers  # Get the response headers

    # Perform assertions
    assert r.status_code == 200  # Assert that the status code is 200
    assert body['name'] == 'Chris Wanstrath'  # Assert that the user's name is 'Chris Wanstrath'
    assert headers['Server'] == 'GitHub.com'  # Assert that the server header is 'GitHub.com'


@pytest.mark.http
def test_third_http_response():
    """
    Test to perform an HTTP GET request to retrieve information for a non-existent GitHub user.

    This test sends a GET request to the endpoint and asserts that the status code is 404.
    """
    r = requests.get('https://api.github.com/users/notasuser94325423')  # Send a GET request

    # Perform assertions
    assert r.status_code == 404  # Assert that the status code is 404 (user not found)
