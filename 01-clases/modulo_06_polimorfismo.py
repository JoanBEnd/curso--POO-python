#El polimorfismo
#permite usar un mismo nombre de metodo en diferentes clases, aun que el comportamiento y resultado puede ser diferente.

#Ejemplo:
#Las siguientes 2 clases tienen el mismo metodo, pero el resultado que nos brinda es distinto.


class Padre():
    def hablar(self):
        return "Habla con tu madre"

class Madre():
    def hablar(self):
        return "Habla con tu padre"



padre = Padre()
madre = Madre()

# Ambos métodos se llaman igual pero tienen diferente implementación:
print(padre.hablar())
print(madre.hablar())


print("=================\n=================")

#polimorfismo en acción:
#Donde podemos pasar el objeto que tiene la clase y ejecutar el mismo metodo que tengan cada clase.

#Ejemplo:

## Una función que puede trabajar con cualquier objeto que tenga un método `hablar`

def ejecutar_saludo(objeto):
    return objeto.hablar()

print(ejecutar_saludo(padre))
print(ejecutar_saludo(madre))