class Perro:
    def __init__(self, id, nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado, temperamento):
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = estado  # 'disponible', 'reservado', 'adoptado'
        self.temperamento = temperamento

    def cambiar_estado(self, nuevo_estado):
        estados_validos = ['disponible', 'reservado', 'adoptado']
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
        else:
            print("Estado inválido")

    def mostrar_informacion(self):
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Tamaño: {self.tamaño}")
        print(f"Peso: {self.peso} kg")
        print(f"Salud: {self.estado_salud}")
        print(f"Vacunado: {'Sí' if self.vacunado else 'No'}")
        print(f"Estado: {self.estado}")
        print(f"Temperamento: {self.temperamento}")
