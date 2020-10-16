import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 3 numeros
2*4*3 = 24
"""


# start-->
def multiplicar(num1, num2, num3):
    return num1*num2*num3


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1000 al 2000
"""


# start-->
def sumaDivTresYCincoPlus():
    suma=0
    i=1000
    while i>=1000 and i<=2000:
        modulo3 = i%3
        modulo5 = i%5
        if modulo3 == 0 and modulo5 == 0:
            suma+=i
            i+=1
    else:
        i+=1
    result = suma
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area y el volumen de un ortoedro
longitud = 10 m
latitud = 6 m
altura = 5 m

area: A = 2(longitud · latitud + longitud · altura + latitud · altura)
volumen: V = longitud · latitud · altura
"""


# start-->
def definicionOrtoedro(longitud, latitud, altura):
    Area= obtenerArea(longitud, latitud, altura)
    Volumen = obtenerVolumen(longitud, latitud, altura)
    result = {
        'area':Area,
        'volumen':Volumen,
    }
    return result


def obtenerArea(longitud, latitud, altura):
    result = 2*((longitud*latitud)+(longitud*altura)+(latitud*altura))
    return result


def obtenerVolumen(longitud, latitud, altura):
    result = longitud*latitud*altura
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Ortoedro:
    def definicionOrtoedro(self, longitud, latitud, altura):
        Area= obtenerArea(longitud, latitud, altura)
        Volumen = obtenerVolumen(longitud, latitud, altura)
        result = {
            'area':Area,
            'volumen':Volumen,
        }
        return result


"""
***************************************************************
@@ ejercicio 5 @@
VentaComputadoras
Computadora
    procesador
    ram
    tarjeta_grafica
    ssd
    costo
    conDescuento
    descuento
    conPlazo
    cuota
"""


class VentaComputadoras:
    def orden(self):
        pass

    def totalProcesadorIntel(self):
        return 0

    def totalRam16ConDescuento(self):
        return 0


class Computadora:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/victoriaZepeda/AndreaVictoriaVasquezZepeda_20192380.git"
