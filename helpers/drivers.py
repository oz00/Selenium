from selenium import webdriver
from selenium.webdriver.chrome.options import Options


driver_path = "D:/ambiente/selenium_drivers"


def chrome():
    driver = webdriver.Chrome(executable_path=driver_path + "/chromedriver.exe")
    return driver


def firefox():
    driver = webdriver.Chrome(executable_path=driver_path + "/geckodriver.exe")
    return driver


def chrome_headless():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver = webdriver.Chrome(executable_path=driver_path + "/chromedriver.exe", chrome_options=options)
    return driver


