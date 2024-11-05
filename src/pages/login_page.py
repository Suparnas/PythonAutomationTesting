from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")
    POST_TITLE = (By.CLASS_NAME, "post-title")

    def login_user(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        
    def is_logged_in_successfully(self): 
        post_title = self.get_text(self.POST_TITLE)
        return post_title == "Logged In Successfully"