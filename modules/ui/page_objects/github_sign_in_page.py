from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = 'https://github.com/login'

    def __init__(self):
        # Call the constructor of the parent class in which to initialize the driver for communication with the browser
        super().__init__()

    def go_to(self):
        # Open the sign-in page by navigating to the specified URL.
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # Attempt to log in to the page with the given username and password.

        # Find the username or email input field.
        login_field = self.driver.find_element(By.ID, 'login_field')

        # Enter the provided username or email.
        login_field.send_keys(username)

        # Find the password input field.
        password_field = self.driver.find_element(By.ID, 'password')

        # Enter the provided password.
        password_field.send_keys(password)

        # Find the commit button (login button).
        btn = self.driver.find_element(By.NAME, 'commit')

        # Emulate a click with the left mouse button to attempt login.
        btn.click()

    def check_title(self, expected_title):
        # Check if the page title matches the expected title.
        return self.driver.title == expected_title
