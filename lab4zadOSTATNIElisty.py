import random
L=[]
for i in range(100):
    L.append(random.randint(0,1000))
kopia = L.copy()
print(max(L), "znajduje się w miejscu", i)

#rozwiązanie w wordzie