#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import *
#Importamos todo de math 
print("aaaaa")
print("bbbbbbb")
print("cccccc")
print("ddddd")
file = open('caneva2.txt','r')
nuevo = open('nuevo.txt', 'w')
#Abre archivo y lo lee, escribira uno nuevo
R=6300000
latPT = float(raw_input("Por favor indica la Latitud: "))
lonPT = float(raw_input("Por favor indica la Longitud: "))
#Definimmos el valor de R y los datos de latitud y longitud los pedimos de consola 
file.readline()
#Saca primer linea del archivo, son encabezados 
for line in file:
#Ciclo for que recorrera linea por linea del archivo

    # separamos los números por el caracter que los separa (tabulador)
    linea = line.split('\t')
    # el valor lo lee como carácter. Hay que pasarlo a número.
    lonP = float(linea[1])
    latP = float(linea[2])
    # suponiendo que los grados son en sexagesimales: hay que pasarlos a radianes
    lonP = radians(lonP)
    latP = radians(latP)
    x=(R*cos(latP)*sin(lonP-lonPT))/((sin(latPT)*sin(latP))+(cos(latPT)*cos(latP)*cos(lonP-lonPT)))
    y=(R*((sin(latP)*cos(latPT))-(cos(latP)*sin(latPT)*cos(lonP-lonPT))))/((sin(latPT)*sin(latP))+(cos(latPT)*cos(latP)*cos(lonP-lonPT)))
    fila = '[%s, %s, %s]\n' % (linea[0], x, y)
    nuevo.write(fila) 
nuevo.close()
file.close()
