class Persona:
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def crear_persona(self):
        return f"Se realizó el registro correcto de {self.nombre} {self.apellido}"

class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo, tipo):        
        self.cuenta = numero_cuenta
        self.saldo = saldo
        self.tipo = tipo

    def crear_cuenta_bancaria(self):
        return f"Se realizó el registro de la cuenta {self.cuenta} del cliente: {self.nombre} {self.apellido}"

    def mostrar_cuenta(self):
        return  f"La cuenta del cliente es {self.cuenta} y cuenta con un saldo de: {self.saldo}"
    
class Cliente(Persona, CuentaBancaria):
    def __init__(self,  nombre, apellido, edad, genero, numero_cuenta, saldo, tipo):
        
        Persona.__init__(self, nombre, apellido, edad, genero)
        CuentaBancaria.__init__(self, numero_cuenta, saldo, tipo)

    def informacion_cliente(self):

        mensaje = ("los datos del cliente son: \n"
                   f"Nombre Completos: {self.apellido}, {self.nombre} \n"                   
                   f"Edad: {self.edad}  - Género: {self.genero}\n"
                   f"{super().mostrar_cuenta()}"
                   )

        return mensaje


