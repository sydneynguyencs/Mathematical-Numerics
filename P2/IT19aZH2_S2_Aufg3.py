# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:31:49 2020

@author: Team 02: Sydney Nguyen, Jari Rentsch
"""

import numpy as np
import matplotlib.pyplot as plt

def s(n):
    if(n==6):
        return 1
    n /= 2    
    return np.sqrt(2-2*np.sqrt(1-s(n)**2/4))

n = 50
a = 6
arr = []
for i in range(1, n):  
    arr.append(a*s(a))
    a*=2 
plt.plot(arr)
plt.grid()
plt.xlabel('n')
plt.ylabel('2n*s(2n) near 2*pi')
plt.show()


def s2(n):
    if(n==6):
        return 1
    n /= 2
    temp = s2(n)**2
    return np.sqrt(temp/(2*(1+np.sqrt(1-temp/4))))

n = 600
a = 6
arr = []
for i in range(1, n):  
    arr.append(a*s2(a))
    a*=2
   
plt.plot(arr)
plt.grid()
plt.xlabel('n')
plt.ylabel('2n*s2(2n) near 2pi')

#je mehr rekursionen man ausführt desto kleiner wird s(n)
#wenn s(n) nahe bei 0 ist gibt es cancelation da 2 minus 
#eine zahl nahe bei 2 gerechnet wird. Dadurch erhöht sich 
#der relative Fehler enorm. Irgendwann kann float die zu 
#kleinen s(n) nicht mehr darstellen und macht s(n) einfach gleich 0

