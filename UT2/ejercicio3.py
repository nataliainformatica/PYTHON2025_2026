# solución si usar arrays o colecciones 

#Programa principal

# Pedir los tres nombres
nombre1 = input("Introduce el primer nombre: ")
nombre2 = input("Introduce el segundo nombre: ")
nombre3 = input("Introduce el tercer nombre: ")

# Convertir a minúsculas para comparar correctamente (sin importar mayúsculas/minúsculas)
n1 = nombre1.lower()
n2 = nombre2.lower()
n3 = nombre3.lower()

# Ordenar alfabéticamente 
if n1 <= n2 and n1 <= n3:
    primero = nombre1
    if n2 <= n3:
        segundo = nombre2
        tercero = nombre3
    else:
        segundo = nombre3
        tercero = nombre2

elif n2 <= n1 and n2 <= n3:
    primero = nombre2
    if n1 <= n3:
        segundo = nombre1
        tercero = nombre3
    else:
        segundo = nombre3
        tercero = nombre1

else:
    primero = nombre3
    if n1 <= n2:
        segundo = nombre1
        tercero = nombre2
    else:
        segundo = nombre2
        tercero = nombre1

# Requisito del enunciado: mostrar el resultado en mayúsculas, un nombre por línea
print("\nNombres ordenados alfabéticamente:")
print(primero.upper())
print(segundo.upper())
print(tercero.upper())
