print("--- Detector de Vocales y Consonantes ---")
print("Introduce letras una por una. Presiona la barra espaciadora y Enter para salir.\n")

# Solicitamos la primera entrada antes de entrar al bucle
entrada = input("Introduce una letra: ")

# El ciclo continúa MIENTRAS la entrada no sea un espacio en blanco
while entrada != " ":
    
    # Aseguramos de que el usuario haya ingresado solo una letra y no esté vacío
    if len(entrada) == 1 and entrada.isalpha():
        # Convertimos a minúscula para simplificar la evaluación
        letra = entrada.lower()
        
        # Verificar si es una vocal
        if letra in "aeiouáéíóúü":
            print(f"La letra '{entrada}' es una VOCAL.\n")
        else:
            print(f"La letra '{entrada}' es una CONSONANTE.\n")
    else:
        print("Entrada no válida. Por favor, introduce solo una letra del abecedario.\n")
    
    # Solicitar la siguiente letra dentro del bucle
    entrada = input("Introduce otra letra: ")
print("\n¡Programa finalizado por ingreso de espacio!")