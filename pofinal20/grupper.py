from itertools import permutations
from math import floor
stolar, stolpar = [int(x) for x in input().split()]
stolparlista = []
for n in range(stolpar):
    stolparlista.append([int(x) for x in input().split()])
if stolar % 2 == 0:
    stolstring1 = int(stolar/2)*"1"+int(stolar/2)*"2"
    permutationslista = []
    permlist = permutations(stolstring1)
    for perm in list(permlist):
        permutationslista.append("".join(perm))
    #print(permutationslista)
else:
    stolstring1 = floor(stolar/2)*"1"+(floor(stolar/2)+1)*"2"
    stolstring2 = floor(stolar/2)*"2"+(floor(stolar/2)+1)*"1"
    permutationslista = []
    permlist = permutations(stolstring1)
    for perm in list(permlist):
        permutationslista.append("".join(perm))
    permlist = permutations(stolstring2)
    for perm in list(permlist):
        permutationslista.append("".join(perm))
    #print(permutationslista)

möjliga = set()
for permutation in permutationslista:
    for par in stolparlista:
        if permutation[par[0]-1] != permutation[par[1]-1]:
            break
    else:
        möjliga.add(permutation)
#print(möjliga)

möjliga = list(möjliga)
sistamöjliga = []

for n in range(len(möjliga)):
    current = möjliga.pop(0)
    ones = 0
    twos = 0
    broke = False
    for n in range(stolar):
        if current[n] == "1":
            ones += 1
        else:
            twos += 1
        if abs(ones-twos) > 1:
            broke = True
            break
    for par in stolparlista:
        if current[par[0]-1] != current[par[1]-1]:
            broke = True
            break
    if broke == False:
        sistamöjliga.append(current)
if len(sistamöjliga) == 0:
    print(-1)
else:
    print(sorted(sistamöjliga)[0])

# from itertools import permutations
# from math import floor
# stolar, stolpar = [int(x) for x in input().split()]
# stolparlista = []
# for n in range(stolpar):
#     stolparlista.append([int(x) for x in input().split()])

# for n in range(stolar)