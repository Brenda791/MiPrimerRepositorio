# 1 Solicitar el numero al usuario y convertirlo a entero
n =int("introduce el numero enterno no negativo:")
# 2 Validar que el numero no sea negativo
if n <0:
    print("Error:el factorial no esta definido para numeros enteros")
else:
# 3 El factorial de 0 es 1. Iniciamos nuestra variable acimulativa en 1
    factorial =1
# 4 Usamos un ciclo para multiplicar desde 1 hasta n
# range (1,n+1) genera numeros desde 1 hasta n de forma exacta
for i in range(1, n +1 ):
    factorial =factorial*i
# 4 Imprimir el resultado final
print(f"El factorial de {n} ({n}!) es: {factorial}")