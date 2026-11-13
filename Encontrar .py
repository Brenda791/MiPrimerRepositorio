# Crear una lista vacia para almacenar los 8 numeros
numeros = []
# Leer 8 numero enteros desde el teclado usando un ciclo
print("Introduce 8 numeros enteros:")
for i in range(8):
    numero = int(input(f"Numero {i + 1}: "))
    numeros.append(numero)
    # Determinar el numero mayor y menor de la lista usando funciones intergradas
    mayor = max(numeros)
    menor = min(numeros)
    # Mostrar los resultados en la consola
    print(f"\nLista de numeros ingresados: {numeros}")
    print(f"El numero mayor es: {mayor}")
    print(f"El numero menor es: {menor}")