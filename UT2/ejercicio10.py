def menu_usuario():
    nombre = None
    direccion = None
    dni = None

    while True:
        print("\n*** MENÚ DE USUARIO *** ELIGE UNA OPCIÓN")
        print("1. Introduce tu nombre")
        print("2. Introduce tu dirección")
        print("3. Introduce DNI")
        print("4. Salir comprobando campos")
        print("5. Salir sin comprobar")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Introduce tu nombre: ")
        elif opcion == "2":
            direccion = input("Introduce tu dirección: ")
        elif opcion == "3":
            dni = input("Introduce tu DNI: ")
        elif opcion == "4":
            # comprobación de datos
            if not nombre or not direccion or not dni:
                print("Te falta algún dato por introducir, continúa por favor")
            else:
                print("\nDATOS CONFIRMADOS DEL USUARIO:")
                print(f"NOMBRE: {nombre}")
                print(f"DIRECCIÓN: {direccion}")
                print(f"DNI: {dni}")
                break
        elif opcion == "5":
            break
        else:
            print("Opción no válida, intenta de nuevo.")


# PROGRAMA PRINCIPAL
menu_usuario()
