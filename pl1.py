import string
ciag = input("Podaj ciąg tekstowy: ")
ciag = ciag.lower()
#pojedyncze = ciag.strip()
ilee = 0
litery = 0
znaki = 0
L = " "
C = "0123456789"
punkty = string.punctuation + L + C
for i in range(len(ciag)):
#for i in range(len(pojedyncze)):
    if 'e'==ciag[i]:
        ilee = ilee + 1
    if ciag[i] in punkty:
        znaki = znaki+1
    else:
        litery=litery+1
procent = ((ilee/litery)*100)
print("W ciągu znaleziono:",ilee,"liter \'e', co stanowi:",round(procent,2),"% wszystkich liter",",znaki:",znaki,",litery:",litery)