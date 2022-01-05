#Paulina Jimenez 21464
#Nathalia Oliva 21118
#Ayda Sulecio 21128
#Ximena Chavarria 21382
#Seccion 10
#Proyecto final
#Programa Book me

import tabulate

def menu():
    banderaM = True
    while banderaM:
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print("\t Bienvenid@a Book.me")
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print ("\t 1. Donador (Registro)")
        print ("\t 2. Donatario (Retirar)")
        print ("\t 3. Ver disponibilidad de libros")
        print ("\t 4. Salir")
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        OpcionPrincipal = int(input("¿Va a donar o retirar libros?, ingrese el numero de la opcion que desee: "))
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        if OpcionPrincipal ==1:
            donador()
        elif OpcionPrincipal ==2:
            donatario()
        elif OpcionPrincipal ==3:
            disponibilidad()
        elif OpcionPrincipal ==4:
            banderaM = False
        else:
            print ("Porfavor ingrese una opcion de las del menu para poder continuar")
            
            
basedatos3 = []
basedatos1 = {}

def donador():
    bandera1 = True
    while bandera1:
        print("Inicio formulario: pregunta 1/7") 
        GastoEnvio1 = int(input("¿Desea donar para el envio?, Si (1) o No (2): " ))
        
        if GastoEnvio1 == 1:
            print("Te sugerimos que dejes  entre Q25 y Q50 en efectivo")
        elif GastoEnvio1 == 2:
            print("Muchísimas gracias por tu donación, esperamos que a la próxima te sea posible regalar un envío!")
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print("Pregunta 2/7")
        EstadoLibro1= int(input("Ingrese el estado del libro en una escala de 1 a 5 (1 siendo mal estado y 5 excelente estado): "))
        
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print("Pregunta 3/7")
        NombreLibro1= input("Ingrese el nombre del libro: ")
        
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print("Pregunta 4/7")
        MateriaLibro1= input("Ingrese la materia a la que pertenece el libro: ")
        
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print("Pregunta 5/7")
        GradoLibro1= int(input("Ingrese el grado (de 1ro a 6to primaria) al que pertenece el libro (recuerda solamente ingresar numeros del 1 al 6): "))
        
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print("Pregunta 6/7")
        TipoLibro1= int(input("Indique si el libro es práctico (1) o teórico (2): "))
        
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print("Pregunta 7/7")
        ISBN1=int(input("Ingrese el ISBN del libro, debe consistir de 13 dígitos: "))
        
        basedatos1[ISBN1] = {"Nombre": NombreLibro1, "Estado": EstadoLibro1, "Materia": MateriaLibro1, "Grado": GradoLibro1, "Tipo": TipoLibro1}
        
        basedatos3 = [ISBN1, NombreLibro1]
        
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        
        regresar = input("¿Desea donar otro libro? S/N: ")
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        
        if (regresar == "N"):
                bandera1 = False
        return(basedatos1)
                
basedatos2 = {}                
def donatario():
    bandera2 = True
    while bandera2:
        print("Inicio formulario: pregunta 1/9") 
        Beneficiario2= int(input("Indique si el beneficiario es una institucion (1) o escuela (2): "))
        
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print("Pregunta 2/9")
        NombreBeneficiario2= input("Ingrese el nombre del beneficiario: ")
        
        
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print("Pregunta 3/9")
        GastoEnvio2 = input("¿Necesita cubrir el gasto de envio? S/N: ")
        
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print("Pregunta 4/9")
        NombreLibro2= input("Ingrese el nombre del libro a retirar: ")
        
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print("Pregunta 5/9")
        EstadoLibro2= int(input("Ingrese el estado del libro en una escala de 1 a 5 (1 siendo mal estado y 5 excelente estado): "))
        
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print("Pregunta 6/9")
        MateriaLibro2= input("Ingrese la materia a la que pertenece el libro: ")
        
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print("Pregunta 7/9")
        GradoLibro2= input("Ingrese el grado (de 1ro a 6to primaria) al que pertenece el libro (recuerda solamente ingresar numeros del 1 al 6): ")
        
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print("Pregunta 8/9")
        TipoLibro2= int(input("Indique si el libro es práctico (1) o teórico (2): "))
        
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
        print("Pregunta 9/9")
        ISBN2=int(input("Ingrese el ISBN del libro, debe consistir de 13 dígitos: "))
        
        borrar= ISBN2
        del basedatos1 [borrar]
        
        
        basedatos2[ISBN2] = {"Nombre": NombreLibro2, "Estado": EstadoLibro2, "Materia": MateriaLibro2, "Grado": GradoLibro2, "Tipo": TipoLibro2}
       
       
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")

        regresar = input("¿Desea retirar otro libro? S/N: ")
        print("✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎")
         
        if (regresar == "N"):
                bandera2 = False

        return(basedatos1)
 
def disponibilidad():
   print(tabulate(basedatos3, headers=["Nombre", "ISBN"], tablefmt = "fancy_grid"))
    


menu()

