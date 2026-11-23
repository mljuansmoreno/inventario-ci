import pytest

from inventario.core import Inventario


@pytest.fixture
def inventario():
    return Inventario()


def test_agregar_registra(inventario):
    inventario.agregar("café", 5)
    assert inventario.consultar("café") == 5


def test_agregar_acumula(inventario):
    inventario.agregar("pan", 2)
    inventario.agregar("pan", 3)
    assert inventario.consultar("pan") == 5


def test_retirar_descuenta(inventario):
    inventario.agregar("arroz", 8)
    inventario.retirar("arroz", 3)
    assert inventario.consultar("arroz") == 5


def test_retirar_sin_saldo(inventario):
    inventario.agregar("té", 2)
    with pytest.raises(ValueError, match="insuficientes"):
        inventario.retirar("té", 3)
    assert inventario.consultar("té") == 2


def test_retirar_desconocido(inventario):
    with pytest.raises(KeyError):
        inventario.retirar("sal", 1)
