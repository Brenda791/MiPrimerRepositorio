# Solicitar el número de mes al usuario
mes = int(input("Introduce el número de mes (1 - 12): "))

# Determinar la estación del año usando match-case
match mes:
    case 3 | 4 | 5:
        estacion = "Primavera"
    case 6 | 7 | 8:
        estacion = "Verano"
    case 9 | 10 | 11:
        estacion = "Otoño"
    case 12 | 1 | 2:
        estacion = "Invierno"
    case _:
        estacion = "Mes no válido"

# Mostramos el resultado en pantalla
if estacion == "Mes no válido":
    print("Error: El número introducido debe estar entre 1 y 12.")
else:
    print(f"La estación correspondiente es: {estacion}")