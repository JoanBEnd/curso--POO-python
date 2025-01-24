
#Herencia: le permite heredar a la clase hija los atributos y metodos que tiene una clase padre
#En este caso veremos un tipo de herencia, Herencia Simple.

#                                            ---------------
#                                                persona
#                                            ---------------
#                                                    |    
#                                            -------------                         
#                                               profesor                          
#                                           -------------                         

#Herencia simple: Basicamente es solo la relacion entre una clase Padre y Clase Hija

#Para ello veremos el siguiente ejemplo:
#Tenemos 2 clases:
#Clase Persona
#Clase Profesor

#Cual seria la clase pradre?
#Seria la clase Persona, porque si vemos los atributos que definimos en la Clase persona, esa misma podria usar la Clase Profesor.
#Y si mas adelante tenemos más clases, como, Clase Ingeniero, Clase Astronauta, estos pueden heredar la Clase Persona.

#Creacion Clase Padre: Como hemos venido creando una clase normal, es como se crea la clase Padre, no hay diferencia

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad   = edad

    def saludar(self):
        return "deseo expresar mi mas sentidos saludos a todos los estudiantes que están en el salón de clase."

#Ahora con la creacion de la clase hija:
#En esta clase es donde encontraremos algunos cambios
#primero dentro del metodo __init_ creamos otro constructor super()
# super() me hace la referencia a la clase Padre que es Persona.
# y dentro de super() mandamos los parametros que le corresponde a esa clase( que son nombre, apellido, edad).
#despues de eso ya declaramos los atributos que le corresponden a la clase hija Profesor y le asignamos los parametros que le corresponden

#La clase hija no solo hereda sino que tambien puede extender su funcionalidad ya que puede manejar sus propios metodos.
#En esta clase  creamos un metodo  y dentro estamos retornando un mensaje y dentro del mensaje podemos encontrar que se esta llamando a un metodo que está
#dentro de la clase Padre que es self.saludar()

#De acuerdo a como hemos estructurado nuestra forma de llamar a la clase Padre, es de esta forma como llamamos a sus metodos usando el self. antes del metodo


class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, salario, puesto):
        super().__init__(nombre, apellido, edad)
        self.salario = salario
        self.puesto = puesto
     
    def presentarme(self):
       return f"Hola, mi nombre es {self.nombre} y {self.saludar()}"


#Ahora hacemos uso de las clases creadas y ejecutamos el siguiente ejemplo

primera_persona = Profesor("Joan","Paredes", 36, 25000, "Analista de datos")
saludos = primera_persona.saludar()
print(saludos)
presentarse = primera_persona.presentarme()
print(presentarse)



