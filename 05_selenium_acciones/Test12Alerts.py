import pytest
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from helpers.data_driven import URL_BASE, URL_LOGIN, CONTRASENA, USUARIO, URL_PRODUCTO, URL_LIST_MULTI_OPTS, URL_PLP, \
    PRODUCTO_SELECCIONAR_PLP, URL_CONTACT, DIR_ARCHIVOS, ARCHIVO_SUBIDA, URL_FRAMES
from helpers.BaseTest02 import BaseTest02
from helpers.generics import get_data_ui_element, switch_window_by_title_contains


class Test12Alerts(BaseTest02):


    def test_alerts(self):
        #Abrir URL
        self.driver.get(URL_LOGIN)

        #Crear ALERTA DUMMY con JS
        self.driver.execute_script("alert('TEST ALERT');")
        time.sleep(3)

        #Esperar y Aceptar la alerta
        self.wait.until(expected_conditions.alert_is_present()) #Detectar si alerta esta presente
        self.driver.switch_to.alert.accept()

        #Crear confirmo dummy con js, prueba
        self.driver.execute_script("confirm('presionando btn')")
        time.sleep(3)

        #Crear ALERTA DUMMY con JS
        self.driver.execute_script("alert('TEST ALERT 2');")
        time.sleep(3)

        #Esperar y Get Text de la alerta
        self.wait.until(expected_conditions.alert_is_present())
        text = self.driver.switch_to.alert.text
        print("\n" + text)

        #Descartar Cerrar la alerta
        self.driver.switch_to.alert.dismiss()

