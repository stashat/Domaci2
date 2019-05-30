import random
l=[]
nova_l=[]
iskorisceni=[]
for i in range (10):
    l.append(random.randrange(1, 11, 1))
print(l)

for i in l:
        if i not in nova_l:
                nova_l.append(i)

while len(iskorisceni)!=len(nova_l):
        if len(nova_l)%2!=0 and len(iskorisceni)==len(nova_l)-1:
                break
        parovi = (random.choice(l), random.choice(l))
        if parovi[0] not in iskorisceni and parovi[1] not in iskorisceni and parovi[0]!=parovi[1]:
                iskorisceni.append(parovi[0])
                iskorisceni.append(parovi[1])
                print(parovi)