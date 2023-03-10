## Zadatak 2
## Napišite program u kojem korisnik definira iznos početne brzine v0 u m s i kut otklona θ u stupnjevima.
## Neka program crta x−y, x−t i y−t graf za prvih 10 sekundi gibanja u dvije dimenzije. 
## Diferencijalne jednadžbe rješavajte numerički. 
## Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.

import numpy as np
import matplotlib.pyplot as plt

v0 = int(input("Iznos početne brzine v0 u m /s: "))
theta = int(input("Iznos kuta otklona θ u stupnjevima: "))

dt = np.linspace(0, 10)
g = 9.81

vx = v0 * np.cos(theta * np.pi/180) + np.zeros(50)
vy = v0 * np.sin(theta * np.pi/180) - g * dt

x = vx * dt + np.zeros(50)
y = vy * dt - 0.5 * g * dt * dt
print(x)

#x-y
plt.title("x - y")
plt.xlabel("x / m")
plt.ylabel("y / m")
           

plt.plot(x, y)

plt.show()
