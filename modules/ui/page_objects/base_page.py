import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    def __init__(self) -> None:
        """
        Initialize the BasePage by setting up the Chrome WebDriver using webdriver_manager.
        Set up the Chrome WebDriver using webdriver_manager to automatically handle driver installation
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def close(self):
        """ Close the browser """
        self.driver.close()
