#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
os.system("clear")

myList = [1,2,3,4,5,6,7,8,9,10]
#Iterar sobre la lista usando el bucle for
print("Iterar sobre la lista utilizando el bucle for")
for i in myList:
    print(i)
print("\n")
print("Iterar sobre la lista utilizando el bucle for loop y range")
for i in range(0, len(myList)):
    print(myList[i])  
print("\n")
print("Iterar sobre la lista utilizando while y loop")
index = 0
while (index < len(myList)):
    print(myList[index])
    index += 1  
print("\n")
print("Iterar sobre la lista utilizando comprension de listas (list comprehension)")
print("!!! Esta es la forma mas optima !!!")
[ print(i) for i in myList ]  #Imprimir el contenido de la lista por comprehension list
print("\n")
print("Iterar sobre la lista utilizando enumerate") #Imprime indice y valor
for i, val in enumerate(myList):
    print (i, " =>", val)
print("Imprimir la lista utilizando numpy")
print("\n")
import numpy as np
a = np.arange(9) #crear un array utilizando el metodo arange
a = a.reshape(3, 3) #Dar forma al array en tres filas y tres columnas
for x in np.nditer(a):
    print(x)

#Se configura el entorno virtual de python en Visual Studio Code con el comando
# Ctrl + Shift + P ... y se selecciona Python: Select Interpreter / Enter interpreter path / y se selecciona el entorno virtual de python 

#CRear listas a partir de una tupla, usando el constructor de las listas
lista = list(range(1, 1000)) #llenar la lista con valores del 1 al 1000
print(lista)


#Buscar un elemento dentro de una lista
found = (7777 in lista)
print("7777 esta en la lista?: " + str(found))

#Operaciones con listas
longitud = len(lista)
print("Longitud de la lista: " + str(longitud)) #Obtiene la longitud de la lista

colors = ["Red","Green","Blue"]
colors.append("Violet") #Agregar un elemento nuevo a la lista
colors.extend(("Yellow","Orange","Gray")) #Agregar varios elementos nuevo a la lista usando tuplas
print(colors)

colors.insert(1, 'Violet')
print(colors)

colors.pop() #Eliminar el ultimo elemento de una lista
print(colors) 

colors.pop(1) #Eliminar el elemento en la posicion 1 de la lista
print(colors) 

colors.remove("Violet") #Eliminar el elemento "violet" de la lista
print(colors)

colors.sort() #Ordenar los elementos de la lista
print(colors)

colors.sort(reverse=True) #Ordenar los elementos de la lista del ultimo al primero 
print(colors)

print ("Posicion: " + str(colors.index("Orange"))) #Obtiene el indice de la posicion en la que se encuentra el elemento "Orange"
                                                   #Las posiciones inician desde cero. (0)
