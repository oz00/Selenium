import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from helpers.data_driven import URL_BASE, URL_LOGIN
from helpers.drivers import chrome
import helpers.data_driven


@pytest.fixture
def driver(request):
    print("\n***************************")
    print("\nBEFORE TEST")
    print("\n***************************")
    driver = chrome()
    request.instance.driver = driver
    driver.maximize_window()
    yield driver
    print("\n***************************")
    print("\nAFTER TEST")
    print("\n***************************")
    driver.quit()


@pytest.fixture
def wait(driver):
    print("\n***************************")
    print("\nBEFORE TEST")
    print("\n***************************")
    wait = WebDriverWait(driver, 30)
    yield wait
    print("\n***************************")
    print("\nAFTER TEST")
    print("\n***************************")
    driver.quit()
