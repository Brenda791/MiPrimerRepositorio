def obtener_datos_estudiante():
    print("=== Registro de Nuevo Estudiante ===\n")

    # Solicitar datos de texto de forma directa
    nombre = input("Introduce el nombre completo: ").strip()

    # Validar la edad para asegurar que sea un número entero
    while True:
        try:
            edad = int(input("Introduce la edad: "))
            if edad > 0:
                break
            print("Por favor, introduce una edad válida mayor a 0.")
        except ValueError:
            print("Error: La edad debe ser un número entero.")

    carrera = input("Introduce la carrera: ").strip()
      # Validar el promedio para asegurar que sea un número decimal
    while True:
        try:
            promedio = float(input("Introduce el promedio (0.0 - 10.0): "))
            if 0.0 <= promedio <= 10.0:
                break
            print("Por favor, introduce un promedio en el rango de 0.0 a 10.0.")
        except ValueError:
            print("Error: El promedio debe ser un número con o sin decimales.")

    # Almacenar los datos recolectados en un diccionario
    estudiante = {
        "Nombre": nombre,
        "Edad": edad,
        "Carrera": carrera,
        "Promedio": promedio,
    }

    return estudiante
def mostrar_ficha(estudiante):
    # Mostrar la ficha del estudiante de forma formateada
    print("\n" + "=" * 40)
    print("         FICHA DEL ESTUDIANTE         ")
    print("=" * 40)
    for clave, valor in estudiante.items():
        # Formatear el promedio a dos decimales en caso de ser necesario
        if clave == "Promedio":
            print(f"{clave:<12}: {valor:.2f}")
        else:
            print(f"{clave:<12}: {valor}")
    print("=" * 40)


# Ejecución del programa
estudiante_registrado = obtener_datos_estudiante()
mostrar_ficha(estudiante_registrado)