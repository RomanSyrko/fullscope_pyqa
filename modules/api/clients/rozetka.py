import requests


class Rozetka:
    URL = 'https://api-seller.rozetka.com.ua/items/search'

    def get_status_code(self):
        """
        Get the HTTP status code from the Rozetka API.
        """
        response = requests.get(self.URL)
        return response.status_code

    def find_products(self):
        """
        Retrieve products from the Rozetka API

        This method sends a GET request to the Rozetka API and returns the JSON response containing product data

        :return:
        dict: A dictionary containing the product data from the Rozetka API.
        """
        response = requests.get(self.URL)
        return response.json()
