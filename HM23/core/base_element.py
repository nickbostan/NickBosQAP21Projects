from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement:
    def __init__(self, driver, selector):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.selector = selector

    def get_element(self, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.selector)
        )

    def click(self):
        element = self.get_element()
        element.click()

    def fill(self, text):
        element = self.get_element()
        element.clear()
        assert element.get_attribute("value") == ""
        element.send_keys(text)
        return self

    def should_be_has_text(self, expected):
        element = self.get_element()
        actual = element.text.strip()
        assert actual == expected, f"ACTUAL IS:  {actual}, EXPECTED IS: {expected}"

    def should_be_visible(
        self,
    ):
        element = self.get_element()
        assert element.is_displayed()

    def should_be_not_visible(self, timeout=5):
        return WebDriverWait(self.driver, timeout).until_not(
            EC.element_to_be_clickable(self.selector)
        )

    def wait_for_windows_count(self, expected_count):
        self.wait.until(EC.number_of_windows_to_be(expected_count))

    def switch_to_new_window(self, expected_windows=2):
        original_window = self.driver.current_window_handle
        original_url = self.driver.current_url

        self.wait_for_windows_count(expected_windows)

        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                break

        new_url = self.driver.current_url
        assert new_url != original_url
        return new_url
