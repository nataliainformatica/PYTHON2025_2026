"""
Invertir una cadena de texto usando un bucle"""

#Pedir una cadena al usuario
cadena = input("Introduce una cadena de texto: ")

reversa =""
for letra in cadena:
    reversa = letra + reversa

print("Cadena invertida:", reversa)
#print(f"Cadena invertida: {reversa}")