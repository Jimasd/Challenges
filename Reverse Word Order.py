# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 17:39:30 2018

@author: Jimmy
"""
b=""
phrase=input("Écrire une phrase:")

for i in range(0,len(phrase)):
    b=b+phrase[len(phrase)-i-1]
print(b)
    
    
    
    
def fonction(poop,*vartuple):
    print(poop)
    for var in vartuple:
        print(var)
fonction(10,10,2345,2345,2345,4)
fonction("a","b")
    
x="a b c"
x.split(,)
print(x)
def reverse_v1(x):
  y = x.split()
  result = []
  for word in y:
    result.insert(0,word)
  return " ".join(result)

# method 2
def reverse_v2(x):
  y = x.split()
  return " ".join(y[::-1])
reverse_v2("caca pipi")
# method 3
def reverse_v3(x):
  y = x.split()
  return " ".join(reversed(y))

# method 4
def reverse_v4(x):
  y = x.split()
  y.reverse()
  return " ".join(y)

# test code
test1 = raw_input("Enter a sentence: ")
print reverse_v1(test1)
print reverse_v2(test1)
print reverse_v3(test1)
print reverse_v4(test1)

def reverso(x):
    y=x.split()
    return " ".join(reversed(y))
reverso("hihi haha")