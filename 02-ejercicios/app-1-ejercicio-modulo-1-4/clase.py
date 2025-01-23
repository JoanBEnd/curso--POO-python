class Estudiante:
    def __init__(self, nombre, apellidos, edad, cursos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.cursos = cursos
    
    def mostrar_informacion(self):
        variable_info = (f"Apellidos y Nombre: {self.apellidos}, {self.nombre}\n"
                         f"Edad: {self.edad}\n"
                         f"Cursos: {"".join( curso  for curso in self.cursos) }\n"
                         )
        return variable_info
    
    def cursos_registrados(self):
        variable_cursos =  f"Los cursos registrados son: {"".join( curso  for curso in self.cursos) }\n"
        return variable_cursos