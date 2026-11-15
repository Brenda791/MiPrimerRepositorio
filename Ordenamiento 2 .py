# 1. Pedir al usuario la cantidad de elementos
n = int(input("¿Cuántos números deseas ingresar? "))

# 2. Solicitar cada número y almacenarlo en una lista
lista = []
for i in range(n):
    numero = float(input(f"Ingresa el número {i + 1}: "))
    lista.append(numero)

print(f"\nLista original: {lista}")

# 3. Implementar el método de ordenamiento burbuja (Descendente)
for i in range(n):
    for j in range(0, n - i - 1):
        # CAMBIO: Intercambiar si el elemento actual es MENOR que el siguiente
        if lista[j] < lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

# 4. Muestra la lista ordenada
print(f"Lista ordenada descendente: {lista}")