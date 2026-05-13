import os
from modelos import Libro, Audiovisual


FICHERO = "catalogo.txt"
SEPARADOR = ","


def cargar_catalogo():

    if not os.path.exists(FICHERO):
        return []
    # defino la lista a la que voy a añadir las obras
    obras = []

    with open(FICHERO, "r", encoding="utf-8") as f: 
        #leer linea a linea

        for linea in f: 
            linea = linea.strip()
            # en la línea tendré los elementos separados por comas 
            # tratar la linea - TITULO, AUTOR, AÑO
            # TIPO DE OBRA - 
            # LIBRO - PÁGINAS 
            # AUDIOVISUAL - DURACIÓN
            # TIPO - AUTOR, ANIO, 

            
            campos = linea.split(SEPARADOR)
            tipo = campos[0]
            titulo = campos[1]
            autor = campos[2]
            anio = campos[3]

            # DEPENDIENDO DEL TIPO 
            if tipo == "LIBRO":
                paginas = campos[4]
                #  def __init__(self,titulo,autor,anio,paginas):
                obras.append(Libro( titulo,autor,anio,paginas))


            if tipo == "AUDIOVISUAL":
                duracion = campos[4]
                #    def __init__(self,titulo,autor,anio,duracion):
                obras.append(Audiovisual(titulo,autor,anio, duracion))
        return obras

def guardar_catalogo(obras):
       # tratar la linea - TITULO, AUTOR, AÑO
            # TIPO DE OBRA - 
            # LIBRO - PÁGINAS 
            # AUDIOVISUAL - DURACIÓN
            # TIPO - AUTOR, ANIO, 
    with open(FICHERO, "w",encoding="utf-8") as f:
        for obra in obras:
            if isinstance(obra,Libro):
                tipo = "LIBRO"
                linea = f"{tipo},{obra.titulo},{obra.autor}, {obra.anio}, {obra.paginas} \n"
                print(linea)
                # linea = tipo + obra.titulo+","+obra.autor+","+ obra.anio + ","+ obra.paginas 
            

            else:
                tipo = "AUDIOVISUAL"
                linea = f"{tipo},{obra.titulo},{obra.autor}, {obra.anio}, {obra.duracion} \n"
                print(linea)
           # linea = tipo + obra.titulo+","+obra.autor+","+ obra.anio + ","+ obra.duracion 

           
            f.write(linea)

