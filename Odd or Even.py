# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:34:20 2018

@author: Jimmy
"""
#Voir si il est un multiple de 4 et s'il est pair
while True:
    num=int(input("Quel nombre?:"))
    if num%4==0:
        print(num, "est un multiple de 4")
    elif num%2==0:
        print("Le nombre", num, "est pair")
    else:
        print(num, "est impair")