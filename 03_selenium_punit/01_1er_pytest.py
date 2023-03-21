import pytest

def un_metodo():
    return 1

def test_1():
    #un metodo no es ejecutado como test ya que los test deben tener el prefijo "test_"
    un_metodo()
    print("\nprimer test")


def test_2():
    print("\nsegundo test")


def test_fallar_prueba():
    pytest.fail("\nTEST FALLIDO POR QUE SI")


def test_agregar_productos_carrito():
    print("\ntest deberia tener nombre descriptivo (nombre del metodo)")
    print("test agregar productos a carrito de compras")



def test_cambiar_cantidad_productos_carrito():
    print("\ntest deberia tener nombre descriptivo (nombre del metodo)")
    print("test cambiar cantidad de productos en el carrito de compras")


def test_eliminar_carrito():
    print("\ntest deberia tener nombre descriptivo (nombre del metodo)")
    print("test eliminar el carrito de compras")
