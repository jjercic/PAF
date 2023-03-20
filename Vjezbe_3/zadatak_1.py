##Zadatak 1 
##(a) Oduzmite 5.0 i 4.935. Koji rezultat očekujete? Koji rezultat dobijete koristeći Python? Objasnite. 
##(b) Provjerite iznosi li suma brojeva 0.1, 0.2 i 0.3 broj 0.6. Objasnite rezultat koji ste dobili.
a = 5.0
b = 4.935
##realno je očekivati 0.065, ali zbog aproksimacije pri računanju moguće je dobiti malo drugačiji rezultat
print(a-b)
##rezultat u py-u je 0.06500000000000039
##brojevi u py-u se zapisuju u obliku potencija broj 2 u binarnom zapisu, zbog čega dolazi do pogreške u aproksimaciji pri prijelazu u dekadski sustav

x = 0.1
y = 0.2
z = 0.3
q = 0.6

print("0.1 + 0.2 + 0.3 = {}".format(x + y + z))
#dobiveni rezultat je jednak 0.6 do određene decimale nakon čega je različit. to se događa zbog ograničenja preciznosti aproksimacije.
print(x + y + z == q)
