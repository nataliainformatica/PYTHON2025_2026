## Ejercicio 1
La cabecera de Google del- 23 de octubre de 2022

![RETO](https://github.com/nataliainformatica/PROGRAMACION_DAM_25_26/blob/main/recursos%26imagenes/secuenciaADNjpg.jpg?raw=true)

 Me acuerdo de que el ADN tiene A, T, C y G, 
pero ¿cómo se sabe cuál va en cada lugar? 
¿Cómo se arma la secuencia?
Y si se desordena, ¿qué pasa? 
¿Hacemos un programa que compruebe si el emparejamiento es correcto?


## Enunciado :
```
Disponemos de una molécula de ADN formada por dos cadenas complementarias, cada una con 15 bases nitrogenadas.

Queremos comprobar si la molécula está correctamente ordenada (es decir, si las bases se emparejan según las reglas de complementariedad) o si presenta una mutación.

## ACTIVIDAD


Se pedirá al usuario que introduzca las dos cadenas, carácter a carácter.

El usuario podrá escribir las bases en mayúscula o minúscula (A, T, C, G o a, t, c, g).

El programa comprobará si las dos cadenas son complementarias correctamente:

A ↔ T

T ↔ A

C ↔ G

G ↔ C

Si el apareamiento es correcto, se mostrarán las dos cadenas en mayúsculas, una debajo de la otra.

Si existe alguna mutación (es decir, una base que no cumple la regla de apareamiento), se mostrarán ambas cadenas en mayúsculas, excepto las bases afectadas por la mutación, que se mostrarán en minúsculas.

Ejemplo correcto:

Cadena 1: A T G C A G T T C A T G A C T
Cadena 2: T A C G T C A A G T A C T G A

Ejemplo con mutación:

Cadena 1: A T G C A G T T C A T G A C T
Cadena 2: T A C G T C A A g T A C T G A


```
Para entender el objetivo de nuestro programa, hay que saber qué estamos haciendo, así que... un poco más de información 

¿Qué es el ADN y cómo se ordenan sus bases?

El **ADN (ácido desoxirribonucleico)** es la molécula que contiene la información genética de todos los seres vivos. Está formada por dos cadenas que se enrollan entre sí formando una doble hélice.

Cada cadena del ADN está compuesta por unidades llamadas nucleótidos, y cada nucleótido contiene una de las cuatro bases nitrogenadas:

Adenina (A)

Timina (T)

Citosina (C)

Guanina (G)

Estas bases se emparejan siempre de la misma forma, siguiendo una regla fija conocida como complementariedad de bases:
```

A siempre se une con T

C siempre se une con G
 ```

Este orden o secuencia de las bases es lo que codifica la información genética. Así, el ADN funciona como un manual biológico: su secuencia de letras contiene las instrucciones que determinan cómo funciona y se desarrolla un organismo.

 **El orden de las bases en el ADN** 

El ADN está formado por dos cadenas complementarias, como dos tiras paralelas que encajan perfectamente.
Cada cadena puede tener cualquier secuencia de bases, lo importante es que la otra cadena siga las reglas de apareamiento complementario:

```
Cadena 1: A  T  G  C  A  T
Cadena 2: T  A  C  G  T  A
```
En una cadena, puebe haber cualquier orden de A, T, C, G,lo que debe cumplirse es que su cadena complementaria tenga las bases emparejadas correctamente


# Ejercicio 2: validador de contraseñas

Implementa un validador de contraseñas. Ésta se debe leer por teclado y debemos comprobar que cumple determinadas características:
- Tiene entre 8 y 20 caracteres.
- Tiene alguna letra mayúscula y alguna letra minúscula.
- Tiene algún carácter raro entre $ % _ *
- Tiene algún número

Implementa un método que devuelva true o false para indicar si se cumplen los requisitos de contraseña válida o no. La contraseña debe enviarse al método como parámetro.

## Ejercicio 2 versión 2
El programa debe indicar exactamente qué le falta a la contraseña para ser válida

##  Ejercicio 3.
Realiza un programa que ordene alfabéticamente el nombre de tres
alumnos, que estarán en tres variables String.
Al comenzar el programa, se pide al usuario los nombres quiere ordenar alfabéticamente de la a la z
Finalizará mostrando el resultado imprimiendo en mayúsculas un nombre en cada línea


# Ejercicio 4: carácter repetido

Escribir un programa en Python que detecte el primer carácter repetido de una cadena de caracteres.


# Ejercicio5: Códigos de barras

[Enlace al ejercicio original](https://aceptaelreto.com/problem/statement.php?id=106&cat=4)

En el lejano 1952, tres norteamericanos patentaron lo que terminó llamándose código de barras. Consiste en una técnica para representar números (y, en menos ocasiones, letras) mediante una serie de líneas verticales paralelas, con diferentes grosores y separaciones entre ellas. Si bien el primer uso sirvió para identificar de manera automática los vagones de un ferrocarril, hoy los códigos de barras se utilizan en infinidad de lugares, siendo la catalogación de productos la más habitual.

La manera concreta de codificar mediante barras los números y las letras puede ser muy variada, lo que ha llevado a la aparición de diferentes estándares. De todos ellos, el EAN (European Article Number) resulta ser el más extendido. De éste, hay principalmente dos formatos, que se diferencian en el ancho. Existe así el llamado EAN-8, que codifica 8 números, y el EAN-13, que, naturalmente, codifica 13.


El último dígito del código se utiliza para detección de errores, y se calcula a partir de los demás. Para eso:

Empezando por la derecha (sin contar el dígito de control que se está calculando), se suman los dígitos individuales, multiplicados por un factor:
Los dígitos en posiciones impares (empezando a contar por la derecha saltándonos el de control) se multiplican por 3.
Los dígitos en posiciones pares se multiplican por 1.
Por ejemplo, para el  primer código de los ejemplos (65839522) código EAN-8 de la figura, la operación a realizar es:

2 · 3 + 5 · 1 + 9 · 3 + 3 · 1 + 8 · 3 + 5 · 1 + 6 · 3 = 88

El dígito de comprobación es el número que hay que sumar al resultado anterior para llegar a un valor múltiplo de 10. En el ejemplo de EAN-8, para llegar al múltiplo de 10 más cercano por encima del número 88 hay que sumar 2 (y llegar al 90). Ten en cuenta que si la suma resulta ser ya múltiplo de 10, el dígito de control será 0.
En EAN-13, los primeros dígitos se usan además para identificar al país. A continuación se indica una tabla (parcial) de esos códigos de país.

Código	País		

0	EEUU		
539	 Irlanda		
759	Venezuela
380	Bulgaria		
560	Portugal		
850	Cuba
50	Inglaterra	 	
70	Noruega	 
890	India


**Entrada**

La entrada estará formada por una serie de casos de prueba. Cada uno contendrá una sucesión de números pertenecientes a un código de barras EAN-8 o EAN-13, incluyendo el dígito de control. 
Si el número de dígitos es inferior a 8, se asumirá que es un código EAN-8; si es superior a 8 pero inferior a 13, se asumirá EAN-13. 

En ambos casos, se completarán el resto de dígitos colocando ceros a la izquierda.

El último caso de prueba es seguido por una línea con un 0 que no provoca salida.

**Salida**

Para cada caso de prueba, el programa indicará si el dígito de control es correcto o no. Si lo es, escribirá "SI". En otro caso, escribirá "NO".

(Ampliación para el uso de colecciones) . Si el código de barras es EAN-13 y correcto, el programa escribirá además el país al que pertenece utilizando la tabla anterior (separado por un espacio). 

Si el código no aparece en la tabla, el programa mostrará "Desconocido". Ten cuidado al escribir los países; deberás respetar el uso de mayúsculas y minúsculas de la tabla.

**Entrada de ejemplo**
```
65839522
65839521
8414533043847
5029365779425
5129365779425
0
```
**Salida de ejemplo**
 ```
SI
NO
SI Desconocido
SI Inglaterra
NO
``` 

# Ejercicio 6: Radares de tramo
[Acepta el reto](https://aceptaelreto.com/problem/statement.php?id=112&cat=4)

# Ejercicio 7

Invertir una cadena de textousando un bucle

# Ejercicio 8

Contar el número de vocales en una cadena de texto


