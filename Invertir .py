# Crea una lista vacia para almacenar los 6 numeros
numeros = []
# Leer 6 numeros enteros desde el teclado usando un ciclo
print("Introduce 6 nuemros enteros:")
for i in range(6):
    numero = int(input(f"Numero {i + 1}: "))
    numeros.append(numero)
# Invertir el orden de los numeros de la lista
numeros.reverse()
# Mostrar el resultado en la consola
print(f"\nLista de numeros ingresados en orden inverso: {numeros}")