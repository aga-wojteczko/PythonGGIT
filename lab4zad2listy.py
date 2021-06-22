zdanie = input("podaj zdanie: ")
lista = zdanie.split()
dlugosc = len(lista)
for n in range(dlugosc):
    i = len(lista[n])
    print(lista[n], "ma dlugosc", format(i))