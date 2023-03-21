from asyncio import __main__
import pytest
import unittest
import time
from helpers.data_driven import URL_BASE, URL_LOGIN
from helpers.drivers import chrome
import helpers.data_driven



#PRUEBA CON PYTEST
def test_verificar_titulo():
    driver = chrome()
    driver.get(URL_LOGIN)
    titulo_esperado = "Account Login" #titulo correcto
    titulo_actual = driver.title
    assert titulo_actual == titulo_esperado, "ASSERT TITULO DE PAGINA LOGIN"
    driver.quit()

"""#Prueba con Unittest
class prueba(unittest.TestCase):
    def test_prueba(self):
        driver = chrome()
        driver.get(URL_LOGIN)
        titulo_esperado = "Account Login"  # titulo correcto
        titulo_actual = driver.title
        self.assertEqual(titulo_actual, titulo_esperado, "ASSERT TITULO DE PAGINA LOGIN")
        driver.quit()

if __main__ == "__main__":
    unittest.main()"""