# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

print("¡Bienvenido al juego de adivinar el número!")
print("Pensar un número entre 1 y 100. ¿Puedes adivinar cuál es?")

# Iniciar la variable de la suposición del usuario
suposicion = 0

# El ciclo se repite MIENTRAS la suposición sea diferente al número secreto
while suposicion != numero_secreto:
    # Solicitar la suposición al usuario
    suposicion = int(input("Introduce tu suposición: "))
    
    # Comprobar si es alta, baja o si acertó
    if suposicion > numero_secreto:
        print("Demasiado alta. ¡Inténtalo de nuevo!")
    elif suposicion < numero_secreto:
        print("Demasiado baja. ¡Inténtalo de nuevo!")
    else:
        print(f"¡Felicidades! Has adivinado el número. Era el {numero_secreto}.")