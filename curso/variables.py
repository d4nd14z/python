#!/usr/bin/python3
#-*- coding: utf-8 -*-

#Las variables en python son case sensitive
#Sensibles a mayusculas
book = "Libro"
Book = "Libro"
#book y Book son dos variables distintas

#Se puede hacer la declaracion y la inicializacion de varias variables en una sola linea
book, Book, valor1 = "Libro1", "Libro2", 3.1416
print(book)
print(Book)
print(valor1)

#Convenciones para la declaracion de variables
book_name = "I Robot"           #Snake  Case
bookName = "Digital Fortress"   #Camel  Case
BookName = "The Net"            #Pascal Case

#Convenciones para la declaracion de constantes
PI = 3.14165294 #Las constantes se escriben siempre en mayusculas

#Python es un lenguaje dinamico. se puede cambiar el tipo de dato
book_name = "I Robot"
book_name = 123456
book_name = []