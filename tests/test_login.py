from pages.home_page import HomePage
from pages.login_page import LoginPage
from config import BASE_URL, USERNAME, PASSWORD

def test_login_success(driver):
    """Demo login test using the-internet credentials (works for demo site)."""
    driver.get(BASE_URL)
    home = HomePage(driver)
    home.go_to_login()

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    # After successful login the URL contains '/secure' on the demo site
    assert '/secure' in driver.current_url or 'You logged into a secure area!' in login.get_flash_text()
