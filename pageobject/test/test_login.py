import pytest

from pageobject.login_page import LoginPage
from pageobject.success_page import SuccessPage


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def success_page(driver):
    return SuccessPage(driver)


@pytest.mark.only
def test_check_all_elements(login_page):
    login_page.open("https://practicetestautomation.com/practice-test-login/")

    login_page.check_that_page_opened(
        title="Test login",
        description="This is a simple Login page. "
        "Students can use this page to practice writing simple positive and negative LogIn tests. "
        "Login functionality is something that most of the test automation engineers need to automate.",
    )


@pytest.mark.smoke
def test_positive_login(login_page, success_page):
    login_page.open("https://practicetestautomation.com/practice-test-login/")

    login_page.login("student", "Password123")
    success_page.check_that_page_opened(
        "Logged In Successfully", "Congratulations student. You successfully logged in!"
    )


@pytest.mark.smoke
@pytest.mark.parametrize(
    "user, password, expect",
    [
        ("incorrectUser", "Password123", "Your username is invalid!"),
        ("student", "incorrectPassword", "Your password is invalid!"),
    ],
)
def test_negative_username(login_page, user, password, expect):
    login_page.open("https://practicetestautomation.com/practice-test-login/")

    login_page.login(user, password)
    login_page.check_that_error_is_visible(expect)


@pytest.mark.only
def test_logout(success_page, login_page):
    login_page.open("https://practicetestautomation.com/practice-test-login/")
    login_page.login("student", "Password123")
    success_page.check_that_page_opened(
        "Logged In Successfully", "Congratulations student. You successfully logged in!"
    )
    success_page.logout()
    login_page.check_that_page_opened(
        title="Test login",
        description="This is a simple Login page. "
        "Students can use this page to practice writing simple positive and negative LogIn tests. "
        "Login functionality is something that most of the test automation engineers need to automate.",
    )
