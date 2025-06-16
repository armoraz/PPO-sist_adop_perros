from sistema_adopcion.sistema_adopcion import SistemaAdopcion
from sistema_adopcion.usuario_adoptante import UsuarioAdoptante

sistema = SistemaAdopcion()

# Algunos usuarios de prueba
usuarios_prueba = [
    UsuarioAdoptante(nombre="Juan Perez", dni="12345678", email="juan@gmail.com", preferencias={"raza": "Labrador", "edad": 3, "tamaño": "Grande"}),
    UsuarioAdoptante(nombre="Ana Gomez", dni="87654321", email="ana@hotmail.com", preferencias={"raza": "Beagle", "edad": 2, "tamaño": "Mediano"}),
    UsuarioAdoptante(nombre="Carlos Lopez", dni="11223344", email="carlos@yahoo.com", preferencias={"raza": "Caniche", "edad": 1, "tamaño": "Pequeño"}),
]

for usuario in usuarios_prueba:
    sistema.registrar_usuario(usuario)

# Guardamos los usuarios (cuando implementemos persistencia)
# sistema.guardar_datos()
