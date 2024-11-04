import json
import pytest
from selenium import webdriver
# from PythonAutomationTesting.src.pages.register_page import RegisterPage
# from PythonAutomationTesting.src.pages.login_page import LoginPage
from register_page import RegisterPage
from login_page import LoginPage

@pytest.fixture(scope="module")
def driver():
    browser= webdriver.Firefox();
    driver.maximize_window()
    yield driver
    # driver.quit()

def load_test_data():
    with open("test_data.json") as f:
        return json.load(f)

@pytest.mark.parametrize("data", load_test_data())
def test_register_and_login(driver, data):
    register_page = RegisterPage(driver)
    login_page = LoginPage(driver)

    # Go to Register Page and register user
    register_page.go_to("https://example.com/register")
    register_page.register_user(data["username"], data["password"], data["confirm_password"])
    print ("yes")
    
    # Go to Login Page and login user
    login_page.go_to("https://example.com/login")
    login_page.login_user(data["username"], data["password"])
    print ("yes")

    # Assert login success
    if data["login_success"]:
        # Replace with the actual condition for a successful login, e.g., URL check or element visibility
        assert "dashboard" in driver.current_url
    else:
        # Replace with the actual failure check, e.g., error message display
        assert "error" in driver.page_source
