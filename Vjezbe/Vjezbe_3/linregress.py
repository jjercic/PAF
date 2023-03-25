## Zadatak 4 
## Napišite program linregress.py za određivanje modula torzije Dt aluminijske šipke ako znamo da vrijedi M=Dt·φ. 
## Parametri su nam zadani kao M = [0.052,0.124,0.168,0.236,0.284,0.336] Nm, φ = [0.1745,0.3491,0.5236,0.6981,0.8727,1.0472] rad. 
import numpy as np
import matplotlib.pyplot as plt

M = np.array([0.052,0.124,0.168,0.236,0.284,0.336])
phi = np.array([0.1745,0.3491,0.5236,0.6981,0.8727,1.0472])
n = len(M)

xy_avg = np.average([M[i] * phi[i] for i in range(n)])
x2_avg = np.average([ph**2 for ph in phi])
y2_avg = np.average([m**2 for m in M])

a = xy_avg / x2_avg
dev = np.sqrt((y2_avg / x2_avg - a**2)/n)

print("Modul torzije aluminijske šipke iznosi: {0:.4f} +/- {1:.4f} Nm/rad".format(a, dev))

plt.title("Modul torzije D$_{t}$ aluminijske šipke")
plt.xlabel("$\phi$ [rad]")
plt.ylabel("M [Nm]")
plt.plot(phi, M, "go")
fit = np.polyfit(phi, M, 1)          #[0.32215867 0.00320401]
M_lr = [fit[0] * ph for ph in phi]   # = [a * ph for ph in phi]
plt.plot(phi, M_lr)
"""
graph = np.poly1d(fit)
plt.plot(phi, graph(phi))
"""
plt.show()