import random
def  busqueda_lineal(Lista, objetivo):
    comparaciones = 0
    for i in range(len(Lista)):
        comparaciones += 1
        if Lista[i] == objetivo:
            return i, comparaciones
    return -1, comparaciones
def busqueda_binaria(Lista, objetivo):
    comparaciones = 0
    bajo = 0
    alto = len(Lista) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        comparaciones += 1
        if Lista[medio] == objetivo:
            return medio, comparaciones
        elif Lista[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1

    return -1, comparaciones
# 1 Generar 1000 numeros aleatorios entre 1 y 10000
numeros = shorted = random.sample(range(1, 10000), 1000)
# 2 Seleccionar un numero aleatorio de la lista para buscar
# Elegimos un numero aleatorio de la lista para buscar
numero_a_buscar = random.choice(numeros)
print(f"---busacar el numero {numero_a_buscar} en la listsa---")
# 3 Ejecutar la busqueda lineal
resultado_lineal, comparaciones_lineal = busqueda_lineal(numeros, numero_a_buscar)
print("\n[Búsqueda Lineal]")
print(f"Resultado: Encontrado en el índice {numero_a_buscar}")
print(f"Número de comparaciones realizadas: {busqueda_lineal}")
# 4 Ejecutar la busqueda binaria
pos_binaria, comp_binaria = busqueda_binaria(numeros, numero_a_buscar)
print("\n[Búsqueda Binaria]")
print(f"Resultado: Encontrado en el índice {numero_a_buscar}")
print(f"Número de comparaciones realizadas: {busqueda_binaria}")