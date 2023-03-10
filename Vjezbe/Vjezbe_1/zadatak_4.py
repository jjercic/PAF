##Zadatak 4 
##Napišite funkciju koja kao ulazne parametre prima (x,y) koordinate za dvije točke. 
##Neka ta funkcija na ekran ispisuje jednadžbu pravca koji prolazi kroz te dvije točke. 
##Pozovite tu funkciju u svom programu.

def pravac(xa, ya, xb, yb):
    k = (yb - ya) / (xb - xa)
    l = ya - xa * k
    print("y = {}x + {}".format(k, l))

pravac(0, 1, 10, 21)
