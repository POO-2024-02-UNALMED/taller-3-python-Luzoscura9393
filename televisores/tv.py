class TV:
    _numTV = 0

    def __init__(self, _marca, _estado):
        self._marca = _marca
        self._estado = _estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self.control = None
        TV._numTV += 1
    def setMarca(self, marca):
        self._marca = marca
   
    def getMarca(self):
        return self._marca
    
    def setCanal(self, canal):
        if self._estado == True:
            if canal <= 120 and canal >= 1:
                self._canal = canal
   
    def getCanal(self):
        return self._canal
    
    def setPrecio(self, precio):
        self._precio = precio
   
    def getPrecio(self):
        return self._precio
    
    def setVolumen(self, volumen):
        if self._estado == True:
            if volumen <= 7 and volumen >= 0:
                self._volumen = volumen
   
    def getVolumen(self):
        return self._volumen
    
    def setControl(self, control):
        self.control = control
   
    def getControl(self):
        return self.control

    def setNumTV(num):
        TV._numTV = num
    
    def getNumTV():
        return TV._numTV

    def turnOff(self):
        if self._estado == True:
            self._estado = False
    
    def turnOn(self):
        if self._estado == False:
            self._estado = True
    
    def getEstado(self):
        return self._estado
    
    def canalUp(self):
        if self._estado ==True:
            if self._canal < 120:
                self._canal += 1
    
    def canalDown(self):
        if self._estado == True:
            if self._canal > 1:
                self._canal -= 1
    
    def volumenUp(self):
        if self._estado == True:
            if self._volumen < 7:
                self._volumen += 1
    
    def volumenDown(self):
        if self._estado == True:
            if self._volumen > 0:
                self._volumen -= 1
