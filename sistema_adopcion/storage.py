import json
from perro import Perro
from usuario_adoptante import UsuarioAdoptante

def guardar_datos(perros, usuarios):
    # Serializamos
    perros_serializados = [perro.__dict__ for perro in perros]
    usuarios_serializados = [
        {
            "nombre": u.nombre,
            "dni": u.dni,
            "email": u.email,
            "preferencias": u.preferencias,
            "historial_adopciones": [p.id for p in u.historial_adopciones]
        } for u in usuarios
    ]

    with open("perros.json", "w") as f:
        json.dump(perros_serializados, f, indent=4)
    
    with open("usuarios.json", "w") as f:
        json.dump(usuarios_serializados, f, indent=4)

def cargar_datos():
    perros = []
    usuarios = []

    try:
        with open("perros.json", "r") as f:
            perros_data = json.load(f)
            for p in perros_data:
                perros.append(Perro(**p))
    except FileNotFoundError:
        pass

    try:
        with open("usuarios.json", "r") as f:
            usuarios_data = json.load(f)
            for u in usuarios_data:
                usuario = UsuarioAdoptante(
                    u["nombre"], u["dni"], u["email"], u["preferencias"]
                )
                usuario.historial_adopciones = u["historial_adopciones"]  # luego resolvemos objetos
                usuarios.append(usuario)
    except FileNotFoundError:
        pass

    return perros, usuarios
