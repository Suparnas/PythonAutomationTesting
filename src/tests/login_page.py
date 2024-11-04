from selenium.webdriver.common.by import By
from base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "login-username")
    PASSWORD_INPUT = (By.ID, "login-password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login_user(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)