#funkcja losująca dowolny znak ciągu. rozwiązanie w wordzie
import random
def losuj(ciag):
losowa = random.randint(0, len(ciag)-1)
return ciag[losowa]

ciag = input("Podaj ciag: ")
print(losuj(ciag))

