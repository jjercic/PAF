## Zadatak 1 
## Napišite program u kojem korisnik definira iznos sile u N i masu čestice u kg,
## a program crta x − t, v − t i a −t graf za prvih 10 sekundi jednolikog gibanja u jednoj dimenziji. 
## Diferencijalne jednadžbe rješavajte numerički. 
## Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.
import numpy as np
import matplotlib.pyplot as plt

F = int(input("Iznos sile F u N: "))
m = int(input("Iznos mase čestice m u kg: "))
dt = 10

a = F / m
v0 = 0
##v = v0 + a*dt
##s = v0*dt + 0.5*a*dt*dt

#a-t
plt.title("a - t")
plt.xlabel("t / s")
plt.ylabel("a / m/s^2")

plt.axhline(y = a)
plt.xlim(0, 10)
plt.ylim(0, 1.5 * a)

plt.show()

##v-t
plt.title("v - t")
plt.xlabel("t / s")
plt.ylabel("v / m/s")
           
ts = np.linspace(0, dt)
vs = a * ts

plt.xlim(0, dt)
plt.ylim(0, dt * a)
plt.plot(ts, vs)

plt.show()

#s-t
plt.title("s - t")
plt.xlabel("t / s")
plt.ylabel("s / m")
           
ss = 0.5 * a * ts *ts

plt.xlim(0, dt)
plt.ylim(0, 0.5 * a * dt *dt)
plt.plot(ts, ss)

plt.show()