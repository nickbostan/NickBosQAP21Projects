import pytest

from HM23.pageobj_orange.dashboard_page import DashboardPage
from HM23.pageobj_orange.login_page import LoginPage
from HM23.urls import URLS


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def dashboard_page(driver):
    return DashboardPage(driver)


@pytest.fixture()
def open_page(login_page):
    login_page.open_page()
    login_page.login("Admin", "admin123")


@pytest.mark.smoke
def test_dashboard_page(dashboard_page, open_page, driver):
    dashboard_page.check_that_page_opened()
    assert dashboard_page.driver.current_url == URLS.DASHBOARD


def test_config(dashboard_page, open_page):
    dashboard_page.CONFIG_EMPL_LEAVE.click()
    dashboard_page.SHOW_BUTTON.click()
    dashboard_page.SAVE_BUTTON.click()
    dashboard_page.CONFIG_EMPL_LEAVE.click()
    assert not dashboard_page.SHOW_BUTTON.is_checked()
    dashboard_page.CANCEL_BUTTON.click()
