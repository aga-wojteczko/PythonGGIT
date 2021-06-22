ct = "Ala ma kota. Ola ma psa. Jeszcze jedno zdanie"
pocz = ct.find("Ola")
kon = pocz+1
while ct[kon] != ".":
    kon+=1
print(ct[pocz:kon])