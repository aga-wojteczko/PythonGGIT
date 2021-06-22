import random
zdanie = input("podaj zdanie: ")
los = random.randint(0, len(zdanie)-1)
print(zdanie[los])