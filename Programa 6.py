# 1. Solicitar la temperatura en grados Celsius al usuario
celsius = float(input("Introduce la temperatura en grados Celsius (°C): "))
# 2. Mostramos el menú de opciones
print("\n--- MENÚ DE CONVERSIÓN ---")
print("1. Convertir a Fahrenheit")
print("2. Convertir a Kelvin")
opcion = int(input("Selecciona una opción (1 o 2): "))

# 3. Usamos match-case para realizar la conversión indicada
match opcion:
    case 1:
        resultado = (celsius * 9/5) + 32
        print(f"\n{celsius}°C equivalen a {resultado:.2f}°F (Grados Fahrenheit).")
    case 2:
        resultado = celsius + 273.15
        print(f"\n{celsius}°C equivalen a {resultado:.2f} K (Kelvin).")
    case _:
        print("\nError: Opción no válida. Por favor, selecciona 1 o 2.")