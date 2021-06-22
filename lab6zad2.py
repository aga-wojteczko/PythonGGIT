#zle zrozumialam tresc. rozwiazanie w wordzie
slownik ={}
haslo = input("Podaj slowo: ")
klucz = len(haslo)
if klucz not in slownik:
    slownik[klucz]=haslo
print(slownik)