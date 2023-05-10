import harmonic_oscillator as har
import matplotlib.pyplot as plt
import numpy as np

m = 0.1
k = 10
x0 = 0.3
v0 = 0
vrijeme = 2

def analitic(m, k, x0):
    omega = np.sqrt(k / m)
    t_ana = np.linspace(0, vrijeme, 1000)
    x_ana = x0 * np.cos(omega * t_ana)
    return t_ana, x_ana

dts = [0.001, 0.01, 0.05]
xs, ts = [], []

for t in dts:
    osc = har.HarmonicOscillator(m, k, x0, v0, t, vrijeme)
    osc.gibanje()
    ts.append(osc.t)
    xs.append(osc.x)

analitic_xt = analitic(m, k, x0)
ts.append(analitic_xt[0])
xs.append(analitic_xt[1])

plt.title("Harmonic oscillator")
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.plot(ts[0], xs[0], label = "analytical", color = 'r')
for i in range(len(dts)):
    plt.scatter(ts[i], xs[i], label = "$dt = {}$".format(dts[i]), s = i**3 + 1)
plt.legend()
plt.show()

"""
def analitic_T(m, k):
    omega = np.sqrt(k / m)
    return 2*np.pi/omega

T0 = analitic_T(m, k)
dt = np.linspace(0.001, 0.01, 1000)
err = []

for t in dt:
    osc = har.HarmonicOscillator(m, k, x0, v0, t)
    err.append(100 * np.abs(T0 - osc.period())/T0 )

plt.title("Apsolutna relativna pogreška perioda titranja")
plt.xlabel("$dt$ [s]")
plt.ylabel("Error [%]")
plt.plot(dt, err)
plt.show()
"""