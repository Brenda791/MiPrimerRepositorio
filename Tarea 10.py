print("--- Generador de Números Impares (Simulando do-while) ---")

# Solicitar el número entero positivo al usuario
numero = int(input("Introduce un número entero positivo: "))

# Inicializar el contador en 1 (el primer número impar)
contador = 1

print(f"\nNúmeros impares desde 1 hasta {numero}:")

# Iniciamos la simulación del bucle do-while
while True:
    # --- BLOQUE DE CÓDIGO (Se ejecuta al menos una vez) ---
    # Si el contador actual es impar, lo mostramos
    if contador % 2 != 0:
        print(contador, end=" ")
    
    # Incrementar el contador para la siguiente vuelta
    contador += 1
    
    # --- CONDICIÓN DE PARADA (Al final del bucle) ---
    if contador > numero:
        break  # Rompe el bucle si superamos el número ingresado

print("\n\n¡Finalizado!")
