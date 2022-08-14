dict_cedula = {}

while True:
    opciones = ['1. Registrar', '2. Consultar', '3. Actualizar nota', '4. Borrar', '5. Salir']

    #Recorrer el menu
    def recorrerMenu(lista):
        print("\nFundamentos de computacion")
        for i in lista:
            print(i)
    recorrerMenu(opciones)

    while True:
        try:
            #Bucle para pedir una opcion dentro del rango
            op = -1
            while op < 1 or op > len(opciones):
                op = int(input('Eliga una opcion: '))
                if op < 1 or op > len(opciones):
                    print("Por favor ingrese una opcion dentro del rango :)\n")
            break
        except ValueError:
            print('Caracter no valido, debe ingresar un numero\n')

    
    if op == 1:
        print("\n#### Registrar ####")
        cedula = input("Ingrese la cedula: ")
        nombre = input("Ingrese el nombre: ")
        nota = input("Ingrese la nota: ")
        paralelo = input("Ingrese el paralelo: ")
        lista_datos = [nombre, nota, paralelo]
        dict_cedula[cedula] = lista_datos
        print("Estudiante ingresado correctamente!\n")
    
    if op == 2:
            print("\n#### Consultar ####")
            cedula_buscar = input("Ingrese la cedula: ")
            if dict_cedula.get(cedula_buscar):
                print(f"Estudiante {dict_cedula[cedula_buscar][0]} con cedula {cedula_buscar} del paralelo {dict_cedula[cedula_buscar][2]} su nota parcial es {dict_cedula[cedula_buscar][1]}\n")
            elif dict_cedula.get(cedula_buscar) == None:
                print("Estudiante no encontrado!\n")

    if op == 3:
            print("\n#### Actualizar nota ####")
            cedula_buscar = input("Ingrese la cedula: ")
            if dict_cedula.get(cedula_buscar):
                print(f"Nota actual del estudiante: {dict_cedula[cedula_buscar][1]}")
                nota_actualizada = input("Actualizacion: ")
                print("...\nActualizando\n...")
                nombre = dict_cedula[cedula_buscar][0]
                paralelo = dict_cedula[cedula_buscar][2]
                dict_cedula.update({cedula_buscar:[nombre, nota_actualizada, paralelo]})
                print("Nota actualizada correctamente!")
                print(f"Estudiante {dict_cedula[cedula_buscar][0]} con cedula {cedula_buscar} del paralelo {dict_cedula[cedula_buscar][2]} su nota parcial es {dict_cedula[cedula_buscar][1]}\n")
            elif dict_cedula.get(cedula_buscar) == None:
                print("Estudiante no encontrado!\n")

    if op == 4:
            cedula_buscar = input("Ingrese la cedula: ")
            if dict_cedula.get(cedula_buscar):
                dict_cedula.pop(cedula_buscar)
                print("Estudiante eliminado con exito!\n")
            elif dict_cedula.get(cedula_buscar) == None:
                print("Estudiante no encontrado!\n")
    if op == 5:
            break