import pytest
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from helpers.data_driven import URL_BASE, URL_LOGIN, CONTRASENA, USUARIO, URL_PRODUCTO, URL_LIST_MULTI_OPTS
from helpers.BaseTest02 import BaseTest02
from helpers.generics import get_data_ui_element, select_multiple_options


class Test05SelectListas02(BaseTest02):
    # Manejo de listas
    #       Recomendado por Selenium
    #       LISTAS CON CLASE SELECT
    def test_lista_usando_select(self):
        #Abrir URL Login
        self.driver.get(URL_PRODUCTO)

        #Opcion a elegir de la lista
        opcion_esperada = "L"

        #Identificar select list
        sl_talla = self.driver.find_element(By.ID, "group_1")

        #Construir Clase Select (listas deplegables)
        lista = Select(sl_talla)

        #seleccionar opciones
        lista.select_by_visible_text(opcion_esperada) #Seleccion con texto esperados
        lista.select_by_value("2") #Selección con bali
        lista.select_by_index(0) #Selección
        lista.select_by_visible_text(opcion_esperada)
        time.sleep(5)

        #Imprimir información de web element de cada opcion
        get_data_ui_element("OPCION 1", lista.options[0])
        get_data_ui_element("OPCION 2", lista.options[1])
        get_data_ui_element("OPCION 3", lista.options[2])

        #Assert, validar que este seleccionada la opcion esperada
        opcion_actual = lista.first_selected_option.text
        assert opcion_esperada == opcion_actual, "ASSERT OPCION SELECICONADA"


    # Manejo de listas
    #       USANDO SEND KEYS
    def test_listas_con_sendkeys(self):
        # Abrir URL
        self.driver.get(URL_PRODUCTO)

        # Opcion a elegir de la lista
        opcion_esperada = "L"

        # Identificar select list
        sl_talla = self.driver.find_element(By.ID, "group_1")
        sl_talla.send_keys(opcion_esperada)
        time.sleep(5)


    # Manejo de listas
    #       USANDO SEND KEYS
    def test_multiple_options(self):
        # Abrir URL
        self.driver.get(URL_LIST_MULTI_OPTS)

        #OPCIONES A ELEGIR
        opciones = "Honda Civic,Audi TT"
        #XPATH
        xpath = "//select[@id='cars']"

        #seleccionar multiples opciones desde un metodo en la clase
        self.select_multiple_options(opciones, By.XPATH, xpath)
        time.sleep(5)
        #seleccionar multiples opciones desde un metodo en los helpers
        self.driver.refresh()
        select_multiple_options(self.driver, opciones, By.XPATH, xpath)
        time.sleep(5)


    def select_multiple_options(self, opciones, by, locator):
        multiple_options = str(opciones).split(",")
        lista = self.driver.find_element(by, str(locator))

        for opcion in multiple_options:
            Select(lista).select_by_visible_text(opcion)
            self.driver.find_element(by, str(locator)).send_keys(Keys.CONTROL)

