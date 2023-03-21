import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from otros_ejemplos.pageobject.contact_page import ContactPage

@pytest.fixture
def browser():
    #driver = Chrome()
    options = Options()
    driver = webdriver.Chrome(chrome_options=options, executable_path="D:/ambiente/selenium_drivers/chromedriver.exe")
    sleep(5)
    yield driver
    sleep(5)
    driver.quit()

def test_fill_contact_info(browser):
    contact_page = ContactPage(browser)
    contact_page.open()
    contact_page.set_name('Nuevo Usuario de Prueba')
    contact_page.set_email('mrtesteloper@gmail.com')
    contact_page.set_message('Esta es solo una prueba')

    assert contact_page.get_name()
    assert contact_page.get_email()
    assert contact_page.get_message()