# SolicitaR la calificacion al usuario y convertirla a numero decimal)
calificacion = float(input("Introduce tu calificacion numerica: "))

# Evaluar el rango de la calificacion de mayor a menor
if calificacion >=90: and calificacion <100:
    letra ="A"
if calificacion >= 80:
    letra ="B"
if calificacion >= 70:
    letra ="C"
if calificacion >= 60:
    letra ="D"
if calificacion >=0:
    letra ="F"
else:
    letra ="Invalida(no puede ser menor que 0)"

    # Mostrar el resultado en la pantalla
    print(f"Tu calificacion es:{letra}")