##Zadatak 3 
##(a) Napišite program arithm.py koji računa aritmetičku sredinu i standardnu devijaciju za 10 točaka. 
##Formula za aritmetičku sredinu je dana u 1, a za standardnu devijaciju u 2. 
##(b) Napišite program pod (a) koristeći gotove module.
import numpy as np
# (a)
def sredina(nums):
    return sum(nums)/len(nums)

def std_dev(nums):
    N = len(nums)
    sigma = np.sqrt(sum((num - sredina(nums))**2 for num in nums)/(N*(N-1)))
    return sigma

tocke = [1,2,3,4,5,6,7,8,9,10]
print("Prosječna vrijednost iznosi {} +/- {}".format(sredina(tocke), std_dev(tocke)))

# (b)
print("Aritmetička sredina iznosi: {}".format(np.average(tocke)))
print("Standardna devijacija iznosi: {}".format(np.std(tocke) / np.sqrt(len(tocke) - 1)))

