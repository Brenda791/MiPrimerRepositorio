# Solicitar el numero al usuario y convertirlo a entero
numero =int(input("Introduce un numero entero:"))
# Guardar el numero original
numero_original =numero
# Usamos valor absoluto por si el numero es negativo
numero =abs(numero)
#Si el numero es 0, tiene un digito
if numero ==0:
    cantidad_digitos =1
else:
    cantidad_digitos =0
# Dividir consecutivamente entre 10 hasta llegar a 0
while numero >0:
    numero//=10 # Division entera (eliminar el ultimo digito)
    cantidad_digitos +=1
    # Mostrar el resultado
    print (f"El numero{numero_original}tiene {cantidad_digitos}digitos.")