from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://erick-pavani.github.io/")
print(driver.title)
