import numpy as np
import matplotlib.pyplot as plt
import particle_em as prt

E = np.array((0, 0, 0))
B = np.array((0, 0, 1))
q = m = 1
t = 20
#gibanje elektrona - Eulrova metoda
ele = prt.Particle_EB(-q, m, E, B, np.array((0.1, 0.1, 0.1)))
xe, ye, ze = ele.gibanje(t)

#gibanje pozitrona - Runge-kutta metoda 4. reda
pos = prt.Particle_EB(+q, m, E, B, np.array((0.1, 0.1, 0.1)))
xp, yp, zp = pos.gibanje(t, 'rk4')

fig = plt.figure()
ax = plt.axes(projection = '3d')

ax.plot3D(xe, ye, ze, label = "elektorn [Euler]")
ax.plot3D(xp, yp, zp, label = "pozitron [Runge-Kutta]")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

