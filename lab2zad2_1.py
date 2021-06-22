import random
losowa = random.randint(0, 10)
liczba = input("zgadnij liczbe: ")
if losowa==int(liczba):
    print("gratulacje")
elif losowa!=int(liczba):
    liczba = input("zgaduj dalej: ")
   
        
    