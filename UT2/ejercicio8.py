"""
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir. 
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:

La suma de los números que están dentro del intervalo (intervalo abierto).
Cuantos números están fuera del intervalo.
Además informa si hemos introducido algún número igual a los límites del intervalo.
"""


try:
    limite_inferior =int(input("Introduce el límite inferior: "))
    limite_superior =int(input("Introduce el límite superior: "))
    while limite_inferior >limite_superior:
        print("El límite inferior debe ser menor que el límite superor")
        limite_inferior =int(input("Introduce el límite inferior: "))
        limite_superior =int(input("Introduce el límite superior: "))
    print("Intervalo válido")
    # pedir números hasta que se introduzca el 0

    numeros_en_intervalo=0
    numeros_fuera_intervalo =0
    limites_iguales = False

    while True: 
        num=int(input("Introduce un número( 0 PARA TERMINAR): "))
        if num== 0:
            break; 
        if limite_inferior <= num <= limite_superior: 
            numeros_en_intervalo +=1
            if num == limite_inferior or num== limite_superior:
                limites_iguales=True
        else: 
            numeros_fuera_intervalo +=1
        
    print("Resultados")

    print(f"Números en el intervalo: {numeros_en_intervalo}")
    print(f"Números fuera del intervalo: {numeros_fuera_intervalo}")

    if limites_iguales:
        print("Se han introducido números iguales a los límites del intervalo")
    else:
        print("No se han introducido números iguales a los límites del intervalo")

except ValueError: 
    print("Por favor, para la próxima introduce números enteros válidos")







