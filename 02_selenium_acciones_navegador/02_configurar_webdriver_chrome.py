from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver_path = "C:/ambiente/selenium_drivers/chromedriver.exe"

driver=webdriver.Chrome(executable_path=driver_path)

print("Bienvenido a selenium con chrome")

driver.get("http://opencart.abstracta.us/index.php?route=common/home")

time.sleep(5)

driver.quit()



