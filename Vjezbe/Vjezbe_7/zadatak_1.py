import projectile as proj
import matplotlib.pyplot as plt
 
dts = [0.1, 0.01, 0.001]
xs = []
ys = []

plt.title("$x - y$")
plt.xlabel("$x  [m]$")
plt.ylabel("$y  [m]$") 

for dt in dts:
    pr = proj.Projectile(1, 10, 60, dt)
    pr.gibanje()
    pr.plot_trajectory()


plt.show()
