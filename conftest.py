import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture
def driver():
    opts = ChromeOptions()
    opts.headless = True
    opts.add_argument("--window-size=1080,1680")
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
