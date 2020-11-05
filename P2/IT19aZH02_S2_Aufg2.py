# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:28:37 2020

@author: Team 02: Sydney Nguyen, Jari Rentsch
"""

import numpy as np
import matplotlib.pyplot as plt

# a) f1 ist ungenauer als f2, da f1 mehr Operationen beinhaltet, 
# wobei mehr Rundungsfehler entstehen.
x = np.arange(1.99, 2.01, 0.02/501)
a = [-128,448,-672,560,-280,84,-14,1]
b =[0,0,0,0,0,0,0,7]

def polynom(x, array):
    p = 0
    degree = len(array)
    for i in range(degree):
        p += array[i]*x**i
    return p

f1 = polynom(x,a)
f2 = polynom((x-2),b)

plt.plot(x,f1)
plt.plot(x,f2)
plt.grid()
plt.title('Polynomial:')
plt.legend(['f1', 'f2'])
plt.show()


# b) Nein. 
# Cancellation wenn x nahe 0, da im Nenner ähnlich grosse Zahlen voneinander
# subtrahiert werden -> relativer Fehler maximiert
x = np.arange(-10**(-14), 10**(-14), 10**(-17))
g = x/(np.sin(1+x)-np.sin(1))
plt.plot(x,g)
plt.grid()
plt.title('Polynomial:')
plt.legend('g')


# c) Grenzwert ist eindeutig. Weil es keine Cancellation gibt.
# hier tritt der Fall wie bei b) nicht ein.
# GW ist 1.8508 (durch de l'hopital berechnet)

g2 = x/(2*np.cos((1+x+1)/2)*np.sin(x/2))
plt.plot(x,g2)
plt.legend(['g', 'g2'])