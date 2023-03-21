import pytest
import time
from selenium.webdriver.common.by import By
from helpers.data_driven import URL_BASE, URL_LOGIN
from helpers.drivers import chrome
from helpers.BaseTest01 import BaseTest

URL_PRUEBA = "https://www.liverpool.com.mx/tienda/home"

class Test_01(BaseTest):
    def test_xpath(self):
        self.driver.get(URL_PRUEBA)
        print("\nOBTENER ELEMENTO POR XPATH")
        element = self.driver.find_element(By.XPATH, "(//*[@class='carouselHeading-link'])[2]")
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    def test_css(self):
        self.driver.get(URL_PRUEBA)
        print("\nOBTENER ELEMENTO POR CSS SELECTOR")
        element = self.driver.find_element(By.CSS_SELECTOR,"*[class='a-header__logo']")#"a > #a-header__logo")
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    def test_css_selector(self):
        self.driver.get(URL_PRUEBA)
        element = self.driver.find_element(By.CSS_SELECTOR, "a > img[class = 'a-header__logo']")
        assert element.is_displayed()== True, "ASSERT ELEMENTO VISIBLE"

    def test_css_selector(self):
        self.driver.get(URL_PRUEBA)
        element = self.driver.find_element(By.CSS_SELECTOR, "a > .a-header__logo")
        assert element.is_displayed()== True, "ASSERT ELEMENTO VISIBLE"

    def test_css_selector(self):
        self.driver.get(URL_PRUEBA)
        element = self.driver.find_element(By.LINK_TEXT, "WhatsApp")
        assert element.is_displayed()== True, "ASSERT ELEMENTO VISIBLE"