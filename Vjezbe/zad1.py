## Zadatak 1 
## Napišite program u kojem korisnik definira iznos sile u N i masu čestice u kg,
## a program crta x − t, v − t i a −t graf za prvih 10 sekundi jednolikog gibanja u jednoj dimenziji. 
## Diferencijalne jednadžbe rješavajte numerički. 
## Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.
import numpy as np
import matplotlib.pyplot as plt

F = int(input("Iznos sile F u N: "))
m = int(input("Iznos mase čestice m u kg: "))
dt = 10

a = F / m
v0 = 0 ##početna brzina je nula?
v = v0 + a*dt
s = v0*dt + 0.5*a*dt*dt

plt, ax = plt.subplots(figsize=(12, 6))

plt.axhline(y = a)
plt.show()