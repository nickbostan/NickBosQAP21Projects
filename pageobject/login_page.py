from selenium.webdriver.common.by import By

from pageobject.base_page import BasePage


class LoginPage(BasePage):
    LOGO = By.CSS_SELECTOR, ".custom-logo-link"
    MENU_PRACTICE = By.CSS_SELECTOR, "#menu-item-20"
    MENU_HOME = By.CSS_SELECTOR, "#menu-item-43"
    MENU_COURSES = By.CSS_SELECTOR, "#menu-item-21"
    MENU_BLOG = By.CSS_SELECTOR, "#menu-item-19"
    MENU_CONTACT = By.CSS_SELECTOR, "#menu-item-18"
    PAGE_TITLE = By.CSS_SELECTOR, "#login h2"
    PAGE_DESCRIPTION = By.CSS_SELECTOR, "#login ul li:nth-child(1)"
    PAGE_TEXT_INFO = By.XPATH, '//*[@id="login"]/ul/li[2]'
    PAGE_TEXT_CREDS = By.CSS_SELECTOR, "#login > ul > li:nth-child(2) b"
    INPUT_USER_NAME = (By.ID, "username")
    INPUT_PASSWORD = (By.ID, "password")
    SUBMIT = By.ID, "submit"
    LINE = By.CLASS_NAME, ".wp-block-separator"
    ERROR = By.ID, "error"

    def __init__(self, driver):
        super().__init__(driver)

    def check_that_page_opened(self, title, description):
        self.should_be_visible(self.LOGO)
        self.should_be_visible(self.MENU_PRACTICE)
        self.should_be_visible(self.MENU_COURSES)
        self.should_be_visible(self.MENU_CONTACT)
        self.should_be_visible(self.MENU_BLOG)
        self.should_be_visible(self.PAGE_TEXT_CREDS)
        self.should_be_visible(self.SUBMIT)
        self.should_be_visible(self.INPUT_PASSWORD)
        self.should_be_visible(self.INPUT_USER_NAME)
        self.should_be_visible(self.PAGE_TITLE)
        self.should_be_visible(self.PAGE_DESCRIPTION)
        self.should_be_visible(self.PAGE_TEXT_INFO)

        self.should_be_has_text(self.PAGE_TITLE, title)
        self.should_be_has_text(self.PAGE_DESCRIPTION, description)

        self.should_be_not_visible(self.ERROR)

    def login(self, username, password):
        self.fill(self.INPUT_USER_NAME, text=username)
        self.fill(self.INPUT_PASSWORD, text=password)
        self.click(self.SUBMIT)

    def check_that_error_is_visible(self, text):
        self.should_be_visible(self.ERROR)
        self.should_be_has_text(self.ERROR, text)
