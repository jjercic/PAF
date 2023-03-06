##Zadatak 5 
##Unaprijedite kod iz prethodnog zadatka koristeći modul matplotlib.pyplot tako da nacrtate unesene koordinate i pravac koji prolazi kroz njih. 
##Ponudite u funkciji opciju da se graf prikaže na ekranu ili da se spremi kao PDF. 
##Dopustite korisniku da bira ime pod kojim će se spremiti graf.
import matplotlib.pyplot as plt
import numpy as np

def pravac(xa, ya, xb, yb):
    k = (yb - ya) / (xb - xa)
    l = ya - xa * k
    print("y = {}x + {}".format(k, l))

    xs = np.linspace(-5, 5, 20)
    ys = k * xs + l

    plt.title("Pravac")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot(xs, ys)
    plt.plot(xa, ya, marker="o")
    plt.plot(xb, yb, marker="o")

    plt.show()

pravac(1, 2, 4, 8)