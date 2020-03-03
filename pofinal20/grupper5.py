antalstolar, antalpar = [int(x) for x in input().split()]
edges = {n:[] for n in range(1, antalstolar+1)}
values = {n: None for n in range(1, antalstolar+1)}
for n in range(1, antalstolar+1, 2):
    if n == antalstolar and n%2==1:
        break
    edges[n].append((n+1, 1))
    edges[n+1].append((n, 1))

#print(edges)
for n in range(antalpar):
    stol1, stol2 = [int(x) for x in input().split()]
    edges[stol1].append((stol2, 0))
    edges[stol2].append((stol1, 0))
#print(edges, values)
loopcurrent = 1
broke = False
while True:
    if broke == True:
        break
    if loopcurrent == antalstolar+1:
        break
    try:
        edge = edges[loopcurrent][0]
    except:
        if values[loopcurrent] == None:
            values[loopcurrent] = 1
        loopcurrent += 1
        continue
    targetnode = edge[0]
    parity = edge[1]
    values[loopcurrent] = 1
    current = loopcurrent
    while targetnode:
        for tup in edges[current]:
            if tup[0] == targetnode:
                edges[current].remove(tup)
        for tup in edges[targetnode]:
            if tup[0] == current:
                edges[targetnode].remove(tup)
        if values[targetnode] == None:
            values[targetnode] = (values[current] + parity) % 2
        elif values[targetnode] == (values[current] + parity) % 2:
            pass
        else:
            broke = True
            break
        current = targetnode
        try:
           targetnode = edges[current][0][0]
           parity = edges[current][0][1]
        except:
            break

#print(edges, values)
if broke:
    print(-1)
# else:
#     for char in values:
#         print((values[char]+1)%2+1, end="", sep="")
#     print("\n")
else:
    string = ""
    for val in values:
        string += str((values[val]+1)%2+1)
    print(string)