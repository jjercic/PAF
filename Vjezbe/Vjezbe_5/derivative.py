import calculus as calc
import numpy as np
import matplotlib.pyplot as plt

def fun_trig(x):
    return np.sin(x)

def fun_cub(x):
    return 5*x**3 - 2*x**2 + 2*x + 3

x_ana = np.linspace(-2, 2, 10000)
df_ana = 15*x_ana**2 - 4*x_ana + 2

num_1 = calc.segment_derivative(fun_cub, -2, 2, eps = 0.01)
num_2 = calc.segment_derivative(fun_cub, -2, 2, eps = 0.1)

plt.title("Derivacija", size = 18)
plt.xlabel("$x$", size = 14)
plt.ylabel('$f\'(x)$', size = 14)

plt.plot(x_ana, df_ana, label = "Analitička derivacija")
plt.plot(num_1[0], num_1[1], label = "$\epsilon = 0.01$")
plt.plot(num_2[0], num_2[1], label = "$\epsilon = 0.1$")
plt.legend()
#plt.savefig("derivacija.pdf", bbox_inches = "tight", pad_inches = 0.5)
plt.show()
