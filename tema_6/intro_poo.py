from abc import ABC, abstractmethod

# Abstracción 
# Este es el guion, con los espacios vacíos
class Vehiculo(ABC):  # ABC = Es un guion base, abstracto
    def __init__(self, marca, modelo):
        self.__marca = marca          # Encapsulación
        self.__modelo = modelo

    def get_marca(self):
        return self.__marca

    def set_marca(self, nueva_marca):
        self.__marca = nueva_marca

    @abstractmethod
    def arrancar(self):              # Método abstracto
        pass  # "pass" significa: aquí va algo, pero lo pone cada actor


# Herencia + Polimorfismo
class Carro(Vehiculo):
    def arrancar(self):
        print(f"El carro {self.get_marca()} arranca con llave.")

class Moto(Vehiculo):
    def arrancar(self):
        print(f"La moto {self.get_marca()} arranca con botón.")

# Uso del sistema
vehiculos = [
    Carro("Toyota", "Corolla"),
    Moto("Yamaha", "R15")
]

for v in vehiculos:
    v.arrancar()  # Polimorfismo en acción
