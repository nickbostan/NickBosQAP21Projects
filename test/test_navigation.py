from selenium.webdriver.common.by import By

url = "https://sbg.by/testimonials/"
url1 = "https://letcode.in/frame/"


def test_navigation(driver_Chrome):
    driver_Chrome.get(url)
    element = driver_Chrome.find_element(By.XPATH, '//*[@xlink:href="#youtube"]')
    element.click()
    element.click()
    window_handles = driver_Chrome.window_handles
    assert len(window_handles) == 3

    driver_Chrome.switch_to.window(window_handles[1])
    current_url = driver_Chrome.current_url
    assert current_url != url


def test_frame(driver_Chrome):
    driver_Chrome.get(url1)
    frame = driver_Chrome.find_element(By.ID, "firstFr")
    driver_Chrome.switch_to.frame(frame)
    element = driver_Chrome.find_element(By.CSS_SELECTOR, '[name="lname"]')
    element.send_keys("Ave")
    assert element.get_attribute("value") == "Ave"

    driver_Chrome.switch_to.default_content()
