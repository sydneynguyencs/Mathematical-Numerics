# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:04:24 2020

@author: Team 02: Sydney Nguyen, Jari Rentsch
"""
import matplotlib.pyplot as plt

from IT19aZH02_S1_Aufg2 import IT19aZH02_S1_Aufg2

#[x,p,dp,dpint] = IT19aZH02_S1_Aufg2([2,1,3],-10,10)
[x,p,dp,dpint] = IT19aZH02_S1_Aufg2([-105, 29, 110, -30, -5, 1],-10,10)


def listToFunc(array):
    y = 0;
    degree = len(array)
    for i in range(degree):
        y += array[i]
    return y

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title('polynom')
plt.legend(['polynom', 'derivation', 'integration'])
plt.xlim(-7.5,9)
plt.ylim(-2700,1700)
plt.plot(x, listToFunc(p))
plt.plot(x, listToFunc(dp))
plt.plot(x, listToFunc(dpint))
plt.grid()
