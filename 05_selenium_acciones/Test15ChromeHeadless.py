import os

import pytest
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from helpers.data_driven import URL_BASE, URL_LOGIN, CONTRASENA, USUARIO, URL_PRODUCTO, URL_LIST_MULTI_OPTS, URL_PLP, \
    PRODUCTO_SELECCIONAR_PLP, URL_CONTACT, DIR_ARCHIVOS, ARCHIVO_SUBIDA, URL_FRAMES, DIR_PROYECT, DIR_EVIDENCIAS
from helpers.BaseTest03 import BaseTest03
from helpers.generics import save_evidence, mouse_hover


class Test15ChromeHeadless(BaseTest03):

    def test_chrome_headless(self):
        # Nombre del TEST
        test_name = "Run Chrome Headless"

        # Abrir URL
        self.driver.get(URL_BASE)
        save_evidence(self.driver, test_name)
        self.driver.get(URL_LOGIN)
        save_evidence(self.driver, test_name)

        #Datos de login
        email_esperado = USUARIO
        password = CONTRASENA

        #Llenar text email
        txt_email = self.wait.until(expected_conditions.presence_of_element_located((By.ID, "input-email")))
        txt_email.send_keys(email_esperado)
        assert txt_email.get_attribute("value") == email_esperado, "ASSERT TEXT EMAIL ESCRITO"
        save_evidence(self.driver, test_name)

        #Llenar text password
        txt_password = self.wait.until(expected_conditions.visibility_of_element_located((By.ID, "input-password")))
        txt_password.send_keys(password)
        save_evidence(self.driver, test_name)

        #Click boton sign in
        btn_sign_in = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@type='submit' and @value='Login']")))
        btn_sign_in.click()
        save_evidence(self.driver, test_name)

        #Validar se muestre My account
        lbl_my_account = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'My Account')]")))
        text_my_account_esperado = "my account"
        text_my_account_actual = lbl_my_account.text.lower()
        assert text_my_account_actual == text_my_account_esperado, "ASSERT MY ACCOUNT PAGE ES VISIBLE"
        assert lbl_my_account.is_displayed() == True, "ASSERT ETIQUETA MY ACCOUNT VISIBLE"
        save_evidence(self.driver, test_name)
