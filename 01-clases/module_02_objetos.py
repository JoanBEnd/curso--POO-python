import module_01_clase_libo as module_01_clase_libo

data = module_01_clase_libo.Libro()


#El objeto viene a ser la instancia de una clase. Que quiere decir esto, que el objeto viene a ser una representacion concreta de la plantilla que se define
# en la clase.
#Al momento de ejecutar clases_libo.Libro(), esto crea un objeto en memoria y se lo asignamos la variable data. data no viene ser un objeto en si, sino que
#esa variable va apuntar al objeto que está en memoria y como sabemos eso, porque al momento de ejecutar el print(data)
print(data)
#nos mostrará algo como esto: <clases_libo.Libro object at 0x00000257A1EBCA40>

#Esto 0x00000257A1EBCA40 es una direccion en memoria, el cual la variable data apunta para traer los datos.
print(data.autor)

#Si tenemos la misma instancia o muchas instancias de una clase asignadas a una variable
data2 = module_01_clase_libo.Libro()
data3 = module_01_clase_libo.Libro()
#veremos que se crean en distintos lugares de la memoria y que las variables donde asignamos esas instancias nos apuntan a esos lugares de memoria.
print(data2)
print(data3)
