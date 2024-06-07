from selenium.webdriver import Keys
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from modules.ui.page_objects.constants.rozetka_constants import CheckBasketConstants, SearchProductConstants


class SearchProduct(BasePage):
    """
    Page Object for searching products on Rozetka website.
    """

    def __init__(self):
        super().__init__()

    def go_to(self):
        # Opens the Rozetka search page.
        self.driver.get(SearchProductConstants.URL)

    def try_to_find(self, find_elem):
        # Enters the search query and presses Enter.
        get_input = self.driver.find_element(By.XPATH, SearchProductConstants.INPUT_XPATH)
        get_input.send_keys(find_elem)
        get_input.send_keys(Keys.RETURN)

    def check_title(self, expected_title):
        # Checks if the title of the current page matches the expected title.
        return self.driver.title == expected_title


class CheckBasket(BasePage):
    """
    Page Object for checking the shopping basket on Rozetka website.
    """

    def __init__(self):
        super().__init__()

    def go_to(self):
        # Opens the Rozetka shopping basket page.
        self.driver.get(CheckBasketConstants.URL)

    def add_product(self):
        # Adds a product to the shopping basket.
        self.driver.find_element(By.XPATH, CheckBasketConstants.BUTTON_XPATH).click()

    def open_basket(self):
        # Opens the shopping basket.
        self.driver.find_element(By.XPATH, CheckBasketConstants.BASKET_XPATH).click()

    def delete_product(self):
        # Deletes a product from the shopping basket.
        self.driver.find_element(By.XPATH, CheckBasketConstants.BASKET_BTN_XPATH).click()
        self.driver.find_element(By.XPATH, CheckBasketConstants.BASKET_DELETE_BTN_XPATH).click()

    def check_basket_not_contain(self, expected_message):
        # Checks if the shopping basket does not contain the specified message.
        check_message = self.driver.find_element(By.XPATH, CheckBasketConstants.CHECK_IN_BASKET_MSG_XPATH)
        return check_message == expected_message

    def check_basket_contain(self):
        # Checks if the shopping basket contains any items.
        return self.driver.find_element(By.XPATH, CheckBasketConstants.CHECK_BASKET_XPATH)
