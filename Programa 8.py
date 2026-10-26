# Solicitar al usuario el tema de su interés
entrada = input("Ingresa el nombre de un artista, película o serie (ej. Shakira, Inception, Breaking Bad, Batman, Lionel Messi): ")

# Normalizamos el texto: pasamos a minúsculas y quitamos espacios en los extremos
tema = entrada.lower().strip()

print("\n--- INFORMACIÓN ENCONTRADA ---")

# Estructura match-case para desplegar la información detallada
match tema:
    case "shakira":
        print(" Categoría: Artista / Cantante")
        print(" País de origen: Colombia")
        print(" Discografía destacada: 'Pies descalzos', 'Dónde están los ladrones', 'Las mujeres ya no lloran'.")
        print(" Resumen: Icono global del pop latino, ganadora de múltiples premios Grammy y reconocida por su labor filantrópica.")

    case "inception" | "el origen":
        print(" Categoría: Película (Ciencia Ficción)")
        print(" Director: Christopher Nolan")
        print(" Año de estreno: 2010")
        print(" Sinopsis: Un ladrón prófugo experto en el arte de extraer secretos del subconsciente ajeno durante el sueño recibe la misión inversa: implantar una idea en la mente de un heredero.")

    case "breaking bad":
        print(" Categoría: Serie de Televisión (Drama / Suspenso)")
        print(" Creador: Vince Gilligan")
        print(" Protagonistas: Bryan Cranston (Walter White) y Aaron Paul (Jesse Pinkman)")
        print(" Resumen: Narra la transformación de un frustrado profesor de química de secundaria con cáncer terminal en un despiadado productor y traficante de metanfetamina.")

    case "batman" | "el caballero de la noche":
        print(" Categoría: Superhéroe / Personaje de Cómics")
        print(" Creadores: Bob Kane y Bill Finger (DC Comics)")
        print(" Identidad secreta: Bruce Wayne (Bruno Díaz)")
        print(" Resumen: Un multimillonario filántropo que, tras presenciar el asesinato de sus padres en su infancia, jura venganza contra el crimen protegiendo la ciudad de Gotham de noche.")

    case "lionel messi" | "messi":
        print(" Categoría: Deportista (Fútbol)")
        print(" País de origen: Argentina")
        print(" Logros clave: Campeón del Mundo (2022), múltiples Balones de Oro y leyenda histórica del FC Barcelona.")
        print(" Resumen: Considerado uno de los mejores futbolistas de todos los tiempos, famoso por su regate, visión de juego y consistencia goleadora.") 
    case _:
        print(f"XLo  sentimos, no encontramos información registrada para '{entrada}'.")
        print("Prueba ingresando uno de nuestros temas disponibles.")