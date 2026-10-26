# Input(Verificar edad para votar)
edad = int(input("Introduce tu edad: "))

# Vañidar si la edad es real o negativa
if edad < 0 or edad > 120:
    print("X Error: La edad ingresada es inválida o irreal.")
elif edad >= 18:
    print("SI Eres elegible para votar. ¡No olvides tu identificación oficial!")
else:
    print("NO No eres elegible para votar. Debes tener al menos 18 años.")