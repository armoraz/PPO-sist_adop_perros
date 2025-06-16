from registros import registrar_perro, registrar_usuario

def menu():
    while True:
        print("\n--- Sistema de Adopción de Perros ---")
        print("1. Registrar perro")
        print("2. Registrar usuario adoptante")
        print("3. Buscar perros según preferencias")
        print("4. Postular adopción")
        print("5. Confirmar adopción")
        print("6. Listar perros disponibles")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_perro()
        elif opcion == "2":
            registrar_usuario()
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
