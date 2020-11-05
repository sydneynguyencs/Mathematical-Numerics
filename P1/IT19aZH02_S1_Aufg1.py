# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:32:32 2020

@author: Team 02: Sydney Nguyen, Jari Rentsch
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10,10,0.1)

coeffs = [-105, 29, 110, -30, -5, 1]

def polynom(x, coeffs):
    degree = len(coeffs)
    y = 0
    for i in range(degree):
        y += coeffs[i]*x**i
    return y

def deriv(x, coeffs):
    degree = len(coeffs)
    y = 0
    for i in range(degree):
        y += coeffs[i]*i*x**(i-1)
    return y

def integ(x, coeffs):
    degree = len(coeffs)
    y = 0
    for i in range(degree):
        y += coeffs[i]/(i+1)*x**(i+1)
    return y

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title('polynom')
plt.legend(['polynom', 'derivation', 'integration'])
plt.xlim(-7.5,9)
plt.ylim(-2700,1700)
plt.plot(x, polynom(x, coeffs))
plt.plot(x, deriv(x, coeffs))
plt.plot(x, integ(x, coeffs))
plt.grid()

