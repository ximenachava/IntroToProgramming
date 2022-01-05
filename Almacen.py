from tabulate import tabulate
datos = []

#CREAR EL ARCHIVO Y MANDAR DATOS
def agregarUsuario():
    archivo = open("testmelvin.txt", "a+", encoding = "utf-8")
    codigo = input("Ingrese el código: ")
    nombre = input("Ingrese el nombre: ")
    direccion = input("Ingrese su dirección: ")
    telefono = input("Ingrese su número telefónico: ")
    datos = archivo.write(codigo + ", " +
                          nombre + ",  " +
                          direccion +  ", " +
                          telefono + "\n")
    archivo.close()

#DESPLEGAR INFORMACIÓN DEL ARCHIVO
def desplegarInfo():
    archivo = open("testmelvin.txt", "r", encoding = "utf-8")
    datos = archivo.readlines()
    archivo.close()
    datos = list(linea.split(', ') for linea in datos)
    print(tabulate (datos,
                    headers = ["CODIGO",
                               "NOMBRE",
                               "DIRECCION",
                               "TELEFONO"],
                    tablefmt='fancy_grid'))


#ELIMINAR UN USUARIO
def eliminarUsuario():
    temp = ""
    eliminar = 0
    archivo = open("testmelvin.txt", "r", encoding = "utf-8")
    datos = archivo.readlines()
    datos = list(datos.split(", ") for datos in datos)
    archivo.close()
    
    print (datos)
    codigo = input("Ingrese el código del usuario a eliminar: ")
    for fila in range (len(datos)):
        for columna in range (len(datos[fila])):
            print (datos[fila][columna])
            if datos[fila][columna] == codigo:
                eliminar = fila
                #datos.pop(fila)
                break            
            #else:
            #    print("no lo encontré")
    
    datos.pop(eliminar)
    
    archivo = open("testmelvin.txt", "w", encoding ="utf-8")
    temporal = list(datos)
    
    for fila in range(len(temporal)):
        for columna in range(len(temporal[fila])):
            
            if columna == 4:
                
                temp = str(temp) + str(temporal[fila][columna]) + str('\n')
                 
            else:
                temp = str(temp) + str(temporal[fila][columna]) + str(", ")        
        print (temp)
        temp = temp[:-2]
        print(temp)
        datos = archivo.writelines(temp)
        temp = ""
    archivo.close()

def modificarusuario():
    archivo = open("testmelvin.txt", "r", encoding="utf-8")
    datos = archivo.readlines()
    datos = list(datos.split(", ") for datos in datos)
    archivo.close()

    codigo = input("ingrese el codigo del usuario que desea modificar")
    for fila in range(len(datos)):
        for columna in range(len(datos[fila])):
            if datos[fila][columna] == codigo:
                cambio = input("ingrese el nombre por el cual desea cambiar el existente: ")
                datos[fila][1] = cambio
    print(datos)
#-----------------------------------------------------------------------#
    archivo = open("testmelvin.txt", "w", encoding="utf-8")
    temporal = list(datos)

    for fila in range(len(temporal)):
        for columna in range(len(temporal[fila])):

            if columna == 4:

                temp = str(temp) + str(temporal[fila][columna]) + str('\n')

            else:
                temp = str(temp) + str(temporal[fila][columna]) + str(", ")
        print(temp)
        temp = temp[:-2]
        print(temp)
        datos = archivo.writelines(temp)
        temp = ""
    archivo.close()


#haciendo menu de opciones
def menu():
    bandera = True
    while bandera :
        print("1. Ingreso de datos \n"
              "2. Listar Usuarios\n"
              "3. Eliminar usuarios\n"
              "4. Actualizar Usuarios\n"
              "5. Salir\n")

        opcion = int(input("Ingrese opción del menú: "))
        if opcion == 1:
            agregarUsuario()
        if opcion == 2:
            desplegarInfo()
        if opcion == 3:
            eliminarUsuario()
        if opcion == 4:
           modificarusuario()
        if opcion == 5:
            bandera = False


menu()






                
                        
