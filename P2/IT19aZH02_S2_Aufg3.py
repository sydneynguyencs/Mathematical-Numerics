# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:31:49 2020

@author: Team 02: Sydney Nguyen, Jari Rentsch
"""

import numpy as np
import matplotlib.pyplot as plt


# a) ab ~ n = 22 entfernen sich die Werte von 2pi
# Je grösser n ist, desto mehr nähert sich s_n 0 an.
# Folglich nähert sich s(n) 0 und es kommt zu einer Cancellation.

def s(n): 
    if(n==6):
        return 1
    n/=2
    return np.sqrt(2-2*np.sqrt(1-s(n)**2/4))


# b) n für grosse Zahlen immernoch bei 2pi
# keine Cancellation da GW von s_2 bei n gegen unendlich sich nicht 0 annähert.
def s2(n):
    if(n==6):
        return 1
    n/=2
    temp = s2(n)**2
    return np.sqrt(temp/(2*(1+np.sqrt(1-temp/4))))

n = 30
arr = []
arr2 = []
a = 6
i = 0
while(i<n):
    a*=2
    arr.append(a*s(a))
    arr2.append(a*s2(a))
    i+=1
    
plt.plot(arr)
plt.plot(arr2)
plt.grid()
plt.xlabel('n')
plt.ylabel('near 2*pi')
plt.legend(['a)','b)'])
plt.show()