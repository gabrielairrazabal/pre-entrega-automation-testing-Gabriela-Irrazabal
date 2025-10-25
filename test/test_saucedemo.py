import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils.helpers import login_saucedemo, get_driver


@pytest.fixture
def driver():

    # configuracion para consultar a selenium webdriver
    driver = get_driver()
    yield driver
    driver.quit() 

    
    # logeo de usuario con username y password
    # click al botón de login

def test_login(driver):
    login_saucedemo(driver)

    #Validar login exitoso verificando que se haya redirigido a la página de inventario

    assert "/inventory.html" in driver.current_url

    #verificar el título de la página
  
    titulo= driver.find_element(By.CLASS_NAME,"title").text
    assert titulo == 'Products'

def test_catalogo(driver):
    # logeo de usuario con username y password
    # click al botón de login
   
    login_saucedemo( driver )

    #Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0

    #Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)


def test_carrito(driver):
    # logeo de usuario con username y password
    # click al botón de login
    login_saucedemo( driver )
    #llevarme a la pagina del carrito de compras
    products = driver.find_elements(By.CLASS_NAME,'inventory_item')
    total_products = len(products)

    #Añadir un producto al carrito haciendo clic en el botón correspondiente
    products[0].find_elements(By.TAG_NAME,'button').click()
    
    #Verificar que el contador del carrito se incremente correctamente
    badge = driver.find_elements(By.CLASS_NAME, 'shopping_cart_badge').text
    assert badge == "1"

    #Comprobar que el producto añadido aparezca correctamente en el carrito