class UsuarioAdoptante:
    def __init__(self, nombre, dni, email, preferencias):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = {
            "raza": preferencias.get("raza", None),
            "edad": preferencias.get("edad", None),
            "tamaño": preferencias.get("tamaño", None)
        }  #predefino preferencias para que no se rompa buscar perros por preferencias
        self.historial_adopciones = []

    def modificar_datos(self, nombre=None, email=None, preferencias=None):
        if nombre:
            self.nombre = nombre
        if email:
            self.email = email
        if preferencias:
            self.preferencias = preferencias

    def ver_historial(self):
        if not self.historial_adopciones:
            print(f"{self.nombre} no ha realizado adopciones aún.")
        else:
            print(f"Historial de adopciones de {self.nombre}:")
            for perro in self.historial_adopciones:
                print(f"- {perro.nombre} (ID: {perro.id})")

    def agregar_adopcion(self, perro):
        self.historial_adopciones.append(perro)