import csv
import pytest
from selenium import webdriver
from pages.register_page import RegisterPage

# Fixture to initialize the WebDriver
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

# Load test data from CSV file
def load_test_data():
    test_data = []
    with open('data/test_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            test_data.append(row)
    return test_data

# Parametrize the test with the loaded data
@pytest.mark.parametrize("data", load_test_data())
def test_register(driver, data):
    register_page = RegisterPage(driver)

    # Go to Register Page and register user
    register_page.go_to("https://demo.wpeverest.com/user-registration/column-1/")
    assert driver.current_url == "https://demo.wpeverest.com/user-registration/column-1/", "Test failed: URL does not match 'https://demo.wpeverest.com/user-registration/column-1/'"
    register_page.register_user(data["username"], data["email"], data["password"], data["confirm_password"])
    
    # Check if registration was successful by asserting the success message
    assert register_page.is_registration_successful(), "Test failed: Registration was not successful"
