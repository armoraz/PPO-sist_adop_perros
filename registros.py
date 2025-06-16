from perro import Perro
from usuario_adoptante import UsuarioAdoptante

def registrar_perro(sistema):
    print("\n--- Registrar nuevo perro ---")
    id = input("ID: ")
    nombre = input("Nombre: ")
    raza = input("Raza: ")
    edad = int(input("Edad: "))
    tamaño = input("Tamaño: ")
    peso = float(input("Peso (kg): "))
    estado_salud = input("Estado de salud: ")
    vacunado = input("¿Está vacunado? (s/n): ").lower() == 's'
    estado = 'disponible'  # siempre inicia como disponible
    temperamento = input("Temperamento: ")

    perro = Perro(id, nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado, temperamento)
    sistema.agregar_perro(perro)
    print(f"Perro {nombre} registrado exitosamente.\n")

def registrar_usuario(sistema):
    print("\n--- Registrar nuevo usuario adoptante ---")
    nombre = input("Nombre: ")
    dni = input("DNI: ")
    email = input("Email: ")

    print("\n--- Preferencias de adopción ---")
    raza = input("Raza preferida (puede dejar vacío): ") or None
    try:
        edad = int(input("Edad preferida (puede dejar vacío): ") or 0)
    except ValueError:
        edad = None
    tamaño = input("Tamaño preferido (puede dejar vacío): ") or None

    preferencias = {
        "raza": raza,
        "edad": edad if edad != 0 else None,
        "tamaño": tamaño
    }

    usuario = UsuarioAdoptante(nombre, dni, email, preferencias)
    sistema.registrar_usuario(usuario)
    print(f"Usuario {nombre} registrado exitosamente.\n")