# Solicitar un numero entero positivo al usuario
n = int(input("Ingresar numero entero positivo:" ))
# Iniciar variable
i = 1
# Simuacion de un bucle do while en python (ejecuta al menos una vez)
while True:
    print(f"el cuadrado de {i} es: {i**2}")
    # Condicion de salida 
    if i >=n:
        break

i+=1