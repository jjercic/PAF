##Napišite svoj modul "kinematika.py" koji će sadržavati funkcije jednoliko_gibanje() i kosi_hitac(). 
##Neka funkcije kao ulazne parametre primaju sve podatke neophodne za izračun (iznos sile, iznos brzine, kut otklona, masa, vrijeme, ...) 
##i neka crtaju iste grafove kao i u prošlim zadatcima. 
##Napravite novi program u kojem ćete uključiti razvijeni modul i pozvati obe funkcije.
import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m, dt):
    a = F / m

    #a-t
    plt.subplot(1,3,1)
    plt.title("a - t")
    plt.xlabel("t / s")
    plt.ylabel("a / m/s^2")

    plt.axhline(y = a)
    plt.xlim(0, 10)
    plt.ylim(0, 1.5 * a)
    ##v-t
    plt.subplot(1,3,2)
    plt.title("v - t")
    plt.xlabel("t / s")
    plt.ylabel("v / m/s")
            
    ts = np.linspace(0, dt)
    vs = a * ts

    plt.xlim(0, dt)
    plt.ylim(0, dt * a)
    plt.plot(ts, vs)

    #s-t
    plt.subplot(1,3,3)
    plt.title("s - t")
    plt.xlabel("t / s")
    plt.ylabel("s / m")
            
    ss = 0.5 * a * ts *ts

    plt.xlim(0, dt)
    plt.ylim(0, 0.5 * a * dt *dt)
    plt.plot(ts, ss)

    plt.show()

def kosi_hitac(v0, theta, t):
    theta = np.pi*theta/180
    dt = 0.01
    eps = int(t / dt)
    g = 9.81

    vx = []
    vy = []

    vy.append(v0 * np.sin(theta) - g * dt)

    for i in range(eps):
        vx.append(v0 * np.cos(theta))
        if i != 0:
            vy.append(vy[i - 1] - g * dt)

    x = []
    y = []
    x.append(vx[0] * dt)
    y.append(vy[0] * dt)

    for i in range(1, eps):
        x.append(x[i - 1] + vx[i] * dt)
        y.append(y[i - 1] + vy[i] * dt)

    dt = np.linspace(0, t, eps)

    #x-y
    plt.subplot(1, 3, 1)
    plt.title("x - y")
    plt.xlabel("x / m")
    plt.ylabel("y / m")        
    plt.plot(x, y)

    #x-t
    plt.subplot(1, 3, 2)
    plt.title("x - t")
    plt.ylabel("x / m")
    plt.xlabel("t / s")   
    plt.plot(dt, x)

    #y-t
    plt.subplot(1, 3, 3)
    plt.title("y - t")
    plt.ylabel("y / m")
    plt.xlabel("t / s")
    plt.plot(dt, y)
    plt.show()
