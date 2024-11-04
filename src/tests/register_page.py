from selenium.webdriver.common.by import By
from base_page import BasePage

class RegisterPage(BasePage):
    USERNAME_INPUT = (By.ID, "register-username")
    PASSWORD_INPUT = (By.ID, "register-password")
    CONFIRM_PASSWORD_INPUT = (By.ID, "register-confirm-password")
    REGISTER_BUTTON = (By.ID, "register-button")

    def register_user(self, username, password, confirm_password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.enter_text(self.CONFIRM_PASSWORD_INPUT, confirm_password)
        self.click(self.REGISTER_BUTTON)
