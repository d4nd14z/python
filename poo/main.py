#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
from funciones.usuario import Usuario
import utilities

if __name__ == '__main__':
    os.system("clear")
    daniel = Usuario("Daniel Mauricio", "Diaz Forero", "Calle 7B # 14 - 19", "newdmdiazf@gmail.com", "d4nd14z", "123456siete")
    ingrid = Usuario("Ingrid Tatiana", "Gomez Gamboa", "Calle 7B # 14 - 19", "intagoga@gmail.com", "intagoga", "abcundostres")
    godzilla = Usuario("Godzilla Steven", "Diaz Gomez", "Calle 7B # 14 - 19", "godzillathedog@gmail.com", "godzilla", "godzillathedog")
    usuarios = [daniel, ingrid, godzilla]
    for user in usuarios:
        if utilities.validateUser(user) == True:
            print(user.getNombres() + " " + user.getApellidos() + "\tAuth(OK)")
            print("===========================\t========")
        utilities.mostrarUsuario(user)
        
    




