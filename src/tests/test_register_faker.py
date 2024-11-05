import pytest
from selenium import webdriver
from pages.register_page import RegisterPage
from faker import Faker

fake = Faker() 

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

# @pytest.fixture(scope="module") 
def user_data(): 
  password = fake.password() 
  return { 
    "username": fake.unique.user_name(), 
    "email": fake.email(), 
    "password": password, 
    "confirm_password": password, 
    }
                                                                                                                                                                                                       
def test_register(driver, user_data):
    register_page = RegisterPage(driver)

    # Go to Register Page and register user
    register_page.go_to("https://demo.wpeverest.com/user-registration/column-1/")
    assert driver.current_url == "https://demo.wpeverest.com/user-registration/column-1/", "Test failed: URL does not match 'https://demo.wpeverest.com/user-registration/column-1/'"
    register_page.register_user(user_data["username"], user_data["email"], user_data["password"], user_data["confirm_password"])    
   
    # Check if registration was successful by asserting the success message
    assert register_page.is_registration_successful(), "Test failed: Registration was not successful"