import time
from helpers.data_driven import URL_BASE, URL_LOGIN
from helpers.drivers import chrome
import helpers.data_driven

driver = chrome()

#maximizar
driver.maximize_window()

#abrir url's
driver.get("https://www.google.com")
time.sleep(3)
driver.get("http://opencart.abstracta.us")
time.sleep(3)
driver.get(URL_LOGIN)
time.sleep(3)

#simular botones del navegador < atras
driver.back()
time.sleep(3)
#simular botones del navegador > siguiente
driver.forward()
time.sleep(3)
#simular botones del navegador > refresh
driver.refresh()
time.sleep(3)

#obtener url actual
url_actual = driver.current_url
print(url_actual)

#obtener titulo de la pagina actual
titulo_pagina = driver.title
print(titulo_pagina)

#obtener codigo fuente de la pagina
codigo_fuente = driver.page_source

#matar sesion selenium (cerrar todas las ventanas)
driver.quit()
