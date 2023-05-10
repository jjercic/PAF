import numpy as np
import matplotlib.pyplot as plt
import particle_em as prt

E = np.array((0, 0, 0))
B = np.array((0, 0, 1))
v = np.array((0.1, 0.1, 0.1))
q = m = 1
t = 20

ele = prt.Particle_EB(-q, m, E, B, v)
xe, ye, ze = ele.gibanje(t)

pos = prt.Particle_EB(q, m, E, B, v)
xp, yp, zp = pos.gibanje(t)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(xe, ye, ze)
ax.plot3D(xp, yp, zp)

plt.show()

