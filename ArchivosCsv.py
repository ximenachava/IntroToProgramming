import csv
datosCSV = []
def leercsv():
    with open("testcsv.csv", newline="") as Archivo:
        leer = csv.reader(Archivo, delimiter=";")
        for fila in leer:
            datosCSV.append(fila)
            print(datosCSV)
    return(datosCSV)
#leercsv()
def escribircsv(carne, nombre, apellido):
#vamos a usar parámetros
    resultado = [carne, nombre, apellido]
    with open("testcsv.csv", "a+",) as Archivo:
        escribir = csv.writer(Archivo, delimiter=";", lineterminator="\n")
        escribir.writerow(resultado)

'''carne = input("Ingrese el carné del estudiante: ")
nombre = input("Ingrese el nombre del estudinante:   ")
apellido = input("Ingrese el apellido del estudiante:")
escribircsv(carne, nombre, apellido)
leercsv()'''

#eliminar una fila
def eliminarCSV(carne):
    resultado = []
    nuevoData = []
    with open("testcsv.csv", newline="") as Archivo:
        leer =csv.reader(Archivo, delimiter=";")
        i = 1
        indice = 0
        for fila in leer:
            i += 1
            if fila[0] == carne:
                resultado.append(fila)
                i = i-2
                with open("testcsv.csv", newline="") as Archivo:
                    leer = csv.reader(Archivo, delimiter=";")
                    for fila in leer:
                        nuevoData.append(fila)
                nuevoData.pop(i)
                with open("testcsv.csv", "w", ) as Archivo:
                    escribir = csv.writer(Archivo, delimiter=";", lineterminator="\n")
                    escribir.writerows(nuevoData)
                break

#elimina un alumno
#carne = input("Ingrese el carné del estudiante: ")
#eliminarCSV()







