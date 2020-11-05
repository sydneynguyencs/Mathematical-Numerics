# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:49:58 2020

@author: Team 02: Sydney Nguyen, Jari Rentsch
"""

def IT19aZH02_S1_Aufg2(a,xmin,xmax):
    import numpy as np

    p = []
    dp = []
    dpint = []
    x = np.arange(xmin,xmax,0.1)
    
    if not isinstance(a, (list, np.ndarray)) or len(a) == 0 or len(np.shape(a)) > 1:
        raise Exception('Fehler')
        
    degree = len(a)
    
    for i in range(degree):
        p.append(a[i]*x**i)
        dp.append(a[i]*i*x**(i-1))
        dpint.append(a[i]/(i+1)*x**(i+1))
        
    return(x,p,dp,dpint)
