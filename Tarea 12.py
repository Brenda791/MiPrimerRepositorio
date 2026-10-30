# Solicitar los datos al usuario
primer_numero =int(input("Introduce el primer numero: "))
diferencia =int(input("Introduce la diferemcia: "))
maximo =int(input("Introduce el numero maximo: "))
# Iniciar la variable de control con el valor de partida
actual = primer_numero
print("Secuencia aritmetica generda:")
# Simulacion de bucle do while
while True:
    # Mostrar el numero actual de la secuencia
    print(actual,end="")
    # Calcular el siguiente elemento sumando la diferencia
    actual +=diferencia
    # Condicion de salida
    if actual > maximo:
        break
    print() # Salto de linea final
