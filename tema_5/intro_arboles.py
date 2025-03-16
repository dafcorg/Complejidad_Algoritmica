class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)

# Crear nodos
raiz = NodoArbol("A")
nodo_B = NodoArbol("B")
nodo_C = NodoArbol("C")
nodo_D = NodoArbol("D")

# Construir el árbol
raiz.agregar_hijo(nodo_B)
raiz.agregar_hijo(nodo_C)
nodo_B.agregar_hijo(nodo_D)

print(raiz.valor)  # A
print(raiz.hijos[0].valor)  # B
