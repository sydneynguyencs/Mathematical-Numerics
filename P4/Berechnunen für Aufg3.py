# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:33:54 2020

@author: Sydney Nguyen
"""
import numpy as np

def fixpunktiteration(k,n):
    for i in range(n):
        #print(i)
        print(k)
        k = np.sin(k) + 0.5 * np.pi
        
fixpunktiteration(135,50)