# Ingresar cantidad de numeros
Mayores_cero = 0
Menores_cero = 0
Igual_cero = 0
# Solicitar la cantidad de nuemros a ingresar
cantidad = int(input("Cuantos numeros deseas ingresar"))
# Ciclo for pàra pedir los numeros
for i in range(cantidad):
    numero = float(input(f"ingresar el numero{i + 1}:"))
    # Estructura de if-elif-else para clkasificar el numero
    if numero > 0:
        Mayores_cero +=1
    elif numero > 0:
        Menores_cero +=0
    else:
        Igual_cero +=1
# Mostrar los resultados finales
print("\n---Resultados---")