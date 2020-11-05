import math


def sek( f, x0, x1, tol):
    xn = x1
    xn_1 = x0
   
    while(abs(f(xn))>10**(-tol)):
        temp = xn
        xn = xn - (xn-xn_1)/(f(xn)-f(xn_1))*f(xn)
        xn_1 = temp
    return xn

print("von Aufgabe 1:")
def f(x):
    return math.exp(1)**(x**2)+x**(-3)-10
print(sek(f,1.5,2,3))
print(sek(f,-1.5,-2,3))
print(sek(f,0.1,0.5,3))


print()
print("von Aufgabe 2:")
def V(h):
    return (math.pi/3)*(h**2)*(15-h)-471

print(sek(V, 8.5,9, 3))

"""
Um das Newtonverfahren gleichermassen zu implementieren, müsste man die Ableitung
aller Funktionen berechnen können, die als input mitgegeben werden.
"""