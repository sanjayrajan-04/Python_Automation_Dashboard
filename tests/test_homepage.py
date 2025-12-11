from pages.home_page import HomePage
from config import BASE_URL

def test_homepage_heading(driver):
    """Simple test: page has a heading (easy to explain in interview)."""
    driver.get(BASE_URL)
    home = HomePage(driver)
    heading = home.get_heading_text()
    assert heading is not None and len(heading) > 0
