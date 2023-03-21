import pytest
import time
from helpers.data_driven import URL_BASE, URL_LOGIN, CONTRASENA, USUARIO, URL_PRODUCTO
from helpers.BaseTest03 import BaseTest03

class TestCookies(BaseTest03):
    def test_cookie_p(self):
        self.driver.get(URL_PRODUCTO)
        #Obtener toda la información de la cookie
        self.driver.get_cookies()

        for cookie in self.driver.get_cookies():
            print("Información de cookie")
            print("Full text:", cookie)
            print("Name: ", cookie['name'])
            print("Value: ", cookie['value'])
            print("Domanin: ", cookie['domain'])
            print("Path: ", cookie['path'])
            print("Secure?: ", cookie['secure'])
            print("HTTPonly", cookie['httpOnly'])

        self.driver.delete_all_cookies()

        self.driver.refresh()
        time.sleep(5)

