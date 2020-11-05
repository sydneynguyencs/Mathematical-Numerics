# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:43:16 2020

@author: Sydney Nguyen
"""

import numpy as np  

def aufg1Newton(x0, n):
    xn = x0
    for i in range(n): 
        f = np.exp(xn**2) + xn**(-3) - 10
        f_deriv = 2*np.exp(xn**2)*xn-3/xn**4  
        print(xn)
        xn = xn - f/f_deriv
#aufg1Newton(2, 5)    
    
def aufg1NewtonVereinfacht(x0, n):
    xn = x0
    f_deriv = 2*np.exp(xn**2)*xn-3/xn**4 
    for i in range(n): 
        f = np.exp(xn**2) + xn**(-3) - 10
        print(xn)
        xn = xn - f/f_deriv
#aufg1NewtonVereinfacht(0.5, 5)  
 
def aufg1Sekanten(x0, x1, n):
    xn_1 = x0
    xn = x1
    for i in range(n): 
        fn = np.exp(xn**2) + xn**(-3) - 10
        fn_1 = np.exp(xn_1**2) + xn_1**(-3) - 10
        print(xn_1)
        temp = xn - (xn-xn_1)/(fn-fn_1) * fn
        xn_1 = xn
        xn = temp
#aufg1Sekanten(-1.0,-1.2,10)
    
