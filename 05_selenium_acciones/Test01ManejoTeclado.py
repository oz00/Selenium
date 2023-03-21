import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from helpers.data_driven import URL_BASE, URL_LOGIN, CONTRASENA, USUARIO
from helpers.BaseTest01 import BaseTest


class Test01ManejoTeclado(BaseTest):

    def test_send_keys_and_clear_text(self):
        self.driver.get(URL_LOGIN)
        email_esperado = USUARIO

        print("\nIDENTIFICAR ELEMENTO")
        txt_email = self.driver.find_element(By.ID, "input-email")
        print("\nESCRIBIR EN EL TEXT")
        time.sleep(5)
        txt_email.send_keys(email_esperado) #Escribir en cuadros de texto
        assert txt_email.get_attribute("value") == email_esperado, "ASSERT TEXT EMAIL ESCRITO"
        time.sleep(5)

        print("\nLIMPIAR EL TEXT")
        txt_email.clear()
        assert txt_email.get_attribute("value") == "", "ASSERT TEXT EMAIL CLEAR"
        time.sleep(5)

    def test_special_keys(self):
        self.driver.get(URL_LOGIN)
        email_esperado = USUARIO
        password = CONTRASENA

        txt_email = self.driver.find_element(By.ID, "input-email")
        txt_email.send_keys(email_esperado)
        print("\nUSO DE TECLAS ESPECIALES")
        txt_email.send_keys(Keys.TAB) #tabulador
        time.sleep(5)

        txt_password = self.driver.find_element(By.ID, "input-password")
        txt_password.send_keys(password)
        print("\nUSO DE TECLAS ESPECIALES")
        txt_email.send_keys(Keys.ENTER) #Enter
        time.sleep(15)


