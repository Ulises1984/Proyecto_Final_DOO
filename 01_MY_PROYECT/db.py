from collection import Collection

class BaseDeDatosDocumental:
    def __init__(self, nombre):
        self.nombre = nombre
        self.colecciones = {}

    def crear_coleccion(self, nombre_coleccion):
        # Crea una nueva colección si no existe
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Collection(nombre_coleccion)
        else:
            print(f"La colección '{nombre_coleccion}' ya existe.")

    def obtener_coleccion(self, nombre_coleccion):
        # Devuelve la colección por nombre
        return self.colecciones.get(nombre_coleccion)

