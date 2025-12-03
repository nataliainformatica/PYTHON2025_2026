import random

def devolverAleatorio(n):
    if n <= 0:
        # Primer intento y lo devolvemos
        return random.randint(0, 999)

    mayor = 0
    for _ in range(n):
        num = random.randint(0, 999)
        if num > mayor:
            mayor = num

    return mayor
