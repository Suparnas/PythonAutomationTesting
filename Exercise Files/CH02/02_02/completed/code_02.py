from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.get("file:///Users/suparnasoman/Documents/SeleniumPython/PythonAutomationTesting/Exercise%20Files/CH02/html_code_02.html")
login_form = driver.find_element(By.ID,'loginForm')
print("My login form element is:")
print(login_form)
driver.close()

