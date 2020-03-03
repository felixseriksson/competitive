'''
def movetonextparty(lista,serielista):
    dagjustnu = lista[0]
    timmarattkolla = int(dagjustnu[0]*10)
    serierattsepådentiden = dagjustnu[2:]
    tiddetskulleta = 0
    for n in serierattsepådentiden:
        tiddetskulleta += serier[n]
    if tiddetskulleta > timmarattkolla:
        print("Nej")
        return ["STOPP"], {}
    else:
        for serie in serierattsepådentiden:
            for nestedlist in lista[1:]:
                if serie in nestedlist[2:]:
                    nestedlist.reverse()
                    nestedlist.remove(serie)
                    nestedlist.reverse()
                    nestedlist[1] -= 1
            del serielista[serie]
        del lista[0]
        tidkvar = timmarattkolla - tiddetskulleta
        while tidkvar > 0 and len(kalas) > 0:
            for nestedlist in lista:
                if tidkvar == 0:
                    break
                for serie in nestedlist[2:]:
                    if tidkvar >= serielista[serie]:
                        tidkvar -= serielista[serie]
                        serielista[serie] = 0
                    elif tidkvar < serielista[serie]:
                        serielista[serie] -= tidkvar
                        tidkvar = 0
                        break
    return lista, serielista

inputline1 = [int(char) for char in input().split()]
antalkalas = inputline1[0]
antalserier = inputline1[1]
serier = {} # nummer av serien:längd(h) ex 3:5
inputline2 =[int(char) for char in input().split()]
for n in range(len(inputline2)):
    serier[int(n+1)] = inputline2[n]
kalas = [] # lista av listor, där varje lista har dagar från förra kalaset till det nuvarande på index 0,
           # antal filmer som diskuteras på index 1 och filmer att diskuteras på resterande
# läs in första
kalas.append([0, 0])
# läs in dagar att titta på mellan föregående och nu och hur många/vilka serier som ska ses för resterande
values = []
for n in range(antalkalas):
    temp = [int(char) for char in input().split()]
    values.append(temp[0])
    kalas.append(temp)

#print(kalas)
for n in range(antalkalas-1):
    kalas[n+2][0] -= (values[n]+1) # ändrar antal dagar från start till antal dagar att kolla mellan nu och nästa kalas
# kalas är nu på formen [[0,0], [bla, blaha, nåt mer], ...] där [0,0] är idag och vi har 0 filmer att se
#print(kalas) #ta bort vid submission!!!!!!
#om movetonextparty returnerar False, bryt loopen
while len(kalas) > 0:
    kalas, serier = movetonextparty(kalas, serier)
    if kalas == ["STOPP"]:
        break
    #print(kalas) # ta bort vid submission!!!!!

if isinstance(kalas, list) and kalas != ["STOPP"]:
    print("Ja")
#alternativ om jag kör fast: lägg filmerna i en typ priority-queue lista, kolla steg för steg om han hinner
'''
'''
inputline1 = [int(char) for char in input().split()]
antalkalas = inputline1[0]
antalserier = inputline1[1]
serietider = [int(char) for char in input().split()]
sorteradserietider = []
kalasdagar = []
dagartid = []
antal = []
serieprioritet = []
listaavlistor = []
lyckas = True
for n in range(antalkalas):
    temp = [int(char) for char in input().split()]
    kalasdagar.append(temp[0])
    antal.append(temp[1])
    temporär = []
    for serie in temp[2:]:
        if serie not in serieprioritet:
            serieprioritet.append(serie)
            sorteradserietider.append(serietider[serie-1])
        temporär.append(serie)
    listaavlistor.append(temporär)

# print(kalasdagar)
# print(antal)
# print(serietider)
# print(serieprioritet)
for n in range((antalkalas-1)):
    dagartid.append(kalasdagar[-(n+1)]-kalasdagar[-(n+2)]-1)
dagartid.append(kalasdagar[0])
dagartid.reverse()
# print(antalkalas)
# print(antalserier)
# print(serietider)
# print(kalasdagar)
# print(dagartid)
# print(antal)
# print(serieprioritet)
if 10*sum(dagartid) < sum(sorteradserietider):
    lyckas = False

for dag in range(len(dagartid)):
    if lyckas == False:
        break
    tid = int(10*dagartid[dag])
    while tid > 0:
        if len(serieprioritet) == 0:
            break
        for serie in serieprioritet:
            index = serieprioritet.index(serie)
            if tid >= sorteradserietider[index]:
                tid -= sorteradserietider[index]
                del serieprioritet[0]
                del sorteradserietider[0]
                break
            else:
                sorteradserietider[index] -= tid
                tid = 0
                break
    for val in listaavlistor[dag]:
        if val in serieprioritet:
            lyckas = False
            break

if lyckas == True:
    print("Ja")
else:
    print("Nej")
'''

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

# print(kalasdagar)
# print(dagartid) #!
# print(serieprioritet) #!
# print(serietider) 
# print(sorteradserietider) #!
# print(antalsteg) #!
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