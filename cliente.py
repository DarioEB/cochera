# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:52:24 2020

@author: Eduardo
"""
import datetime

class Cliente:
    idCliente = 0
    def __init__(self, tipo):
        Cliente.idCliente += 1
        self.id = Cliente.idCliente
        self.inicio = datetime.datetime.today()
        self.tipo = tipo
        self.movimientos = []

    # Clase Cliente
    def __str__(self):
        if self.tipo == 'Persona':
            return self.apellido + ', ' + self.nombres
        elif self.tipo == 'Empresa':
            return self.nombre

    # Clase Cliente
    def __eq__(self, otro):
        return self.id == otro.id

    def registrarMovimiento(self, monto):
        self.movimientos.append(monto)

    def saldo(self):
        return sum(self.movimientos)