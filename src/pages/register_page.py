from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    USERNAME_INPUT = (By.ID, "user_login")
    EMAIL_INPUT = (By.ID, "user_email")
    PASSWORD_INPUT = (By.ID, "user_pass")
    CONFIRM_PASSWORD_INPUT = (By.ID, "user_confirm_password")
    REGISTER_BUTTON = (By.CLASS_NAME, "btn.button.ur-submit-button")
    SUCCESS_MESSAGE = (By.ID, "ur-submit-message-node")

    def register_user(self, username, email, password, confirm_password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.enter_text(self.CONFIRM_PASSWORD_INPUT, confirm_password)
        self.click(self.REGISTER_BUTTON)
        
    def is_registration_successful(self): 
        success_message = self.get_text(self.SUCCESS_MESSAGE)
        return success_message == "User successfully registered."
