# input(calcular la acalificacion final de un estudiante)
print("===calcular la calificacion final de un estudiante===")
# 1 solicitar la calificacion final del estudiante
parciales = float(input("ingresar la calificacion de los parciales (0-100): "))
proyectos = float(input("ingresar la calificacion de los proyectos (0-100): "))
examen_final = float(input("ingresar la calificacion del examen final (0-100): "))
# validar que las calificaciones esten en el rango de 0 a 100
if parciales < 0 or parciales >100:
    print("la calificacion de los parciales debe estar en el rango de 0 a 100")
if proyectos < 0 or proyectos >100:
    print("la calificacion de los proyectos debe estar en el rango de 0 a 100")
if examen_final < 0 or examen_final >100:
    print("la calificacion del examen final debe estar en el rango de 0 a 100")
else: calificar = (parciales *0.40)+(proyectos *0.30)+(examen_final *0.30)
print(f"la calificacion final del estudiante es: {calificar}")