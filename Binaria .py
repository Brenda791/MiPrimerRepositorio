def busqueda_binaria (lista,objetivo):
    bajo = 0
    alto = len(lista) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1

    return -1
1 # Definir una lista de numeros desordenados
numeros = [5,2,9,1,5,6]
numeros.sort()  # Ordenar la lista antes de realizar la búsqueda binaria
print("Listas ordenadas:", numeros)
# Solicitar al usuario que ingrese el numero a buscar
try:
    numero_a_buscar = int(input("Introduce el numero que deseas buscar: "))
    # Ejecutar la búsqueda binaria
    resultado = busqueda_binaria(numeros, numero_a_buscar)
    # Mostrar el resultado
    if resultado != -1:
        print(f"¡Encontrado! El número {numero_a_buscar} está en la posición (índice) {resultado}.")
    else:
        print(f"El número {numero_a_buscar} no se encuentra en la lista.")
except ValueError:
    print("Por favor, asegúrate de introducir un número entero válido.")