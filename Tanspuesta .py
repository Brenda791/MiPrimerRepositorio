# Crea una matriz vacia para la matriz original
matriz_original = []
# Leer los elementos de la matriz 3x3 desde el teclado usando un ciclo
print("Introduce los elementos de la matriz 3x3:")
for i in range(3):
    fila= []
    for j in range(3):
        elemento = int(input(f"Elemento [{i}][{j}]: "))
        fila.append(elemento)
    matriz_original.append(fila)
    # Crear una matriz vacia para almacenar la transpuesta
    matriz_transpuesta ={{0,0,0},{0,0,0},{0,0,0}}
    # Calcular la transpuseta intercambiando filas por columnas
    for i in range(3):
        for j in range(3):
            matriz_transpuesta[i][j] = matriz_original[j][i]
            # Mostrar la matriz original
            print("/nMatriz original:")
            for fila in matriz_original:
                print(fila)
            # Mostrar la matriz transpuesta
            print("/nMatriz transpuesta:")
            for fila in matriz_transpuesta:
                print(fila)