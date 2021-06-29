# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 01:05:38 2021

@author: maril
"""

class Cargo:
    secuencia=0
    def __init__(self, des="Sin cargo"):
        Cargo.secuencia+=1
        self.codCarg= Cargo.secuencia
        self.descripCarg= des

if __name__ == '__main__':
    cargo1= Cargo()
    print(cargo1.codCarg, cargo1.descripCarg)
    cargo2= Cargo()
    cargo2.descripCarg= "Director"
    print(cargo2.codCarg, cargo2.descripCarg)
    cargo3= Cargo("Analista")
    print(cargo3.codCarg, cargo3.descripCarg)
    # print(Cargo.secuencia)
    # print(cargo1.secuencia)
    # print(cargo2.secuencia)
    # print(cargo3.secuencia)
