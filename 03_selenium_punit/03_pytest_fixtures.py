import pytest
import time
from helpers.data_driven import URL_BASE, URL_LOGIN
from helpers.drivers import chrome
import helpers.data_driven

@pytest.fixture(autouse=True) #GENERAL SIEMPRE QUE SE LLAME FIXTURE
def driver_PRUEBA():
    print("\n***************************")
    print("\nBEFORE TEST")
    print("\n***************************")
    driver = chrome()
    driver.maximize_window()
    yield driver #ENVIAR HACIA DRIVER DE CHROME
    time.sleep(5)
    print("\n***************************")
    print("\nAFTER TEST")
    print("\n***************************")
    driver.quit()


@pytest.fixture(autouse=True, scope="session") #Caso de prueba
def fixtures_sesion():
    print("\n***************************")
    print("\nBEFORE SESSION")
    print("\n***************************")
    yield
    print("\n***************************")
    print("\nAFTER SESSION")
    print("\n***************************")


def test_valida_titulo(driver_PRUEBA):
    print("\nTEST VERIFICAR TITULO")
    driver_PRUEBA.get(URL_LOGIN)
    titulo_esperado = "Account Login"
    titulo_actual = driver_PRUEBA.title
    assert titulo_actual == titulo_esperado, "ASSERT TITULO DE PAGINA LOGIN"


def test_otro_test():
    print("\nOTRO TEST")
