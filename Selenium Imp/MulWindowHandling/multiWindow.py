from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
driver= webdriver.Firefox()

# Open the Python website
driver.get("https://www.python.org/")

# Open a new tab with a different URL
driver.execute_script("window.open('https://wiki.python.org/moin/FrontPage');")

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

# Perform actions in the new tab (e.g., search for 'Selenium')
search_bar = driver.find_element(By.ID,'searchinput')
search_bar.clear()
search_bar.send_keys("Selenium")
search_bar.send_keys(Keys.RETURN)

# Switch back to the original tab
driver.switch_to.window(driver.window_handles[0])

# Close the browser
driver.quit()