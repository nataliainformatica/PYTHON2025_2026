"""
Algoritmo que pida números hasta que se introduzca un cero. 
Debe imprimir la suma y la media de todos los números introducidos.
"""
suma = 0
contador = 0
continua =True
while continua:
    # TODO modificar el código para añadir el tratamiento de las excepciones
    numero = int(input("Introduce un número (0 para terminar): "))
    if numero != 0:
        suma += numero
        contador += 1
    else:
        # si se ha introducido un cero, no se tiene en cuenta  para la media
        continua = False

# para evitar errores de división por cero
if contador > 0:
    media = suma / contador
    print(f"La suma es: {suma}")
    print(f"La media es: {media}")
else:
    print("No se han introducido números válidos.")