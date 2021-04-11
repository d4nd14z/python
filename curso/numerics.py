#!/usr/bin/python3
#-*- coding: utf-8 -*-

num1 = 10
num2 = 3.5

print(type(num1))
print(type(num2))

#Operaciones con numericos
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2 
division = num1 / num2
divisionEntera = num1 // num2
residuo = num1 % num2
potencia = num1 ** num2

print("Suma: " + str(suma))
print(type(suma))
print("Resta: " + str(resta))
print(type(resta))
print("Multiplicacion: " + str(multiplicacion))
print(type(multiplicacion))
print("Division: " + str(division))
print(type(division))
print("DivisionEntera: " + str(divisionEntera))
print(type(divisionEntera))
print("Residuo: " + str(residuo))
print(type(residuo))
print("Potenciacion: " + str(potencia))
print(type(potencia))

#Obtener datos desde la consola del usuario
#Inserte la edad del usuario

#Limpiar la consola en Python
import os
os.system("clear")

age = input("Edad: ")
newage = int(age) + 5
tofloat = newage / 3.1416  #float(newage)
print("Edad: " + age)
print("Nueva edad: " + str(newage))
print("A flotante: " + str(tofloat))
