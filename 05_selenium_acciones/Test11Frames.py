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


class Test11Frames(BaseTest02):


    def test_switch_frames(self):
        #Abrir URL
        self.driver.get(URL_FRAMES)

        #Switch frame A by string id
        self.driver.switch_to.frame("id_frame_a") #Movernos a frame A
        text = "ESTO ESTA EN FRAME A"
        #Posterior al cambio de frame, ya se permite la busqueda de elementos
        txt_frm_a = self.driver.find_element(By.ID, "id_input-frame_a") #Busqueda de elemento
        txt_frm_a.send_keys(text) #Ingresar texto
        time.sleep(5)

        #Switch a contenido DEFAULT
        self.driver.switch_to.default_content() #Esto es para moverme a otro frame, pero primero tengo que regresar al FRAME DEFAULT

        #Switch frame B by string name
        #Posterior al camio de frame default ya se puede cambiar a otro frame
        self.driver.switch_to.frame("name_frame_b") #Busqueda de frame por su nombre
        text = "ESTO ESTA EN FRAME B"
        txt_frm_b = self.driver.find_element(By.ID, "id_input-frame_b")
        txt_frm_b.send_keys(text)
        time.sleep(3)

        #Si se desea ingresar a un frame que está dentro del frame actual, se puede cambiar
        #obtener frame C como WEBELEMENT
        frm_c = self.driver.find_element(By.ID, "id_frame_c") #Obtener el elemento C

        #Switch frame C by WEBELEMENT
        self.driver.switch_to.frame(frm_c)#Hacer cambio a frame que está dentro de un nivel al frame actual
        text = "ESTO ESTA EN FRAME C"
        txt_frm_c = self.driver.find_element(By.ID, "id_input-frame_c")
        txt_frm_c.send_keys(text)
        time.sleep(3)

        #Una vez terminado el frame dentro del frame, se tiene que regresar al frame actual
        #Switch a contenido DEFAULT
        self.driver.switch_to.default_content()

        #Interactura, escribir en el contenido default
        text = "ESTO ESTA EN EL CONENIDO DEFAULT"
        txt_contenido_default = self.driver.find_element(By.ID, "id_input-default")
        txt_contenido_default.send_keys(text)
        time.sleep(3)
