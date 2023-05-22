import solar  as sys
import matplotlib.pyplot as plt

s1 = sys.Solar()
s1.gibanje()
plt.plot(s1.x, s1.y, label="Zemlja")
plt.plot(s1.xs, s1.ys, label="Sunce")
plt.axis("scaled")
plt.legend()
plt.show()