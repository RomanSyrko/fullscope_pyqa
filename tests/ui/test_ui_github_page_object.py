import pytest


@pytest.mark.ui_github
def test_ui_github_page_object(github_sign_in_page):
    # Navigate to the GitHub sign-in page
    github_sign_in_page.go_to()

    # Attempt to log in with incorrect credentials
    github_sign_in_page.try_login('page_object@gmail.com', 'wrongPassword')

    # Assert that the page title is as expected after a failed login
    assert github_sign_in_page.check_title('Sign in to GitHub · GitHub')
