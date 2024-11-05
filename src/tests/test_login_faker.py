import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.register_page import RegisterPage 
from faker import Faker

fake = Faker()

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def user_data(driver):
    register_page = RegisterPage(driver)
    password = fake.password()
    user_data = {
        "username": fake.unique.user_name(),
        "email": fake.email(),
        "password": password,
        "confirm_password": password,
    }

    # Register the user
    register_page.go_to("https://demo.wpeverest.com/user-registration/column-1/")
    register_page.register_user(user_data["username"], user_data["email"], user_data["password"], user_data["confirm_password"])
    assert register_page.is_registration_successful(), "Test failed: Registration was not successful"

    return user_data

def test_login(driver, user_data):
    login_page = LoginPage(driver)

    # Go to Login Page and login user
    login_page.go_to("https://practicetestautomation.com/practice-test-login/")
    assert driver.current_url == "https://practicetestautomation.com/practice-test-login/", "Test failed: URL does not match 'https://practicetestautomation.com/practice-test-login/'"
    login_page.login_user(user_data["username"], user_data["password"])

    # Check if login was successful by asserting the URL
    assert driver.current_url == "https://practicetestautomation.com/logged-in-successfully/", "Test failed: URL does not match 'https://practicetestautomation.com/logged-in-successfully/'"

    # Check if the post-title class contains the text "Logged In Successfully"
    assert login_page.is_logged_in_successfully(), "Test failed: post-title text does not match 'Logged In Successfully'"
