from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_positive_login(driver):

    driver.get("https://practicetestautomation.com/practice-test-login/")
    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.element_to_be_clickable((By.ID, "username")))
    username.send_keys("student")
    password = driver.find_element(By.ID, "password")
    password.send_keys("Password123")

    submit = driver.find_element(By.ID, "submit")
    submit.click()

    wait.until(EC.url_contains("/logged-in-successfully/"))
    assert "/logged-in-successfully/" in driver.current_url

    title = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
    assert "Congratulations" in title.text

    logout = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log out")))
    assert logout.is_displayed()


def test_negative_username(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.ID, "username"))).send_keys(
        "incorrectUser"
    )
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    error = wait.until(EC.visibility_of_element_located((By.ID, "error")))
    assert error.is_displayed()
    assert error.text == "Your username is invalid!"
    assert "practice-test-login" in driver.current_url


def test_negative_password(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.ID, "username"))).send_keys("student")
    driver.find_element(By.ID, "password").send_keys("incorrectPassword")
    driver.find_element(By.ID, "submit").click()

    error = wait.until(EC.visibility_of_element_located((By.ID, "error")))
    assert error.is_displayed()
    assert error.text == "Your password is invalid!"
    assert "practice-test-login" in driver.current_url


def test_page_elements(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://practicetestautomation.com/practice-test-login/")

    wait.until(EC.title_contains("Login"))
    wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h2")))
    wait.until(EC.visibility_of_element_located((By.ID, "username")))
    wait.until(EC.visibility_of_element_located((By.ID, "password")))
    wait.until(EC.visibility_of_element_located((By.ID, "submit")))
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    wait.until(EC.element_to_be_clickable((By.ID, "username")))
    wait.until(EC.element_to_be_clickable((By.ID, "password")))
    wait.until(EC.element_to_be_clickable((By.ID, "submit")))
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "custom-logo-link")))
    wait.until(EC.element_to_be_clickable((By.ID, "menu-item-43")))
    wait.until(EC.element_to_be_clickable((By.ID, "menu-item-20")))
    wait.until(EC.element_to_be_clickable((By.ID, "menu-item-21")))
    wait.until(EC.element_to_be_clickable((By.ID, "menu-item-19")))
    wait.until(EC.element_to_be_clickable((By.ID, "menu-item-18")))
    # wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Home')]")))#
    # wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Practice')]")))#
    # wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Courses')]")))#
    # wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Blog')]")))#
    # wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Contact')]")))#
