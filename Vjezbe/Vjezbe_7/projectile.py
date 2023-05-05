import numpy as np
import matplotlib.pyplot as plt
g = 9.81

class Projectile:
    def __init__(self, m, v0, theta, dt = 0.01, x_0 = 0, y_0 = 0):
        self.m = m
        self.v0 = v0
        self.theta = theta
        self.x_0 = x_0
        self.y_0 = y_0
        self.dt = dt

        self.a_x = []
        self.a_y = []
        self.v_x = []
        self.v_y = []
        self.x = []
        self.y = []
        self.t = []

    def initial(self):
        self.x.append(self.x_0)
        self.y.append(self.y_0)
        self.v_x.append(self.v0 * np.cos(self.theta * np.pi/180))
        self.v_y.append(self.v0 * np.sin(self.theta * np.pi/180))
        self.a_x.append((-1) * np.sign(self.v_x[0]) * self.__resistence() * (self.v_x[0])**2)
        self.a_y.append((-1) * g - np.sign(self.v_y[0]) * self.__resistence() * (self.v_y[0])**2)
        self.t.append(0)

    def printInfo(self):
        print("Masa čestice = {} kg".format(self.m))
        print("Početna brzina čestice = {} m/s".format(self.v0))
        print("Kut otklona = {}°".format(self.theta))
        print("Početni položaj = ({}, {})".format(self.x_0, self.y_0))

    def moveToOrigin(self):
        self.x_0 = 0
        self.y_0 = 0

    def __move(self):
        self.x.append(self.x[-1] + self.v_x[-1] * self.dt)           
        self.y.append(self.y[-1] + self.v_y[-1] * self.dt)
        self.v_x.append(self.v_x[-1] + self.a_x[-1] * self.dt)
        self.v_y.append(self.v_y[-1] + self.a_y[-1] * self.dt)
        self.a_x.append((-1) * np.sign(self.v_x[-1]) * self.__resistence() * (self.v_x[-1])**2)
        self.a_y.append((-1) * g - np.sign(self.v_y[-1]) * self.__resistence() * (self.v_y[-1])**2)        
        self.t.append(self.t[-1] + self.dt)

    def reset(self):
        self.x_0 = 0
        self.y_0 = 0
        self.a_x = []
        self.a_y = []        
        self.v_x = []
        self.v_y = []
        self.x = []
        self.y = []
        self.t = []

    def gibanje(self):
        self.initial()
        while True:
            if self.y[-1] >= 0:
                self.__move()
            else:
                self.x.pop()
                self.y.pop()
                break
        return self.x, self.y
    
    def plot_trajectory(self):
        plt.title("x - y")
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")        
        plt.plot(self.x, self.y, label = "$dt = {}$".format(self.dt))

    def __resistence(self, rho = 1.293, c_d = 0.295, a = 0.1):
        return rho * c_d * a /(2 * self.m)
    
    def a_v(self, vx, rho = 1.293, c_d = 0.295, a = 0.1):
        return -np.sign(vx) * rho * c_d * a /(2 * self.m) * vx**2

    def __runge_kutta_4(self):
        self.reset()
        self.initial()
        k1_vx = self.a_v(self.v_x[-1]) * self.dt
        k1_x = self.v_x[-1] * self.dt

        k2_vx = self.a_v(self.v_x[-1] + k1_vx/2)
        k2_x = (self.v_x[-1] + k1_vx/2) * self.dt        
        
        k3_vx = self.a_v(self.v_x[-1] + k2_vx/2)
        k3_x = (self.v_x[-1] + k2_vx/2) * self.dt

        k4_vx = self.a_v(self.v_x[-1] + k3_vx/2)
        k4_x = (self.v_x[-1] + k3_vx/2) * self.dt

        self.v_x.append(self.v_x[-1] + 1/6 * (k1_vx + 2 * k2_vx + 2 * k3_vx +k4_vx))
        self.x.append(self.x[-1] + 1/6 * (k1_x + 2 * k2_x + 2 * k3_x +k4_x))

        self.t.append(self.t[-1] + self.dt)

