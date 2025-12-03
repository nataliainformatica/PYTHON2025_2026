def mostrarABC():
    pass  # Se completará en el ejercicio 2

def devolverAleatorio(n):
    pass  # Se completará en el ejercicio 3

def devolverNumero():
    pass  # Se completará en el ejercicio 4


def menu():
    while True:
        print("\nMENÚ DE OPCIONES")
        print("1. Mostrar ABC")
        print("2. Mostrar aleatorio (con 15 intentos)")
        print("3. Devolver número")
        print("s. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrarABC()

        elif opcion == "2":
            print("Número aleatorio:", devolverAleatorio(15))

        elif opcion == "3":
            print("Resultado:", devolverNumero())

        elif opcion.lower() == "s":
            print("Saliendo del programa...")
            break

        else:
            print("OPCIÓN NO VÁLIDA")
