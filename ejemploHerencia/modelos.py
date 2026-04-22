"""
Toda obra tiene: título, autor y año de publicación.

Existen dos tipos de obras:

Libro además guarda el número de páginas.
Audiovisual además guarda la duración en minutos.
"""
class Obra: 
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio=anio
    #necesitamos el método que nos convierte el objeto a formato str
    def __str__(self):
        return f'"{self.titulo}" -"{self.autor} ({self.anio})'

class Libro(Obra):
    #herencia de obra con número de páginas
    def __init__(self,titulo,autor,anio,paginas):
        super().__init__(titulo,autor,anio)
        self.paginas = paginas
    #polimorfismo 
    def __str__(self):
       base = super().__str__()
       #TODO - SUSTITUIR ",", por <<COMA>>
       return f"{base}{self.paginas}"
    
    #MÉTODO PARA "CONVERTIR EL OBJETO A UNA LÍNEA PARA PERSISTENCIA"

    

class Audiovisual(Obra):
   #herencia de obra con duración
    def __init__(self,titulo,autor,anio,duracion):
        super().__init__(titulo,autor,anio)
        self.duracion = duracion
    def __str__(self):
       base = super().__str__()
       #TODO - SUSTITUIR ",", por <<COMA>>
       return f"{base}{self.duracion}"
    