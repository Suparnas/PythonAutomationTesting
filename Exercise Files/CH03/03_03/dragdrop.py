from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver import ActionChains

driver= webdriver.Firefox()
driver.get('http://jqueryui.com/droppable')
driver.switch_to.frame(0)

action_chains= ActionChains(driver)

source= driver.find_element(By.ID,'draggable')
target = driver.find_element(By.ID,'droppable')
action_chains.drag_and_drop_by_offset(source, 200, 100).perform()
time.sleep(2)

action_chains.drag_and_drop(source, target).perform()
time.sleep(2)

driver.close()
