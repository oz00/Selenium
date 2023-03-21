import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from helpers.data_driven import *
from helpers.BaseTest01 import BaseTest

TIME = 1

class Test01ManejoTeclado(BaseTest):
    def test_registro(self):
        self.driver.get(URL_REGISTRO)
        text_fristname = self.driver.find_element(By.ID, "input-firstname")
        text_fristname.send_keys(FIRST_NAME)
        assert text_fristname.get_attribute("value") == FIRST_NAME, "Se ingreso de manera correcta nombre"
        time.sleep(TIME)

        text_lastname = self.driver.find_element(By.ID, "input-lastname")
        text_lastname.send_keys(LAST_NAME)
        assert text_lastname.get_attribute("value") == LAST_NAME, "Se ingresó el apellido"
        time.sleep(TIME)

        text_email = self.driver.find_element(By.ID, "input-email")
        text_email.send_keys(EMAIL)
        assert text_email.get_attribute("value") == EMAIL, "Se ingreso de manera correcto mail"
        time.sleep(TIME)

        text_telefono = self.driver.find_element(By.ID, "input-telephone")
        text_telefono.send_keys(TELEFONO)
        assert text_telefono.get_attribute("value") == TELEFONO, "Se ingreso de manera correcto mail"
        time.sleep(TIME)

        text_password = self.driver.find_element(By.ID, "input-password")
        text_password.send_keys(CONTRASENA)
        assert text_password.get_attribute("value") == CONTRASENA, "Se ingreso de manera correcto mail"
        time.sleep(TIME)

        text_confpass = self.driver.find_element(By.ID, "input-confirm")
        text_confpass.send_keys(CONTRASENA)
        assert text_confpass.get_attribute("value") == CONTRASENA, "Se ingreso de manera correcto mail"
        time.sleep(TIME)

        btn_si  = self.driver.find_element(By.XPATH, "(//label/input[@type='radio'])[2]")
        btn_si.click()
        assert btn_si.is_selected() == True, "Esta seleccionado"
        time.sleep(TIME)

        boxp = self.driver.find_element(By.NAME, "agree")
        boxp.click()
        assert boxp.is_selected() == True, "Esta seleccionado"
        time.sleep(TIME)

        btn_continue = self.driver.find_element(By.XPATH, "//div/input[@type='submit' and @class = 'btn btn-primary']")
        btn_continue.click()
        time.sleep(3)
        lbl_my_account = self.driver.find_element(By.XPATH, "//div/h1[contains(text(), 'Account')]")
        text_my_account_esperado = "account"
        text_my_account_actual = lbl_my_account.text.lower()
        assert text_my_account_actual == text_my_account_esperado, "ASSERT MY ACCOUNT PAGE ES VISIBLE"
        assert lbl_my_account.is_displayed() == True, "ASSERT ETIQUETA MY ACCOUNT VISIBLE"


