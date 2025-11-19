"""
Contar el número de vocales en una cadena de texto
"""

vocales ="aeiouAEIOU"
cadena = input("Introduce una cadena de texto: ")

contador_vocales = 0

for letra in cadena:
    if letra in vocales:
        contador_vocales += 1

print(f"Número de vocales: {contador_vocales}")