from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.get("https://www.seleniumhq.org")
idq = driver.find_element(By.ID,'announcement-banner')
# nameq = driver.find_element(By.NAME,'q')
# xpaths = driver.find_element(By.XPATH,//form[@id='loginForm']'HEADING="What is Selenium?"')
# xpaths = driver.find_element(By.XPATH,"//h1[@class='d-1 fw-bold']")
classn = driver.find_element(By.CLASS_NAME,'nav-item dropdown')
print("My id element is:")
print(idq)
# print("My name element is:")
# print(nameq)
# print("My xpath element is:")
# print(xpaths)
# print("My class element is:")
print(classn)
driver.close()
