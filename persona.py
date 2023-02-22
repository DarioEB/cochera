# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:52:39 2020

@author: Eduardo
"""
from cliente import Cliente

class Persona(Cliente):
    def __init__(self, nombres, apellido, documento = None):
        Cliente.__init__(self, 'Persona')
        self.nombres = nombres
        self.apellido = apellido
        self.documento = documento
