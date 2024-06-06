from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self):
        """
        Call the constructor of the parent class in which to initialize the driver for communication with the browser
        """
        super().__init__()

    def go_to(self):
        """
        Open the sign-in page by navigating to the specified URL.
        """
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        """
        Attempt to log in to the page with the given username and password.

        :param username: The username or email to be entered into the login field.
        :param password: The password to be entered into the password field.
        """
        login_field = self.driver.find_element(By.ID, 'login_field')  # Find the username or email input field.
        login_field.send_keys(username)  # Enter the provided username or email.

        password_field = self.driver.find_element(By.ID, 'password')  # Find the password input field.
        password_field.send_keys(password)  # Enter the provided password.

        btn = self.driver.find_element(By.NAME, 'commit')  # Find the commit button (login button).
        btn.click()  # Emulate a click with the left mouse button to attempt login.

    def check_title(self, expected_title):
        """
        Check if the page title matches the expected title.

        :param expected_title: The expected title of the page.
        :return: True if the page title matches the expected title, False otherwise.
        """
        return self.driver.title == expected_title
