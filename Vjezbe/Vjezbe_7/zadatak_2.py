import projectile as proj
import matplotlib.pyplot as plt
 
dts = [0.1, 0.01, 0.001]
xs = []
ys = []

pr = proj.Projectile(1, 10, 60, 0.01)
pr.gibanje()

pr.plot_trajectory()
