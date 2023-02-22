# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:56:56 2020

@author: Eduardo
"""
import datetime

class Alquiler:
    idAlquiler = 0
    def __init__(self, cochera, cliente, movil, darsena):
        Alquiler.idAlquiler += 1
        self.id = Alquiler.idAlquiler
        self.darsena = darsena
        self.cliente = cliente
        self.moviles = [movil]
        self.autorizados = []
        self.inicio = datetime.datetime.today()
        self.fin = None

    def __str__(self):
        return str(self.id) + '-' + str(self.darsena) + '-' + str(self.inicio)

    def estaVigente(self):
        if self.fin == None:
            return True
        return False

    def tieneMovilRegistrado(self, movil):
        return movil in self.moviles

    def tieneClienteRegistrado(self, cliente):
        return cliente == self.cliente

    def registrarMovil(self, movil):
        self.moviles.append(movil)

    def desregistrarMovil(self, movil):
        self.moviles.remove(movil)

    def registrarCliente(self):
        self.cliente.alquileres(self)

    def tieneMoviles(self):
         return len(self.moviles) > 0

    def finalizar(self):
        self.fin = datetime.datetime.today()


        