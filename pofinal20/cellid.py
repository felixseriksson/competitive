celltyper, beståndsdelar = [int(x) for x in input().split()]
celler = [["finns ej"] for n in range(2**beståndsdelar)]
for n in range(1, celltyper+1):
    typ = int(input(), 2)
    celler[typ] = [n]
#print(celler)

for index in reversed(range(len(celler))):
    cellnamn = celler[index][0]
    if cellnamn == "finns ej":
        continue
    mängd = index
    temp = []
    binary = bin(mängd)[2:]
    for c in range(len(binary)):
        if binary[-(c+1)] == "1":
            temp.append(mängd-2**c)
    for subtyp in temp:
        if celler[subtyp][0] == "finns ej":
            celler[subtyp] = [cellnamn]
        elif celler[subtyp][0] == cellnamn:
            continue
        else:
            celler[subtyp] = ["vet ej"]
#print(celler)

testcases = int(input())
for n in range(testcases):
    querynum = int(input(), 2)
    print(celler[querynum][0])