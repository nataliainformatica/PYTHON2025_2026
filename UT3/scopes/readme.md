
10 ejercicios en Python para  practicar y comprender los distintos ámbitos de las variables siguiendo la regla LEGB: Local – Enclosing – Global – Built-in.



Recordatorio: regla LEGB
Python busca una variable en este orden:

1.    Local (dentro de la función actual)

2.    Enclosing (funciones envolventes)

3.    Global (módulo)

4.    Built-in (len, sum, print, etc.)

 

Instrucciones
·       Intenta razonar cada ejercicio antes de ejecutarlo.

·       No mires la solución hasta haberlo intentado.

·       Las soluciones están ocultas y puedes desplegarlas cuando quieras.


## Ejercicio 1 – Ámbito Local
 ```
def saludar():
    mensaje = "Hola"
    print(mensaje)

saludar()
# print(mensaje)
```
**Preguntas**

1.    ¿Por qué la última línea produce un error?

2.    ¿Dónde existe la variable mensaje?

**Solución**

mensaje es una variable local, solo existe dentro de la función saludar. Fuera de ella, Python no la encuentra y lanza un NameError.

 
## Ejercicio 2 – Ámbito Global

```
contador = 0

def incrementar():
    contador = 10
    print("Dentro:", contador)

incrementar()
print("Fuera:", contador)
```

Preguntas

1.    ¿Por qué el valor global no cambia?

2.    Modifica la función para que incremente el contador global.

Solución

Dentro de la función se crea una variable local llamada contador.

```
def incrementar():
    global contador
    contador += 1
```
 
## Ejercicio 3 – Ámbito Enclosing
```
def exterior():
    x = "exterior"

    def interior():
        print(x)

    interior()

exterior()
```

**Preguntas**

1.    ¿Por qué interior() puede acceder a x?

2.    ¿Es x local o global?

Solución

x pertenece al ámbito enclosing (función envolvente). No es local de interior, pero está disponible por estar definida en la función exterior.

 

##  Ejercicio 4 – Uso de nonlocal
```
def contador():
    total = 0

    def incrementar():
        total += 1
        return total

    return incrementar()

contador()
```


**Preguntas**

1.    ¿Qué error se produce?

2.    ¿Por qué ocurre?

3.    Arréglalo.

Solución

Python intenta crear un total local en incrementar. Para modificar el de la función envolvente:
```
def incrementar():
    nonlocal total
    total += 1

 ```

##  Ejercicio 5 – Enclosing vs Local

def padre():
    x = "padre"

    def hijo():
        x = "hijo"
        print(x)

    hijo()
    print(x)

padre()
```

**Preguntas**

1.    ¿Qué se imprime?

2.    ¿Por qué x no cambia en padre()?

3.    Modifica el código para que sí cambie.

Solución

La x de hijo es local y oculta a la enclosing.
```
def hijo():
    nonlocal x
    x = "hijo"
```

 

## Ejercicio 6 – Built‑in ocultado
```
print(len("Python"))

def prueba():
    len = 100
    print(len)

prueba()
print(len("Python"))
```

**Preguntas**

1.    ¿Por qué funciona el último len()?

2.    ¿Qué pasaría si se llamara a len() dentro de prueba()?

Solución

Dentro de prueba, len es una variable local que oculta al built‑in. Fuera de la función, el built‑in sigue intacto.

 

##  Ejercicio 7 – Error común con built‑ins
```
sum = 0
numeros = [1, 2, 3]

# print(sum(numeros))

```

**Preguntas**

1.    ¿Por qué falla?

2.    ¿Cómo evitar este problema?

Solución

sum es una función built‑in. Al usarla como variable, se pierde el acceso. Regla básica: no usar nombres de built‑ins como variables.

 

##  Ejercicio 8 – Regla LEGB completa
```

x = "global"

def a():
    x = "enclosing"

    def b():
        print(x)

    b()

a()
```

**Preguntas**

1.    ¿Qué x se imprime?

2.    ¿Qué ocurre si eliminas la x de a()?

Solución

Se imprime la x enclosing. Si se elimina, Python buscará la x global.

 

## Ejercicio 9 – Closure
```
def crear_multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

por_dos = crear_multiplicador(2)
por_tres = crear_multiplicador(3)

print(por_dos(5))
print(por_tres(5))
```
**Preguntas**

1.    ¿Dónde está n?

2.    ¿Por qué sigue existiendo después de ejecutar la función exterior?

Solución

n pertenece al ámbito enclosing. Python crea un closure, conservando el valor aunque la función exterior haya terminado.

 

## Ejercicio 10 – Reto final
```
x = 5

def f():
    x = 10
    def g():
        print(x)
    g()

f()
``` 
**Preguntas**

1.    ¿Qué se imprime?

2.    ¿Por qué?

3.    ¿Cómo imprimir el x global desde g()?

Solución

Se imprime 10 porque g() encuentra primero la x del ámbito enclosing (f).

Para acceder al global:

print(globals()['x'])
