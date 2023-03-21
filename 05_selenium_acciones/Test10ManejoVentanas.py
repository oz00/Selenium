import pytest
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from helpers.data_driven import URL_BASE, URL_LOGIN, CONTRASENA, USUARIO, URL_PRODUCTO, URL_LIST_MULTI_OPTS, URL_PLP, \
    PRODUCTO_SELECCIONAR_PLP, URL_CONTACT, DIR_ARCHIVOS, ARCHIVO_SUBIDA, URL_PRODUCTO_APPLE
from helpers.BaseTest02 import BaseTest02
from helpers.generics import get_data_ui_element, switch_window_by_title_contains


class Test10ManejoVentanas(BaseTest02):


    def test_manejo_ventanas(self):
        #Abrir URL
        self.driver.get(URL_PRODUCTO_APPLE)
        print(self.driver.title)
        print(self.driver.current_window_handle)#Obtener el id de la ventana actual, id único

        #click en compartir con FACEBOOK - Abre una nueva ventana
        btn_compartir_facebook = self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@class='addthis_button_expanded']")))
        btn_compartir_facebook.click()
        btn_comp= self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@class='at-icon at-icon-facebook'][1]")))
        btn_comp.click()
        time.sleep(5)

        #Switch a Ventana Facebook
        switch_window_by_title_contains(self.driver, "Facebook")#Moverme a otra ventana por medio del titulo
        print(self.driver.title) #Obtener el título de la ventana
        print(self.driver.current_window_handle)

        #Click al boton entrar (login) de la ventana Facebook
        btn_entrar = self.wait.until(expected_conditions.element_to_be_clickable((By.NAME, "login")))
        btn_entrar.click()
        time.sleep(5)

        #Cerrar venana actual (donde se quedo switcheado selenium)
        self.driver.close()

        #Switch a venana original
        switch_window_by_title_contains(self.driver, "Apple Cinema 30")#Cambiarme a ventana original

        #Click en elemento de la ventana principal
        img_producto = self.wait.until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "thumbnail"))) #Comprobar que estoy en la página
        img_producto.click()
        time.sleep(5)


