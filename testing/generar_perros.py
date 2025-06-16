from sistema_adopcion.sistema_adopcion import SistemaAdopcion
from sistema_adopcion.perro import Perro

sistema = SistemaAdopcion()

# Algunos perros de prueba
perros_prueba = [
    Perro(nombre="Luna", raza="Labrador", edad=3, tamaño="Grande", peso=25, estado_salud="Bueno", vacunado=True, temperamento="Tranquilo", id="P001"),
    Perro(nombre="Max", raza="Beagle", edad=2, tamaño="Mediano", peso=15, estado_salud="Excelente", vacunado=True, temperamento="Activo", id="P002"),
    Perro(nombre="Rocky", raza="Pitbull", edad=4, tamaño="Grande", peso=30, estado_salud="Bueno", vacunado=False, temperamento="Protector", id="P003"),
    Perro(nombre="Nina", raza="Caniche", edad=1, tamaño="Pequeño", peso=5, estado_salud="Excelente", vacunado=True, temperamento="Juguetón", id="P004"),
]

for perro in perros_prueba:
    sistema.cargar_perro(perro)

# Guardamos los perros (una vez tengamos persistencia)
# sistema.guardar_datos()
