from selenium import webdriver
import time

# Pra abrir o navegador em segundo plano
chrome_options = webdriver.ChromeOptions()
# Pra abrir o navegador em segundo plano
chrome_options.add_argument('headless')
driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.get("https://erick-pavani.github.io/")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="navbarNav"]/div/a[5]').click()
time.sleep(2)
driver.find_element_by_class_name("Linkedin").click()
print(driver.title)
