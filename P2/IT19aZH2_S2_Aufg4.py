# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:31:49 2020

@author: Team 02: Sydney Nguyen, Jari Rentsch
"""

i=1.0
last =0.0
n=0
while (i+1!=1):
    last=i
    i =  i/2
    n=n+1
print("eps: ", last)

i=0.0
last =0.0
n=0
while (i+1!=i):
    last=i
    i =  (i+1)*2
    n=n+1
while(last+1!=last):
    last = last+1
print("qMax: ",last)