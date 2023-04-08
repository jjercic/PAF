import calculus as calc
import numpy as np
import matplotlib.pyplot as plt

def fun_trig(x):
    return np.sin(x)

def fun_cub(x):
    return 2*x**2 + 3

plt.title("Integral", size = 18)
plt.xlabel("N", size = 14)
plt.ylabel("$\int_{0}^{1}\ (2x^2 + 3)\ dx\ $", size = 14)

N = np.arange(50, 1000, 50)
int_trap = []
int_up = []
int_down = []

for n_i in N:
    int_trap.append(calc.integrate_trap(fun_cub, 0, 1, n = n_i))
    int_up.append(calc.integrate_rect(fun_cub, 0, 1, n = n_i)[0])
    int_down.append(calc.integrate_rect(fun_cub, 0, 1, n = n_i)[1])

plt.axhline(y = 11/3, label = "Integral")
plt.scatter(N, int_trap, label = "Metoda trapeza")
plt.scatter(N, int_up, label = "Gornja integralna suma")
plt.scatter(N, int_down, label = "Donja integralna suma")
plt.legend()
#plt.savefig("integral.pdf", bbox_inches = "tight", pad_inches = 0.5)
plt.show()
