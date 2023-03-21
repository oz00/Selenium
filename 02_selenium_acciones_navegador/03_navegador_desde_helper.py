from helpers.drivers import chrome
import time

driver = chrome()

driver.get("http://opencart.abstracta.us/index.php?route=common/home")
time.sleep(3)

driver.quit()