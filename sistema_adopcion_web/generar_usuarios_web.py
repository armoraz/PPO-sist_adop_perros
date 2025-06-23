# populate_dummy_data.py

import os
import django
import random

# Setear entorno Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema_adopcion_web.settings")
django.setup()

# Importar modelos
from adopciones.models import Perro, UsuarioAdoptante

# Opciones de datos dummy
razas = ["Labrador", "Bulldog", "Beagle", "Caniche", "Galgo"]
tamaños = ["pequeño", "mediano", "grande"]
temperamentos = ["Tranquilo", "Juguetón", "Protector", "Sociable"]
estados = ['disponible', 'reservado', 'adoptado']

# Crear perros
for i in range(20):
    perro = Perro(
        nombre=f"Perro{i+1}",
        raza=random.choice(razas),
        edad=random.randint(1, 12),
        tamaño=random.choice(tamaños),
        peso=round(random.uniform(5.0, 35.0), 1),
        estado_salud="Saludable",
        vacunado=random.choice([True, False]),
        estado=random.choice(estados),
        temperamento=random.choice(temperamentos)
    )
    perro.save()
    print(f"[+] Perro creado: {perro.nombre} ({perro.estado})")

# Crear usuarios
for i in range(10):
    usuario = UsuarioAdoptante(
        nombre=f"Usuario{i+1}",
        dni=f"{random.randint(20000000, 50000000)}",
        email=f"usuario{i+1}@correo.com",
        preferencias_raza=random.choice(razas),
        preferencias_edad=random.randint(1, 12),
        preferencias_tamaño=random.choice(tamaños)
    )
    usuario.save()
    print(f"[+] Usuario creado: {usuario.nombre}")
