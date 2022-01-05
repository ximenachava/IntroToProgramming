def menu():
    bandera = True

    while bandera:
        print("*****************************************")
        print("Bienvenido al cálculo del salario")
        print("*****************************************")
        print("1. Ingreso de datos")
        print("2. Reporte")
        print("3. Salida del sistema")
        opcion = int(input("Ingrese opcion: "))
        if opcion == 1:
            ingresoDatos()
        else:
            bandera = False
            if datos == 0:
                print("Ingrese datos primero")
                ingresoDatos()
            else:
                if opcion == 2:
                    Reporte()
            exit()
datos = 0
def ingresoDatos():
    nombre= input("Ingrese su nombre:")
    print("*****************************************")
    print( "********Código de trabajador  *********\n")
    print("**** 1. Constructor   **** ")
    print("**** 2. Administrador ****")
    print("**** 3. Inspector     ****")
    puesto= input("Ingrese el código del Puesto: ")
    print("\n*****************************************")
    telefono= input ("Ingrese su teléfono:")
    horasTrabajadas= int(input("Ingrese horas trabajadas:"))
    costo= 0
    HorasExtras= horasTrabajadas-8

    if HorasExtras< 0:
        HorasExtras= 0

    if puesto == "1":
        costo = 18
    elif puesto =="2":
        costo = 30

    elif puesto== "3":
        costo = 40


    salario= costo * horasTrabajadas + (HorasExtras * costo * 2)

    IGSS= salario*0.0483

    Seguro= salario*0.01

    CuotaP= salario*0.1267

    IGSSP= salario*0.1067

    SalarioBruto= salario+(IGSS + Seguro)

    SalarioLiquido= salario-(IGSS + Seguro)

def Reporte():
    print("*****************************************")
    print("Reporte Final: Boleta de Pago")
    print("*****************************************\n")


    print("Empleado:", nombre)
    print("Trabajó:", horasTrabajadas, "horas")
    print("\t Salario Bruto: ", SalarioBruto)
    print("\t Descuentos")
    print("IGSS: ", IGSS)
    print("Seguro:", Seguro)
    print("\t Aportes de la empresa")
    print("Cuota Patronal: ", CuotaP)
    print("IGSS Patronal: ", IGSSP)
    print("\t Salario Real")
    print("\t", SalarioLiquido)
menu()




