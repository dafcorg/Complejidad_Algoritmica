class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class EmpleadoTiempoCompleto(Empleado):
    def calcular_pago(self):
        return 3000

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, horas):
        super().__init__(nombre)
        self.horas = horas

    def calcular_pago(self):
        return self.horas * 20
