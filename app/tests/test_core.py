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
