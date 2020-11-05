# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:12:06 2020

@author: Sydney Nguyen
"""

def IT19aZH02_S6_Aufg2(A,b):    
    A_triangle = []
    detA=0
    x=0
    n = len(A)
    for i in range(n):
        detA+=A[i][i]
        if A[i][i]==0:
            for j in range(n):
                if A[j][i]!=0:
                    temp = zi
                    zi = zj
                    zj = temp
            
                
    return[A_triangle, detA, x]
    
def det(A):
    n = len(A)
    for i in range(n):
        