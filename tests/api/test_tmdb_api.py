import pytest  # Importing the pytest library for testing


@pytest.mark.tmdb_api
def test_tmdb_api(tmdb_api):
    """
    Test case to verify the account details from TMDB API.

    This test retrieves account details for a specific account ID
    and verifies the ID and username in the response.

    :param:
    tmdb_api (TMDBClient): The TMDB API client fixture.

    Assertions:
    - The account ID matches the expected value.
    - The username matches the expected value.
    """
    # Get account details for the given account ID
    resp = tmdb_api.get_account_details('12557371')

    # Verify the account ID
    assert resp['id'] == 12557371
    # Verify the username
    assert resp['username'] == 'Sirko'


@pytest.mark.tmdb_api
def test_tmdb_api_error(tmdb_api):
    """
    Test case to verify the client error response from TMDB API.

    This test simulates a client error by making a request to an invalid endpoint
    and verifies that the response status code is 404.

    :param:
    tmdb_api (TMDBClient): The TMDB API client fixture.

    Assertions:
    - The status code of the response is 404.
    """
    # Simulate a client error
    resp = tmdb_api.get_client_error()

    # Verify the status code is 404
    assert resp == 404


@pytest.mark.tmdb_api
def test_get_popular_movies(tmdb_api):
    """
    Test case to verify the popular movies from TMDB API.

    This test retrieves the list of popular movies and verifies
    that the response is not empty and the first movie's title matches
    the expected value.

    :param:
    tmdb_api (TMDBClient): The TMDB API client fixture.

    Assertions:
    - The response contains at least one movie.
    - The original title of the first movie matches the expected value.
    """
    # Get popular movies
    resp = tmdb_api.get_popular_movies()

    # Verify the response is not empty
    assert len(resp) > 0
    # Verify the title of the first movie
    assert resp['results'][0]['original_title'] == 'Kingdom of the Planet of the Apes'


@pytest.mark.tmdb_api
def test_get_movie_details(tmdb_api):
    """
    Test case to verify the movie details from TMDB API.

    This test retrieves the details of a specific movie by its ID and verifies
    various attributes of the movie such as title, status, overview, production
    company, and production country.

    :param:
    tmdb_api (TMDBClient): The TMDB API client fixture.

    Assertions:
    - The original title of the movie matches the expected value.
    - The status of the movie is 'Released'.
    - The overview is not empty.
    - The first production company's name matches the expected value.
    - The first production country's name matches the expected value.
    """
    # Get movie details for the given movie ID
    resp = tmdb_api.get_movie_details('653346')

    # Verify the original title of the movie
    assert resp['original_title'] == 'Kingdom of the Planet of the Apes'
    # Verify the status of the movie
    assert resp['status'] == 'Released'
    # Verify the overview is not empty
    assert resp['overview'] != ''
    # Verify the name of the first production company
    assert resp['production_companies'][0]['name'] == '20th Century Studios'
    # Verify the name of the first production country
    assert resp['production_countries'][0]['name'] == 'United States of America'
