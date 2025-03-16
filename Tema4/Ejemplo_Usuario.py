while True:
    try:
        nombre = input("Ingrese su nombre: ")
        if not nombre.isalpha():
            raise ValueError("El nombre debe contener solo letras.")

        edad = int(input("Ingrese su edad: "))
        if edad <= 0:
            raise ValueError("La edad debe ser un número positivo.")

        break  # Salimos si ambas entradas son correctas
    except ValueError as e:
        print(f"❌ Error: {e}")
    except KeyboardInterrupt:
        print("\n❌ Operación cancelada por el usuario.")
        exit()

print(f"✅ ¡Bienvenido, {nombre}! Tienes {edad} años.")
