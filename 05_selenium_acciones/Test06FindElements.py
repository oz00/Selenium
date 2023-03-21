import pytest
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from helpers.data_driven import URL_BASE, URL_LOGIN, CONTRASENA, USUARIO, URL_PRODUCTO, URL_LIST_MULTI_OPTS, URL_PLP, \
    PRODUCTO_SELECCIONAR_PLP
from helpers.BaseTest02 import BaseTest02
from helpers.generics import get_data_ui_element, select_multiple_options


class Test06FindElements(BaseTest02):


    def test_seleccionar_producto(self):
        #Abrir URL
        self.driver.get(URL_PLP)

        #Identificar select list
        productos = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'product-layout')]")
        producto_a_seleccionar = PRODUCTO_SELECCIONAR_PLP

        index = 0
        time.sleep(5)
        #Iterar la lista de productos (WEBELEMENTS)
        for producto in productos:
            #Si el producto (WEBELEMNET) en su codigo HTML contiene el texto del producto a buscar,
            #   se hace click en el producto
            if producto.get_attribute("outerHTML").find(producto_a_seleccionar) > 0 :
                get_data_ui_element("PRODUCTO: " + str(index), producto)
                producto.click()
                break
            index += 1

        time.sleep(5)

