import os

import pytest
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from helpers.data_driven import URL_BASE, URL_LOGIN, CONTRASENA, USUARIO, URL_PRODUCTO, URL_LIST_MULTI_OPTS, URL_PLP, \
    PRODUCTO_SELECCIONAR_PLP, URL_CONTACT, DIR_ARCHIVOS, ARCHIVO_SUBIDA, URL_FRAMES, DIR_PROYECT, DIR_EVIDENCIAS
from helpers.BaseTest02 import BaseTest02
from helpers.generics import save_evidence, mouse_hover


class Test14MouseHover(BaseTest02):

    def test_mousehover(self):
        # Nombre del TEST
        test_name = "Mouse Hover"
        # Abrir URL
        self.driver.get(URL_BASE)
        save_evidence(self.driver, test_name)

        #Obtener elementos
        menu = self.driver.find_element(By.XPATH, "//a[text()='Desktops']")
        submenu = self.driver.find_element(By.XPATH, "//a[text()='Mac (1)']")

        ActionChains(self.driver)\
            .move_to_element(menu)\
            .pause(3)\
            .move_to_element(submenu)\
            .pause(3)\
            .click(submenu)\
            .perform()

        time.sleep(5)
        save_evidence(self.driver, test_name)

    def test_mousehover_desde_helpers(self):
        # Nombre del TEST
        test_name = "Mouse Hover Desde Helper"
        # Abrir URL
        self.driver.get(URL_BASE)
        save_evidence(self.driver, test_name)

        menu = self.driver.find_element(By.XPATH, "//a[text()='Components']")
        mouse_hover(self.driver, menu)
        save_evidence(self.driver, test_name)

        submenu = self.driver.find_element(By.XPATH, "//a[text()='Monitors (2)']")
        mouse_hover(self.driver, submenu)
        save_evidence(self.driver, test_name)
        submenu.click()

        time.sleep(5)
        save_evidence(self.driver, test_name)
