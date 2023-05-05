import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self, m, k, x0, v0, dt = 0.01, time = 2):
        self.m = m
        self.k = k
        self.x0 = x0
        self.v0 = v0
        self.dt = dt
        self.time = time

        self.omega = np.sqrt(k / m)

        self.t = []
        self.x = []
        self.v = []
        self.a = []

        self.t.append(0)
        self.x.append(x0)
        self.v.append(v0)
        self.a.append(-k/m * x0)

    def __move(self):
        self.a.append(-self.k/self.m * self.x[-1])
        self.v.append(self.v[-1] + self.a[-1] * self.dt)
        self.x.append(self.x[-1] + self.v[-1] * self.dt)
        self.t.append(self.t[-1] + self.dt)


    def gibanje(self):
        while self.t[-1] + self.dt <= self.time:
                self.__move()

    def reset(self):
        self.t = []
        self.x = []
        self.v = []
        self.a = []

        self.t.append(0)
        self.x.append(self.x0)
        self.v.append(self.v0)
        self.a.append(-self.k/self.m * self.x0)
        
    def plot(self):
        plt.subplot(1, 3, 1)
        plt.title("x - t")
        plt.ylabel("x [$m$]")
        plt.xlabel("t [s]")        
        plt.plot(self.t, self.x)

        plt.subplot(1, 3, 2)
        plt.title("v - t")
        plt.ylabel("v [$\dfrac{m}{s}$]")
        plt.xlabel("t [s]")        
        plt.plot(self.t, self.v)

        plt.subplot(1, 3, 3)
        plt.title("a - t")
        plt.ylabel("a [$\dfrac{m}{s^2}$]")
        plt.xlabel("t [s]")        
        plt.plot(self.t, self.a)
        plt.show()
        
    def period(self):
        self.reset()
        self.gibanje()
        if(self.x0 != 0):

            #xmax = [xi for xi in self.x if xi/self.x0 > 0.999]
            #xmin = [xi for xi in self.x if xi/(-self.x0) > 0.999]            
            
            xmax = [xi for xi in self.x if xi - self.x0 < 1e-6]
            xmin = [xi for xi in self.x if xi + self.x0 < 1e-6]

            tmax = [self.t[self.x.index(x)] for x in xmax]
            tmin = [self.t[self.x.index(x)] for x in xmin]
        
        return np.abs(tmin[0] - tmax[0]) * 2