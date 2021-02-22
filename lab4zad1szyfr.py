user = 'ala ma kota' #input("Podaj znak: ")
user = user.lower()
key = [3,4,5,6]
spacja = " "
szyfr = ""
i = 0
for znak in user:
    if znak == spacja:
        szyfr += spacja
        continue
    for klucz in key:
        szyfr += chr((ord(znak)-97+klucz[i])%26+97)
        i = (i+1)%4
print(szyfr)