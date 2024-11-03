from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Firefox()
driver.get('https://wiki.python.org/moin/FrontPage')

searchBox= driver.find_element(By.ID,'searchinput')
searchBox.clear()
searchBox.send_keys("Beginner")
searchBox.send_keys(Keys.RETURN)
time.sleep(5)

# select = Select(driver.find_element(By.XPATH,'//*/form/div/select'))
# select.select_by_visible_text('Print View')
# time.sleep(5)


select = Select(driver.find_element(By.XPATH,'//select[@name="action"]'))
select.select_by_visible_text("Raw Text")
time.sleep(5)

driver.close()
