def movimientos_caballo(fila, columna):
    # Todos los movimientos posibles del caballo
    movimientos = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
  # también podemos usar una tupla, en lugar de una lista

  # para cada uno de los elemntentos 
    contador = 0
    for df, dc in movimientos:
        nueva_fila = fila + df
        nueva_columna = columna + dc
        # Verificamos que esté dentro del tablero 1-8
        if 1 <= nueva_fila <= 8 and 1 <= nueva_columna <= 8:
            contador += 1

    return contador

# Programa principal
#mejorable con control de excepciones - TODO
fila = int(input("Introduce la fila del caballo (1-8): "))
columna = int(input("Introduce la columna del caballo (1-8): "))

print(f"El caballo puede moverse a {movimientos_caballo(fila, columna)} casillas válidas.")
