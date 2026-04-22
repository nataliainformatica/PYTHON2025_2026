from modelos import Libro, Audiovisual

def listar(obras):
    
# si el catálogo está vacío mostramos un mensaje
    if not obras:
        print("El catálogo está vacío")
    for i, o in enumerate(obras,1):
        print(f"{i}. {o}")

def menu():
   #la biblioteca debe gestionar un catálogo de obras
   #def __ini__(self,titulo,autor,anio,paginas):

    obra1 = Libro("titulo", "autor",2006,7)
   #def __ini__(self,titulo,autor,anio,duracion):
    obra2 =Audiovisual("titulo2", "autor2",2007,74)



    obras = [obra1,obra2]
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
            print("TODO")
        elif eleccion == "2":
            #
            print("TODO")
        elif eleccion == "3":
            #
            print("TODO")
        elif eleccion == "4":
            #
            print("TODO")
        elif eleccion == "5":
            #
            print("TODO")  
            #SALIR
        else:
            print("OPCIÓN NO RECONOCIDA EN EL MENÚ")
              
