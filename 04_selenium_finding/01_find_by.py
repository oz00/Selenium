import pytest
import time
from selenium.webdriver.common.by import By
from helpers.data_driven import URL_BASE, URL_LOGIN
from helpers.drivers import chrome
from helpers.BaseTest01 import BaseTest

class Test_FindBy(BaseTest):

    def test_buscar_by_id(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR SU HTML ATRIBUTO: 'ID'")
        txt_email = self.driver.find_element(By.ID, "input-email")
        time.sleep(15)
        assert txt_email.is_displayed() == True, "ASSERT TEXT EMAIL VISIBLE"

    def test_buscar_by_name(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR SU HTML ATRIBUTO: 'NAME'")
        txt_email = self.driver.find_element(By.NAME, "email")
        assert txt_email.is_displayed() == True, "ASSERT TEXT EMAIL VISIBLE"

    def test_buscar_by_tag(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER 1ER ELEMENTO POR SU HTML ATRIBUTO: 'TAG HTML'")
        element = self.driver.find_element(By.TAG_NAME, "div")
        assert element.is_displayed() == True, "ASSERT ELEMENTO WEB VISIBLE"

    def test_buscar_by_class(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER 1ER ELEMENTO POR SU HTML ATRIBUTO: '1 DE SUS CLASES'")
        element = self.driver.find_element(By.CLASS_NAME, "form-control")
        assert element.is_displayed() == True, "ASSERT ELEMENTO WEB VISIBLE"

    def test_buscar_by_link_text(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR SU HTML ATRIBUTO: 'LINK_TEXT'")
        lk_contact_us = self.driver.find_element(By.LINK_TEXT, "Forgotten Password")
        assert lk_contact_us.is_displayed() == True, "ASSERT LINK CONTAC US VISIBLE"

    def test_buscar_by_partial_link_text(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR SU HTML ATRIBUTO: 'PARTIAL_LINK_TEXT'")
        lk_sign_in = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Forgotten")
        assert lk_sign_in.is_displayed() == True, "ASSERT LINK SIGN IN VISIBLE"

