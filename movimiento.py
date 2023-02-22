# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:47:17 2020

@author: Eduardo
"""
import datetime

class Movimiento:
    def __init__(self, monto):
        self.fechaHora = datetime.datetime.now()
        self.monto = monto
