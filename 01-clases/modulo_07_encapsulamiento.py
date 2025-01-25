
#Encapsulamiento
#El encapsulamiento permite proteger las atributos, limitando el acceso directo.
# Para interactuar con estos atributos protegidos, se suelen utilizar métodos definidos dentro de la clase, como setters y getters,
# que pueden incluir decoradores.

#
#atributos privados: self.__nombre
#atributos públicos: self.nombre

#Que pasa con el privado: Al asignar el doble guion __, lo que hace es que protege el atributo y si queremos
#acceder de manera directa no se podrá, lo veremos lineas abajo.
#Es útil que usar atributos privados con la finalidad de no comprometer la lógica de negocio e integridad de los datos.

#No necesariamente todos los atributos deben ser privados, sino solo los que son necesarios para la logica del negocio o aquellos sencibles que requieran
#algun trato especial.

class Persona:
    def __init__(self, nombre, apellido, edad, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.__salario = salario

    def get_mostrar_salario(self):
        return self.__salario
    
    def actualizar_salario(self, new_salario):
        self.__salario = new_salario

primera_persona = Persona("Joan", "Paredes", 36, 2622)

#Para poder acceder a un atributo es a travez de un metodo, como el método usa self, este puede
#llamar al atributo privado ya que está dentro de la misma clase y de esa forma se puede acceder
salario = primera_persona.get_mostrar_salario()
print(salario)

#Podemos actualizar un atributo privado, mediante otro metedo enviando el nuevo valor y reemplazando.
primera_persona.actualizar_salario(4500)
new_salario = primera_persona.get_mostrar_salario() 
print(new_salario)


#Aqui es donde queremos acceder a ese atributo que es privado y al acceder nos arrojara un error.
#print(primera_persona.__salario)

#Pero hay otra forma de acceder al atributo privado el cual no es recomendado debido a que rompe el porpósito del ENCAPSULAMIENTO.
#Te dejo esta forma para que sepas como se accede pero recalcando que no es RECOMENDADO.
print(primera_persona._Persona__salario)

 

#En el siguiente modulo veremos los setters y getters.
#Estos se aplicaran a los metodos que estan en la clase (get_mostrar_salario, actualizar_salario) usaremos el mismo ejercicio.