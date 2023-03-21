import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from helpers.data_driven import URL_BASE, URL_LOGIN, CONTRASENA, USUARIO
from helpers.BaseTest01 import BaseTest


class Test03ImplicitWait(BaseTest):

    def test_login(self):
        #IMPLICIT WAIT
        self.driver.implicitly_wait(60)

        #Abrir URL Login
        self.driver.get(URL_LOGIN)
        #Datos de login
        email_esperado = USUARIO
        password = CONTRASENA

        #Llenar text email
        txt_email = self.driver.find_element(By.ID, "input-email")
        txt_email.send_keys(email_esperado)
        assert txt_email.get_attribute("value") == email_esperado, "ASSERT TEXT EMAIL ESCRITO"

        #Llenar text password
        txt_password = self.driver.find_element(By.ID, "input-password")
        txt_password.send_keys(password)

        #Click boton sign in
        btn_sign_in = self.driver.find_element(By.XPATH,"//*[@type='submit' and @value='Login']")
        btn_sign_in.click()

        #Validar se muestre My account
        lbl_my_account = self.driver.find_element(By.XPATH, "//h2[contains(text(), 'My Account')]")
        text_my_account_esperado = "my account"
        text_my_account_actual = lbl_my_account.text.lower()
        assert text_my_account_actual == text_my_account_esperado, "ASSERT MY ACCOUNT PAGE ES VISIBLE"
        assert lbl_my_account.is_displayed() == True, "ASSERT ETIQUETA MY ACCOUNT VISIBLE"






