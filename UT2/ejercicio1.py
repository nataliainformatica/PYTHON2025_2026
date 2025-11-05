"""
Se pedirá al usuario que introduzca las dos cadenas, carácter a carácter.

El usuario podrá escribir las bases en mayúscula o minúscula (A, T, C, G o a, t, c, g).

El programa comprobará si las dos cadenas son complementarias correctamente:

A ↔ T

T ↔ A

C ↔ G

G ↔ C

Si el apareamiento es correcto, se mostrarán las dos cadenas en mayúsculas, una debajo de la otra.

Si existe alguna mutación (es decir, una base que no cumple la regla de apareamiento), se mostrarán ambas cadenas en mayúsculas, excepto las bases afectadas por la mutación, que se mostrarán en minúsculas.

Ejemplo correcto:

Cadena 1: A T G C A G T T C A T G A C T
Cadena 2: T A C G T C A A G T A C T G A

Ejemplo con mutación:

Cadena 1: A T G C A G T T C A T G A C T
Cadena 2: T A C G T C A A g T A C T G A
"""


#c1 = input("Introduce la primera cadena: ").replace(" ", "")
#c2 = input("Introduce la segunda cadena: ").replace(" ", "")


continua = True

while continua:
    cadena1 = input("Introduce la primera cadena: ")
    cadena2 = input("Introduce la segunda cadena: ")
    # Comprobamos que tienen la misma longitud
    if len(cadena1) != len(cadena2):
        print("Error: las dos cadenas deben tener la misma longitud.")
    else:
        continua = False  
        # Convertir a mayúsculas para poder comparar las moléculas
        cadena1 = cadena1.upper()
        cadena2 = cadena2.upper()
        resultado1 = ""
        resultado2 = ""
        for i in range(len(cadena1)):
            b1 = cadena1[i]
            b2 = cadena2[i]

        # Comprobamos las parejas correctas manualmente
            if (b1 == 'A' and b2 == 'T') or \
                (b1 == 'T' and b2 == 'A') or \
                (b1 == 'C' and b2 == 'G') or \
                (b1 == 'G' and b2 == 'C'):
                resultado1 += b1 + " "
                resultado2 += b2 + " "
            else:
            # Si hay mutación, se muestran en minúsculas
                resultado1 += b1.lower() + " "
                resultado2 += b2.lower() + " "
        print("\nResultado del análisis:")
        print("Cadena 1:", resultado1)
        print("Cadena 2:", resultado2)