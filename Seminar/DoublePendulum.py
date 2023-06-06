import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.81

class DoublePendulum:
    def __init__(self, l1 = 1.5, l2 = 1, m1 = 1.5, m2 = 1, theta1 = 90, theta2 = 90, omega1 = 0, omega2 = 0, T = 5, dt = 0.01):
        #duljine njihala
        self.l1 = l1
        self.l2 = l2
        #mase njihala
        self.m1 = m1
        self.m2 = m2
        #početni kutevi otklona [stupnjevi]
        self.theta1 = [np.radians(theta1)]            
        self.theta2 = [np.radians(theta2)]
        #početne kutne brzine [stupnjevi / s]
        self.omega1 = [np.radians(omega1)]        
        self.omega2 = [np.radians(omega2)]

        self.T = T      #trajanje gibanja
        self.dt = dt    #vremenski korak
        self.t = 0

        self.x1, self.y1, self.x2, self.y2 = [], [], [], []

        self.pend1 = None
        self.pend2 = None
        self.timer_text = None
        self.animation = None

    def diff_solve(self, theta1, theta2, omega1, omega2):
        theta1_ = omega1
        theta2_ = omega2

        denom = 2 * self.m1 + self.m2 - self.m2 * np.cos(2*(theta1 - theta2))
        omega1_ = - g * (2 * self.m1 + self.m1) * np.sin(theta1) - self.m2 * g * np.sin(theta1 - 2 * theta2) - 2 * np.sin(theta1 - theta2) * self.m2 * (self.l2 * omega2**2 + self.l1 * np.cos(theta1 -theta2) * omega1) / (self.l1 * denom)
        omega2_ = 2 * np.sin(theta1 - theta2) * (self.l1 * (self.m1 + self.m2) * omega1**2 + g * (self.m1 + self.m2) * np.cos(theta1) + self.l2 * self.m2 * np.cos(theta1 - theta2) * omega2**2) / (self.l2 * denom)
        return theta1_, theta2_, omega1_, omega2_
    
    def __move(self, frame):
        theta1_, theta2_, omega1_, omega2_ = self.diff_solve(self.theta1[-1], self.theta2[-1], self.omega1[-1], self.omega2[-1])

        self.theta1.append(self.theta1[-1] + theta1_ * self.dt)        
        self.theta2.append(self.theta2[-1] + theta2_ * self.dt)
        self.omega1.append(self.omega1[-1] + omega1_ * self.dt)
        self.omega2.append(self.omega2[-1] + omega2_ * self.dt)

        x1 = self.l1 * np.sin(self.theta1[-1])
        y1 = - self.l1 * np.cos(self.theta1[-1])        
        
        x2 = x1 + self.l2 * np.sin(self.theta2[-1])
        y2 = y1 - self.l2 * np.cos(self.theta2[-1])

        self.x1.append(x1)
        self.y1.append(y1)
        self.x2.append(x2)
        self.y2.append(y2)

        self.pend1.set_data([0, x1], [0, y1])
        self.pend2.set_data([x1, x2], [y1, y2])

        self.t += self.dt
        self.timer_text.set_text("Time: {:.2f} s".format(self.t))

        if self.t >= self.T:
            self.animation.event_source.stop()
            plt.close()

        return self.pend1, self.pend2, self.timer_text
    
    def animate(self):
        fig, ax = plt.subplots()
        l = self.l1 + self.l2
        ax.set_xlim(-l, l)
        ax.set_ylim(-l, l)
        plt.title("Double Pendulum")
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")

        self.pend1, = ax.plot([], [], 'bo-')
        self.pend2, = ax.plot([], [], 'go-')
        self.timer_text = ax.text(
            0.1,
            0.9,
            "",
            transform = ax.transAxes,
            ha = "left",
            va = "top",
            fontsize = 10
        )
        self.animation = FuncAnimation(
            fig,
            self.__move,
            frames = int(self.T / self.dt),
            interval = self.dt,
            blit = True
        )

        plt.show()

pend = DoublePendulum()
pend.animate()
