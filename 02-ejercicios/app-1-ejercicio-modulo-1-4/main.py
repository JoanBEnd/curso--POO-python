import clase

presentacion = (
            "===========================================================\n"
            "En esta ocasión vamos a llenar los datos de un estudiante:\n"
)
print(presentacion)

while True:
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = input("Ingrese la edad: ")
    curso = input("Ingrese los cursos: ")

    curso = list(curso)

    espacio = ("\n"
            "Que desea hacer:\n"
            "1. Mostrar todos los datos\n"
            "2. Mostrar los cursos\n"
            "3. Salir"
            )
    print(espacio)

    elegir_opcion = int(input("Ingrese una opción: "))
    estudiante = clase.Estudiante(nombre, apellido, edad, curso)
    
    if elegir_opcion == 1:
        
        informacion = estudiante.mostrar_informacion()
        print("\n=============Mostrar resultado=================")
        print(informacion)
    elif elegir_opcion == 2:
        cursos = estudiante.cursos_registrados()
        print("\n=============Mostrar resultado=================")
        print(cursos)
    else:
        break
 