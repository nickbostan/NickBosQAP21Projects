from selenium.webdriver.common.by import By

url = "https://courses.ultimateqa.com/users/sign_in"


def test_input_mail(driver_Chrome):
    driver_Chrome.get(url)
    element = driver_Chrome.find_element(By.ID, "user[email]")
    element.send_keys("Abracadabra@gmail.com")
    assert not element.get_attribute("value") == ""


def test_input_pass(driver_Chrome):
    driver_Chrome.get(url)
    element = driver_Chrome.find_element(By.NAME, "user[password]")
    element.send_keys("1122334455")
    assert not element.get_attribute("value") == ""


def test_input_check(driver_Chrome):
    driver_Chrome.get(url)
    element = driver_Chrome.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    element.click()
    assert not element.is_selected()


def test_clear(driver_Chrome):
    driver_Chrome.get(url)
    element = driver_Chrome.find_element(By.ID, "user[email]")
    element.send_keys("Abracadabra@gmail.com")
    assert not element.get_attribute("value") == ""
    element.clear()
    assert element.get_attribute("value") == ""
