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

    def agregar(self, nombre, cantidad):
        nombre = self._nombre(nombre)
        self._validar_cantidad(cantidad)
        producto = self._productos.setdefault(nombre, {"cantidad": 0})
        producto["cantidad"] += cantidad

    def consultar(self, nombre):
        return self._productos[self._nombre(nombre)]["cantidad"]

    def retirar(self, nombre, cantidad):
        nombre = self._nombre(nombre)
        self._validar_cantidad(cantidad)
        if self.consultar(nombre) < cantidad:
            raise ValueError("Existencias insuficientes")
        self._productos[nombre]["cantidad"] += cantidad
