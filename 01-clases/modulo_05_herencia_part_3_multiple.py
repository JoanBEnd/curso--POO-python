#La herencia multiple, es un poco más compleja, pero nos permite a que una clase hija
#pueda heredar metodos y atributos a más de una clase padre.
#Gráfica
#                             --------------------                       ------------- 
#                                  persona                                Programador
#                            ---------------------                      --------------
#                                    |                                         |                          
#                                    ------------------------------------------
#                                                       |                                    
#                                             -------------------
#                                             EmpleadoProgramador   
#                                             ------------------

class Persona:
    def __init__(self, nombre, apellidos, edad, genero):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.genero = genero

class Programador:
    def __init__(self, skill):
        self.skill = skill

    def mostrar_skill(self):
        return f"El skill del programador es: {"".join(habil for habil in self.skill)}"


#Donde veremos este cambio significativo es en la clase hija

#Todas las clases que usara la clase hijo se agregan en el inicio dentro del ()
#Como vimos en los 2 modulos anteriores cuando hacemos referencia a la clase Padre usamos super().
#En este caso como es mas de 1 clase Padre usamos los mismo nombres de cada Clase Padre.

#Con respecto a los metodos dentro de la clase hija:
#Si queremos llamar a metodos de la clase padre podemos usar super().metodo(), esto lo vemos en el ejemplo de consultar_empleador.


class EmpleadoProgramador(Persona, Programador):
    def __init__(self, nombre, apellidos, edad, genero, skill, puesto, salario):
        Persona.__init__(self, nombre, apellidos, edad, genero)
        Programador.__init__(self, skill)
        self.puesto = puesto
        self.salario = salario
    
    def consultar_empleador(self):
        return f"La información del empleado es: {self.nombre} {self.apellidos} y {super().mostrar_skill()}"
    



persona_programador = EmpleadoProgramador("Joan", "Paredes", 36, "Masculino", "python, power bi", "Analista de datos", 6500)
mostrar_skill = persona_programador.mostrar_skill()
print(mostrar_skill)

consultar_programador = persona_programador.consultar_empleador()
print(consultar_programador)


#Ahora si te preguntas si puedo usar self.mostrar_skil() en vez de super().mostrar_skill() para llamar al metodo de la clase padre, la respuesta en corto seria si.
#Veamos un poco más:

#Lo ideal como buena práctica si quiere llamar a un metodo de la clase padre es ideal usar super()
#self seria ideal si tienes un método dentro de la instancia actual o en este caso de la clase hija y si tiene el mismo nombre de método
#el cual hará algo distinto y quieres usar eso, pues self.mostrar_skill() seria lo ideal.

#A continuacion usamos la misma clase hija con el cambio respectivo

#class EmpleadoProgramador(Persona, Programador):
#    def __init__(self, nombre, apellidos, edad, genero, skill, puesto, salario):
#        Persona.__init__(self, nombre, apellidos, edad, genero)
#        Programador.__init__(self, skill)
#        self.puesto = puesto
#        self.salario = salario
# 
#   def mostrar_skill():
#       return "Bienvenidos al trabajo"
#     
#    def consultar_empleador(self):
#        return f"La información del empleado es: {self.nombre} {self.apellidos} y {self.mostrar_skill()}"

# En este caso self.mostrar_skill() llamara al método que esta dentro de la clase hija EmpleadoProgramador()
