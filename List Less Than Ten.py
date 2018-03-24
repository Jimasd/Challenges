# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 15:52:31 2018

@author: Jimmy
"""

#creer une liste qui retourne les nombres en bas de x
nb=int(input("En bas de quel nombre?:"))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in range(0,len(a)):
    if a[i]<nb:
        b.append(a[i])
print(b)