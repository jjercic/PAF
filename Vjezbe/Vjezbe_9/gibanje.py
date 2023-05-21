import system as sys
import matplotlib.pyplot as plt

s1 = sys.Solar(1, 24*60*60)
s1.gibanje()
plt.plot(s1.x, s1.y, label="Zemlja")
plt.plot(s1.xs, s1.ys, label="Sunce")
plt.legend(loc = 6)
plt.show()
