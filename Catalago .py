# 1. Crear el catálogo de películas (Lista de diccionarios)
catalogo_peliculas = [
    {"titulo": "Inception", "director": "Christopher Nolan", "año": 2010, "género": "Sci-Fi", "duración": 148},
    {"titulo": "The Godfather", "director": "Francis Ford Coppola", "año": 1972, "género": "Drama", "duración": 175},
    {"titulo": "Pulp Fiction", "director": "Quentin Tarantino", "año": 1994, "género": "Crimen", "duración": 154},
    {"titulo": "Spirited Away", "director": "Hayao Miyazaki", "año": 2001, "género": "Animación", "duración": 125},
    {"titulo": "Interstellar", "director": "Christopher Nolan", "año": 2014, "género": "Sci-Fi", "duración": 169},
    {"titulo": "Whiplash", "director": "Damien Chazelle", "año": 2014, "género": "Drama", "duración": 106}
]


class p:
    def __init__(self, catalogo):
        self.catalogo = catalogo

    def filtrar_por_genero(self, genero):
        """Devuelve las películas de un género, ignorando mayúsculas/minúsculas."""
        return [pelicula for pelicula in self.catalogo if pelicula["género"].lower() == genero.lower()]

    def filtrar_por_año(self, año_limite):
        """Devuelve las películas estrenadas estrictamente después del año dado."""
        return [pelicula for pelicula in self.catalogo if pelicula["año"] > año_limite]

    def ordenar_por_duracion(self, descendente=False):
        """Ordena las películas por duración, ascendente o descendente."""
        return sorted(self.catalogo, key=lambda item: item["duración"], reverse=descendente)

    def calcular_duracion_promedio(self):
        """Calcula la duración media del catálogo en minutos."""
        if not self.catalogo:
            return 0
        total_minutos = sum(pelicula["duración"] for pelicula in self.catalogo)
        return total_minutos / len(self.catalogo)


catalogo = p(catalogo_peliculas)

# --- PRUEBAS DE LAS FUNCIONES ---
print("--- Catálogo Original ---")
for pelicula in catalogo.catalogo:
    print(f"• {pelicula['titulo']} ({pelicula['año']}) - {pelicula['género']} | {pelicula['duración']} min")

print("\n 1. Filtrar por género (Sci-Fi):")
for pelicula in catalogo.filtrar_por_genero("Sci-Fi"):
    print(f"   - {pelicula['titulo']} ({pelicula['género']})")

print("\n 2. Filtrar películas después del año 2010:")
for pelicula in catalogo.filtrar_por_año(2010):
    print(f"   - {pelicula['titulo']} ({pelicula['año']})")

print("\n 3. Ordenar por duración (Ascendente):")
for pelicula in catalogo.ordenar_por_duracion(descendente=False):
    print(f"   - {pelicula['titulo']} ({pelicula['duración']} min)")

print("\n 4. Ordenar por duración (Descendente):")
for pelicula in catalogo.ordenar_por_duracion(descendente=True):
    print(f"   - {pelicula['titulo']} ({pelicula['duración']} min)")

promedio = catalogo.calcular_duracion_promedio()
print(f"\n 5. Duración promedio del catálogo: {promedio:.1f} minutos")