import pytest
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from helpers.data_driven import URL_BASE, URL_LOGIN, CONTRASENA, USUARIO, URL_PRODUCTO, URL_LIST_MULTI_OPTS, URL_PLP, \
    PRODUCTO_SELECCIONAR_PLP, URL_CONTACT, DIR_ARCHIVOS, ARCHIVO_SUBIDA
from helpers.BaseTest02 import BaseTest02
from helpers.generics import get_data_ui_element, select_multiple_options


class Test09JS(BaseTest02):


    def test_javascript(self):
        #Abrir URL
        self.driver.get(URL_LOGIN)

        #   1- JAVASCRIPT - Localizar 1 elemento y accionarlo
        self.driver.execute_script("el = document.getElementById('search'); el.value = 'MI BUSQUEDA DESDE JS';")
        time.sleep(15)

        #   2- JAVASCRIPT - Localicar elemento con WebDriver y realizar 1 accion usando JS
        txt_buscar = self.driver.find_element(By.NAME, "search")
        self.driver.execute_script("arguments[0].value = ''; arguments[0].value = arguments[1];",
                                   txt_buscar,
                                   "MI 2DA BUSQUEDA DESDE JS"
                                   )
        time.sleep(5)

    def test_js_click(self):
        # Abrir URL
        self.driver.get(URL_LOGIN)

        #identificar elemento
        #btn_sign_in = self.driver.find_element(By.XPATH,"//*[@type='submit' and @value='Login']")
        forgotten_link = self.driver.find_element(By.LINK_TEXT, "Forgotten Password")
        #click usando JS
        #self.driver.execute_script("arguments[0].click();", btn_sign_in)
        self.driver.execute_script("arguments[0].click()", forgotten_link)

        time.sleep(5)

