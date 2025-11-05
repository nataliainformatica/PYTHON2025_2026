"""
Crea una aplicación que permita adivinar un número. 
La aplicación genera un número aleatorio del 1 al 100.
 A continuación va pidiendo números y va respondiendo si el número a adivinar 
 es mayor o menor que el introducido,a demás de los intentos que te quedan 
 (tienes 10 intentos para acertarlo). 
 El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), 
 si se llega al limite de intentos te muestra el número que había generado.
"""
import random

def calcular_numero_aleatorio():
    return random.randint(1, 100)

def introduce_numero_valido():
    continua = True
    while continua:
        try:
            numero = int(input("Introduce un número del 1 al 100: "))
            if numero < 1 or numero > 100:
                print("Por favor, introduce un número válido.")
            else:
                continua = False
        except ValueError:
            print("Por favor, introduce un número válido.")
    return numero


# PROGRAMA PRINCIPAL

intentos =10
acertado = False
aleatorio = calcular_numero_aleatorio()

print("En este juego tienes que adivinar un número del 1 al 100 que la máquina ha pensado")

while intentos >0 and not acertado:
 
    print(f"Te quedan {intentos} intentos.")
    numero = introduce_numero_valido()

       
    if numero == aleatorio:
        acertado = True
        print(f"¡Felicidades! Has acertado el número en {10 - intentos + 1} intentos.")
    else:
        intentos -= 1
        if numero < aleatorio:
            print("El número a adivinar es mayor.")
        else:
            print("El número a adivinar es menor.")
      

           
   