from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
driver= webdriver.Firefox()

# Open login yahoo for sample url 
driver.get("https://accounts.google.com/signup")   
  
# print title of yahoo window 
print("First window title = " + driver.title) 
  
# Clicks on privacy and it opens in new window 
driver.find_element(By.LINK_TEXT,"Help").click()
  
# switch window in 7 seconds 
time.sleep(2)   
  
# window_handles[1] is a second window 
driver.switch_to.window(driver.window_handles[1]) 
  
# prints the title of the second window 
print("Second window title = " + driver.title) 
  
# window_handles[0] is a first window 
driver.switch_to.window(driver.window_handles[0]) 
time.sleep(2)  
driver.switch_to.window(driver.window_handles[1]) 
print("Second window title = " + driver.title) 
time.sleep(2)  
driver.switch_to.window(driver.window_handles[0]) 
print("First window title = " + driver.title) 
time.sleep(2)
# prints windows id 
print(driver.window_handles)   
driver.quit()