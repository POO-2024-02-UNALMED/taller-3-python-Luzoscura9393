class Marca:
    def __init__(self, _nombre):
        self._nombre = _nombre
   
    def setNombre(self, nombre):
        self._nombre = nombre
   
    def getNombre(self):
        return self._nombre