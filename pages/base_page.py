class BasePage:
    """Base page that other pages will extend."""
    def __init__(self, driver):
        self.driver = driver
