class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, vertice1, vertice2):
        self.vertices[vertice1].append(vertice2)
        self.vertices[vertice2].append(vertice1)  # Para grafos no dirigidos

# Crear grafo
grafo = Grafo()
grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_arista("A", "B")

print(grafo.vertices)  # {'A': ['B'], 'B': ['A']}
