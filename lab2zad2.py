import random
losowa = random.randint(0, 10)
liczba = input("zgadnij liczbe: ")
if losowa==liczba:
    print("gratulacje")
else:
    print("niestety, była to liczba",losowa)