class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Puntero al siguiente nodo

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Primer nodo de la lista

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza  # El nuevo nodo apunta al anterior
        self.cabeza = nuevo_nodo  # La cabeza se actualiza

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" → ")
            actual = actual.siguiente
        print("None")  # Fin de la lista

# Creamos la lista e insertamos elementos
lista = ListaEnlazada()
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)

lista.mostrar()  # Salida: 1 → 2 → 3 → None
