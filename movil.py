# -*- coding: utf-8 -*-
"""
Created on Sat May 16 21:19:14 2020

@author: Eduardo
"""

class Movil:
    def __init__(self, marca, modelo, color, patente, tipo = 'Sedan'):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.patente = patente
        self.tipo = tipo

    # Movil
    def __eq__(self, otro):
        return isinstance(otro, Movil) and self.patente.lower() == otro.patente.lower()

    def __str__(self):
        return self.marca + ' ' + self.modelo + ' ' + self.color + ' ' + self.patente
