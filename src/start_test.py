from .start import soma
import pytest


def test_soma_numeros():
    """ Testing soma numbers"""
    result = soma(1, 2)
    assert result == 3


def test_soma_strings():
    """ Testing soma with strings """
    concat = soma("ca", "sa")
    assert concat == "casa"


def test_numero_string_1():
    """ Testing errors """
    with pytest.raises(TypeError):
        soma("casa", 1)


def test_numero_string_2():
    """ Testing errors """
    with pytest.raises(TypeError):
        soma(2, "akc")


def test_falta_argumentos():
    """ Testing missing arguments """
    with pytest.raises(TypeError):
        soma(10)
