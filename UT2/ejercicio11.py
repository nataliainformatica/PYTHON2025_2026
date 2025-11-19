# Colores para consola
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print("Bienvenido al Mini Laberinto")
print("Responde con " + GREEN + "true" + RESET + " (sí) o " +
      RED + "false" + RESET + " (no).\n")

# Primera decisión
decision1 = input("Estás en la entrada del laberinto. ¿Quieres ir a la izquierda? "
                  f"({GREEN}true{RESET}/{RED}false{RESET}): ").lower()

if decision1 == "true":
    # Rama izquierda
    decision2 = input("\nAvanzas por la izquierda y encuentras una puerta. "
                      f"¿Quieres abrirla? ({GREEN}true{RESET}/{RED}false{RESET}): ").lower()

    if decision2 == "true":
        print(GREEN + "\n¡Has encontrado la salida secreta! ¡Ganaste!" + RESET)
    else:
        print(RED + "\nLa puerta era falsa y caes en un pozo oculto. Fin del juego." + RESET)

else:
    # Rama derecha
    decision2 = input("\nVas hacia la derecha y llegas a un puente. "
                      f"¿Quieres cruzarlo? ({GREEN}true{RESET}/{RED}false{RESET}): ").lower()

    if decision2 == "true":
        print(RED + "\nEl puente se rompe y caes en un río subterráneo. Fin del juego." + RESET)
    else:
        print(YELLOW + "\nDecides no cruzar… pero un muro se derrumba detrás de ti. ¡Estás atrapado!" + RESET)
