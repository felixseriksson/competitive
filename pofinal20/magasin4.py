björnar, dagaride = [int(x) for x in input().split()]
dagarmånad = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
arbetstid = 365 - dagaride
gåriide = []
for n in range(björnar):
    d, m = [int(x) for x in input().split("/")]
    gåriide.append((sum(dagarmånad[:m-1]) + d - 1))

björnegåriide = gåriide.pop(0)
björnekanjobba = björnegåriide + dagaride
normtillbjörnekanjobba = 365 - björnekanjobba
björnekanjobba = 365
björnegåriide += normtillbjörnekanjobba
kanbörjajobbanormaliserad = sorted([(x + dagaride + normtillbjörnekanjobba ) % 364 for x in gåriide])
#print(kanbörjajobbanormaliserad)
undregräns = björnegåriide
counter = 0
broke = False
while kanbörjajobbanormaliserad:
    if kanbörjajobbanormaliserad[0] <= undregräns and kanbörjajobbanormaliserad[1] > undregräns:
        anställdbjörn = kanbörjajobbanormaliserad[0]
        undregräns = anställdbjörn + arbetstid
        counter += 1
    del kanbörjajobbanormaliserad[0]
    if undregräns >= björnekanjobba - 1:
        broke = True
        break

if not broke:
    print(-1)
else:
    print(counter)




















# björnesovstart = lista[0] - dagaride
# mål = björnesovstart + dagaride - 1
# lista = sorted(lista)
# counter = 1
# broke = True
# if björnesovstart < lista[0]:
#     tempfrämre = (lista[-1] + arbetstid) % 364
# else:
#     for n in range(len(lista)):
#         if lista[n] <= björnesovstart and lista[n+1] > björnesovstart:
#             tempfrämre = lista[n] + arbetstid
#             del lista[:n+1]
#             break

# print(tempfrämre)
# while lista:
#     if tempfrämre >= mål:
#         broke = False
#         break
#     if lista[0] <= tempfrämre and lista[1] > tempfrämre:
#         tempfrämre = lista[0] + arbetstid
#         counter += 1
#     del lista[0]
# if broke:
#     print(-1)
# else:
#     print(counter)