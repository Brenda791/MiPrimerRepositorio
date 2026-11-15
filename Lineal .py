def busqueda_lineal(lista, objetivo):
    # Recorremos la lista elemento por elemento junto con su índice
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice  # Retorna la posición en cuanto lo encuentra
            
    return -1  # Retorna -1 si recorrió toda la lista y no lo encontró

try:
    # 1. Solicitar la lista de números al usuario
    entrada_lista = input("Introduce una lista de números separados por espacios: ")
    # Convertimos la entrada de texto en una lista de números enteros
    numeros = [int(x) for x in entrada_lista.split()]
    
    if not numeros:
        print("La lista está vacía.")
    else:
        # 2. Solicitar el número a buscar
        numero_a_buscar = int(input("Introduce el número que deseas buscar: "))

        # 3. Ejecutar la búsqueda lineal
        resultado = busqueda_lineal(numeros, numero_a_buscar)

        # 4. Mostrar el resultado
        if resultado != -1:
            print(f"¡Encontrado! El número {numero_a_buscar} está en la posición (índice) {resultado}.")
        else:
            print(f"El número {numero_a_buscar} no se encuentra en la lista.")
            
except ValueError:
    print("Por favor, asegúrate de introducir únicamente números enteros válidos.")