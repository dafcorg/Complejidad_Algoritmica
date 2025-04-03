import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import shutil

# ------------------------
# Parámetros del algoritmo
# ------------------------
N_REINAS = 8
TAMANO_POBLACION = 100
MAX_GENERACIONES = 1000
PROB_MUTACION = 0.2
OUTPUT_DIR = "reinas_generaciones"  # Carpeta para guardar imágenes

# ------------------------
# Representación del individuo:
# Lista de 8 números, donde índice = columna y valor = fila
# Ej: [0, 4, 7, 5, 2, 6, 1, 3]
# ------------------------

def generar_individuo():
    return [random.randint(0, N_REINAS - 1) for _ in range(N_REINAS)]

# ------------------------
# Función de evaluación optimizada (O(n))
# ------------------------
def evaluar(individuo):
    n = len(individuo)
    fila_conflictos = [0] * n
    diag1 = [0] * (2 * n - 1)  # fila - col
    diag2 = [0] * (2 * n - 1)  # fila + col

    for col in range(n):
        fila = individuo[col]
        fila_conflictos[fila] += 1
        diag1[fila - col + n - 1] += 1
        diag2[fila + col] += 1

    def contar_conflictos(lista):
        return sum(x * (x - 1) // 2 for x in lista if x > 1)

    total_conflictos = (
        contar_conflictos(fila_conflictos) +
        contar_conflictos(diag1) +
        contar_conflictos(diag2)
    )

    return -total_conflictos

# ------------------------
# Selección por torneo de 3
# ------------------------
def seleccion(poblacion):
    torneo = random.sample(poblacion, 3)
    return max(torneo, key=lambda x: evaluar(x))

# ------------------------
# Cruce de un punto
# ------------------------
def cruzar(padre1, padre2):
    punto = random.randint(1, N_REINAS - 2)
    hijo = padre1[:punto] + padre2[punto:]
    return hijo

# ------------------------
# Mutación: cambiar la fila de una reina
# ------------------------
def mutar(individuo):
    if random.random() < PROB_MUTACION:
        i = random.randint(0, N_REINAS - 1)
        individuo[i] = random.randint(0, N_REINAS - 1)
    return individuo

# ------------------------
# Función para graficar el tablero
# ------------------------
def graficar_tablero(reinas, generacion, output_dir):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, N_REINAS)
    ax.set_ylim(0, N_REINAS)
    ax.set_xticks([])
    ax.set_yticks([])

    # Dibujar el tablero
    for x in range(N_REINAS):
        for y in range(N_REINAS):
            color = 'white' if (x + y) % 2 == 0 else 'gray'
            rect = patches.Rectangle((x, y), 1, 1, facecolor=color)
            ax.add_patch(rect)

    # Dibujar las reinas
    for col, row in enumerate(reinas):
        ax.text(col + 0.5, row + 0.5, '♛', fontsize=24, ha='center', va='center', color='red')

    plt.title(f'Generación {generacion}')
    plt.savefig(f"{output_dir}/gen_{generacion:03d}.png")
    plt.close()

# ------------------------
# Ejecutar el algoritmo genético
# ------------------------

# Preparar carpeta para imágenes
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.makedirs(OUTPUT_DIR)

poblacion = [generar_individuo() for _ in range(TAMANO_POBLACION)]
mejor_solucion = None
mejor_fitness = -1000

for generacion in range(MAX_GENERACIONES):
    nueva_poblacion = []

    for _ in range(TAMANO_POBLACION):
        padre1 = seleccion(poblacion)
        padre2 = seleccion(poblacion)
        hijo = cruzar(padre1, padre2)
        hijo = mutar(hijo)
        nueva_poblacion.append(hijo)

        if evaluar(hijo) == 0:
            mejor_solucion = hijo
            mejor_fitness = 0
            break

    poblacion = nueva_poblacion
    mejor_de_esta_gen = max(poblacion, key=lambda x: evaluar(x))
    graficar_tablero(mejor_de_esta_gen, generacion, OUTPUT_DIR)

    if mejor_fitness == 0:
        break

print("¡Solución encontrada!")
print("Posiciones:", mejor_solucion)
