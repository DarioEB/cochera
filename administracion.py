# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:36:03 2020

@author: Eduardo
"""
from cochera import Cochera

class Administracion:
    def __init__(self):
        self.cocheras = []

    def __str__(self):
        return 'Administración de cocheras'

    def registrarCochera(self, cochera):
        if isinstance(cochera, Cochera):
            self.cocheras.append(cochera)

    def desregistrarCochera(self, cochera):
        if isinstance(cochera, Cochera):
            if cochera in self.cocheras:
                if not cochera.tieneAlquileres():
                    self.cocheras.remove(cochera)

    # Clase Administracion
    def registrarAlquiler(self, cochera, cliente, movil):
        if cochera.estaHabilitada() and cochera.tieneLugar():
            if cochera.registrarAlquiler(cliente, movil):
                print('Alquiler registrado exitosamente!')

    def cantidadDeCocherasRegistradas(self):
        return len(self.cocheras)

    def registrarMovil(self, cochera, cliente, movil, darsena = None):
        if cochera.registrarMovil(cliente, movil, darsena):
            print('Móvil registrado exitosamente!')

    def desregistrarMovil(self, cochera, movil):
        if cochera.desregistrarMovil(movil):
            print('Móvil desregistrado exitosamente!')

    def desregistrarAlquiler(self, cochera, movil):
        if cochera.desregistrarAlquiler(movil):
            print('Alquiler desregistrado exitosamente!')

    def registrarPago(self, cliente, monto):
        cliente.registrarMovimiento(monto * -1)


