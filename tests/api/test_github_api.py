import pytest


@pytest.mark.api
def test_user_exists(github_api):
    """
    Test to check if a specific GitHub user exists.

    This test uses the GitHub API client to get user information for the user 'defunkt'.
    It asserts that the login name in the response is 'defunkt'.
    """
    r = github_api.get_user_from_github('defunkt')  # Get user information for 'defunkt'

    # Perform assertions
    assert r['login'] == "defunkt"  # Assert that the login name is 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    """
    Test to check if a non-existent GitHub user returns the correct error message.

    This test uses the GitHub API client to get user information for a non-existent user.
    It asserts that the message in the response is 'Not Found'.
    """
    r = github_api.get_user_from_github('notexistuserrlfkdofd')  # Get user information for a non-existent user

    # Perform assertions
    assert r['message'] == "Not Found"  # Assert that the response message is 'Not Found'


@pytest.mark.api
def test_repo_exists(github_api):
    """
    Test to check if a specific GitHub repository exists.

    This test uses the GitHub API client to search for the repository 'fullscope_pyqa'.
    It asserts that the total count of search results is 1, and that the name and owner ID
    of the repository match the expected values.
    """
    r = github_api.search_repo('fullscope_pyqa')  # Search for the repository 'fullscope_pyqa'

    # Perform assertions
    assert r['total_count'] == 1  # Assert that the total count of search results is 1
    assert r['items'][0]['name'] == 'fullscope_pyqa'  # Assert that the name of the repository is 'fullscope_pyqa'
    assert 'fullscope_pyqa' in r['items'][0]['name']  # Assert that 'fullscope_pyqa' is in the repository name
    assert r['items'][0]['owner']['id'] == 97445039  # Assert that the repository owner's ID is 97445039


@pytest.mark.api
def test_repo_not_exists(github_api):
    """
    Test to check if a specific GitHub repository does not exist.

    This test uses the GitHub API client to search for a non-existent repository 'fullscope_pyqa_not_exist'.
    It asserts that the total count of search results is 0 and that incomplete results flag is False.
    """
    r = github_api.search_repo('fullscope_pyqa_not_exist')  # Search for a non-existent repository

    # Perform assertions
    assert r['total_count'] == 0  # Assert that the total count of search results is 0
    assert r['incomplete_results'] is False  # Assert that incomplete results flag is False


@pytest.mark.api
def test_repo_with_single_character(github_api):
    """
    Test to search for a GitHub repository with a single character.

    This test uses the GitHub API client to search for repositories with a single character 's'.
    It asserts that the total count of search results is not None.
    """
    r = github_api.search_repo('s')  # Search for repositories with a single character 's'

    # Perform assertion
    assert r['total_count'] is not None  # Assert that the total count of search results is not None
