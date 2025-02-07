class libros:
    def __init__(self, titulo, autor, isbn, disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible


mi_primer_libro = libros("STEELHART","Neil Marcus","RD-341DS","no")
mi_segundo_libro = libros("IA","steve carl","fr-3454DA","si")

print(mi_primer_libro.titulo)
print(mi_segundo_libro.titulo)

#Los atributos son las caracteristicas de un objeto y estos son únicos.
#para poder agregar a los atributos necesitamos:
#1 agregar una funcion especial __init__ ques en realidad es un metodo constructor
#   pasamos por parametros los datos que se asignaran a los atributos
#   declaramos los atributos
#   usamos self: self representa a la instancia actual de la clase. 
#   que quiere decir esto: que cada instancia tendra su self.titulo, self.autor, self.isbn, self.disponible:
#   usando los ejemplos de arriba:
#   mi_primer_libro = libros("STEELHART","Neil Marcus","RD-341DS","no")
#   mi_segundo_libro = libros("IA","steve carl","fr-3454DA","si")
#   cada una de estas instancias tendran sus respectivos atributos

# Aquí `self.titulo` es el atributo, y `titulo` es el argumento del método.
#  self.titulo = titulo