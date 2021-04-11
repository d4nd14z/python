#!/usr/bin/python3
#-*- coding: utf-8 -*-

myStr = "Hello, world !!!"
#print(dir(myStr))   #Muestra todas las funciones disponibles para un tipo de dato particular
print(myStr.upper()) #Convierte todo el texto de la cadena de caracteres a mayusculas
print(myStr.lower()) #Convierte todo el texto de la cadena de caracteres a minusculas
print(myStr.swapcase()) #Reemplaza las minusculas por mayusculas y las mayusculas por minusculas
print(myStr.capitalize()) #Convierte la primera letra a mayuscula
print(myStr.replace("Hello","Bye")) #Reemplaza la subcadena Hello, por la subcadena bye 
print(myStr.replace("Hello","Bye").lower()) #Se pueden encadenar los metodos para genera el resultado de la funcion
print(myStr.count("l")) #Cuenta cuantas veces aparece el caracter "l" dentro de la cadena de texto
print(myStr.startswith("hola")) #Indica si la cadena inicia con los caracteres "hola" retorna True o False
print(myStr.endswith("!!")) #Indica si la cadena termina con los caracteres "!!"retorna True o False
print(myStr.split(",")) #Divide la cadena con base en el caracter coma (,). Similar a explode(PHP)
print(myStr.find("o")) #Devuelve la posicion de la cadena donde se encuentra la primera aparicion del caracter "o". Inicia en cero(0)
print(len(myStr)) #Retorna la longitud de la cadena. (longitud de caracteres que contiene la cadena)
print(myStr.index(",")) #Imprime el indice de la cadena donde esta el caracter coma (,). Similar a find
print(myStr.isnumeric()) #Muestra si la cadena de caracteres representa a un numero con caracteres numericos
print(myStr.isalpha()) #Muestra si la cadena de caracteres representa a una cadena con caracteres alfanumericos
print(myStr[5]) #Imprime el caracter que se encuentra en la posicion 5 de la cadena de texto
print(myStr[-1]) #Imprime el primer caracter de la caden, contando desde la derecha hacia la izquierda
print("Cadena 1" + " " + "Cadena 2") #Imprime y concatena dentro de una unica instruccion print

print(f"My Name is: {myStr}") #Format: indica que el valor dentro de las llaves debe ser reemplazada por el valor de la variable