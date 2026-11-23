import pytest

from inventario.core import Inventario


@pytest.fixture
def inventario():
    return Inventario()
