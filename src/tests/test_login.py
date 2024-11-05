import json
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def load_test_data():
    with open("data/test_data.json") as f:
        return json.load(f)

@pytest.mark.parametrize("data", load_test_data())
def test_register_login(driver, data):
    login_page = LoginPage(driver)

    # Go to Login Page and login user
    login_page.go_to("https://practicetestautomation.com/practice-test-login/")
    assert driver.current_url == "https://practicetestautomation.com/practice-test-login/", "Test failed: URL does not match 'https://practicetestautomation.com/practice-test-login/'"
    login_page.login_user(data["username"], data["password"])

    # Check if login was successful by asserting the URL 
    assert driver.current_url == "https://practicetestautomation.com/logged-in-successfully/", "Test failed: URL does not match 'https://practicetestautomation.com/logged-in-successfully/'" 
  
    # Check if the post-title class contains the text "Logged In Successfully" 
    assert login_page.is_logged_in_successfully(), "Test failed: post-title text does not match 'Logged In Successfully'"