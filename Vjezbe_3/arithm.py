##Zadatak 3 
##(a) Napišite program arithm.py koji računa aritmetičku sredinu i standardnu devijaciju za 10 točaka. 
##Formula za aritmetičku sredinu je dana u 1, a za standardnu devijaciju u 2. 
##(b) Napišite program pod (a) koristeći gotove module.
import numpy as np
def sredina(nums):
    N = len(nums)
    return sum(nums)/N

def st_dev(nums):
    av = sredina(nums)
    N = len(nums)

    for num in nums:
        num = (num - av)**2
    sigma = np.sqrt(sum(nums)/(N*(N-1)))
    print(sigma)

a = [2,4,6,8,10,12,14,16,18,20]
st_dev(a)
