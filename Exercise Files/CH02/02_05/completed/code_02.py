from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.get("file:///Users/suparnasoman/Documents/SeleniumPython/PythonAutomationTesting/Exercise%20Files/CH02/html_code_02.html")
content = driver.find_element(By.CLASS_NAME,'content')
print("My class element is:")
print(content)
driver.close()
