# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 14:06:30 2020

@author: Sydney Nguyen
"""
import numpy as np
import matplotlib.pyplot as plt
#Notiz: alpha:= a

#Aufgabe 2
# a)
#wir sehen, dass sich der Grenzwert von k  
#im jeweilgen Intervall von a wie gefolgt verhaltet: 
#a in [0,1) => k konvergiert zu 0
#a in (1,3) => k konvergiert zu k = 1-1/a
#a in [3,4] => k divergiert, da auch 
#nach 1000 iterationen der Wert von k immer noch zwischen den 
#"min" und "max" Werten hin und her pendelt

# k:= relatve Anzahl erkrankter Kinder zum Zeitpunkt
# a:= Infektionsrate 

def ki1(a):
    ki = 0.1
    for i in range(100000):
        ki = a*ki*(1-ki)
        
    return ki
    
x = np.arange(0,4,0.01)

plt.plot(x,ki1(x))
plt.title('k(100\'000) with a = a0')
plt.xlabel('a0')
plt.ylabel('k (100\'000)')
plt.show()

mymax = []
mymin = []
def ki3(a):
    ki = 0.1
    for i in range(1000):
        ki = a*ki*(1-ki)
    max1 = ki
    min1 = ki
    for i in range(1000):
        ki = a*ki*(1-ki)
        if ki> max1:
            max1 = ki
        if ki < min1:
            min1 =ki
    mymax.append(max1)
    mymin.append(min1)
    return ki


x = np.arange(0,4,0.01)

for i in range(len(x)):
    ki3(x[i])
plt.plot(x, mymax)
plt.plot(x, mymin)
plt.title('max and min value of k after 1000 iterations')
plt.xlabel('a0')
plt.ylabel('k (100\'000)')
plt.ylim(0,1)
plt.legend(['max','min'])
plt.show()

# b) Fixpunkt:= Anzahl Erkrankte und Gesunde befindet sich im Gleichgewicht

# c) a = 1/(1-k))
# Je grösser k ist, desto grösser wird a -> a und k sind proportional.
# Fixpunkt ist proportional zu alpha.