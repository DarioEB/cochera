# -*- coding: utf-8 -*-
"""
Created on Sat May  2 20:27:07 2020

@author: Eduardo
"""
from alquiler import Alquiler

class Cochera:
    def __init__(self, descripcion, capacidad, precio, direccion = None):
        self.descripcion = descripcion
        self.direccion = direccion
        self.capacidad = capacidad
        self.precio = precio
        self.disponible = capacidad
        self.ocupado = 0
        self.habilitada = True
        self.alquileres = []

    def __eq__(self, otra):
        if isinstance(otra, Cochera):
            if otra.descripcion.lower() in self.descripcion.lower():
                return True
        return False

    def __str__(self):
        if self.direccion != None:
            return self.descripcion + ' - Tot.' + str(self.capacidad) + \
            ' - Dis.' + str(self.disponible) + ' - Ocu.' + str(self.ocupado) \
            + ' - ' + self.direccion
        else:
            return self.descripcion + ' - Tot.' + str(self.capacidad) + \
            ' - Dis.' + str(self.disponible) + ' - Ocu.' + str(self.ocupado)

    def tieneAlquileres(self):
        return len(self.alquileres) > 0

    def establecerDireccion(self, direccion):
        self.direccion = direccion

    def tieneLugar(self):
        return self.disponible > 0

    def registrarAlquiler(self, cliente, movil):
        if self.tieneMovilRegistrado(movil):
            print('El móvil ya está registrado')
            return False
        darsena = self.siguienteDarsenaDisponible()
        return self.nuevoAlquiler(Alquiler(self, cliente, movil, darsena))

    def tieneMovilRegistrado(self, movil):
        for alquiler in self.alquileres:
            if alquiler.tieneMovilRegistrado(movil):
                return True
        return False

    def siguienteDarsenaDisponible(self):
        darsenasTotales = []
        darsenasOcupadas = []
        darsenasDisponibles = []
        for i in range(self.capacidad):
            darsenasTotales.append(i+1)
        for alquiler in self.alquileres:
            if alquiler.estaVigente():
                darsenasOcupadas.append(alquiler.darsena)
        darsenasOcupadas.sort()
        darsenasDisponibles = [x for x in darsenasTotales if x not in darsenasOcupadas]
        return darsenasDisponibles[0]

    def nuevoAlquiler(self, alquiler):
        alquiler.cliente.registrarMovimiento(self.precio)
        self.alquileres.append(alquiler)
        self.decrementaDisponibles()
        self.incrementaOcupados()
        return True

    def incrementaDisponibles(self):
        self.disponible += 1

    def decrementaDisponibles(self):
        self.disponible -= 1

    def incrementaOcupados(self):
        self.ocupado += 1

    def decrementaOcupados(self):
        self.ocupado -= 1

    def inhabilitar(self):
        self.habilitada = False

    def habilitar(self):
        self.habilitada = True

    def estaHabilitada(self):
        return self.habilitada

    def registrarMovil(self, cliente, movil, darsena):
        alquileres = self.alquileresRegistrados(cliente)
        if len(alquileres) == 0:
            print('El cliente no posee alquileres registrados en la cochera')
        elif len(alquileres) == 1:
            alquileres[0].registrarMovil(movil)
            return True
        else:
            if darsena == None:
                darsenas = []
                for alquiler in alquileres:
                    darsenas.append(alquiler.darsena)
                darsena = int(input('El cliente usa las dársenas ' + str(darsenas) + \
                                    '. Elija una para registrar el móvil: '))
            for alquiler in alquileres:
                if alquiler.darsena == darsena:
                    alquiler.registrarMovil(movil)
                    return True
        return False

    def alquileresRegistrados(self, cliente):
        alquileres = []
        for alquiler in self.alquileres:
            if alquiler.tieneClienteRegistrado(cliente):
                alquileres.append(alquiler)
        return alquileres

    def desregistrarMovil(self, movil):
        alquiler = self.alquilerDelMovil(movil)
        if isinstance(alquiler, Alquiler):
            alquiler.desregistrarMovil(movil)
            if not alquiler.tieneMoviles():
                alquiler.finalizar()
                self.incrementaDisponibles()
                self.decrementaOcupados()
                return True
        return False

    def alquilerDelMovil(self, movil):
        for alquiler in self.alquileres:
            if alquiler.tieneMovilRegistrado(movil):
                return alquiler
        return None

    def desregistrarAlquiler(self, movil):
        alquiler = self.alquilerDelMovil(movil)
        if isinstance(alquiler, Alquiler):
            alquiler.finalizar()
            self.incrementaDisponibles()
            self.decrementaOcupados()
            return True


