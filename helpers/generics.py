from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys, ActionChains
import time
from datetime import date
import os
from helpers.data_driven import DIR_EVIDENCIAS


#Imprimir propiedades de un WebElement
def get_data_ui_element(nombre_ui_element, ui_element):
    marker = "*************************************"
    print("\n")
    print(marker)
    print("Nombre UI Element: " + nombre_ui_element)
    print(marker)
    print("Outer HTML: " + ui_element.get_attribute("outerHTML"))
    print("Inner HTML: " + ui_element.get_attribute("innerHTML"))
    if not (ui_element.get_attribute("value") is None):
        print("Value: " + ui_element.get_attribute("value"))
    print("Text: " + ui_element.text)
    print("Tag: " + ui_element.tag_name)
    print("Location: " + str(ui_element.location))
    print("Size: " + str(ui_element.size))
    print("Displayed?: " + str(ui_element.is_displayed()))
    print("Selected?: " + str(ui_element.is_selected()))
    print("Enabled?: " + str(ui_element.is_enabled()))
    print(marker)


#Seleccionar multiples opciones de un select list
def select_multiple_options(driver, opciones, by, locator):
    multiple_options = str(opciones).split(",")
    lista = driver.find_element(by, str(locator))

    for opcion in multiple_options:
        Select(lista).select_by_visible_text(opcion)
        driver.find_element(by, str(locator)).send_keys(Keys.CONTROL)


#Switch a windows si la ventana contiene parte del titulo
def switch_window_by_title_contains(driver, window_title):
    result = False

    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if driver.title.find(window_title) > 0:
            result = True
            break

    return result


#Switch a windows si la ventana contiene parte del titulo
def save_evidence(driver, test_name):
    try:
        #nombre unico de imagen
        ts = time.time()
        #calcular fecha de ejecucion
        today = date.today()
        fecha = today.strftime("%Y_%m_%d")
        # Obtener path de evidencias
        path_evidence = DIR_EVIDENCIAS + "/" + fecha + "/" + test_name
        # Calcular path + archivo evidencias
        file_evidence = path_evidence + "/" + str(ts) + ".png"
        # crear directorio de evidencias si no existe
        if not os.path.exists(path_evidence):
            os.makedirs(path_evidence)
        # tomar screenshot
        driver.save_screenshot(file_evidence)

    except FileExistsError:
        print("El directorio para almacenar la evidencia ya existia")
    except:
        print("Error al tomar screenshot de evidencia")


# Mouse Hover sobre un web element
def mouse_hover(driver, ui_element):
    try:
        ActionChains(driver).move_to_element(ui_element).perform()
    except:
        raise Exception("Error al hacer mouse hover")

