import os

import pytest
import time
from datetime import datetime
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from helpers.data_driven import URL_BASE, URL_LOGIN, CONTRASENA, USUARIO, URL_PRODUCTO, URL_LIST_MULTI_OPTS, URL_PLP, \
    PRODUCTO_SELECCIONAR_PLP, URL_CONTACT, DIR_ARCHIVOS, ARCHIVO_SUBIDA, URL_FRAMES, DIR_PROYECT, DIR_EVIDENCIAS
from helpers.BaseTest02 import BaseTest02
from helpers.generics import save_evidence


class Test13Screenshots(BaseTest02):


    def test_screenshot(self):
        #Abrir URL
        self.driver.get(URL_LOGIN)
        #calcular directorio y nombre de la evidenciaf
        evidencia = DIR_EVIDENCIAS + "/screenshot_" + str(time.time()) + ".png" #time.time()
        #tomar screenshot desde helpers
        self.driver.save_screenshot(evidencia)


    def test_screenshot_desde_helpers(self):
        #Nombre del TEST
        test_name = "test"
        #Abrir URLs
        self.driver.get(URL_BASE)
        #tomar screenshot desde helpers
        save_evidence(self.driver, test_name)
        #Abrir URL
        self.driver.get(URL_LOGIN)
        save_evidence(self.driver, test_name)

