import tienda

Tienda = tienda.Tienda

class Mascotas_Exoticas(Tienda):
    def __init__(self, nombre_tienda, ubicacion,  ventas_totales, gastos_operativos):
        super().__init__(nombre_tienda, ubicacion,  ventas_totales, gastos_operativos)
    

    def calcular_ganancias(self):
        
#calculamos los gastos operativos     
        total_prod = sum(self.productos_disponibles.values())
 
#calculamos los gastos operativos           
        self.ventas_totales = total_prod
        self.gastos_operativos = total_prod * 0.15

        mensaje =  (
                    f"El total de o los productos es: {self.ventas_totales - self.gastos_operativos}\n"
                    f"El total de gastos operativos es: {self.gastos_operativos}\n"
                    f"Costo de venta total: {self.ventas_totales}\n"
        )

        return mensaje
 
    def mostrar_informacion(self):
#Devolvemos el mensaje completo de la venta.       
        texto = ""
        for key, value in self.productos_disponibles.items():
            texto = texto + f"{key}: {value}\n"

        mostrar_informacion = (
            "\n=========================================\n"
            "Los productos adquiridos por el comprador son: \n"
            f"{texto}\n"
            f"============\n"
            f"{self.calcular_ganancias()}"
        )
        
        return mostrar_informacion
    
    def agregar_venta(self, nombre, precio):
        self.agregar_producto(nombre, precio)