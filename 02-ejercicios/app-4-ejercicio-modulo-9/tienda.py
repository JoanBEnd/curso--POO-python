from abc import ABC, abstractmethod
#Clase abstracta
class Tienda:
    def __init__(self, nombre_tienda, ubicacion, ventas_totales , gastos_operativos):
        self.nombre_tienda = nombre_tienda
        self.ubicacion = ubicacion
        self.productos_disponibles = {}
        self.__ventas_totales = ventas_totales
        self.__gastos_operativos = gastos_operativos

#métodos abstractos
    @abstractmethod
    def calcular_ganancias(self):
        pass
    
    @abstractmethod
    def mostrar_informacion(self):
        pass

#getters y setters
    @property
    def ventas_totales(self):
        return self.__ventas_totales
    
    @ventas_totales.setter
    def ventas_totales(self, nueva_venta_total):
        self.__ventas_totales = nueva_venta_total

    @property
    def gastos_operativos(self):
        return self.__gastos_operativos
    
    @gastos_operativos.setter
    def gastos_operativos(self, nuevo_gasto_operativo):
        self.__gastos_operativos = nuevo_gasto_operativo
    

#métodos concretos.
    def agregar_producto(self, nombre, precio):
        self.productos_disponibles[nombre] = precio
    