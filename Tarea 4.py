# Recorrer los números del 1 al 100 usando range
# Recordando que el límite superior no se incluye, por eso usamos 101
for i in range(1, 101):
    
    # Verificar si el número es divisible exactamente entre 3 y entre 5
    if i % 3 == 0 and i % 5 == 0:
        print(f"El número {i} es divisible por 3 y por 5")