import pytest
import requests
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://candymapper.com/"
URL2 = "https://candymapperr2.com/"
TIME = 10


@pytest.fixture
def site_response():
    response = requests.get(URL, timeout=TIME)
    return response


def test_candy_status(site_response):
    assert site_response.status_code == 200


def test_candy_loading_speed(site_response):
    assert site_response.elapsed.total_seconds() < 5


def test_env_prod(driver):
    driver.get(URL)
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "popup-widget307423-close-icon"))
        ).click()
    except NoSuchElementException:
        print("Popup not found or already closed")

    expected_title = "CandyMapper.Com"
    actual_title = driver.title
    assert expected_title in actual_title

    expected_url = URL
    actual_url = driver.current_url
    assert actual_url == expected_url


def pytest_sessionstart(session):
    pytest.env = "test"


@pytest.fixture
def site2_response():
    response = requests.get(URL2, timeout=TIME)
    return response


def test_site2_status(site2_response):
    assert site2_response.status_code == 200


def test_site2_loading(site2_response):
    assert site2_response.elapsed.total_seconds() < 5


def test_env_test(driver):
    driver.get(URL2)
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "popup-widget7437-close-icon"))
        ).click()
    except NoSuchElementException:
        print("Popup not found or already closed")

    expected_title = "CandyMapperR2"
    actual_title = driver.title
    assert expected_title in actual_title

    expected_url = URL2
    actual_url = driver.current_url
    assert actual_url == expected_url
