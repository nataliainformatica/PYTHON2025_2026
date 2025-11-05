# Pedimos la cadena al usuario
texto = input("Introduce una cadena de caracteres: ")

#inicializamos las variables que usaremos a un estado "coherente"
encontrado = False
repetido = ""

# Recorremos la cadena carácter por carácter
for i in range(len(texto)):
    c1 = texto[i]
    # Comparamos con los siguientes caracteres
    for j in range(i + 1, len(texto)):
        c2 = texto[j]
        if c1 == c2:
            repetido = c1
            encontrado = True
            break  # salimos del segundo bucle
    if encontrado:
        break  # salimos del primer bucle también

# Mostramos el resultado
if encontrado:
    print("El primer carácter repetido es:", repetido)
else:
    print("No hay caracteres repetidos.")
