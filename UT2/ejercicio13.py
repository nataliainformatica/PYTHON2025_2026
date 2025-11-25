def main():
    numero_secreto = 7
    intentos = 0
    seguir_jugando = True

    print("¡Bienvenido al juego de adivinar el número!")
    print("Pista: es un número del 1 al 10.\n")

    while seguir_jugando:
        entrada = input("Introduce un número: ")

        # Verificamos si es un dígito
        if not entrada.isdigit():
            print("Eso no es un número válido.")
            continue

        numero = int(entrada)
        intentos += 1

        match numero:
            case n if n < numero_secreto:
                print("Demasiado bajo, intenta de nuevo.")
            case n if n > numero_secreto:
                print("Demasiado alto, prueba otra vez.")
            case n if n == numero_secreto:
                print(f"¡Correcto! Lo acertaste en {intentos} intentos.")
                
                # Preguntamos si quiere jugar otra vez
                respuesta = input("¿Quieres jugar otra vez? (s/n): ").lower()

                match respuesta:
                    case "s":
                        intentos = 0
                        print("\n¡Nueva partida! Adivina el número del 1 al 10.")
                    case "n":
                        print("Gracias por jugar. ¡Hasta luego!")
                        seguir_jugando = False
                    case _:
                        print("Respuesta no válida. Salgo del juego.")
                        seguir_jugando = False
            case _:
                print("Número fuera de rango (1–10).")


#PROGRAMA PRINCIPAL

main()