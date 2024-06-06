import pytest
# import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.ui
def test_check_incorrect_username():
    # Alternative creation of an object to control the browser
    # file_place = '/Users/romansyrko/PycharmProjects/my_first_framework/'
    # file = 'chromedriver'
    # driver = webdriver.Chrome(service=Service(file_place + file))

    # Creating an object to control the browser using webdriver_manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get('https://github.com/login')  # Open the page

    login_field = driver.find_element(By.ID, 'login_field')  # Find the username or email input field.
    login_field.send_keys('romansyrko@gmail.com')  # Enter an incorrect username or email

    password = driver.find_element(By.ID, 'password')  # Find the password input field
    password.send_keys('password')  # Enter an incorrect password

    btn = driver.find_element(By.NAME, 'commit')  # Find the commit button (login button)
    btn.click()  # Emulate a click with the left mouse button to attempt login

    check = driver.find_element(By.ID, 'js-flash-container')  # Find the error message container

    assert check is not None  # Check that the error message is present

    assert driver.title == 'Sign in to GitHub · GitHub'  # Verify that the page title is as expected
    # time.sleep(3)  # Optionally pause to observe the result

    driver.close()  # Close the browser
