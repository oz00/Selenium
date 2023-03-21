import pytest
import time
from selenium.webdriver.support.wait import WebDriverWait
from helpers.data_driven import URL_BASE, URL_LOGIN
from helpers.drivers import chrome
import helpers.data_driven


class BaseTest:

    @pytest.fixture(autouse=True)
    def before_test(self):
        print("\n***************************")
        print("\nBEFORE TEST")
        print("\n***************************")
        self.driver = chrome()
        self.driver.maximize_window()
        yield self.driver
        print("\n***************************")
        print("\nAFTER TEST")
        print("\n***************************")
        self.driver.quit()


