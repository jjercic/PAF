import numpy as np

au = 1.486e11
G = 6.67408e-11
M_sun = 1.989e30
M_earth = 5.9742e24

class Solar:
    def __init__(self, dt = 60**2, t0 = 365.22 * 24 * 60* 60):
        self.dt = dt
        self.t0 = t0
        self.t = [0]

        self.Fx, self.Fy = [], []
        self.x, self.y = [au], [0]        
        self.xs, self.ys = [0], [0]
        self.vz = [[0], [29783]]
        self.vs = [[0], [0]]

    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.r = np.sqrt((self.x[-1] - self.xs[-1])**2 + (self.y[-1] - self.ys[-1])**2)

        self.Fx.append(-G * M_sun * M_earth * (self.xs[-1] - self.x[-1]) / self.r**3)
        self.Fy.append(-G * M_sun * M_earth * (self.ys[-1] - self.y[-1]) / self.r**3)

        self.vz[0].append(self.vz[0][-1] - self.Fx[-1] * self.dt / M_earth)
        self.vz[1].append(self.vz[1][-1] - self.Fy[-1] * self.dt / M_earth)
        self.vs[0].append(self.vs[0][-1] + self.Fx[-1] * self.dt / M_sun)
        self.vs[1].append(self.vs[1][-1] + self.Fy[-1] * self.dt / M_sun)

        self.x.append(self.x[-1] + self.vz[0][-1] * self.dt)
        self.y.append(self.y[-1] + self.vz[1][-1] * self.dt)     
        self.xs.append(self.xs[-1] + self.vs[0][-1] * self.dt)
        self.ys.append(self.ys[-1] + self.vs[1][-1] * self.dt)

    def gibanje(self):
        while self.t[-1] <= self.t0:
            self.__move()
