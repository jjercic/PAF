import matplotlib.pyplot as plt
import particle as prt
import numpy as np

dt = np.linspace(0.0001, 0.1, 10000)
error = []

for t in dt:
    p1 = prt.Particle(10, 60, 0, 0, t)
    err = 100 * np.abs(p1.range_ana() - p1.range_num())/p1.range_ana()
    error.append(err)

plt.title("Apsolutna relativna pogreška dometa projektila")
plt.xlabel("dt / s")
plt.ylabel("Apsolutna relativna pogreška / %")        
plt.plot(dt, error)
plt.show()
