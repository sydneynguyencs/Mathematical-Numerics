import numpy as np
import matplotlib.pyplot as plt



#a) bei x = 1.1 hat das Polynom 100x^2-200x+99 eine Nullstelle. 
#In der nähe von x = 1.1 werden also ungefähr gleich grosse Zahlen 
#voneinander abgezogen wodurch Auslöschung entsteht
x0 = 1.10000001
print("x0 = ", x0)
print("h(x0) = ",100*x0**2-200*x0+99)
#wenn man das Polynom berechnet erhält nicht 0 sondern eine sehr kleine Zahl

x1 = np.arange(1.1, 1.3, 10**-7)

def h (x):    
    return np.sqrt(100*x**2-200*x+99)

def derH(x):
    return (100*(x-1))/h(x)

def conH(x):
    return (abs(derH(x))*abs(x))/abs(h(x))


print("Konditionszahl von h(x0): ",conH(x0))
print("\n")

plt.semilogy(x1,conH(x1))

plt.xlabel("x")
plt.ylabel("log( K(h) )")
plt.legend(['K(h)'])
plt.title('Konditionszahl h(x) ')
#b) wir sehen dass die Konditionszahl von h(x) generell relativ klein ist, 
#aber in der nähe von 1.1 plötzlich sehr gross wird

#c) da die Konditionszahl gross ist für x nahe 1.1, kann keine Umformung
# gemacht werden um die Auslöschung zu verhindern


