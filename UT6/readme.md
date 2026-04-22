EJERCICIO DE CLASES - HERENCIA (SIMPLE)- FICHEROS DE CARACTERES - 
=============================================================
 ENUNCIADO
=============================================================
 Una pequeña biblioteca quiere gestionar su catálogo de obras.
 
 Toda obra tiene: título, autor y año de publicación.
 
 Existen dos tipos de obras:
   - Libro        además guarda el número de páginas.
   - Audiovisual  además guarda la duración en minutos.

 El programa debe permitir:
 
   1. Añadir una obra (libro o audiovisual).  (Usando el catálogo guardado previamente)
   2. Listar todas las obras guardadas.
   3. Buscar obras por autor.
   4. Eliminar una obra por título.
   5. Salir (los datos se guardan automáticamente al salir
      y se cargan al arrancar).

 Conceptos practicados
 ─────────────────────
   • Herencia:     Libro y Audiovisual heredan de Obra.
   • Polimorfismo: cada clase redefine __str__ y to_linea().
   • Persistencia: fichero de texto propio separado por comas.
                 
 Formato del fichero 'catalogo.txt'
 ───────────────────────────────────
 Cada línea representa una obra. Los campos están separados
 por comas. El primer campo indica el tipo.

   LIBRO,titulo,autor,anio,paginas
   AUDIOVISUAL,titulo,autor,anio,duracion

 Ejemplo real:
   LIBRO,Don Quijote,Miguel de Cervantes,1605,863
   AUDIOVISUAL,El Padrino,Francis Ford Coppola,1972,175

 Nota: si un título o autor contiene una coma, se sustituye
 por el marcador <<COMA>> al escribir y se restaura al leer.
 
=============================================================

