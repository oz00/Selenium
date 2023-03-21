import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from helpers.data_driven import URL_BASE, URL_LOGIN, CONTRASENA, USUARIO
from helpers.drivers import chrome
from helpers.BaseTest01 import BaseTest


class Test02Click(BaseTest):

    def test_click(self):
        self.driver.get(URL_LOGIN)
        btn_sign_in = self.driver.find_element(By.XPATH,"//*[@type='submit' and @value='Login']")
        assert btn_sign_in.is_enabled() == True, "ASSERT BOTON SIGN IN HABILITADO" #Validar que esté el boton habilitado para un click
        btn_sign_in.click() #Realizar click en el boton
        time.sleep(3)

    def test_login(self):
        self.driver.get(URL_LOGIN)
        email_esperado = USUARIO
        password = CONTRASENA

        txt_email = self.driver.find_element(By.ID, "input-email")
        txt_email.send_keys(email_esperado)
        assert txt_email.get_attribute("value") == email_esperado, "ASSERT TEXT EMAIL ESCRITO"
        time.sleep(2)

        txt_password = self.driver.find_element(By.ID, "input-password")
        txt_password.send_keys(password)
        time.sleep(2)

        btn_sign_in = self.driver.find_element(By.XPATH,"//*[@type='submit' and @value='Login']")
        btn_sign_in.click()
        time.sleep(3)
        #Validar que se haya movido a la pagina que se realizó el login
        lbl_my_account = self.driver.find_element(By.XPATH, "//h2[contains(text(), 'My Account')]")
        text_my_account_esperado = "my account"
        text_my_account_actual = lbl_my_account.text.lower()
        assert text_my_account_actual == text_my_account_esperado, "ASSERT MY ACCOUNT PAGE ES VISIBLE"
        assert lbl_my_account.is_displayed() == True, "ASSERT ETIQUETA MY ACCOUNT VISIBLE"






