# Crear una lista vacia para ingresar los numeros por el usuario
numero = []
# Leer 5 numeros enteros desde el teclado usando un ciclo
print("Introduce 5 numeros enteros:")
for i in range(5):
    # Solicitar el nuemro al usuario y convertirlo a entero
    n = int(input(f"Numero {i + 1}: "))
    # Agregar el numero a la lista
    numero.append(n)
    # Calcular la suma de los numeros en la lista
    suma_total = sum(numero)
    # Mostrar los resultados en la consola
    print(f"Lista de numeros ingresados: {numero}")
    print(f"La suma total de los numeros es: {suma_total}")