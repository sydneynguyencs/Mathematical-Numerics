import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.1,100,0.1)
f = 5*2**(-3)*x**(-2/3)
g = 10**5*((2*np.exp(1))**(-x/100))
h = (10**(2*x)/2**(5*x))**2
plt.loglog(x, f)
plt.title('f(x) ')
plt.xlabel("log(x)")
plt.ylabel("log(f)")
plt.show()

plt.semilogy(x, g)
plt.title('g(x) ')
plt.xlabel("x")
plt.ylabel("log(g)")
plt.show()

plt.semilogy(x, h)
plt.title('h(x) ')
plt.xlabel("x")
plt.ylabel("log(h)")
