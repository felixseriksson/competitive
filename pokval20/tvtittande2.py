inputline1 = [int(char) for char in input().split()]
antalkalas = inputline1[0]
antalserier = inputline1[1]
kalasdagar = []
dagartid = []
serieprioritet = []
sorteradserietider = []
antalsteg = []
serietider = [int(char) for char in input().split()]
for n in range(antalkalas):
    temp = [int(char) for char in input().split()]
    kalasdagar.append(temp[0])
    antalsteg.append(0)
    for serie in temp[2:]:
        if serie not in serieprioritet:
            serieprioritet.append(serie)
            sorteradserietider.append(serietider[serie-1])
            antalsteg[n] += 1

for n in range((antalkalas-1)):
    dagartid.append(kalasdagar[-(n+1)]-kalasdagar[-(n+2)]-1)
dagartid.append(kalasdagar[0])
dagartid.reverse()

if sum(serietider) > sum(dagartid)*10:
    skip = True
    klara = False
else:
    skip = False

faktisktid = 0
for n in range(antalkalas):
    if skip == True:
        break
    tid = dagartid.pop(0)
    faktisktid += tid*10
    tidsombehövs = 0
    for n in range(antalsteg[n]):
        tidsombehövs += sorteradserietider.pop(0)
        del serieprioritet[0]
    faktisktid -= tidsombehövs
    if faktisktid < 0:
        break
    if sorteradserietider == []:
        klara = True
        break

if klara == True:
    print("Ja")
else:
    print("Nej")
'''
print("50 50\n","10 "*50)
a, b, c = 2, 1, 1
for n in range(50):
    print(a,b,c)
    a +=2
    c +=1
'''