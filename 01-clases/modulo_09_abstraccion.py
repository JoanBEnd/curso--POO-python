#Abstraccion:
#Permite manejar la complejidad ocultando los detalles innecesarios y dando las funcionalidades relevantes
#La abstracción viene a ser una plantilla, una estructura el cual definirá los métodos que serán usados en la abstacción y 
#que seran heredados por las subclases o clases hijas y al definir esos métodos en estas subclases usaran esa plantilla
#
#==============================================================================================================================
#Es decir:
#Si en la clase principal se crea un método que tendra un decorador de abstracción con el nombre calcular_suma()
#@abstractmethod
# class def calcular_suma(self):
#
#En la subclase donde usare ese método lo debo crear con el mismo nombre
#
#class def calcular_suma():
#
#==============================================================================================================================

# Lo veremos en el siguiente ejemplo:


from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, apellido, edad, ocupacion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ocupacion = ocupacion
    
    @abstractmethod
    def espacio_laboral(self): #Este metodo que está usando abstracción será creado con el mismo nombre en la subclase que lo herede
        pass


    def saludar(self):
       return f"Mi nombre es {self.nombre} y tengo {self.edad} años"
    


class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, ocupacion):
        super().__init__(nombre, apellido, edad, ocupacion)

    
    def espacio_laboral(self):  #Este metodo debe ser creado con el mismo nombre de la clase donde está con el decorador de abstracción
        return f"Mi cargo u ocupación es de: {self.ocupacion}"
    




joan = Estudiante("Joan", "Paredes", 19, "Estudiante Universitario")
print(joan.espacio_laboral())


martina = Estudiante("Martina", "Melendi", 15, "Estudiante Secundaria")
print(martina.espacio_laboral())



#Ahora:
#Si te has fijado en el método que tiene abstracción dentro de la función estamos solo poniendo
#pass
#Tu te preguntarás, siempre se hará de esa forma cuando creemos nuestras plantillas de clases abstractas
#La respuesta será SI
#En python esta es la forma exacta de crear las clases abstractas donde los métodos no llevaran nada de lógica.
#Podriamos nosotros agregarle alguna lógica si es que fuese necesario y llamar a ese metodo en la subclase con super().metodo_abstroacto_con_logica()
#Pero si hacemos eso, rompemos lo que por definicion seria la abstracción ya que la logica se debe hacer en las subclases que heredan esta
#estructura abstracta de la clase padre.