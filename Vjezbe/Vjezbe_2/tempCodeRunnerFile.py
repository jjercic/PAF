theta = np.pi*theta/180
eps = 1000
dt = 0.01
g = 9.81

vx = []
vy = []

vy.append(v0 * np.sin(theta) - g * dt)

for i in range(eps):
    vx.append(v0 * np.cos(theta))
    if i != 0:
        vy.append(vy[i - 1] - g * dt)
    i += 1


x = []
y = []
x.append(vx[0] * dt)
y.append(vy[0] * dt)

for i in range(1, eps):
    x.append(x[i - 1] + vx[i] * dt)
    y.append(y[i - 1] + vy[i] * dt)
    i += 1

dt = np.linspace(0, 10, eps)

#x-y
plt.subplot(1, 3, 1)
plt.title("x - y")
plt.xlabel("x / m")
plt.ylabel("y / m")        
plt.plot(x, y)

#x-t
plt.subplot(1, 3, 2)
plt.title("x - t")
plt.ylabel("x / m")
plt.xlabel("t / s")   
plt.plot(dt, x)

#y-t
plt.subplot(1, 3, 3)
plt.title("y - t")
plt.ylabel("y / m")
plt.xlabel("t / s")
plt.plot(dt, y)
plt.show()
