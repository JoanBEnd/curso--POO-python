import herencia
 
mensaje = (
           "====================================\n"
           "Ingrese la información del cliente\n"
           "====================================\n"
)

print(mensaje)

nombre = input("Ingrese el nombre: ")
apellidos = input("Ingrese el apellido: ")
edad = input("Ingrese la edad: ")
genero = input("Ingrese el género: ")
cuenta = input("Ingrese el numero de la cuenta: ")
saldo = input("Ingrese el saldo: ")
tipo = input("Ingrese el tipo de cuenta: ")

primer_cliente = herencia.Cliente(nombre, apellidos, edad, genero, cuenta, saldo, tipo)

persona_reg = primer_cliente.crear_persona()
cuenta_reg = primer_cliente.crear_cuenta_bancaria()

resultado = primer_cliente.informacion_cliente()
print("\n==============Mensajes de confirmación================\n")

print(persona_reg)
print(cuenta_reg)

print("\n============= Mostrar los datos registrados =================\n")
print(resultado)

print(herencia.Cliente.mro())
