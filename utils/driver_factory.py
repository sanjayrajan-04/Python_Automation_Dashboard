from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class DriverFactory:
    """Simple driver factory using webdriver-manager for Chrome."""
    @staticmethod
    def get_driver():
        # Installs chromedriver automatically and returns a Chrome WebDriver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        return driver
