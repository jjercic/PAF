import numpy as np
import matplotlib.pyplot as plt

class Particle_EB:
    def __init__(self, q, m, E, B, v, dt = 0.01):
        self.q = q
        self.m = m
        self.E = E
        self.B = B
        self.v = v
        self.dt = dt

        self.x = [0]        
        self.y = [0]        
        self.z = [0]
        self.a = [[0, 0, 0]]
        self.t = [0]

    def __move(self):
        self.a = self.q*(self.E + np.cross(self.v, self.B))/self.m
        self.v += self.a*self.dt
        self.x.append(self.x[-1] + self.v[0]*self.dt)
        self.y.append(self.y[-1] + self.v[1]*self.dt)
        self.z.append(self.z[-1] + self.v[2]*self.dt)
        self.t.append(self.t[-1] + self.dt)

    def gibanje(self, t0, mode = 'eul'):
        while self.t[-1] <= t0:
            if mode == 'eul':
                self.__move()
            elif mode == 'rk4':
                self.__move_rk4()
        return self.x, self.y, self.z

    def a_v(self, k_i = 0):
        return self.q*(self.E + np.cross(self.v + k_i, self.B))/self.m
    
    def __move_rk4(self):
        self.t.append(self.t[-1] + self.dt)

        k1_v = self.a_v() * self.dt
        k1 = self.v * self.dt

        k2_v = self.a_v(k1_v/2) * self.dt
        k2 = (self.v + k1_v/2) * self.dt  

        k3_v = self.a_v(k2_v/2)* self.dt
        k3 = (self.v + k2_v/2) * self.dt

        k4_v = self.a_v(k3_v/2)* self.dt
        k4 = (self.v + k3_v/2) * self.dt

        self.v += 1/6 * (k1_v + 2 * k2_v + 2 * k3_v + k4_v)
        self.x.append(self.x[-1] + 1/6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]))
        self.y.append(self.y[-1] + 1/6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]))
        self.z.append(self.z[-1] + 1/6 * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2]))