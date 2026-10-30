# 1. Solicitar la palabra al usuario
palabra = input("Introduce una palabra: ")

# 2. Inicializar el contador en cero
contador_a = 0

# Convertir la palabra a minúsculas para contar tanto las 'A' como las 'a'
palabra_lista = palabra.lower()

# 3. Recorrer la palabra letra por letra con un ciclo for
for letra in palabra_lista:
    if letra == 'a' or letra == 'á':  # Consideramos también la 'a' con acento
        contador_a = contador_a + 1    # Incrementamos el contador en 1
# 4. Imprimir el resultado final
print(f" La letra 'a' aparece {contador_a} veces en la palabra '{palabra}'.")