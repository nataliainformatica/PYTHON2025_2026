def main():
    CAPACIDAD = 1000 #capacidad total de agua
    agua = 500     # agua inicial
    encendida = True
    cafes_servidos = 0

    print("Bienvenido a la Cafetera Automática\n")

    while encendida:
        print("\nOpciones:")
        print("1. Hacer café solo")
        print("2. Hacer café cortado")
        print("3. Hacer café con leche")
        print("4. Rellenar agua")
        print("5. Consultar agua")
        print("6. Consultar número de cafés servidos")
        print("7. Apagar")

        opcion = input("Elige opción: ").strip()

        match opcion:

            # Café solo (50 ml)
            case "1":
                if agua >= 50:
                    agua -= 50
                    cafes_servidos += 1
                    print("Preparando café solo… ")
                else:
                    print("No hay suficiente agua.")

            # Cortado (70 ml)
            case "2":
                if agua >= 70:
                    agua -= 70
                    cafes_servidos += 1
                    print("Preparando café cortado… ☕")
                else:
                    print("No hay suficiente agua.")

            # Café con leche (100 ml)
            case "3":
                if agua >= 100:
                    agua -= 100
                    cafes_servidos += 1
                    print("Preparando café con leche… ☕")
                else:
                    print("No hay suficiente agua.")

            # Rellenar agua
            case "4":
                cantidad = input("Cuánta agua quieres añadir (ml): ")

                if cantidad.isdigit():
                    cantidad = int(cantidad)
                    if cantidad > 0:
                        if agua + cantidad <= CAPACIDAD:
                            agua += cantidad
                            print(f"Depósito rellenado. Agua actual: {agua} ml.")
                        else:
                            print("Demasiada agua, se desbordaría.")
                    else:
                        print("La cantidad debe ser mayor que 0.")
                else:
                    print("Número no válido.")

            # Consultar agua
            case "5":
                print(f"Agua disponible: {agua} ml.")

            # Apagar
            case "6":
                print("Apagando cafetera…")
                encendida = False

            case _:
                print("Opción no válida.")

#PROGRAMA PRINCIPAL
    main()
