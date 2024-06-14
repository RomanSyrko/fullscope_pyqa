import requests


class GitHub:
    """
    A simple GitHub API client to interact with GitHub's user endpoint.
    """
    def get_user_from_github(self, username):
        """
        Retrieve user information from GitHub.

        This method sends a GET request to the GitHub API to fetch user data
        based on the provided username.

        Parameters:
        username (str): The GitHub username to look up.

        Returns:
        dict: A dictionary containing the user's data from GitHub.
        """
        r = requests.get(f"https://api.github.com/users/{username}")  # Send a GET request to the GitHub API
        body = r.json()  # Parse the response body as JSON
        return body  # Return the parsed JSON data


    def search_repo(self, name):
        r = requests.get(f"https://api.github.com/search/repositories", f"q={name}")
        body = r.json()
        return body
