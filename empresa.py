# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:51:20 2020

@author: Eduardo
"""
from cliente import Cliente

class Empresa(Cliente):
    def __init__(self, nombre):
        Cliente.__init__(self, 'Empresa')
        self.nombre = nombre
