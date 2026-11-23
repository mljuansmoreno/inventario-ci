class Inventario:
    """Existencias por nombre de producto."""

    def __init__(self):
        self._productos = {}

    @staticmethod
    def _nombre(nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("Se requiere un nombre de producto")
        return nombre.strip()
