import ejercicio_facturacion

#En este ejercicio haremos un sistema de facturacion, a continuación tendremos el contexto:

#Contexto: Necesitamos manejar distintos tipos de productos (Productos Físicos, 
#Productos Digitales, Suscripciones) en un sistema de facturación.

#Atributos:
#nombre (públicos)., precio (privado)
#cantidad (privado, accesible mediante getters/setters).
#impuesto (privado, varía según el producto).

#Métodos:
#calcular_total() (polimórfico: el cálculo varía según el producto).
#mostrar_detalle() (común para todas las clases).
#Getters/Setters para cantidad y precio.

primer_mensaje= (
    "A continuación podemos calcular el costo total de acuerdo al tipo de productos:\n"
    "1. Productos Físicos\n"
    "2. Productos Digitales\n"
    "3. Suscripciones\n"    
    )
print(primer_mensaje)
consultar = input("Cual de estos productos desea consultar 1, 2 ó 3: ")

precios_impuesto = {1: [20, 18, ejercicio_facturacion.Productos_Fisicos],
                    2: [25, 10, ejercicio_facturacion.Productos_Digitales],
                    3: [18, 5, ejercicio_facturacion.Suscripciones]}
                   
if consultar.isdigit():
    nombre = input("Ingrese su Nombre: ")
    cantidad = input("Ingrese la cantidad: ")
    
    consultar = int(consultar)
    cantidad = int(cantidad)

    print(precios_impuesto[consultar])


    llamar_funcion = precios_impuesto[consultar][2]
    precio = precios_impuesto[consultar][0]
    impuesto = precios_impuesto[consultar][1]


    producto = llamar_funcion(nombre, cantidad, precio, impuesto)
    print("\n")
    print(producto.mostrar_detalle())
    

    validar_cambio = input("Si está conforme ingrese Si, en caso quiera modificar la cantidad ingrese Modificar :")


    if validar_cambio.upper() == "MODIFICAR":
        nueva_cantidad = input("Ingrese la cantidad a modificar: ")
        nueva_cantidad = int(nueva_cantidad)

        producto.cantidad = nueva_cantidad
        print("\n")
        print(producto.mostrar_detalle())


