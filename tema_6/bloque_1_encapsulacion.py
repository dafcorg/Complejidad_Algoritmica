class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def obtener_precio(self):
        return self.__precio

    def vender(self, cantidad):
        if cantidad <= self.__stock:
            self.__stock -= cantidad
            print(f"Venta realizada: {cantidad} unidades de {self.__nombre}")
        else:
            print("Stock insuficiente.")
