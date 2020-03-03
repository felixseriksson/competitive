björnar, dagaride = [int(x) for x in input().split()]
dagarmånad = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
arbetstid = 365 - dagaride
lista = []
for n in range(björnar):
    d, m = [int(x) for x in input().split("/")]
    lista.append((sum(dagarmånad[:m-1]) + d - 1))

#print(lista)
björnesover = lista.pop(0) # plockar ut björne
lista = [(x - björnesover + dagaride) % 364 for x in lista] # gör om dagar till antal dagar mellan björne sover och arbetaren vaknar
lista = sorted(lista)
#print(lista)
förstadagen = lista[-1] # tar ut sista elementet (då björne är 0, dvs sista är närmast framifrån)
#print(förstadagen, arbetstid)
måstevaramindreän = 0 # fixerar första som ska täckas in till 0
mål = dagaride - 1 # fixerar sista som ska täckas (då björne vaknar)
#print(måstevaramindreän, mål)
counter = 1 # sätter counter till 1 eftersom vi alltid tar den sista björnen (minst)
måstevaramindreän = (förstadagen + arbetstid - 1) % 364 # gör om måstevaramindreän till den senaste täckta dagen
#print(måstevaramindreän)
broke = False
while lista:
    if måstevaramindreän >= mål:
        break
    if lista[0] <= måstevaramindreän and lista[1] > måstevaramindreän:
        måstevaramindreän = lista.pop(0) + arbetstid
        #print(måstevaramindreän)
        counter += 1
    else:
        del lista[0]
        continue
else:
    broke = True
    print(-1)
if not broke:
    print(counter)