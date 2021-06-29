# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 01:12:55 2021

@author: maril
"""

class Empleado:
    secuencia=0
    def __init__(self,nom, ced, sue, cargo):
        self.codigo= self.generarCodigo()
        self.nombre=nom
        self.cedula=ced
        self.sueldo=sue
        self.cargo=cargo

    def mostrar(self):
        print("Codigo: {} nombre:{} cargo:{}-{}" .format(self.codigo, self.nombre, self.cargo.codCarg, self.cargo.descripCarg))

    def generarCodigo(self):
        Empleado.secuencia+=1
        return Empleado.secuencia

cargo1= cargo("Docente")
emp1= Empleado("Daniel", "0914", 500, cargo1)
emp1.mostrar()
cargo2= cargo("Programadora")
emp2= Empleado("María", "0915", 500, cargo2)
emp2.mostrar()
