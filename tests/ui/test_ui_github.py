import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    """
    Alternative creation of an object to control the browser
        file_place = '/Users/romansyrko/PycharmProjects/my_first_framework/'
        file = 'chromedriver'
        driver = webdriver.Chrome(service=Service(file_place + file))
    """

    # Creating an object to control the browser using webdriver_manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open the page
    driver.get('https://github.com/login')

    # Find the username or email input field.
    login_field = driver.find_element(By.ID, 'login_field')

    # Enter an incorrect username or email
    login_field.send_keys('romansyrko@gmail.com')

    # Find the password input field
    password = driver.find_element(By.ID, 'password')

    # Enter an incorrect password
    password.send_keys('password')

    # Find the commit button (login button) and Emulate a click with the left mouse button
    driver.find_element(By.NAME, 'commit').click()

    # Find the error message container
    check = driver.find_element(By.ID, 'js-flash-container')

    # Check that the error message is present
    assert check is not None

    # Verify that the page title is as expected
    assert driver.title == 'Sign in to GitHub · GitHub'

    # Close the browser
    driver.close()
