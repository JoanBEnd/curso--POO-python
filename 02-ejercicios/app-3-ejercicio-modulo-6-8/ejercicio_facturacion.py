class Facturacion:
    def __init__(self, nombre, precio, cantidad, impuesto):
        self.nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad
        self.__impuesto = impuesto

    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad


    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio


    @property
    def impuesto(self):
        return self.__impuesto
        
    def calcular_total(self):
        return self.__cantidad * self.precio


class Productos_Fisicos(Facturacion):
    def __init__(self, nombre, precio, cantidad, impuesto):
        super().__init__(nombre, precio, cantidad, impuesto)
    
    def mostrar_detalle(self):
        mensaje =  ("Datos del comprador:\n"
                    f"Nombre: {self.nombre}\n"
                    f"Cantidad productos: {self.cantidad} total: {super().calcular_total()}\n"
                    f"Impuesto generado: {self.impuesto} %"

                    )

        return mensaje


class Productos_Digitales(Facturacion):
    def __init__(self, nombre, precio, cantidad, impuesto):
        super().__init__(nombre, precio, cantidad, impuesto)

    def mostrar_detalle(self):
        mensaje =  ("Datos del comprador:\n"
                    f"Nombre: {self.nombre}\n"
                    f"Cantidad productos: {self.cantidad} total: {super().calcular_total()}\n"
                    f"Impuesto generado: {super().impuesto} %"

                    )

        return mensaje
    
class Suscripciones(Facturacion):
    def __init__(self, nombre, precio, cantidad, impuesto):
        super().__init__(nombre, precio, cantidad, impuesto)

    def mostrar_detalle(self):
        mensaje =  ("Datos del comprador:\n"
                    f"Nombre: {self.nombre}\n"
                    f"Cantidad productos: {self.cantidad} total: {super().calcular_total()}\n"
                    f"Impuesto generado: {self.impuesto}%"

                    )

        return mensaje


#Si solo quieres ejecutar este archivo deshabilita este codig de abajo y pruébalo:
 

# producto_digital= Productos_Digitales("Joan", 25, 45, 18)
# print(producto_digital.mostrar_detalle())
# producto_digital.precio = 48
# print("======================================")
# print(producto_digital.mostrar_detalle())

# print("\n\n")

# producto_digital= Productos_Fisicos("Martina", 12, 30, 17)
# print(producto_digital.mostrar_detalle())
# producto_digital.precio = 38
# print("======================================")
# print(producto_digital.mostrar_detalle())