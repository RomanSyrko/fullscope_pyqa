import pytest
from modules.ui.page_objects.github_sign_in_page import SignInPage


@pytest.mark.ui
def test_ui_github_page_object():
    # Create an instance of the SignInPage page object
    sign_in_page = SignInPage()

    # Navigate to the GitHub sign-in page
    sign_in_page.go_to()

    # Attempt to log in with incorrect credentials
    sign_in_page.try_login('page_object@gmail.com', 'wrongPassword')

    # Assert that the page title is as expected after a failed login
    assert sign_in_page.check_title('Sign in to GitHub · GitHub')

    # Close the browser
    sign_in_page.close()
