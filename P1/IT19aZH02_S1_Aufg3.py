# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:21:17 2020

@author: Team 02: Sydney Nguyen, Jari Rentsch
"""
import numpy as np
import timeit

def fact_rec(n):
    # y = fact_rec(n) berechnet die Fakultät von n als 
    # fact_rec(n) = n * fact_rec(n -1) 
    # mit fact_rec(0) = 1 # Fehler, falls n < 0 oder nicht ganzzahlig 
    import numpy as np 
    if n < 0 or np.trunc(n) != n: 
        raise Exception('The factorial is defined only for positive integers')
    if n <=1: 
        return 1
    else: 
        return n*fact_rec(n-1)
    
def fact_for(n):
    if n < 0 or np.trunc(n) != n: 
        raise Exception('The factorial is defined only for positive integers')
    y = 1
    for i in range(n):
        y *= i+1
    return y
    
t1=timeit.repeat("fact_rec(500) ", "from __main__ import fact_rec", number=100, repeat = 100)    
t2=timeit.repeat("fact_for(500) ", "from __main__ import fact_for", number=100, repeat = 100)

acc1=0
for i in range(len(t1)):
    acc1 += t1[i]
acc1/=len(t1)

acc2=0
for i in range(len(t2)):
    acc2 += t2[i]
acc2/=len(t2)

print("Time fact_rec: ",acc1)
print("Time fact_for: ",acc2)
# fact_for ist schneller, da bei fact_rec immer wieder eine 
# neue funktion aufgerufen wird und pointer gesetzt werden müssen

for i in range(190,201):    
    temp = fact_for(i)
    print(" factorial(",i,"n) displayed with the type ",type(temp)," is ",temp)
for i in range(170,172):    
    temp= fact_for(i)+0.0
    print(" factorial(",i,"n) displayed with the type ",type(temp)," is ",temp)
# wie man sieht kann das programm fact(200) problemlos darstellen, aber bereits   
# bei fact(171) kann man die zahl nicht mehr als float darstellen.
# ein int ist beliebig gross wobei ein float 8 bytes gross ist. Bei zu
# grossen int werten führt unser fall bei 171 int zu float ein overflow error.

