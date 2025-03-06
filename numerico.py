def calcular_precio_venta(coste_producto, margen_beneficio):
    """
    Calcula el precio de venta de un producto dado su coste y el margen de beneficio.
    
    :param coste_producto: (float) Costo del producto
    :param margen_beneficio: (float) Margen de beneficio en porcentaje
    :return: (float) Precio de venta del producto
    """
    if margen_beneficio >= 100:
        raise ValueError("El margen de beneficio no puede ser 100% o más, ya que el denominador sería cero o negativo.")

    # Paso 1: Convertir el margen de beneficio a decimal
    margen_decimal = margen_beneficio / 100

    # Paso 2: Calcular el denominador (1 - margen_decimal)
    denominador = 1 - margen_decimal

    # Paso 3: Calcular el precio de venta
    precio_venta = coste_producto / denominador

    return precio_venta

# Entrada del usuario
coste = float(input("Ingrese el coste del producto: "))
margen = float(input("Ingrese el margen de beneficio (%): "))

try:
    precio = calcular_precio_venta(coste, margen)
    print(f"El precio de venta del producto es: {precio:.2f}")
except ValueError as e:
    print(e)
