# sistema_adopcion.py

from perro import Perro
from usuario_adoptante import UsuarioAdoptante

class SistemaAdopcion:
    def __init__(self):
        self.perros = []
        self.usuarios = []

    # Métodos para perros
    def agregar_perro(self, perro):
        self.perros.append(perro)

    def eliminar_perro(self, id_perro):
        nueva_lista = []
        for p in self.perros:
            if p.id != id_perro:
                nueva_lista.append(p)
        self.perros = nueva_lista

    def listar_perros_disponibles(self):
        for perro in self.perros:
            if perro.estado == 'disponible':
                perro.mostrar_informacion()
                print("-" * 20)

    def buscar_perros_por_preferencias(self, preferencias):
        resultados = []
        for perro in self.perros:
            if perro.estado != 'disponible':
                continue

            if "raza" in preferencias and preferencias["raza"] != perro.raza:
                continue
            if "edad" in preferencias and preferencias["edad"] != perro.edad:
                continue
            if "tamaño" in preferencias and preferencias["tamaño"] != perro.tamaño:
                continue

            resultados.append(perro)

        return resultados

    # Métodos para usuarios
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_usuario_por_dni(self, dni):
        for usuario in self.usuarios:
            if usuario.dni == dni:
                return usuario
        return None

    # Postulación y adopción
    def postular_adopcion(self, dni_usuario, id_perro):
        usuario = self.buscar_usuario_por_dni(dni_usuario)
        perro = self.buscar_perro_por_id(id_perro)

        if usuario and perro and perro.estado == 'disponible':
            perro.cambiar_estado('reservado')
            print(f"Perro {perro.nombre} ha sido reservado por {usuario.nombre}")
        else:
            print("No se pudo reservar el perro.")

    def confirmar_adopcion(self, dni_usuario, id_perro):
        usuario = self.buscar_usuario_por_dni(dni_usuario)
        perro = self.buscar_perro_por_id(id_perro)

        if usuario and perro and perro.estado == 'reservado':
            perro.cambiar_estado('adoptado')
            usuario.agregar_adopcion(perro)
            print(f"Adopción confirmada: {usuario.nombre} adoptó a {perro.nombre}")
        else:
            print("No se pudo confirmar la adopción.")

    def buscar_perro_por_id(self, id_perro):
        for perro in self.perros:
            if perro.id == id_perro:
                return perro
        return None
