#EJEMPLOS - Utiliza cada ejemplo por separado

#Ejemplo 1 -------------------------------------------------
def saludar():
    print("¡Hola! Bienvenido a Python.")

# Llamamos a la función
saludar()
#Fin Ejemplo 1

#Ejemplo 2 -------------------------------------------------
def saludar_nombre(nombre):
    print(f"¡Hola, {nombre}! Bienvenido a Python.")

# Llamamos a la función pasando un argumento
saludar_nombre("Carlos")
#Fin Ejemplo 2

#Ejemplo 3 -------------------------------------------------
def sumar(a, b):
    return a + b

# Llamamos a la función y almacenamos el resultado
resultado = sumar(5, 3)
print("La suma es:", resultado)
#Fin Ejemplo 3 

#Ejemplo 4 -------------------------------------------------
def potencia(base, exponente=2):
    return base ** exponente

print(potencia(4))  # Usa el valor por defecto (4^2 = 16)
print(potencia(3, 3))  # Usa el valor especificado (3^3 = 27)
#Fin Ejemplo 4

#Ejemplo 5 -------------------------------------------------
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta  # Retorna múltiples valores

# Guardamos los valores retornados
resultado_suma, resultado_resta = operaciones(10, 5)
print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
#Fin Ejemplo 5

#Ejemplo 6 -------------------------------------------------
def sumar_todos(*numeros):
    return sum(numeros)

print(sumar_todos(1, 2, 3, 4, 5))  # Resultado: 15
#Fin Ejemplo 6

#Ejemplo 7 -------------------------------------------------
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=25, ciudad="Madrid")
#Fin Ejemplo 7

#Ejemplo 8 -------------------------------------------------
doble = lambda x: x * 2

print(doble(5))  # Resultado: 10
#Fin Ejemplo 8
