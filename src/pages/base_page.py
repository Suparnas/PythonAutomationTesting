from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        
    def get_text(self, locator): 
        return self.find_element(locator).text