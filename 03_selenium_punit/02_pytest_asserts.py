import pytest


def test_assert_numeros():
    valor_actual = 1
    valor_esperado = 1
    assert valor_actual == valor_esperado, "VALIDACION DE NUMEROS IGUALES"
    #assert valor_actual == 2, "VALIDACION DE NUMEROS IGUALES"


def test_assert_strings():
    valor_actual = "selenium y python son geniales"
    valor_esperado = "selenium y python son geniales"
    assert valor_actual == valor_esperado, "VALIDACION DE TEXTOS IGUALES"
    #assert valor_actual == "otro valor", "VALIDACION DE TEXTOS IGUALES"


def test_assert_boleanos():
    valor_actual = True
    valor_esperado = True
    assert valor_actual == valor_esperado, "VALIDACION DE BOLEANOS IGUALES"
    #assert valor_actual == "otro valor", "VALIDACION DE BOLEANOS IGUALES"