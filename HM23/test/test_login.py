import pytest

from HM23.pageobj_orange.dashboard_page import DashboardPage
from HM23.pageobj_orange.login_page import LoginPage


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def dashboard_page(driver):
    return DashboardPage(driver)


@pytest.fixture()
def open_page(login_page):
    login_page.open_page()


@pytest.mark.only
def test_check_all_elements(login_page, open_page):
    login_page.check_that_page_opened()


@pytest.mark.smoke
def test_positive_login(login_page, dashboard_page, open_page):
    login_page.login("Admin", "admin123")
    dashboard_page.check_that_page_opened()


def test_logout(login_page, dashboard_page, open_page):
    login_page.login("Admin", "admin123")
    dashboard_page.check_that_page_opened()
    dashboard_page.click_logout()
    login_page.check_that_page_opened()


@pytest.mark.parametrize(
    "user, password, expect",
    [
        ("incorrectUser", "admin123", "Invalid credentials"),
        ("Admin", "incorrectPassword", "Invalid credentials"),
    ],
)
def test_negative_username(login_page, open_page, user, password, expect):
    login_page.login(user, password)
    login_page.check_that_error_is_visible(expect)


@pytest.mark.parametrize(
    "user, password, expect",
    [
        ("", "admin123", "Required"),
        ("Admin", "", "Required"),
    ],
)
def test_negative_empty_fields(login_page, open_page, user, password, expect):
    login_page.login(user, password)
    login_page.check_that_empty_error_is_visible(expect)


@pytest.mark.parametrize(
    "link_element,expected_url",
    [
        ("LINKEDIN_LINK", "linkedin.com"),
        ("FACEBOOK_LINK", "facebook.com"),
        ("TWITTER_LINK", "x.com"),
        ("YOUTUBE_LINK", "youtube.com"),
        ("SITE_LINK", "orangehrm.com"),
    ],
)
def test_social_links(login_page, link_element, expected_url, open_page, driver):
    original_url = driver.current_url
    original_window = driver.current_window_handle
    social_link = getattr(login_page, link_element)
    social_link.click()
    new_url = login_page.switch_to_new_window(expected_windows=2)
    assert expected_url in new_url, f"URL {new_url} не содержит {expected_url}"
    driver.close()
    driver.switch_to.window(original_window)
    assert original_url == login_page.driver.current_url
