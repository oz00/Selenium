import pytest
import time
from selenium.webdriver.common.by import By
from helpers.data_driven import URL_BASE, URL_LOGIN
from helpers.drivers import chrome
from helpers.BaseTest01 import BaseTest

class Test_FindBy(BaseTest):

    # XPATH ABSOLUTO "NO RECOMENDADO (PROHIBIDO USARLO)"
    def test_by_xpath_01(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR XPATH")
        element = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[3]/div/div/div[2]/form/div/div[1]/input")#Ruta relativa desde la raíz
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # XPATH RELATIVO - TAG con multiatributo y valores de atributos
    def test_by_xpath_02_01(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR XPATH")
        #Corchete que abre, se tiene que cerrar hasta terminar todos los contenidos del multiatributo
        element = self.driver.find_element(By.XPATH, "//input[@type='text' and @id='input-email']")#TAG con atributo si es texto utilziar @
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # XPATH RELATIVO - TAG con multiatributo y valores de atributos
    def test_by_xpath_02_02(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR XPATH")
        element = self.driver.find_element(By.XPATH, "//input[@type='text' and @id='input-email' and @name='email' and @class='form-control']")
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # XPATH RELATIVO - Cualquier TAG
    def test_by_xpath_03(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR XPATH")
        element = self.driver.find_element(By.XPATH, "//*[@id='input-email']")#(*)
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # XPATH RELATIVO - Text
    def test_by_xpath_04(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR XPATH")
        element = self.driver.find_element(By.XPATH, "//*[text()='Forgotten Password']") #Para texto visible, no se requiere @
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # XPATH Relaciones - Padre-Hijos
    def test_by_xpath_05(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR XPATH")
        element = self.driver.find_element(By.XPATH, "//div/input[@id='input-email']")#Relaciones con padre e hijo se identifica con /
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # XPATH Relaciones - Hermano siguiente
    def test_by_xpath_06(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR XPATH")
        element = self.driver.find_element(By.XPATH, "//label/following-sibling::input[@id='input-email']") #following-sibling -> hermano siguiente
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # XPATH Relaciones - Hermano anterior
    def test_by_xpath_07(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR XPATH")
        element = self.driver.find_element(By.XPATH, "//div/preceding-sibling::div/input[@id='input-email']") #preceding-sibling -> hermano anterior
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # XPATH Relaciones - PARENTS (ANTERIORES)
    def test_by_xpath_08(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR XPATH")
        element = self.driver.find_element(By.XPATH, "//input[@id='input-email']/../..") #padre, abuelos, bisabuelos, etc
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # XPATH Relaciones - DESCENDIENTES
    def test_by_xpath_09(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR XPATH")
        element = self.driver.find_element(By.XPATH, "//form//input[@id='input-email']")#Descendiente: Padres, hijos, nietos, etc...
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # XPATH Relaciones - ANCESTROS
    def test_by_xpath_10(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR XPATH")
        element = self.driver.find_element(By.XPATH, "//input[@id='input-email']/ancestor::form")
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # XPATH Match - contains
    def test_by_xpath_11(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR XPATH")
        element = self.driver.find_element(By.XPATH, "//input[contains(@id, 'ass')]")
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # XPATH Match - starts with
    def test_by_xpath_12(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR XPATH")
        element = self.driver.find_element(By.XPATH, "//input[starts-with(@id, 'input-pass')]") #Comienza con...
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # XPATH Match - contains - text
    def test_by_xpath_13(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR XPATH")
        element = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Forgotten')]")
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

    # XPATH POSICION
    def test_by_xpath_14(self):
        self.driver.get(URL_LOGIN)
        print("\nOBTENER ELEMENTO POR XPATH")
        element = self.driver.find_element(By.XPATH, "(//input[@type='text'])[2]")
        assert element.is_displayed() == True, "ASSERT ELEMENTO VISIBLE"

