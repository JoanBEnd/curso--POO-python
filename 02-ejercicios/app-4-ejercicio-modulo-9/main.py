import tienda_mascotas_domesticas
import tienda_mascotas_exoticas
import servicios_veterinarios

#Las subclases importadas las asignamos a una vaiable para que sea más legible
mascotas = tienda_mascotas_domesticas.Mascotas_Domesticas
exoticos = tienda_mascotas_exoticas.Mascotas_Exoticas
servicios = servicios_veterinarios.Servicios_Veterinario

primer_parrafo = (
    "Elija la tienda de su preferencia: \n"
    "1. Mascotas Domésticas\n"
    "2. Animales Exóticos. \n"
    "3. Servicios Veterinarios\n"
    )

#Asignamos un diccionario para ingresar a esta información de acuerdo al tipo de tienda que seleccionemos
dict_tiendas = {1: ["Mascotas Domésticas","Av Panamericana - 154", mascotas],
                2: ["Animales Exóticos","Av Metropolis - 1311", exoticos],
                3: ["Servicios Veterinarios","Av Zuloaga - 573", servicios]
                }

print(primer_parrafo)

tienda_seleccionada = input("Que tienda desea elegir 1, 2 ó 3: ")

tienda_seleccionada = int(tienda_seleccionada)

#De acuerdo a la tienda seleccionada obtenemos las opciones de servicio que brinda cada tienda
dict_preguntas_compras = {1: ["Que desea compra: \n 1. Medicina\n 2. Comida\n 3. Suplementos\n"],
                          2: ["Que desea compra: \n 1. Medicina\n 2. Comida\n 3. Suplementos\n"],
                          3: ["Que servicio requiere: \n 1. Baño\n 2. Corte y Baño\n 3. Atencion Médica\n"]}


#De acuerdo a la tienda seleccionada, obtenemos:
nombre_tienda = dict_tiendas[tienda_seleccionada][0] #nombre de la tienda
ubicacion = dict_tiendas[tienda_seleccionada][0] # ubicacion de la tienda
mi_funcion_general = dict_tiendas[tienda_seleccionada][2] #La clase que se usara para ejecutar las funciones
funcion_comprador = mi_funcion_general(nombre_tienda, ubicacion, 0, 0)  #Asignamos la clase a un objeto


segundo_parrafo = ""

#Ingresa si son las 2 primeras Tiendas de mascotas
if tienda_seleccionada in (1, 2):

   
    for texto in dict_preguntas_compras[tienda_seleccionada]:
        segundo_parrafo = texto
        
#Mostramos lo que ofrece la tienda
    print(segundo_parrafo)

    compra_seleccionar = input("Que desea compar 1, 2 ó 3: ")
    compra_seleccionar = int(compra_seleccionar)

#Hacemos un recorrido en caso quisieramos más de un producto, para pode ingresar el producto y el precio    
    while True:
            
        nombre_producto = input("Ingrese el producto: ")
        precio = input("Ingrese el precio: ")
        #vamos agregando en el diccionario el producto y el precio usando la funcion de la clase tienda que ha sido heredada
        funcion_comprador.agregar_venta(nombre_producto, int(precio))

        #Validamos si queremos continuar agregando mas productos o salir
        validar_compra = input("Desea agregar otro producto o terminar la Compar  Continuar/Terminar: ")
        if validar_compra.upper() == "TERMINAR":
            break

    #Despues de agregar los productos hacemos los calculos usando las funciones internas.
    funcion_comprador.calcular_ganancias()
    #Mostramos la información     
    print(funcion_comprador.mostrar_informacion())

    
#Ingresa a la tienda de Servicios De Atención
else:
    for texto in dict_preguntas_compras[tienda_seleccionada]:
        segundo_parrafo = texto

    #Mostramos lo que ofrece la tienda
    print(segundo_parrafo)
    
    #Hacemos un recorrido en caso quisieramos más de un producto, para pode ingresar el producto y el precio  
    while True:

        compra_seleccionar = input("Que servicio desea 1, 2 ó 3: ")
        compra_seleccionar = int(compra_seleccionar)
        
        if compra_seleccionar == 1:
            nombre_producto = "Baño"
        elif compra_seleccionar == 2:
            nombre_producto ="Corte y Baño"
        else:
            nombre_producto ="Atención Médica"

        precio = input("Ingrese el precio: ")
        
        #vamos agregando en el diccionario el producto y el precio usando la funcion de la clase tienda que ha sido heredada
        funcion_comprador.agregar_venta(nombre_producto, int(precio))

        #Validamos si queremos continuar agregando mas productos o salir
        validar_compra = input("Desea agregar otro producto o terminar la Compar  Continuar/Terminar: ")

        if validar_compra.upper() == "TERMINAR":
            break

    #Despues de agregar los productos hacemos los calculos usando las funciones internas.
    funcion_comprador.calcular_ganancias()

    #Mostramos la información         
    print(funcion_comprador.mostrar_informacion())

