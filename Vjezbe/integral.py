import calculus as calc
import numpy as np
import matplotlib.pyplot as plt

def fun_trig(x):
    return np.sin(x)

def fun_cub(x):
    return 2*x**2 + 3

plt.title("Integral")
plt.xlabel("N")
plt.ylabel("Integral")

N = np.arange(50, 1000, 50)
int_trap = []
int_up = []
int_down = []

for n_i in N:
    int_trap.append(calc.integrate_trap(fun_cub, 0, 1, n = n_i))
    int_up.append(calc.integrate_rect(fun_cub, 0, 1, n = n_i)[0])
    int_down.append(calc.integrate_rect(fun_cub, 0, 1, n = n_i)[1])

plt.scatter(N, int_trap)
plt.scatter(N, int_up)
plt.scatter(N, int_down)
plt.axhline(y = 11/3)

plt.show()

