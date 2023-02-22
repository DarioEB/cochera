# -*- coding: utf-8 -*-
"""
Created on Mon May 11 18:05:50 2020

@author: Eduardo
"""

from persona import Persona

class Empleado(Persona):
    def __init__(self, legajo, *args, **kwargs):
        Persona.__init__(self, *args, **kwargs)
        self.legajo = legajo

    def __str__(self):
        return self.apellido + ', ' + self.nombres + ' - ' + self.legajo