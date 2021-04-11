#!/usr/bin/python3
#-*- coding: utf-8 -*-

#Tipos de datos String (Cadenas de Texto)
string1 = "Hello world"
string2 = 'Hello World'
string3 = '''Hello World'''
string4 = """Hello World"""
print(string1)
print(string2)
print(string3)
print(string4)
#Funcion type: devuelve el tipo de dato de una variable
print(type(string1))
print(type(string2))
print(type(string3))
print(type(string4))

#Concatenar strings en python (unir string)
print ("Bye" + " " + "World")

#Tipos de datos numericos (Numeros)
numero1 = 1
numero2 = 2
numero3 = 3
numero4 = 4
print(numero1)
print(numero2)
print(numero3)
print(numero4)
print(type(numero1))
print(type(numero2))
print(type(numero3))
print(type(numero4))
print(numero1 + numero2 + numero3 + numero4)

#Tipos de datos flotantes (numeros con decimales)
float1 = 3.1416
float2 = 2.7320
float3 = 1.0001
float4 = 2.5
print(float1)
print(float2)
print(float3)
print(float4)
print(type(float1))
print(type(float2))
print(type(float3))
print(type(float4))


#Tipos de datos booleanos (Tipo de dato Logico)
boolean1 = True
boolean2 = False
print(boolean1)
print(boolean2)
print(type(boolean1))
print(type(boolean2))
#Operaciones con Booleanos
oper1 = not boolean1
oper2 = not boolean2
oper3 = boolean1 and boolean2
oper4 = boolean1 or boolean2
print(oper1)
print(oper2)
print(oper3)
print(oper4)
print(type(oper1))
print(type(oper2))
print(type(oper3))
print(type(oper4))

#Tipos de datos compuestos
#Listas: Grupos de elementos (no necesariamente del mismo tipo)
#El tipo de datos lista es mutable (puede cambiar con el tiempo)
#El caracter normal de las listas es las llaves rectas[]
#Se pueden incluir listas dentro de otras listas
lista1 = [10,20,30,40,50]
print(lista1)
print(type(lista1))
lista2 = ["Cadena 1","Cadena 2","Cadena 3","Cadena 4","Cadena 5"]
print(lista2)
print(type(lista2))
#No necesariamente los elementos de una lista deben ser del mismo tipo
lista3 = ["Cadena 1", 10, 2.5, True, [1,2,3,4,5]]
print(lista3)
print(type(lista3))

#Tipos de datos compuestos
#Tuplas: Grupos de elementos (no necesariamente del mismo tipo)
#El tipo de datos tupla es inmutable (INMUTABLE) (No puede cambiar con el tiempo, siempre deben ser los mismos elementos)
#El caracter normal de las listas es los parentesis ()
#Se pueden incluir tuplas dentro de otras tuplas
tupla1 = (10, 20, 30, 40, 50)
print(tupla1)
print(type(tupla1))
tupla2 = ("a","b","c","d","e")
print(tupla2)
print(type(tupla2))
#No necesariamente los elementos de una tupla deben ser del mismo tipo
tupla3 = ("Cadena 1", 10, 2.5, True, [1,2,3,4,5], ("1","2","3","4","5"))
print(tupla3)
print(type(tupla3))

#Tipos de datos compuestos
#Diccionarios: Grupos de elementos (no necesariamente del mismo tipo).
#Agrupa conjuntos de elementos pares de clave -> valor
#El tipo de datos diccionario es mutable (puede cambiar con el tiempo)
#Se pueden incluir diccionarios dentro de otros diccionarios
diccionario1 = {
    "nombres": "Nombres",
    "apellidos": "Apellidos",
    "nickname": "NickName"
}
print(diccionario1)
print(type(diccionario1))

diccionario2 = {
    "nombres": "Nombres",
    "apellidos": "Apellidos",
    "nickname": "NickName",
    "lista": [10, 20, 30, 40, 50],
    "tupla": (10, 20, 30, 40, 50),
    "dict": {10, 20, 30, 40, 50}   
}
print(diccionario2)
print(type(diccionario2))

diccionario3 = {
    "nombres": "Nombres",
    "apellidos": "Apellidos",
    "nickname": "NickName",
    "data": {
        "nota1": 3.2,
        "nota2": 4.5,
        "nota3": 3.7        
    }
}
print(diccionario3)
print(type(diccionario3))

#Tipos de datos Nulos (Null)
#Se utiliza la palabra clave None
#Utilizar None y conservar minusculas y mayusculas
data = None
print(data)
print(type(data))