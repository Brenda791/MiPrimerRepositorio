# Funcion para leer una matriz de 2x2 desde el teclado
def leer_matriz():
    matriz = []
    print("Introduce los elementos de la matriz 2x2:")
    for i in range(2):
        fila = []
        for j in range(2):
            elemento = int(input(f"Elemento [{i}][{j}]: "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz
# Leer las 2 matrices desde el teclado
matriz1 = leer_matriz()
matriz2 = leer_matriz()
# Crear una matriz resultado para almacenar la suma
matriz_resultado = [[0, 0], [0, 0]]
# Calcular la suma de las dos matrices
for i in range(2):
    for j in range(2):
        matriz_resultado[i][j] = matriz1[i][j] + matriz2[i][j]
# Mostrar la matriz resultado
print("\nMatriz resultado:")
for fila in matriz_resultado:
    print(fila)