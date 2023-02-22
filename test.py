# -*- coding: utf-8 -*-
"""
Created on Thu May 21 07:56:22 2020

@author: Eduardo
"""

from movil import Movil
from persona import Persona
from empresa import Empresa


from administracion import Administracion
from cochera import Cochera

admin = Administracion()
cocheraCentro = Cochera('Centro', 15, 2250)

cocheraKrause = Cochera('Krause', 12, 1750)
cocheraAtletico = Cochera('Atletico', 10, 1900)

#print(cocheraAtletico)
cocheraAtletico.establecerDireccion('España 854')
#print(cocheraAtletico)
cocheraAtletico.establecerDireccion('España 1854')
#print(cocheraAtletico)



#print()
admin.registrarCochera(cocheraCentro)
admin.registrarCochera(cocheraKrause)
admin.registrarCochera(cocheraAtletico)

# Móviles
citC3EBla = Movil('Citroën', 'C3 Exclusive', 'Blanco', 'UOE 322')
citC3EBla1 = Movil('Citroën', 'C3 Exclusive', 'Blanco', 'UOE 322')
fiaPalRoj = Movil('Fiat', 'Palio', 'Rojo', 'WXX 230')
toyEtiBla = Movil('Toyota', 'Etios', 'Blanco', 'AB 234 ST')
volGolVer = Movil('Volkswagen', 'Gol', 'Verde', 'ESX 344')
#print(citC3EBla)

# Clientes
facTur = Persona('Facundo', 'Turing', 17898774)
micEmp = Empresa('Micro')
#print(facTur)
#print(micEmp)

admin.registrarAlquiler(cocheraCentro, micEmp, citC3EBla)
#print(cocheraCentro)
admin.registrarAlquiler(cocheraCentro, micEmp, fiaPalRoj)
#print(cocheraCentro)
admin.registrarAlquiler(cocheraCentro, micEmp, toyEtiBla)

admin.registrarAlquiler(cocheraCentro, micEmp, volGolVer)
#print(cocheraCentro)
#admin.registrarMovil(cocheraCentro, micEmp, toyEtiBla))

#admin.desregistrarMovil(cocheraCentro, toyEtiBla)

#print(cocheraCentro)

#admin.desregistrarMovil(cocheraCentro, citC3EBla)

#print(cocheraCentro)
#admin.desregistrarAlquiler(cocheraCentro, citC3EBla)
#print(cocheraCentro)
#admin.desregistrarAlquiler(cocheraCentro, fiaPalRoj)
#print(cocheraCentro)
#admin.desregistrarAlquiler(cocheraCentro, toyEtiBla)
#print(cocheraCentro)

admin.registrarPago(micEmp, 650)

print(micEmp.saldo())








