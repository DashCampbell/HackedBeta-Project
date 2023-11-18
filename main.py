
# Get data from user input
# data is [price, product name, product link]

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.python.org")
print(driver.title)
driver.quit()