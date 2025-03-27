from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_pago(self):
        pass
      
class EmpleadoTiempoCompleto(Empleado):
    def calcular_pago(self):
        return 3000

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas):
        super().__init__(nombre)
        self.horas = horas

    def calcular_pago(self):
        return self.horas * 20
