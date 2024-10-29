from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://selenium.dev')

element_id = driver.find_element(By.ID,'announcement-banner')
print(element_id)

etexti = element_id.text
print(etexti)

# element_name = driver.find_element(By.NAME,'submit')
# print(element_name)

element_xpath = driver.find_element(By.XPATH,'//*[contains(text(),"Selenium automates browsers")]')
print(element_xpath)

etext = element_xpath.text
print(etext)

element_classname = driver.find_element(By.CLASS_NAME,'d-flex.justify-content-center.td-box--100.pt-5')
print(element_classname)

etextc = element_classname.text
print(etextc)

driver.close()
