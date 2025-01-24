#Metodos
#los metodos en si son funciones, solo que al estár definidos dentro de una clase estos pasan a ser metodos.

class libros:
    def __init__(self, titulo, autor, isbn, disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    
    def solicitar_libro(self) :
        print(f"Estás solicitnado el libro: {self.titulo}")

    def devolver_libro(self):
        print(f"Estas devolviendo el libro: {self.titulo}")


mi_primer_libro = libros("STEELHEART","Neil Marcus","RD-341DS","no")
mi_primer_libro.solicitar_libro()
mi_primer_libro.devolver_libro()


