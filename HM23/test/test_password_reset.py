import pytest
import pytest_check as check
from selenium.webdriver.common.by import By

from HM23.pageobj_orange.password_reset_page import PasswordPage
from HM23.urls import URLS


@pytest.fixture()
def password_page(driver):
    return PasswordPage(driver)


@pytest.fixture()
def open_page(password_page):
    password_page.open_page()


@pytest.mark.smoke
def test_check_all_elements(password_page, open_page, driver):
    password_page.check_that_page_opened()
    assert password_page.driver.current_url == URLS.PASSWORD


def test_cancel(password_page, open_page, driver):
    password_page.CANCEL_BUTTON.click()
    assert password_page.driver.current_url == URLS.LOGIN


def test_reset(password_page, open_page, driver):
    password_page.reset_password("Admin")
    success_message = password_page.driver.find_element(
        By.CSS_SELECTOR, "h6.orangehrm-forgot-password-title"
    )
    check.is_in("sent successfully", success_message.text)
    check.is_true(success_message.is_displayed())
    check.is_in("auth/sendPasswordReset", password_page.driver.current_url)


def test_negative_empty_fields(password_page, open_page):
    password_page.reset_password("")
    password_page.check_that_empty_error_is_visible("Required")


@pytest.mark.parametrize(
    "length,expected",
    [
        (50, "accept"),
        (100, "accept"),
        (255, "accept"),
        (256, "cut off"),
        (500, "cut off"),
        (1000, "cut off"),
    ],
)
def test_password_lengths(password_page, open_page, length, expected):
    password_page.INPUT_USER_NAME.fill("x" * length)

    actual_value = password_page.INPUT_USER_NAME.get_attribute("value")
    actual_length = len(actual_value)

    if expected == "accept":
        assert actual_length == length, f"Expected {length}, granted {actual_length}"
    elif expected == "cut off":
        assert (
            actual_length <= length
        ), f"Entered much more then possible: {actual_length}"
