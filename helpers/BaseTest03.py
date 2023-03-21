import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from helpers.data_driven import URL_BASE, URL_LOGIN, URL_LOGOUT
from helpers.drivers import chrome, chrome_headless, firefox
import helpers.data_driven


class BaseTest03:

    @pytest.fixture(autouse=True)
    def before_test(self):
        print("\n***************************")
        print("\nBEFORE TEST")
        print("\n***************************")
        self.driver = chrome_headless()
        self.wait = WebDriverWait(self.driver, 30)
        self.driver.maximize_window()
        #Eliminar cookies (cache)
        self.driver.delete_all_cookies()
        yield self.driver, self.wait
        print("\n***************************")
        print("\nAFTER TEST")
        print("\n***************************")
        self.driver.get(URL_LOGOUT)
        self.driver.quit()
