import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from helpers.data_driven import *
from basetest import BaseTest02

URL = "https://www.sicert.ipn.mx/plataforma/login.aspx"
email_esperado = "orozcozaratejesus@gmail.com"
contrasena = "A7B6936B"

class Test_Completo_sicert(BaseTest02):
    def test_sicert(self):
        #testIniciar_Sesion.inicarsesionCorrecto()

        self.driver.get(URL)

        txt_email = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@id = 'txtEmail']")))
        txt_email.send_keys(email_esperado)
        assert txt_email.get_attribute('value')== email_esperado, "Ingreso correcto de correo"

        txt_password = self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@id = 'txtPassword']")))
        txt_password.send_keys(contrasena)
        assert txt_password.get_attribute('value') == contrasena, "Ingreso correcto de contraseña"

        time.sleep(2)

        btn_entrar = self.driver.find_element(By.XPATH,"//*[@class = 'btn btn-primary' and @type='button']")
        assert btn_entrar.is_enabled() == True, "ASSERT BOTON ENTRAR HABILITADO" #Validar que esté el boton habilitado para un click
        btn_entrar.click() #Realizar click en el boton
        time.sleep(2)

        lbl_enlinea = self.driver.find_element(By.XPATH, "//*[contains(text(), 'EN LINEA')]")
        text_my_account_esperado = "EN LINEA"
        assert lbl_enlinea.text == text_my_account_esperado, "ASSERT MY ACCOUNT PAGE ES VISIBLE"
        assert lbl_enlinea.is_displayed() == True, "ASSERT ETIQUETA MY ACCOUNT VISIBLE"

        btn_detalle = self.driver.find_element(By.XPATH, "//*[@type = 'button' and @class = 'btn btn-info btn-sm']")
        assert btn_detalle.is_enabled() == True, "ASSERT BOTON DETALLE HABILITADO"
        btn_detalle.click()
        time.sleep(2)

        lbl_folio  = self.driver.find_element(By.XPATH, "//*[contains(text(), '608493')]")
        folio_esperado = "608493"
        assert lbl_folio.text == folio_esperado, "ASSERT FOLIO VISIBLE"
        assert lbl_folio.is_displayed() == True, "ASSERT ETIQUETA FOLIO"

        btn_cerrar_sesion = self.driver.find_element(By.XPATH, "//*[@id = 'btSesion']")
        assert btn_cerrar_sesion.is_enabled() == True, "ASSERT BOTON ENTRAR HABILITADO"  # Validar que esté el boton habilitado para un click
        btn_cerrar_sesion.click()  # Realizar click en el boton
        time.sleep(2)