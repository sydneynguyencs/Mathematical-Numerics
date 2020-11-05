# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 18:58:55 2020

@author: Jari Rentsch, Sydney Nguyen
"""

import numpy as np

# Schwierigkeiten: x_n-1 storen (hier als xn_1 definiert), tol wird it 0.001 nicht eingehalten
    
def Nguyen_Sydney_S6_Aufg3(f, x0, x1, tol):
    xn_1 = x0
    xn = x1
    while(abs(f(xn))>10**(-tol)):
        fn = f(xn)
        fn_1 = f(xn_1)
        print(xn_1)
        temp = xn - (xn-xn_1)/(fn-fn_1) * fn
        xn_1 = xn
        xn = temp
    return xn


def f(xn):
    return np.exp(xn**2) + xn**(-3) - 10

Nguyen_Sydney_S6_Aufg3(f, -1.0, -1.2, 0.001)