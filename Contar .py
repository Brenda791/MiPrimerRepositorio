# Inicializar lista vacia para almacenar los numeros ingresados por el usuario
numeros = []
pares = 0
impares = 0
print ("Introducir los 10 numero:")
for i in range(10):
    while True:
        try:
            # Solicitar al usuarioque ingrese un numero
            num = int(input(f"Introduce el número {i+1}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Por favor, introduce un número válido.")
# Bucle para contar pares e impares
for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
# Mostrar resultados
print(f"\n---Resultados---")
print(f"Lista de numeros integrados: {numeros}")
print(f"Cantidad de numeros pares:{pares}")
print(f"Cantidad de numeros impares:{impares}")