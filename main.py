
# Get data from user input
# data is [price, product name, product link]
from selenium import webdriver 
from selenium.webdriver.common.by import By 

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/search?q=iphone+12&sca_esv=583676307&rlz=1C1RXMK_enCA1020CA1020&tbm=shop&source=lnms&sa=X&ved=2ahUKEwjmn4it1c6CAxVOJzQIHYDTD7cQ_AUoAXoECAMQAw&biw=1536&bih=739&dpr=1.25")

elements = driver.find_elements(By.CLASS_NAME, 'sh-dgr__content') 
for e in elements:
    title = e.find_element(By.CLASS_NAME, "tAxDx")
    price = e.find_element(By.CLASS_NAME, "a8Pemb")
    link = e.find_element(By.CLASS_NAME, "Lq5OHe")
    print(title.text)
    print(price.text)
    print(link.get_attribute('href'))
    print()

elements = driver.find_elements(By.CLASS_NAME, 'KZmu8e') 
for e in elements:
    brand = e.find_element(By.CLASS_NAME, "E5ocAb")
    title = e.find_element(By.CLASS_NAME, "sh-np__product-title")
    price = e.find_element(By.CLASS_NAME, "T14wmb")
    link = e.find_element(By.CLASS_NAME, "shntl")
    print(brand.text)
    print(title.text)
    print(price.text)
    print(link.get_attribute('href'))
    print()


driver.quit()