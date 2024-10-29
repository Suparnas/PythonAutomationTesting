from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.get("http://python.org");

element_id = driver.find_element(By.ID,'submit')
print(element_id)

etexti = element_id.text
print("Text by id is "+ etexti)

element_name = driver.find_element(By.NAME,'submit')
print( element_name)

etextn = element_name.text
print("Text by name is "+ etextn)

element_xpath = driver.find_element(By.XPATH,'//img[@class="python-logo"]')
print(element_xpath)

element_classname = driver.find_element(By.CLASS_NAME,'search-button')
print(element_classname)

etextc = element_classname.text
print("Text by class name is "+ etextc)

driver.close()
