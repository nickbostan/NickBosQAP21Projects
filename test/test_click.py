from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = "https://courses.ultimateqa.com/users/sign_in"
url1 = "https://try.discourse.org/"


def test_mouse_click(driver_Chrome):
    driver_Chrome.get(url1)
    current_url = driver_Chrome.current_url
    element = driver_Chrome.find_element(By.CSS_SELECTOR, '[type="button"]')
    actions = ActionChains(driver_Chrome)
    actions.move_to_element(element).click().perform()
    WebDriverWait(driver_Chrome, 10).until(EC.url_changes(current_url))
    assert driver_Chrome.current_url != current_url


def test_kboard_click(driver_Chrome):
    driver_Chrome.get(url1)
    orig_url = driver_Chrome.current_url
    element = driver_Chrome.find_element(By.CSS_SELECTOR, '[type="button"]')
    actions = ActionChains(driver_Chrome)
    actions.move_to_element(element).click().pause(0.5).send_keys(Keys.ENTER).perform()
    WebDriverWait(driver_Chrome, 10).until(EC.url_changes(orig_url))
    assert driver_Chrome.current_url != orig_url


def test_click(driver_Chrome):
    driver_Chrome.get(url)
    current_url = driver_Chrome.current_url
    element = driver_Chrome.find_element(By.CLASS_NAME, "form__forgot-password")
    element.click()
    WebDriverWait(driver_Chrome, 10).until(EC.url_changes(current_url))
    assert driver_Chrome.current_url != current_url


def teset_JSclick(driver_Chrome):
    driver_Chrome.get(url)
    element = driver_Chrome.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    driver_Chrome.execute_script("arguments[0].click();", element)
    is_checked = driver_Chrome.execute_script("return arguments[0].checked;", element)
    assert not is_checked
