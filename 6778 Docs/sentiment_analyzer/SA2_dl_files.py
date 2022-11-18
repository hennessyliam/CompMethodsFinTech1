from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Github credentials
username = "li621332"
password = "Joseph1102!"


# Initialize the Chrome driver
driver = webdriver.Chrome(options=Options())
# Head to Nexis login page
driver.get("https://guides.ucf.edu/database/LNA")

# Maximize window and wait
driver.maximize_window()
time.sleep(5)

# Login
driver.find_element("id", "userNameInput").send_keys(username)
driver.find_element("id", "passwordInput").send_keys(password)
driver.find_element("id","submitButton").click()

time.sleep(5)

# New URL
#print(driver.current_url)
driver.get(driver.current_url)

# Select News
# Type in company
driver.find_element("class", "Search for").send_keys("3M")

time.sleep(5)

# Select date range



# Search

driver.find_element("class", "Search").click()

time.sleep(5)

# Download

# Articles 1-10

# name file name of company

# Download

# Close Loop

# close the driver
driver.close()

