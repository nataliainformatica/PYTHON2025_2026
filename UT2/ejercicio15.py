import random

# Temperaturas programadas por franja (ejemplo)
man, tar, noc = 19, 21, 18

# Anotaciones de tipo (type hints) -  No obliga a Python a comprobarlo, pero ayuda al programador y al editor
def obtener_temp_programada(franja: str) -> int:
    match franja:
        case "mañana":
            return man
        case "tarde":
            return tar
        case "noche":
            return noc
        case _:
            return None

            """
            asignación múltiple (o unpacking)
            man, tar, noc = 19, 21, 18
           Python crea la tupla implícitamente y luego la "desempaqueta".
            """


def mostrar_menu():
    print("\n=== SISTEMA DE CALEFACCIÓN ===")
    print("1. Mostrar programación semanal")
    print("2. Consultar si la calefacción debería activarse")
    print("3. Salir")

def mostrar_programacion():
    print("\n--- Programación por franjas ---")
    print(f"Mañana: {man}°C")
    print(f"Tarde : {tar}°C")
    print(f"Noche : {noc}°C")

def consultar_activacion():
    dia = input("Día de la semana: ").strip().lower()

    franja = input("Franja (mañana/tarde/noche): ").strip().lower()

    temp_prog = obtener_temp_programada(franja)
    if temp_prog is None:
        print("Franja no válida.")
        return

    try:
        temp_actual = float(input("Temperatura actual: "))
    except ValueError:
        print("Introduce un número válido.")
        return

    print(f"\nTemperatura programada para {franja}: {temp_prog}°C")
    print(f"Temperatura actual: {temp_actual}°C")

    if temp_actual < temp_prog:
        print("La calefacción DEBE encenderse.")
    else:
        print("La calefacción puede permanecer apagada.")

# Bucle principal
op = ""
while op != "3":
    mostrar_menu()
    op = input("Elige una opción: ")

    match op:
        case "1":
            mostrar_programacion()

        case "2":
            consultar_activacion()

        case "3":
            print("Saliendo del sistema...")

        case _:
            print("Opción no válida.")
