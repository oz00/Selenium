import pytest
import time
from selenium.webdriver.common.by import By
from helpers.data_driven import URL_BASE, URL_LOGIN
from helpers.drivers import chrome
from helpers.BaseTest01 import BaseTest

class Test_FindBy(BaseTest):

    # CSS - Tag con atributo y valor en el atributo
    def test_by_css_01(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR CSS SELECTOR")
        element =self.driver.find_element(By.CSS_SELECTOR, "input[name='search']")
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # CSS - Tag con multiple atributo y valores de atributos
    def test_by_css_02(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR CSS SELECTOR")
        element = self.driver.find_element(By.CSS_SELECTOR, "input[name='search'][type='text']")
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # CSS - SIMBOLOS ESPECIALES - ID Elemento
    def test_by_css_03(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR CSS SELECTOR")
        element = self.driver.find_element(By.CSS_SELECTOR, "#input-email") # (#) Para identificar por ID
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # CSS - SIMBOLOS ESPECIALES - CLASE Elemento
    #. Clase #ID
    def test_by_css_04(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR CSS SELECTOR")
        element = self.driver.find_element(By.CSS_SELECTOR, ".form-control#input-email") # (.) Para identificar por clase, se puede completar para ID
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # CSS - SIMBOLOS ESPECIALES - cualquier TAG
    def test_by_css_05(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR CSS SELECTOR")
        element = self.driver.find_element(By.CSS_SELECTOR, "*[id='input-password']")#Cualquier TAG, se puede agregar para identificar de manera más fácil
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # CSS - RELACIONES - Padre-Hijo (notacion >)
    def test_by_css_06(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR CSS SELECTOR")
        element = self.driver.find_element(By.CSS_SELECTOR, "div > #input-password")# (>) Relaciones padre e hijo
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # CSS - RELACIONES - Hermano (notacion +)
    def test_by_css_07(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR CSS SELECTOR")
        element = self.driver.find_element(By.CSS_SELECTOR, "label + #input-password") # (+) Relaciones hermano siguiente
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # CSS - MATCH'S - Contains
    def test_by_css_08(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR CSS SELECTOR")
        element = self.driver.find_element(By.CSS_SELECTOR, "input[id *= 'assw']") # (*=) para buscar contenido (fragmento)
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # CSS - MATCH'S - Start with - ^=
    def test_by_css_09(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR CSS SELECTOR")
        element = self.driver.find_element(By.CSS_SELECTOR, "input[id ^= 'input-pa']") #(^=) inicia con (se utiliza para buscar elemento que inicie con los elementos
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # CSS - MATCH'S - ENDS with - $=
    def test_by_css_10(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR CSS SELECTOR")
        element = self.driver.find_element(By.CSS_SELECTOR, "input[id $= 'word']") # ($=) finaliza con
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # CSS - MATCH'S - Contains Word - ~=
    def test_by_css_11(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR CSS SELECTOR")
        element = self.driver.find_element(By.CSS_SELECTOR, "input[class ~= 'form-control'][id='input-email']") #(~= contenga)
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"
"""
(,) OR elegir entre atributos


"""
