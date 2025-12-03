def mostrarABC():
    # Primera línea: A–Z
    for i in range(65, 65 + 26):
        print(chr(i), end="")
    print()

    # Segunda línea: a–z
    for i in range(97, 97 + 26):
        print(chr(i), end="")
    print()
