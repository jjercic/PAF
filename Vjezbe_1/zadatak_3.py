##Zadatak 3
##Napišite program koji će korisnika tražiti da upiše (x,y) koordinate za dvije točke. 
##Ako korisnik pogriješi prilikom unosa koordinate opomenite ga da ponovi upis. 
##Nakon što je korisnik uspješno upisao dvije koordinate ispišite na ekran jednadžbu pravca koji prolazi kroz te dvije točke.
print("Unesite (x,y) koordinate za dvije točke: ")

try:
    print("Točka A: ")
    xa = int(input("x = "))
    ya = int(input("y = "))

    print("Točka B: ")
    xb = int(input("x = "))
    yb = int(input("y = "))

except:
    print("Niste unijeli broj. Pokušajte ponovno!")
    print("Točka A: ")
    xa = int(input("x = "))
    ya = int(input("y = "))

    print("Točka B: ")
    xb = int(input("x = "))
    yb = int(input("y = "))

k = (yb - ya) / (xb - xa)
l = ya - xa * k
print("y = {}x + {}".format(k, l))