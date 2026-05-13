from modelos import Libro, Audiovisual
from persistencia import guardar_catalogo, cargar_catalogo

def listar(obras):
    
# si el catálogo está vacío mostramos un mensaje
    if not obras:
        print("El catálogo está vacío")
    for i, o in enumerate(obras,1):
        print(f"{i}. {o}")

def aniadir(obras):
    print("Tipo de obra: 1 )Libro 2)Audiovisual")
    opcion = input("Elige").strip()

    titulo = input("Titulo: ").strip()
    autor = input("Autor: ").strip()

    try:
        anio =int(input("Año: "))
    except ValueError:
        print("Año no es vaĺido")
        return
    
    if opcion == "1":
        try:
            paginas = int(input( "Páginas : "))
        except ValueError:
            print("El número no es válido")
            return
           #def __ini__(self,titulo,autor,anio,paginas):

        obras.append(Libro(titulo, autor, anio, paginas))
    elif opcion =="2":
        try:
            duracion = int(input( "Duración : "))
        except ValueError:
            print("El número no es válido")
            return
           #def __ini__(self,titulo,autor,anio,duracion):

        obras.append(Audiovisual(titulo, autor, anio, paginas))
    else:
        print("Opcion no válida")

    print("Obra añadida")
    

def buscar_por_autor(obras):
    autor = input("Nombre del autor: ").strip().lower()
    encontradas=[]
    for o in obras:
       
        if autor in o.autor.lower():
            encontradas.append(o)
    
    if not encontradas:
        print("No se encontraron obras de ese autor")
    else:
        for o in encontradas:
            print(f" {o}")


def eliminar(obras):
    titulo = input("Título que quieres eliminar").strip().lower()
    #len(obras)
    longitud_previa = len(obras)
    i=0
    while i <len(obras):
        if obras[i].titulo.lower() == titulo:
            obras.pop(i)
        else:
            i+=1
    if len(obras)<longitud_previa:
        print("Obra eliminada")
    else:
        print("No se encontró")


def menu():
   #la biblioteca debe gestionar un catálogo de obras

   #def __ini__(self,titulo,autor,anio,paginas):
    obra1 = Libro("titulo", "autor",2006,7)
   #def __ini__(self,titulo,autor,anio,duracion):
    obra2 =Audiovisual("titulo2", "autor",2007,74)



    obras =  cargar_catalogo()
    # TODO - TRATAR LA LISTA USANDO PERSISTENCIA PARA INICIALIZARLA

    while True:
        print("\n" + "-"*30)
        print("1. Listar obras")
        print("2. Añadir obra")
        print("3. Buscar por autor")
        print("4. Eliminar obra")
        print("5. Guardar y salir")
    
        eleccion = input("Opcion:").strip()
        
        if eleccion =="1":
            listar(obras)
            
        elif eleccion == "2":
            aniadir(obras)
            
        elif eleccion == "3":
            buscar_por_autor(obras)
        elif eleccion == "4":
            eliminar(obras)
        elif eleccion == "5":
            guardar_catalogo(obras)
            
            
            break
            #SALIR
        else:
            print("OPCIÓN NO RECONOCIDA EN EL MENÚ")
              
