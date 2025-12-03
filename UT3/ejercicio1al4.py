import random

# -------------------------------
# EJERCICIO 2
# -------------------------------
def mostrarABC():
    for i in range(65, 65 + 26):
        print(chr(i), end="")
    print()

    for i in range(97, 97 + 26):
        print(chr(i), end="")
    print()


# -------------------------------
# EJERCICIO 3
# -------------------------------
def devolverAleatorio(n):
    if n <= 0:
        return random.randint(0, 999)

    mayor = 0
    for _ in range(n):
        num = random.randint(0, 999)
        if num > mayor:
            mayor = num
    return mayor


# -------------------------------
# EJERCICIO 4
# -------------------------------
def devolverNumero():
    try:
        valor = int(input("Introduce un número entero positivo: "))
    except ValueError:
        print("NO ES UN NÚMERO, VOY A DEVOLVER UN -1")
        return -1

    if valor < 0:
        print("NO ES UN NÚMERO POSITIVO, VOY A DEVOLVER UN 0")
        return 0

    return valor


# -------------------------------
# EJERCICIO 1 - MENÚ PRINCIPAL
# -------------------------------
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


# Ejecutar menú
if __name__ == "__main__":
    menu()
