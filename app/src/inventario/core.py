class Inventario:
    """Existencias por nombre de producto."""

    def __init__(self):
        self._productos = {}

    @staticmethod
    def _nombre(nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("Se requiere un nombre de producto")
        return nombre.strip()

    @staticmethod
    def _validar_cantidad(cantidad):
        if type(cantidad) is not int or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo")
