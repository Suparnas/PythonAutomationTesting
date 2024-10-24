from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.get("file:///Users/suparnasoman/Documents/SeleniumPython/PythonAutomationTesting/Exercise%20Files/CH02/html_code_02.html")
username = driver.find_element(By.NAME,'username')
print("My input element is:")
print(username)
driver.close()
