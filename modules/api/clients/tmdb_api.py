import requests  # Importing the requests library to make HTTP requests


class TMDBClient:
    """
    A client to interact with The Movie Database (TMDB) API.
    """
    MAIN_URL = 'https://api.themoviedb.org/3/'  # The base URL for the TMDB API

    # Headers required for authorization and to accept JSON responses
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwM2U1Yjg2NDkxMTYxY2E2NzEwN2NkMjNlNTY5NTUzZiIsInN1YiI6IjYyOTg1ZDcyNTUwN2U5MTQ5Mzg5MGQ1YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.18e0EtimeGJ7fgwVvtDRKrCzunr2LnFizciY9QzLhOY"
    }

    def get_account_details(self, id):
        """
        Get the details of an account by its ID.

        :param:
        id (str): The ID of the account.

        :returns:
        dict: A dictionary containing the account details.
        """
        # Send a GET request to the account details endpoint
        resp = requests.get(f"{self.MAIN_URL}account/{id}", headers=self.headers)
        return resp.json()  # Return the response JSON

    def get_client_error(self):
        """
        Simulate a client error by making a request to an invalid endpoint.

        :returns:
        int: The HTTP status code of the response.
        """
        # Send a GET request to an invalid endpoint to generate a client error
        resp = requests.get(f"{self.MAIN_URL}status", headers=self.headers)
        return resp.status_code  # Return the status code of the response

    def get_popular_movies(self):
        """
        Get a list of popular movies.

        :returns:
        dict: A dictionary containing the list of popular movies.
        """
        # Send a GET request to the popular movies endpoint
        resp = requests.get(f"{self.MAIN_URL}movie/popular?language=en-US&page=1", headers=self.headers)
        return resp.json()  # Return the response JSON

    def get_movie_details(self, movie_id):
        """
        Get the details of a movie by its ID.

        :param:
        movie_id (int): The ID of the movie.

        :returns:
        dict: A dictionary containing the movie details.
        """
        # Send a GET request to the movie details endpoint
        data = requests.get(f"{self.MAIN_URL}movie/{movie_id}?language=en-US", headers=self.headers)
        return data.json()  # Return the response JSON
