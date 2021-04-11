#!/usr/bin/python3
#-*- coding: utf-8 -*-

tupla = (1, 2, 3)
print (tupla)
print(type(tupla))


myTuple = tuple((1,2,3))
print(type(myTuple))
print(dir(tuple))


#Obtener los elementos de una tupla
months = ("","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
mes10 = months[10]
print (mes10)

#Eliminar una tupla
del(months)
print(months)

#modos comunes de utilizar tuples
#cuando se requiere almacenarconjuntos de valores que no varian o se mantienen constantes
#ejemplo: coordenadas

locations = {
    "Bogota": (4.7190918499671515, -74.03456510556657),
    "Sogamoso": (5.740867133827568, -72.91752137739779),
    "Tunja": (5.546469037874712, -73.35280858671634)
}