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
