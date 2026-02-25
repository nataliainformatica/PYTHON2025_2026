# Reto 1
Compatibilidad de tipos de sangre

**Objetivo:**

Escribir un programa en Python que determine si una donación de sangre es posible entre un donante y un receptor, según su tipo de sangre.

**Descripción:**

Los tipos de sangre son: O-, O+, A-, A+, B-, B+, AB- y AB+. 
```
compatibilidad_sanguinea = {
    "O-": ["O-"],
    "O+": ["O-", "O+"],
    "A-": ["O-", "A-"],
    "A+": ["O-", "O+", "A-", "A+"],
    "B-": ["O-", "B-"],
    "B+": ["O-", "O+", "B-", "B+"],
    "AB-": ["O-", "A-", "B-", "AB-"],
    "AB+": ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"]
}
# Ejemplo de uso: ver qué grupos pueden donar a A+
print(compatibilidad_sanguinea["A+"])

```


otra posibilidad de uso de datos: 
```
# Listado de grupos sanguíneos como tuplas (tipo, rh)
grupos = [
    ("O", "-"), ("O", "+"),
    ("A", "-"), ("A", "+"),
    ("B", "-"), ("B", "+"),
    ("AB", "-"), ("AB", "+")
]

# Diccionario receptor  con  lista de  grupos donantes  y sus grupos compatibles en el receptor
compatibilidad_sanguinea = {
    ("O", "-"): [("O", "-")],
    ("O", "+"): [("O", "-"), ("O", "+")],
    ("A", "-"): [("O", "-"), ("A", "-")],
    ("A", "+"): [("O", "-"), ("O", "+"), ("A", "-"), ("A", "+")],
    ("B", "-"): [("O", "-"), ("B", "-")],
    ("B", "+"): [("O", "-"), ("O", "+"), ("B", "-"), ("B", "+")],
    ("AB", "-"): [("O", "-"), ("A", "-"), ("B", "-"), ("AB", "-")],
    ("AB", "+"): grupos  # Todos los grupos son compatibles
}
# Ejemplo de uso
receptor = ("A", "+")
print(f"Donantes compatibles con {receptor}: {compatibilidad_sanguinea[receptor]}")
``` 
# Ejemplo de uso: ver qué grupos pueden donar a A+
print(compatibilidad_sanguinea["A+"])


Cada tipo de sangre puede donar a ciertos otros tipos, según las reglas de compatibilidad.

Tu programa debe:

Pedir al usuario que introduzca el tipo de sangre del donante y del receptor.

Comprobar si los tipos de sangre son válidos.

Determinar si la donación es compatible.

Mostrar un mensaje indicando si la donación es posible o no es posible.

Opcional:

Usar diccionarios, listas o tuplas para almacenar las relaciones de compatibilidad.

Mostrar al usuario la lista de tipos de sangre válidos.
```
Ejemplo de salida:

Tipos de sangre disponibles: ['O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+']
Introduce el tipo de sangre del donante: A+
Introduce el tipo de sangre del receptor: AB+
```
¡Compatible! A+ puede donar a AB+.

Si quieres, puedo hacer una versión más visual y con colores en la consola para que sea más divertida de usar.
