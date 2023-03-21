from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver_path = "C:/ambiente/selenium_drivers/geckodriver.exe"

driver=webdriver.Firefox()

print("Bienvenido a selenium con firefox")

driver.get("http://opencart.abstracta.us/index.php?route=common/home")
time.sleep(3)

driver.quit()


