import numpy as np

au = 1.486e11
G = 6.67408e-11
M_sun = 1.989e30
M_earth = 5.9742e24

class Solar:
    def __init__(self, dt, t0):
        self.dt = dt
        self.t0 = t0
        self.t = [0]
        self.reps = self.t0 / self.dt
        self.phi = self.reps * 2 * np.pi / (24 * 60 * 60) - np.pi

        self.rz0 = au
        self.rs0 = 0

        self.xz0 = -au
        self.yz0 = 0
        self.xs0 = 0
        self.ys0 = 0
        self.vz0 = 29783
        self.vs0 = 0

        self.a_s = []
        self.a_z = []

        self.v_s = [self.vs0]
        self.v_z = [self.vz0]        
        
        self.r_s = [self.rs0]
        self.r_z = [self.rz0]

        self.x = [self.xz0]
        self.y = [self.yz0]        
        
        self.xs = [self.xs0]
        self.ys = [self.ys0]
        
    def __move(self):
        self.t.append(self.t[-1] + self.dt)

        self.a_z.append(-G * M_sun/np.abs(self.r_z[-1] - self.r_s[-1])**3 * (self.r_z[-1] - self.r_s[-1]))
        self.a_s.append(-G * M_earth/np.abs(self.r_s[-1] - self.r_z[-1])**3 * (self.r_s[-1] - self.r_z[-1]))

        self.v_z.append(self.v_z[-1] + self.a_z[-1] * self.dt)
        self.v_s.append(self.v_s[-1] + self.a_s[-1] * self.dt)

        self.r_z.append(self.r_z[-1] + self.v_z[-1] * self.dt)
        self.r_s.append(self.r_s[-1] + self.v_s[-1] * self.dt)

        self.x.append(np.cos(self.phi) * self.r_z[-1])
        self.y.append(np.sin(self.phi) * self.r_z[-1])        
        
        self.xs.append(np.cos(self.phi) * self.r_s[-1])
        self.ys.append(np.sin(self.phi) * self.r_s[-1])

        self.phi += self.t0 / (24 * 60 * 60) * 2 * np.pi / self.reps

    def gibanje(self):
        while self.t[-1] <= self.t0:
            self.__move()
