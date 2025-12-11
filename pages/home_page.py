from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    """Page object for the home page of the demo site."""
    heading = (By.TAG_NAME, "h1")
    form_auth_link = (By.LINK_TEXT, "Form Authentication")

    def get_heading_text(self):
        return self.driver.find_element(*self.heading).text

    def go_to_login(self):
        self.driver.find_element(*self.form_auth_link).click()
