# Programa para comprobar si una molécula de ADN está correctamente emparejada
# Solo usa tipos básicos, bucles y comparaciones

# Pedir longitud de la molécula
longitud = int(input("Introduce la longitud de la molécula de ADN: "))

# Inicializar cadenas vacías
cadena1 = ""
cadena2 = ""

# Variables para formar el resultado final
resultado1 = ""
resultado2 = ""

# Bandera para saber si hay mutación
hay_mutacion = False

# Pedir las bases una a una
print("\nIntroduce las bases de la primera cadena:")
for i in range(longitud):
    # base = input(f"Base {i+1}: ").strip()
    base = input("Base ", i+1, " ").strip()
    if len(base) == 0:
        base = " "  # Evitar errores por vacío
    cadena1 += base.upper()

print("\nIntroduce las bases de la segunda cadena:")
for i in range(longitud):
    # base = input(f"Base {i+1}: ").strip()
    base = input("Base ", i+1, " ").strip()
    if len(base) == 0:
        base = " "
    cadena2 += base.upper()

# Comprobar complementariedad base a base
for i in range(longitud):
    b1 = cadena1[i]
    b2 = cadena2[i]

    # Comprobamos las combinaciones válidas
    if (b1 == "A" and b2 == "T") or \
       (b1 == "T" and b2 == "A") or \
       (b1 == "C" and b2 == "G") or \
       (b1 == "G" and b2 == "C"):
        # Emparejamiento correcto
        resultado1 += b1
        resultado2 += b2
    else:
        # Mutación → minúsculas
        resultado1 += b1.lower()
        resultado2 += b2.lower()
        hay_mutacion = True

# Mostrar resultados
print("\nResultado:")
print(resultado1)
print(resultado2)

if hay_mutacion:
    print("\n Se ha detectado una mutación en las bases mostradas en minúsculas.")
else:
    print("\nLa molécula está correctamente emparejada.")
