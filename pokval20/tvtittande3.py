inputline1 = [int(char) for char in input().split()]
antalkalas = inputline1[0]
antalserier = inputline1[1]
serier = {}
dagartid = [-1]
nyaserier = []
prioritet = []
checkade = []
num = 1
for char in input().split():
    serier[int(num)] = int(char)
    num += 1
for n in range(antalkalas):
    temp = [int(char) for char in input().split()]
    dagartid.append(temp[0])
    nyaserier.append(temp[1])
    for serie in temp[2:]:
        if serie not in checkade:
            checkade.append(serie)
            prioritet.append([serie, serier[serie]])
        else:
            nyaserier[n] -= 1

dagartid = [dagartid[n+1]-dagartid[n]-1 for n in range(len(dagartid)-1)]

hinner = True
if sum(dagartid)*10 < sum(serier.values()):
    hinner = False

tid = 0
while hinner == True:
    if prioritet == []:
        break
    tid += 10*dagartid.pop(0)
    behövs = 0
    for n in range(nyaserier.pop(0)):
        behövs += prioritet.pop(0)[1]
    tid -= behövs
    if tid < 0:
        hinner = False

if hinner == True:
    print("Ja")
else:
    print("Nej")