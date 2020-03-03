N = int(input())
år = 0
bonsai = {n:[] for n in range(N)}           # sedan {node:[children]}
parents = {n: None for n in range(N)}       # sedan {node:parent}
potentialdict = {n:[] for n in range(N)}    # sedan {node:[potential]}
användpotential = {n:0 for n in range(N)}  # sedan {node: använd potential}
for n in range(N):
    siffror = [int(char) for char in input().split()]
    potential = siffror.pop(0)
    while siffror != []:
        granne = siffror.pop(0)
        parent = min(granne, n)
        child = max(granne, n)
        if child not in bonsai[parent]:
            bonsai[parent].append(child)
            parents[child] = parent

            if potentialdict[child] == []:
                potentialdict[child].extend([p for p in range(1,potential)])
            if potentialdict[parent] != []:
                användpotential[parent] += 1
                if användpotential[parent] == max(potentialdict[parent]):
                    for key in parents:
                        if parents[key] == parents[parent]:
                            potentialdict[key].remove(användpotential[parent])
            else:
                år += 1

    # print("children: ", bonsai)
    # print("parents: ", parents)
    # print("potential: ", potentialdict)
    # print("använd potential: ", användpotential)
    # print("år gångna: ", år)
print(år)