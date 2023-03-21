import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from helpers.data_driven import *
from basetest import BaseTest02
from helpers.generics import mouse_hover

URL = "https://www.liverpool.com.mx/tienda/home"


class Test_02(BaseTest02):
    def test_1(self):
        self.driver.get(URL)

        menu = self.driver.find_element(By.XPATH, "//*[text()='Categorías']")
        mouse_hover(self.driver, menu)

        submenu = self.driver.find_element(By.XPATH, "//*[text()='Videojuegos']")
        mouse_hover(self.driver, submenu)
        time.sleep(1)

        submenu1 = self.driver.find_element(By.LINK_TEXT, "PC Gamer")
        assert submenu1.is_enabled() == True, "ASSERT LINK SIGN IN VISIBLE"
        submenu1.click()
