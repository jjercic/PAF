import numpy as np
import matplotlib.pyplot as plt

class Particle_EB:
    def __init__(self, q, m, E, B, v, dt = 0.001):
        self.q = q
        self.m = m
        self.E = E
        self.B = B
        self.v = v
        self.dt = dt

        self.x = [0]        
        self.y = [0]        
        self.z = [0]
        self.a = 0
        self.t = [0]

    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.x.append(self.x[-1] + self.v[0]*self.dt)
        self.y.append(self.y[-1] + self.v[1]*self.dt)
        self.z.append(self.z[-1] + self.v[2]*self.dt)
        self.v += self.a*self.dt
        self.a = self.q*(self.E + np.cross(self.v, self.B))/self.m

    def gibanje(self, t0):
        while self.t[-1] <= t0:
            self.__move()
        return self.x, self.y, self.z

