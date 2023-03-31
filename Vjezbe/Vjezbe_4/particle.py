import numpy as np
import matplotlib.pyplot as plt
g = 9.81

class Particle:
    def __init__(self, v0, theta, x_0, y_0, dt = 0.01):
        self.v0 = v0
        self.theta = theta
        self.x_0 = x_0
        self.y_0 = y_0
        self.dt = dt

        self.v_x = []
        self.v_y = []
        self.x = []
        self.y = []
        self.t = []

        self.v_x.append(self.v0 * np.cos(self.theta * np.pi/180))
        self.v_y.append(self.v0 * np.sin(self.theta * np.pi/180))
        self.x.append(x_0)
        self.y.append(y_0)
        self.t.append(0)
    

    def printInfo(self):
        print("Početna brzina čestice = ", self.v0)
        print("Kut otklona = {}°".format(self.theta))
        print("Početni položaj = ({}, {})".format(self.x_0, self.y_0))

    def moveToOrigin(self):
        self.x_0 = 0
        self.y_0 = 0

    def __move(self):
        self.x.append(self.x[-1] + self.v_x[-1] * self.dt)           
        self.y.append(self.y[-1] + self.v_y[-1] * self.dt)
        self.v_x.append(self.v0 * np.cos(self.theta * np.pi/180))
        self.v_y.append(self.v_y[-1] - g * self.dt)
        self.t.append(self.t[-1] + self.dt)
        #1xy, 2v, 3a

    def reset(self):
        self.v0 = 0
        self.theta = 0
        self.x_0 = 0
        self.y_0 = 0
        self.v_x = []
        self.v_y = []
        self.x = []
        self.y = []
        self.t = []
    
    def range_ana(self):
        return self.v_x[0] * (self.v_y[0] + np.sqrt(self.v_y[0]**2 + 2 * g * self.y_0)) / g 

    def range_num(self):
        i = 1
        while True:
            if self.y[i-1] < 0:
                break
            self.__move()
            i += 1
        return self.x[i-1] - self.x_0
    
    def plot_trajectory(self):
        plt.title("x - y")
        plt.xlabel("x / m")
        plt.ylabel("y / m")        
        plt.plot(self.x, self.y)
        plt.show()