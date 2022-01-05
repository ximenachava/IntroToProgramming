# Ximena Chavarria 21382
# Ejercicio 04, Persistencia de Datos y Archivos
# Algoritmos y Programación Básica, Ciclo II 2021

from tabulate import tabulate
import csv
datosCSV = []
#Módulo para leer el archivo
def leercsv():
    with open("TemarioB.csv", newline="") as Archivo:
        leer = csv.reader(Archivo, delimiter=",")
        for fila in leer:
            datosCSV.append(fila)
            print(datosCSV)
    return(datosCSV)


#Módulo para agregar una nueva serie
def escribircsv():
    FechaInicio = input("Ingresa la fecha en la que iniciaste a ver la serie (Formato dd/mm/aaaa): ")
    NombreSerie = input("Ingrese el nombre de la nueva serie: ")
    Estado = input("Ingresa el estado  de la serie, ingresa uno de los siguientes: \n En proceso, Finalizado o Nunca la terminé de ver ")
    Duracion = int(input("Ingresa la duración de cada capítulo en minutos"))
    CapitulosVistos = int(input("Ingresa cuántos capítulos has visto de la serie"))
    Plataforma = input("Ingresa en qué plataforma viste la serie")
    TiempoInvertido = Duracion*CapitulosVistos

    nuevaserie = [FechaInicio, NombreSerie, Estado, Duracion, CapitulosVistos, Plataforma, TiempoInvertido]
    with open("TemarioB.csv", "a+", ) as Archivo:
        escribir = csv.writer(Archivo, delimiter=",", lineterminator="\n")
        escribir.writerow(nuevaserie)
        return(datosCSV)


def modificarestado():
    with open("TemarioB.csv") as Archivo:
        lector = csv.reader(Archivo, delimiter=",")
        for fila in lector:
            buscar = input("Ingrese la serie que quiere modificar")
            if buscar == datosCSV[2]:
                nuevoestado = input("ingrese el nuevo estado de la serie")
                datosCSV[5] = nuevoestado
            else:
                print("No se puede")
            break

#Mostrando todas las series vistas en un formato amigable
def mostrarcsv():
    print(tabulate(datosCSV, headers="", tablefmt="fancy_grid"))


def Reportes():
    with open("TemarioB.csv") as Archivo:
        lector = csv.reader(Archivo, delimiter=",")
        linea = 0
        for fila in lector:
            if linea == 0:
                print(f'los nombres de las columnas son:{", ".join(fila)} \n')
                linea += 1
            else:
                print(fila[5])


def menu():
    bandera = True
    while bandera :
        print("1. Leer los Datos \n"
              "2. Modificar el Estado de una Serie\n"
              "3. Ingresar una nueva Serie\n"
              "4. Mostrar todas las Series\n"
              "5. Mostrar los Reportes\n"
              "6. Salir del Sistema")

        opcion = int(input("Ingrese opción del menú: "))
        if opcion == 1:
            leercsv()
        if opcion == 2:
            modificarestado()
        if opcion == 3:
            escribircsv()
        if opcion == 4:
            mostrarcsv()
        if opcion == 5:
           Reportes()
        if opcion == 6:
            bandera = False




menu()