##Zadatak 2
##Napišite funkciju koja uzima broj iteracija N te N puta zbraja 1/3 pa zatim N puta oduzima 1/3 broju 5. 
##Ispišite konačni rezultat za 200, 2000 i 20000 iteracija. Objasnite rezultat koji ste dobili.
def iter(N):
    broj = 5
    for i in range(N):
        broj += 1/3
    for i in range(N):
        broj -= 1/3
    print(broj)

iter(200)
iter(2000)
iter(20000)

##za različiti broj iteracija dobivamo različite rezultate i nijedan nije 5.0000... 
##to je posljedica nepreciznosti aproksimacije pri racunanju zadanih brojeva jer oni nisu zadani u oblike potenicja broja 2