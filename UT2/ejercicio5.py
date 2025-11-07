def calcular_digito_control(codigo):
    n = len(codigo)

    # EAN-8: usa los primeros 7 dígitos
    if n == 8:
        suma = 0
        for i in range(7):
            digito = int(codigo[i])
            if i % 2 == 0:
                suma += digito * 3
            else:
                suma += digito
        check = (10 - (suma % 10)) % 10
        #devolvemos el dígito de control
        return check

    # EAN-13: usa los primeros 12 dígitos
    elif n == 13:
        suma = 0
        for i in range(12):
            digito = int(codigo[i])
            if i % 2 == 0:
                suma += digito
            else:
                suma += digito * 3
        check = (10 - (suma % 10)) % 10
         #devolvemos el dígito de control
        return check

    else:
        return None


def obtener_pais(prefijo):
    prefijo = int(prefijo)
    if 0 <= prefijo <= 19:
        return "EE.UU."
    elif 30 <= prefijo <= 37:
        return "Francia"
    elif 40 <= prefijo <= 44:
        return "Alemania"
    elif 45 <= prefijo <= 49:
        return "Japón"
    elif prefijo == 50:
        return "Inglaterra"
    elif prefijo == 84:
        return "España"
    else:
        return "Desconocido"

continua = True

while continua:
    codigo = input("Introduce un número de código de barras: ").strip()
    if codigo != "0":
                # Determinar tipo y completar con ceros a la izquierda
        if len(codigo) < 8:
            codigo = codigo.zfill(8) #completar los dígitos a 8
            # print(codigo) # traza para ver el resultado de zfill
        elif 8 < len(codigo) < 13:
            codigo = codigo.zfill(13)

        tipo = len(codigo)
        check_real = int(codigo[-1])
        check_calc = calcular_digito_control(codigo)

        if check_calc == check_real:
            if tipo == 13:
                pais = obtener_pais(codigo[:2])
                print("SI", pais)
            else:
                print("SI")
        else:
            print("NO")
    else :
        continua=False
        print("Fin Programa")
