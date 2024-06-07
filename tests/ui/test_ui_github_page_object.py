import pytest
from modules.ui.page_objects.github_sign_in_page import SignInPage


@pytest.mark.ui
def test_ui_github_page_object():
    sign_in_page = SignInPage()

    sign_in_page.go_to()

    sign_in_page.try_login('page_object@gmail.com', 'wrongPasword')

    assert sign_in_page.check_title('Sign in to GitHub · GitHub')

    sign_in_page.close()
