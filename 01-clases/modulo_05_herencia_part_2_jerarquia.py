#herencia jerarquica:

#                                               --------------------
#                                                    persona
#                                             ---------------------
#                                                      |                                                    
#                     ----------------------------------------------------------------------
#                    |                                |                                    |
#               ---------                        ------------                         -----------
#                docente                          estudiante                           director
#               --------                        ------------                          ----------
#
#
#Herencia jerarquica, es donde mas de una clase hija heredan los metodos y atributos
#de la clase Padre.

#La construcción de las clases serán parecidas a la que se hizo en el de herencia simple.

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad   = edad

    def saludar(self):
        return "deseo expresar mi mas sentidos saludos a todos los estudiantes que están en el salón de clase."
    



class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, salario, puesto):
        super().__init__(nombre, apellido, edad)
        self.salario = salario
        self.puesto = puesto
     
    def presentarme(self):
       return f"Hola, mi nombre es {self.nombre} y {self.saludar()}"
    


class estudiante(Persona):
    def __init_(self, nombre, apellido, edad, cursos):
        super().__init__(self, nombre, apellido, edad)
        self.cursos = cursos
    
    def mostrar_cursos(self):
        return f"Los cursos del estudiante son: {self.cursos}"


class director(Persona):
    def __init_(self, nombre, apellido, edad, salario, comite, objetivos):
        super().__init__(self, nombre, apellido, edad)
        self.salario = salario
        self.comite = comite
        self.objetivos = objetivos


    def objetivos(self):
        return f"Los objetivos son: {self.objetivos}"
