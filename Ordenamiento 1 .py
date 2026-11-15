# 1 Pedir al usuario la cantidad de elementos
n = int(input("Introduce la cantidad de elementos: "))
# 2 Solicitar cada numero y almacenarlo en una lista
lista = []
for i in range(n):
    numero = float(input(f"Ingresar el numero {i + 1}:"))
    lista.append(numero)
    print(f"\nLista original: {lista}")
# 3 Implementar el metodo de ordenamiento burbuja
for i in range(n):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
# 4 Muestra la lista ordenada
print(f"Lista ordenada ascendente: {lista}")