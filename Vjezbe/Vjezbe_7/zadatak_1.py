import projectile as proj
import matplotlib.pyplot as plt

for dt in [0.1, 0.01, 0.001]:
    pr = proj.Projectile(0.1, 10, 60, dt)
    x, y = pr.gibanje()
    plt.plot(x, y, label = "$dt = {}$ (Euler)".format(dt))

pr4 = proj.Projectile(0.1, 10, 60, 0.01)
x4, y4 = pr4.gibanje_rk4()
plt.plot(x4, y4, label = "$dt = {}$ (Runge-Kutta [4])".format(pr4.dt))

plt.title("$x - y$")
plt.xlabel("$x  [m]$")
plt.ylabel("$y  [m]$") 
plt.legend()
plt.show()
