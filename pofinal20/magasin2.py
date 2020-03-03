# björnar, dagaride = [int(x) for x in input().split()]
# dagarmånad = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# #första-sista:0-30,31-58,59-99...
# skiftlista = []
# björned, björnem = [int(x) for x in input().split("/")]
# björnestartdag = (sum(dagarmånad[:björnem-1]) + björned - 1)
# leftbound = björnestartdag + dagaride #första inkl som måste täckas
# goal = björnestartdag + 364 #sista inkl som måste täckas
# for n in range(björnar-1):
#     d, m = [int(x) for x in input().split("/")]
#     skiftlista.append((sum(dagarmånad[:m-1]) + d - 1))
# print(skiftlista)
# print(leftbound, goal)

# skiftlista = sorted([(x+dagaride - leftbound - 1) % 365 for x in skiftlista])
# print(skiftlista)
# # skiftlista = [[x, x + 365 - dagaride] for x in skiftlista]
# # print(skiftlista)
# counter = 0
# currentleft = leftbound
# currentright = 0
# for n in skiftlista:
#     if n <= currentleft:
#         currentright = n + 365 - dagaride
#     #elif
björnar, dagaride = [int(x) for x in input().split()]
dagarmånad = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
lista = []
for n in range(björnar):
    d, m = [int(x) for x in input().split("/")]
    lista.append((sum(dagarmånad[:m-1]) + d - 1))
#print(lista)
förstadagatttäcka = lista.pop(0)
förstadagattintetäcka = förstadagatttäcka+dagaride
#print(förstadagatttäcka, förstadagattintetäcka)

lista = sorted([(x + dagaride) % 365 for x in lista])
#print(lista)
while lista[0] > förstadagatttäcka:
    lista.insert(0, lista[-1]-365)
#print(lista)

counter = 0
broke = False
for n in range(len(lista)):
    if lista[n] <= förstadagatttäcka:
        if lista[n+1] > förstadagatttäcka:
            counter += 1
            förstadagatttäcka = lista[n] + 365 - dagaride
        if förstadagatttäcka >= förstadagattintetäcka:
            broke = True
            break
        else:
            continue
if broke:
    print(counter)
else:
    print(-1)