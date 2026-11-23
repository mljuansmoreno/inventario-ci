import pytest

from inventario.core import Inventario


@pytest.fixture
def inventario():
    return Inventario()


def test_agregar_registra(inventario):
    inventario.agregar("café", 5)
    assert inventario.consultar("café") == 5
