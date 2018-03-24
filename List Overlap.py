# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 16:47:19 2018

@author: Jimmy
"""
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

import random

#genere une liste a
lst_a=[]
for i in range(0,random.randint(0,100)):
    lst_a.append(random.randint(-500,500))

#genere une liste b
lst_b=[]
for i in range(0,random.randint(0,100)):
    lst_b.append(random.randint(-500,500))

#retourne une valeur unique de chaque liste(la liste d peut etre vide)
c=[]
d=lst_a+lst_b
for i in range(min(d),max(d)):
    if i in d:
        c.append(i)
print(c)
