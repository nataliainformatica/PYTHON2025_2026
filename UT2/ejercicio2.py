def validar_contraseña(contraseña):
    # 1️Longitud entre 8 y 20 caracteres
    if len(contraseña) < 8 or len(contraseña) > 20:
        return False

    # Variables para comprobar los requisitos
    tiene_mayus = False
    tiene_minus = False
    tiene_numero = False
    tiene_raro = False

    # 2️Recorremos carácter a carácter
    for c in contraseña:
        if 'A' <= c <= 'Z':
            tiene_mayus = True
        elif 'a' <= c <= 'z':
            tiene_minus = True
        elif '0' <= c <= '9':
            tiene_numero = True
        elif c in "$%_*":
            #comprobar si c está en la cadena "$%_*"
            tiene_raro = True

    # Devolvemos True solo si TODOS los requisitos se cumplen
    if tiene_mayus and tiene_minus and tiene_numero and tiene_raro:
        return True
    else:
        return False


# Programa principal
pwd = input("Introduce una contraseña: ")

if validar_contraseña(pwd):
    print("Contraseña válida")
else:
    print("Contraseña no válida")
