import pytest
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from helpers.data_driven import URL_BASE, URL_LOGIN, CONTRASENA, USUARIO, URL_PRODUCTO, URL_LIST_MULTI_OPTS, URL_PLP, \
    PRODUCTO_SELECCIONAR_PLP, URL_CONTACT, DIR_ARCHIVOS, ARCHIVO_SUBIDA,URL_FILE_UPLOAD
from helpers.BaseTest02 import BaseTest02
from helpers.generics import get_data_ui_element, select_multiple_options


class Test08UploadFile(BaseTest02):


    def test_upload_file(self):
        #Abrir URL
        #self.driver.get(URL_CONTACT)
        self.driver.get(URL_FILE_UPLOAD)

        #Obtener directorio y nombre del archivo a subir
        archivo_subida = DIR_ARCHIVOS + "/" + ARCHIVO_SUBIDA

        #Identificar text input file
        txt_archivo = self.wait.until(expected_conditions.presence_of_element_located((By.NAME, "myFile")))
        time.sleep(3)

        #enviar sendkeys con la ruta y nombre de archivo
        txt_archivo.send_keys(archivo_subida)
        time.sleep(3)

        #click al boton subir
        btn_send = self.driver.find_element(By.ID, "uploadFile")
        btn_send.click()


