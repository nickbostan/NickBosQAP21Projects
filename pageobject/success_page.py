from selenium.webdriver.common.by import By

from pageobject.base_page import BasePage


class SuccessPage(BasePage):
    TITLE = By.CLASS_NAME, "post-title"
    TEXT = By.TAG_NAME, "strong"
    BUTTON_LOGOUT = By.CSS_SELECTOR, "a.wp-block-button__link"

    def __init__(self, driver):
        super().__init__(driver)

    def check_that_page_opened(self, title, text):
        self.should_be_visible(self.TITLE)
        self.should_be_visible(self.TEXT)
        self.should_be_visible(self.BUTTON_LOGOUT)

        self.should_be_has_text(self.TITLE, title)
        self.should_be_has_text(self.TEXT, text)

    def logout(self):
        self.should_be_visible(self.BUTTON_LOGOUT)
        self.click(self.BUTTON_LOGOUT)
