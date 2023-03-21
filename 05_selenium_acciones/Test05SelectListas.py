import pytest
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from helpers.data_driven import URL_BASE, URL_LOGIN, CONTRASENA, USUARIO, URL_PRODUCTO, URL_LIST_MULTI_OPTS
from helpers.base_test_02 import driver, wait
from helpers.generics import get_data_ui_element, select_multiple_options


@pytest.mark.usefixtures("driver", "wait")
class Test05SelectListas:

    # Manejo de listas
    #       Recomendado por Selenium
    #       LISTAS CON CLASE SELECT
    def test_lista_usando_select(self, driver, wait):
        #Abrir URL Login
        driver.get(URL_PRODUCTO)

        #Opcion a elegir de la lista
        opcion_esperada = "Price (High > Low)"

        #Identificar select list
        sl_sort = driver.find_element(By.ID, "input-sort")

        #Construir Clase Select (listas deplegables)
        lista = Select(sl_sort)

        #seleccionar opciones
        lista.select_by_visible_text(opcion_esperada)
        time.sleep(5)
        #lista.select_by_value("http://opencart.abstracta.us:80/index.php?route=product/category&path=25_28&sort=p.model&order=DESC")
        #lista.select_by_index(5)




    # Manejo de listas
    #       USANDO SEND KEYS
    def test_listas_con_sendkeys(self, driver, wait):
        # Abrir URL Login
        driver.get(URL_PRODUCTO)

        # Opcion a elegir de la lista
        opcion_esperada = "25"

        # Identificar select list
        sl_talla = driver.find_element(By.ID, "input-limit")
        sl_talla.send_keys(opcion_esperada)
        time.sleep(3)



    # Manejo de listas
    #       USANDO SEND KEYS
    def test_multiple_options(self, driver, wait):
        # Abrir URL Login
        driver.get(URL_LIST_MULTI_OPTS)

        #OPCIONES A ELEGIR
        opciones = "Honda Civic,Audi TT"
        #XPATH
        xpath = "//select[@id='cars']"

        #Seleccionar opciones
        self.driver = driver
        #seleccionar multiples opciones desde un metodo en la clase
        self.select_multiple_options(opciones, By.XPATH, xpath)
        time.sleep(5)
        #seleccionar multiples opciones desde un metodo en los helpers
        driver.refresh()
        select_multiple_options(driver, opciones, By.XPATH, xpath)
        time.sleep(5)


    def select_multiple_options(self, opciones, by, locator):
        multiple_options = str(opciones).split(",")
        lista = self.driver.find_element(by, str(locator))

        for opcion in multiple_options:
            Select(lista).select_by_visible_text(opcion)
            self.driver.find_element(by, str(locator)).send_keys(Keys.CONTROL)

