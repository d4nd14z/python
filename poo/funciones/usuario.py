#!/usr/bin/python3
#-*- coding: utf-8 -*-

import hashlib
import utilities

class Usuario:
    
    nombres = ""
    apellidos = ""
    direccion = ""
    email = ""
    login = ""
    password = ""

    #Metodo Constructor
    def __init__(self, nombres, apellidos, direccion, email, login, password):
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion = direccion
        self.email = email
        self.login = login
        self.password = utilities.encryptPassword(password)
        
    def getNombres(self):
        return self.nombres

    def getApellidos(self):
        return self.apellidos

    def getDireccion(self):
        return self.direccion

    def getEmail(self):
        return self.email

    def getLogin(self):
        return self.login

    def getPassword(self):
        return self.password
