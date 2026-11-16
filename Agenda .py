class encontrados(list):
    """Contenedor útil para los resultados de búsqueda de contactos."""

    def agregar(self, contacto):
        if not isinstance(contacto, dict):
            raise TypeError("El contacto debe ser un diccionario.")
        self.append(contacto)
        return contacto

    def buscar(self, nombre_buscar):
        texto = (nombre_buscar or "").strip()
        if not texto:
            return self.__class__()
        return self.__class__([
            contacto for contacto in self
            if texto.lower() in str(contacto.get("Nombre", "")).lower()
 ])

    def limpiar(self):
        self.clear()
        return self

    def listar(self):
        return sorted(self, key=lambda contacto: str(contacto.get("Nombre", "")).lower())


# Inicializar la agenda con una lista vacia para almacenar los diccionarios
agenda_contactos = [
    {
        "Nombre": "Ana", 
        "Teléfono": "555-1001",
        "Email": "ana@correo.com",
    },
    {
        "Nombre": "Luis",
        "Teléfono": "555-2002",
        "Email": "luis@correo.com",
    },
]


def agregar_contacto(nombre, telefono, email):
    """Crea un diccionario con los datos del contacto y lo añade a la lista."""
    nombre = nombre.strip()
    telefono = telefono.strip()
    email = email.strip()

    for contacto in agenda_contactos:
        if contacto.get("Nombre", "").strip().lower() == nombre.lower():
            print(f"\n El contacto '{nombre}' ya existe en la agenda.")
            return

    nuevo_contacto = {
        "Nombre": nombre,
        "Teléfono": telefono,
        "Email": email,
    }
    agenda_contactos.append(nuevo_contacto)
    print(f"\n Contacto '{nombre}' agregado con éxito.")


def buscar_contacto(nombre_buscar):
    """Busca un contacto por su nombre o coincidencia parcial."""
    termino = (nombre_buscar or "").strip()
    resultados = encontrados(
        contacto for contacto in agenda_contactos
        if termino.lower() in contacto["Nombre"].lower()
    )

    if resultados:
        print(f"\nResultados para '{nombre_buscar}':")
        for c in resultados:
            print(f"- {c['Nombre']} | Tel: {c['Teléfono']} | Email: {c['Email']}")
    else:
        print(f"\n No se encontró ningún contacto que coincida con '{nombre_buscar}'.")


def eliminar_contacto(nombre_eliminar):
    """Busca un contacto por nombre exacto y lo remueve de la lista."""
    for contacto in agenda_contactos:
        if contacto["Nombre"].lower() == nombre_eliminar.strip().lower():
            agenda_contactos.remove(contacto)
            print(f"\n El contacto '{contacto['Nombre']}' ha sido eliminado.")
            return
    print(f"\n No se encontró el contacto '{nombre_eliminar}' para eliminar.")


def listar_contactos():
    """Muestra en pantalla todos los contactos ordenados alfabéticamente.""" if not agenda_contactos:
    print("\n La agenda está vacía.")
    return

    # Ordenamos la lista temporalmente por el campo 'Nombre' para mostrarla bonita
    agenda_ordenada = sorted(agenda_contactos, key=lambda x: x["Nombre"])

    print("\n=================== AGENDA DE CONTACTOS ===================")
    print(f"{'Nombre':<20} | {'Teléfono':<15} | {'Email':<25}")
    print("-" * 65)
    for c in agenda_ordenada:
        print(f"{c['Nombre']:<20} | {c['Teléfono']:<15} | {c['Email']:<25}")
    print("===========================================================")


# --- MENÚ INTERACTIVO DE USUARIO ---
def menu():
    while True:
        print("\n--- MENÚ AGENDA ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Listar todos los contactos")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == "1":
            nom = input("Nombre completo: ")
            tel = input("Teléfono: ")
            em = input("Email: ")
            agregar_contacto(nom, tel, em)
        elif opcion == "2":
            nom_b = input("Introduce el nombre (o parte de él) a buscar: ")
            buscar_contacto(nom_b)
        elif opcion == "3":
            nom_e = input(
                "Introduce el nombre exacto del contacto a eliminar: "
            )
            eliminar_contacto(nom_e)
        elif opcion == "4":
            listar_contactos()
        elif opcion == "5":
            print("\n ¡Hasta luego!")
            break
        else:
            print("\n Opción no válida. Intenta de nuevo.")


# Ejecutar el menú principal si se corre el archivo
if __name__ == "__main__":
    menu()