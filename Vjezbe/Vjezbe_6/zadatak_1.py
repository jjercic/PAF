import harmonic_oscillator as har

m = 0.1
k = 10
x0 = 0.3
v0 = 0

ho = har.HarmonicOscillator(m, k, x0, v0)
ho.gibanje()
ho.plot()