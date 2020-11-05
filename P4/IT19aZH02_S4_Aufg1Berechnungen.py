# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 09:26:21 2020

@author: Sydney Nguyen
"""

#Aufgabe 1 (nur Notizen bzw Berechnungen)
# a)
x1 = -1
x2 = 0
x3 = 1
x4 = 0.5

def fixpunktiteration(x, n):
    for i in range(n):
        #print(i)
        print(x)
        x = (230*x**4+18*x**3+9*x**2-9)/221
          
fixpunktiteration(0.5, 2)

# b)
f_array = [-9,-221,9,18,230]
F_array = [-9/221,0,9/221,18/221,230/221]

def deriv(x, array):
    degree = len(array)
    y = 0
    for i in range(degree):
        y += array[i]*i*x**(i-1)
    return y
a = deriv(0.5,F_array)
print(a)

# c) Lösung: ab n = 45
x0 = 0.04468325791855204
x1 = 0.5
n = 45
for i in range(n):
    apriori = a**i/(1-a) * (x1-x0)
    #print(i)
    print(apriori)
