#Ximena Chavarria 21382
#Algoritmos y programación básica
#Sección 10

import re
print("*****************************************")
print("Bienvenido la creación de contraseñas")
print("*****************************************")
contrasenas = []
numero = False
minuscula = False
mayuscula = False
letrasynumeros = False

def recorrerlista():
    puntaje = 0
    conteoM = 0
    conteomin = 0
    for i in range(5):
        contrasena1 = (input("Ingrese su contraseña: "))
        contrasenas.append(contrasena1)
        mayuscula = contrasena1.isupper()
        minuscula = contrasena1.islower()
        letrasynumeros = contrasena1.isalpha() and contrasena1.isdigit()

        #revisar si tiene mas de 8 caracteres
        if (len(contrasena1) >= 8):
           puntaje = puntaje + 5
        #revisar si tiene mayusculas y minusculas
        for i in range(len(contrasena1)):
            letra = contrasena1.isupper()
            if letra == True:
                conteoM = conteoM +1
            else:
                conteomin = conteomin +1
        if conteoM > 0 or conteomin > 0:
            puntaje = puntaje + 10
        #revisar si tiene signos
        if re.search('[.,;:]', contrasena1):
            puntaje = puntaje + 5
        #revisar si tiene letras y numeros
        if letrasynumeros == True:
            puntaje = puntaje + 10
        print(puntaje)

def ordenarcontrasenas():
    contrasenas.sort(reverse=True)
    print("debe seleccionar la contraseñas que aparece primero en la siguiente lista: ")
    print(contrasenas)


#correrprograma
recorrerlista()
ordenarcontrasenas()

