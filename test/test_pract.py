from selenium.webdriver.common.by import By


def test_window(driver):
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.find_element(By.CSS_SELECTOR, '[target="_blank"]').click()
    window_handles = driver.window_handles
    assert len(window_handles) == 2
    driver.switch_to.window(window_handles[1])
    element1 = driver.find_elements(By.XPATH, "//*[text()='New Window']")
    element2 = driver.find_element(By.CSS_SELECTOR, '[class="example"]')
    element2.is_displayed()
    element1.is_not_displayed()
