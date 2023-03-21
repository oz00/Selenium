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


class Test07ElementosAnidados(BaseTest02):


    def test_seleccionar_1er_producto(self):
        #Abrir URL
        self.driver.get(URL_PLP)

        #Identificar select list
        productos = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'product-layout')]")#Posición linea de productos, Identifcar por ID
        lbl_precio = productos[0].find_element(By.XPATH, ".//*[@class='price-tax']")
        img_producto = productos[0].find_element(By.XPATH, "//*[@class='product-thumb']//*[contains(@class, 'img-responsive')]/ancestor::a")
        get_data_ui_element("ETIQUETA PRECIO DEL PRODUCTO", lbl_precio)
        get_data_ui_element("IMAGEN DEL PRODUCTO", img_producto)

        #Abrir producto haciendo ENTER en la imagen
        img_producto.send_keys(Keys.ENTER)
        time.sleep(5)


    def test_seleccionar_producto_por_nombre(self):
        #Abrir URL
        self.driver.get(URL_PLP)

        #Identificar select list
        productos = self.driver.find_elements(By.XPATH, "//*[contains(@class, 'product-layout')]")
        producto_a_seleccionar = PRODUCTO_SELECCIONAR_PLP

        index = 0
        #Iterar la lista de productos (WEBELEMENTS)
        for producto in productos:
            #obtener datos del producto, haciendo busqueda anidada
            producto_web = producto.find_element(By.XPATH, ".//h4")
            lbl_precio = producto.find_element(By.XPATH, ".//*[@class='price-tax']")
            img_producto = producto.find_element(By.XPATH, "//*[@class='product-thumb']//*[contains(@class, 'img-responsive')]/ancestor::a")
            print("\nPRODUCTO #NO: " + str(index + 1) + " => " + str(producto_web))

            #Si el producto (WEBELEMNET) en su codigo HTML contiene el texto del producto a buscar,
            #   se hace click en el producto
            if producto.get_attribute("outerHTML").find(producto_a_seleccionar) > 0 :
                producto_web.click()
                break
            index += 1

        time.sleep(5)

