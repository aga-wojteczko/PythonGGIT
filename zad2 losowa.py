import random
losowa1 = random.randint(0, 10)
losowa2 = random.randint(0, 10)
losowa3 = random.randint(0, 10)
wynik = (10*losowa1 + losowa2 + 0.1*losowa3)%100
print(wynik)
