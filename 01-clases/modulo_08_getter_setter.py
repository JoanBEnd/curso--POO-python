#Si bien en el modulo anterior vimos los 2 metodos que hacian un obtener salario y actualizar salario
#esos metodos eran un getter (get_mostrar_salario) y un setter (actualizar_salario)

#Ahora con ayuda con los decoradores nos permite identificar estos metodos que nos ayudaran a que podamos modificar esos atributos
#pero dandole una legilibidad a nuestro codigo para que pueda ser de mejor acceso y entendible por el desarrollador que pueda ver nuestro código en un futuro.

#Aplicando decoradores:
#El metodo que es el getter, es decir que el obtiene el atributo privado se le asigna el decorador @property, el cual transforma un método en una propiedad,
# lo que significa que podemos acceder a él como si fuera un atributo, sin necesidad de usar paréntesis ()

#El metodo que es el setter, se le asigna como decorador el nombre del metodo getter seguido de un punto y le asignamos el setter explicitamente.

#Entonces para hacerlo entendible o practico a las metodos les cambiamos el nombre, asignandole el del atributo en este caso seria salario.


class Persona:
    def __init__(self, nombre, apellido, edad, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.__salario = salario

    @property
    def salario(self):  #cambiamos el nombre del metodo por salario
        return self.__salario
    
    @salario.setter
    def salario(self, new_salario):  #cambiamos el nombre del metodo por salario
        self.__salario = new_salario

primera_persona = Persona("Joan", "Paredes", 36, 2622)


#Miralo de esta forma, el cambio del nombre de los metodos por practicamente el mismo nombre del atributo lo hace mas sencillo y practico.
#Asi para poder acceder al atributo privado __salario lo hacemos mediante el metodo salario y ya no usamos () y es parecido a como llamar a un atributo publico

#Entonces en el modulo_07 este metodo tenia el nombre de get_mostrar_salario() y se accedia usando los ()
#pero ahora usando los decoradores y cambiando el nombre del metodo a salario se accede como si fuera un atributo público
print(primera_persona.salario) 


#Y para el setter
# En el modulo_07 este metodo tenia el nombre de actualizar_salario() y se accedia usando los () y dentro iba el nuevo valor a actualizar
#pero ahora usando los decoradores y cambiando el nombre del metodo a salario y en este caso le asignamos el valor nuevo como si fuera una nueva variable
primera_persona.salario = 4500

#Y aqui volvemos a llamar al metodo getter para mostrar el nuevo resultado.
print(primera_persona.salario)


#Otra cosa que podria generar confusion a los que estan aprendiendo es que pueden ver 2 métodos con el mismo nombre (como el caso de def salario) y 
# podrias pensar y esto no genera conflicto? A lo que la respuesta seria que no.
#  ya al usar decoradores y la forma en como los utilicemos python sabra  cual de ellos ejecutar

#¿Cómo lo resuelve Python?
#@property: Este decorador marca un método como un "getter", lo que significa que Python lo tratará como una propiedad cuando se acceda al atributo 
# por su nombre (sin paréntesis).
#<nombre>.setter: Este decorador indica que el método será usado para establecer el valor de esa propiedad.

# Gracias a los decoradores, Python sabe cuál método debe ejecutar en cada caso:

#Si accedes al atributo (por ejemplo, objeto.atributo), se ejecuta el método marcado con @property (el getter).
#Si asignas un valor al atributo (por ejemplo, objeto.atributo = valor), se ejecuta el método marcado con el decorador <nombre>.setter (el setter).

# Beneficio:
# Usar decoradores hace que el acceso al atributo privado sea más limpio y legible.
# En lugar de llamar a métodos con (), trabajamos con el atributo como si fuera público,
# pero manteniendo el control y la protección del encapsulamiento.