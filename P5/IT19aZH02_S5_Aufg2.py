# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 19:55:04 2020

@author: Sydney Nguyen
"""
import numpy as np

#Aufg 2: newton für kugel volumen
def aufg2(h,n):
    for i in range(n):
        f = 1/3 * np.pi * (15-h) * h**2 - 471
        f_deriv = 10 * np.pi * h - np.pi * h**2
        print(h)
        h = h - f/f_deriv
aufg2(9, 10)