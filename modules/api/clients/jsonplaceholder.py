import requests


class JSONPlaceHolder:
    MAIN_URL = 'https://jsonplaceholder.typicode.com/'

    def get_status_code(self):
        """
        Get the status code of the response from the main URL.

        Returns:
        int: The status code of the response.
        """
        r = requests.get(self.MAIN_URL)
        return r.status_code

    def get_all_users(self):
        """
        Get all users from the JSONPlaceholder API.

        Returns:
        list: A list of user data retrieved from the API.
        """
        r = requests.get(JSONPlaceHolder.MAIN_URL + 'users')
        return r.json()

    def get_headers(self):
        """
        Get the headers from the 'users' endpoint of the JSONPlaceholder API.

        Returns:
        dict: A dictionary containing the headers of the response.
        """
        r = requests.get(JSONPlaceHolder.MAIN_URL + 'users')
        return r.headers
