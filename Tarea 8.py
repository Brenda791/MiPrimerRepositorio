print("--- Calculadora de Media de Números Positivos ---")
print("Introduce números positivos uno por uno. Introduce un número negativo para terminar.\n")

# Inicializar los acumuladores
suma_positivos = 0
contador_positivos = 0

# Solicitar el primer número antes de entrar al bucle
numero = float(input("Introduce un número: "))

# El ciclo continúa MIENTRAS el número sea positivo (o cero)
while numero >= 0:
    suma_positivos += numero        # Sumamos el número al total
    contador_positivos += 1         # Incrementamos el contador en 1
    
    # Solicitar el siguiente número dentro del bucle
    numero = float(input("Introduce otro número: "))

# Al salir del bucle, verificamos que se haya ingresado al menos un número positivo
if contador_positivos > 0:
      media = suma_positivos / contador_positivos
      print(f"\n¡Programa finalizado!")
      print(f"Cantidad de números positivos ingresados: {contador_positivos}")
      print(f"La media aritmética es: {media:.2f}")
else:
    print("\n¡Programa finalizado!")
    print("No se ingresó ningún número positivo, por lo que no se puede calcular la media.")