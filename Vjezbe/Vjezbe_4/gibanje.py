import particle as prt

p1 = prt.Particle(10, 60, 10, 10)
p1.printInfo()

print("Numerički domet iznosi {0:.6f} m".format(p1.range_num()))
print("Analitički domet iznosi {0:.6f} m".format(p1.range_ana()))

p1.plot_trajectory()
p1.reset()


#numeričko i analitičko rješenje nije jednako. postoji odstupanje za zadani korak i i zadane parametre manja od 1%
#ovisnost vremenskog koraka i relativne pogreške prikazana je u idećem zadatku