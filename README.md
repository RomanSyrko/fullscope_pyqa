# Fullscope PyQA Project
This repository contains my first framework for automated testing using Python. The framework is designed to facilitate both API and UI testing.

## Overview
The Fullscope PyQA Project is a testing framework built with Python to help Quality Assurance (QA) engineers automate both API and UI testing. This framework leverages popular libraries and tools to provide a comprehensive solution for test automation.
This project is a comprehensive testing suite for various aspects of a web application, including API endpoints, database operations, and user interface interactions. It utilizes Python as the primary programming language, along with pytest for test execution and Selenium for UI automation.

## Features
- **API Testing**: The project includes testing of APIs using the requests library to interact with the API endpoints and validate the responses.
- **Database Testing**: Database testing is performed using Python libraries such as pytest and SQL connectors to ensure data integrity and accuracy.
- **UI Testing**: UI testing is conducted using Selenium WebDriver to automate interactions with web applications and validate their behavior.

## Project Structure
    fullscope_pyqa/
    ├── config/
    │   └── config.py
    ├── modules/
    │   ├── api/
    │   │   └── clients/
    │   │       ├── github.py 
    │   │       ├── jsonplaceholder.py 
    │   │       ├── rozetka.py 
    │   │       ├── tmdb_api.py 
    │   │       └── weather_api.py
    │   ├── common/
    │   │   └── database.py
    │   └── ui/
    │       └── page_object/ 
    │           ├── constants/
    │           │   ├── novaposhta_constants.py
    │           │   └── rozetka_constants.py
    │           ├── base_page.py
    │           ├── github_sign_in_page.py
    │           ├── novaposhta_search_track_number.py
    │           └── rozetka_search.py 
    ├── tests/
    │   ├── api/
    │   │   ├── test_api.py
    │   │   ├── test_fixtures.py 
    │   │   ├── test_github_api.py 
    │   │   ├── test_http.py 
    │   │   ├── test_jsonplaceholder.py
    │   │   ├── test_rozetka.py
    │   │   ├── test_tmdb.py
    │   │   └── test_weather_api.py
    │   ├── database/
    │   │   └── test_database.py
    │   └── ui/
    │       ├── test_ui_github.py
    │       ├── test_ui_github_page_object.py
    │       ├── test_ui_novaposhta.py
    │       └── test_ui_rozetka.py
    ├── .gitignore
    ├── README.md
    ├── chromedriver
    ├── conftest.py
    ├── pytest.ini
    └── qa_auto_tests.db

## Installation
To use this framework, you need to have **Python 3.12.1** or higher installed.

## Running Tests
The framework uses `pytest` for running tests. Below are examples of how to run different types of tests.

### Run All Tests
To run all tests, execute the following command:
  ```commandline
  pytest
  ```

### Run Tests by Marker
You can run tests by specific markers. Here are some examples:

- #### Run API Tests:
  ```commandline
  pytest -m api
  ```

- #### Run JSONPlaceholder API Tests:
  ```commandline
  pytest -m jsonplaceholder
  ```

- #### Run Weather API Tests:
  ```commandline
  pytest -m weather_api
  ```

- #### Run TMDb API Tests:
  ```commandline
  pytest -m tmdb_api
  ```

- #### Run Database Tests:
  ```commandline
  pytest -m database
  ```

### Running UI Tests

To run the UI tests in this framework, you need to have `pytest` and `selenium` installed. You can install them via pip if you haven't already:

```commandline
pip install pytest selenium
```

#### WebDriver Setup
Make sure you have the appropriate WebDriver for your browser installed and accessible in your system's PATH. For example, if you're using Chrome, you can download the ChromeDriver from [here](https://getwebdriver.com/chromedriver).

### Running UI Tests by Markers

- #### Run GitHub UI Tests:
  ```commandline
  pytest -m ui_github
  ```

- #### Run Rozetka UI Tests:
  ```commandline
  pytest -m ui_rozetka
  pytest -m ui_rozetka_basket
  ```


- #### Run Novaposhta UI Tests:
  ```commandline
  pytest -m ui_novaposhta
  ```


## Notes
Ensure the `chromedriver` executable is in your PATH or specify its location in your test setup if you are running UI tests using Selenium.
Update the API keys and other sensitive information as needed.
