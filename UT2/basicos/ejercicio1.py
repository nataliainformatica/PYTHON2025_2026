"""
Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120),
sin usar recursividad
"""

numero = int(input("Introduce un número para calcular su factorial: "))


if numero <0 :
    print("El factorial no está definido para números negativos.")
else:
    resultado = 1
    print(f"{numero}!=" , end="")
    for i in range (1, numero + 1):
        resultado *= i
        print(i , end="")
        #si no es el último número imprimiremos x
        if i < numero:
            print("x", end="")
    #al finalizar el bucle mostramos el resultado 
    print(f" = {resultado}")


for num in range(1, 6):
    if num == 3:
        continue   # salta el número 3
  
    print(num)
#en este ejemplo hemos usado f-string y el argumento end de la función pring
#f-string, permite insertar valores de variables directmente dentro del texto usando llaves{}

"""
def calcular_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_factorial(n-1)

numero = int(input("Introduce un número para calcular su factorial: "))
resultado = calcular_factorial(numero)
print(f"El factorial de {numero} es {resultado}")
"""