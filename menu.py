from registros import registrar_perro, registrar_usuario
from sistema_adopcion import SistemaAdopcion

# Inicializamos el sistema
sistema = SistemaAdopcion()


def buscar_perros_para_usuario(): #Función para buscar perros según las preferencias del usuario
    print("\n--- Buscar perros según preferencias ---")
    dni = input("\nIngrese su DNI: ")
    usuario = sistema.buscar_usuario_por_dni(dni)

    if usuario:
        resultados = sistema.buscar_perros_por_preferencias(usuario.preferencias)
        if resultados:
            print("\nPerros encontrados según tus preferencias:")
            for perro in resultados:
                perro.mostrar_informacion()
                print("-" * 20)
        else:
            print("No se encontraron perros que coincidan con tus preferencias.\n")
    else:
        print("Usuario no encontrado.\n")

def postular_adopcion():
    dni = input("\nIngrese su DNI: ")
    id_perro = input("Ingrese el ID del perro a postular: ")
    sistema.postular_adopcion(dni, id_perro)

def confirmar_adopcion():
    dni = input("\nIngrese su DNI: ")
    id_perro = input("Ingrese el ID del perro a confirmar adopción: ")
    sistema.confirmar_adopcion(dni, id_perro)

def listar_perros():
    print("\n--- Lista de perros disponibles ---")
    sistema.listar_perros_disponibles()

# Menú principal
def mostrar_menu():
    while True:
        print("\n--- Sistema de Adopción de Perros ---")
        print("1. Registrar perro")
        print("2. Registrar usuario adoptante")
        print("3. Buscar perros por usuario")
        print("4. Postular adopción")
        print("5. Confirmar adopción")
        print("6. Listar perros disponibles")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_perro(sistema)
        elif opcion == "2":
            registrar_usuario(sistema)
        elif opcion == "3":
            buscar_perros_para_usuario()
        elif opcion == "4":
            postular_adopcion()
        elif opcion == "5":
            confirmar_adopcion()
        elif opcion == "6":
            listar_perros()
        elif opcion == "0":
            print("Gracias por utilizar el sistema.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")