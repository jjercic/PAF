## Zadatak 2
## Napišite program u kojem korisnik definira iznos početne brzine v0 u m s i kut otklona θ u stupnjevima.
## Neka program crta x−y, x−t i y−t graf za prvih 10 sekundi gibanja u dvije dimenzije. 
## Diferencijalne jednadžbe rješavajte numerički. 
## Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.

import numpy as np
import matplotlib.pyplot as plt

v0 = int(input("Iznos početne brzine v0 u m /s: "))
theta = int(input("Iznos kuta otklona θ u stupnjevima: "))

eps = 100
dt = np.linspace(0, 10, eps)
dt = 0.1
g = 9.81

vx = []
vy = []

for i in range(eps):
    vx.append(v0 * np.cos(theta))
    i += 1

for i in range(eps):
    if i == 0:
        vy.append(v0 * np.sin(theta) - g * dt)
    else:
        vy.append(vy[i - 1] + v0 * np.sin(theta) - g * dt)
    i += 1


x = []
y = []

for i in range(eps):
    if i == 0:
        x.append(vx[i] * dt)
    else:
        x.append(x[i - 1] + vx[i] * dt)
    i += 1

for i in range(eps):
    if i == 0:
        y.append(vy[i] * dt)
    else:
        y.append(y[i - 1] + vy[i] * dt)
    i += 1

"""for i in range(50):
    x[i] = vx[i] * dt[i]
for i in range(50):
    y[i] = vy[i] * dt[i] - 0.5 * g * dt[i] * dt[i]
"""
#x-y
plt.title("x - y")
plt.xlabel("x / m")
plt.ylabel("y / m")
           
plt.plot(x, y)
plt.show()
"""
#x-t
plt.title("x - t")
plt.ylabel("x / m")
plt.xlabel("t / s")
           
plt.plot(x, dt)
plt.show()

#y-t
plt.title("y - t")
plt.ylabel("y / m")
plt.xlabel("t / s")
           
plt.plot(y, dt)
plt.show()
"""