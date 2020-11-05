# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:04:24 2020

@author: Sydney Nguyen
"""
import matplotlib.pyplot as plt
import numpy as np
import Gruppe_S2_Aufg2 as g

a = [1,2,3,4,5]
x = np.arange(-10, 10, 0.1)

def listToFunc(array):
    y = 0;
    degree = len(a)
    for i in len(a):
        y += array[i]
    return y

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title('polynom')
plt.legend(['polynom', 'derivation', 'integration'])

plt.plot(x, listToFunc(g.polynom(x,a)))
plt.plot(x, listToFunc(g.f(x,a)))
plt.plot(x, listToFunc(g.F(x,a)))
plt.grid()
