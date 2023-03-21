import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.data_driven import URL_BASE, URL_LOGIN, CONTRASENA, USUARIO
from helpers.BaseTest01 import BaseTest


class Test04ExplicitWait(BaseTest):

    def test_login(self):
        #INSTANCIA OBJETO WAIT PARA USAR EXPLICIT WAIT
        #Se modifico para que se pueda configurar desde el inicio
        wait = WebDriverWait(self.driver, 60) #Driver, tiempo de espera máximo

        #Abrir URL Login
        self.driver.get(URL_LOGIN)
        #Datos de login
        email_esperado = USUARIO
        password = CONTRASENA

        #Llenar text email
        txt_email = wait.until(expected_conditions.presence_of_element_located((By.ID, "input-email")))
        txt_email.send_keys(email_esperado)
        assert txt_email.get_attribute("value") == email_esperado, "ASSERT TEXT EMAIL ESCRITO"

        #Llenar text password
        txt_password = wait.until(expected_conditions.visibility_of_element_located((By.ID, "input-password")))
        txt_password.send_keys(password)

        #Click boton sign in
        btn_sign_in = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@type='submit' and @value='Login']")))
        btn_sign_in.click()

        #Validar se muestre My account
        lbl_my_account = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'My Account')]")))
        text_my_account_esperado = "my account"
        text_my_account_actual = lbl_my_account.text.lower()
        assert text_my_account_actual == text_my_account_esperado, "ASSERT MY ACCOUNT PAGE ES VISIBLE"
        assert lbl_my_account.is_displayed() == True, "ASSERT ETIQUETA MY ACCOUNT VISIBLE"






