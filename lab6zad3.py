#czestosc wystepowania wyrazow w tekscie
tekst = "ala ala ma kota kota kota"
slownik = {}
for i in tekst.split():
    slownik[i] = slownik.get[i,0] + 1
print(slownik)