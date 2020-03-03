antalstolar, antalpar = [int(x) for x in input().split()]
edges = []
values = {}
for n in range(1, antalstolar+1, 2):
    if n == antalstolar and n%2==1:
        break
    edges.append((n, n+1, 1))
    values[n] = None
    values[n+1] = None
if antalstolar %2 == 1:
    values[antalstolar] = None

#print(edges)
for n in range(antalpar):
    stol1, stol2 = [int(x) for x in input().split()]
    if stol1 < stol2:
        edges.append((stol1, stol2, 0))
    else:
        edges.append((stol2, stol1, 0))
#print(edges)
#print(values)
edges = sorted(edges, reverse=True)

def fillcyclefromnode(node, edgelist, valuelist):
    while edgelist:
        if valuelist[node] == None:
            prevscore = 0
            parity = 1
            nextnode = node
        else:
            prevscore = valuelist[node]
            parity = edgelist[-1][2]
            nextnode = edgelist[-1][1]
            del edgelist[-1]
        while True:
        #try:
            if valuelist[nextnode] == None:
                valuelist[nextnode] = (parity + prevscore) % 2
            elif valuelist[nextnode] == (parity + prevscore) % 2:
                break
            else:
                return -1
            neighbours = []

            for edgeindex in sorted(range(len(edgelist)), reverse=True):
                if edgelist[edgeindex][0] == nextnode:
                    neighbours.append(edgelist[edgeindex])
                    prevscore = valuelist[nextnode]
                    nextnode = neighbours[0][1]
                    parity = neighbours[0][2]
                    del edgelist[edgeindex]
                    break
                elif edgelist[edgeindex][1] == nextnode:
                    neighbours.append(edgelist[edgeindex])
                    prevscore = valuelist[nextnode]
                    nextnode = neighbours[0][0]
                    parity = neighbours[0][2]
                    del edgelist[edgeindex]
                    break
            if neighbours == []:
                break
    return edgelist, valuelist

broke = False
startnode = edges[-1][0]
try:
    edges, values = fillcyclefromnode(startnode, edges, values)
except TypeError:
    broke = True

if broke:
    print(-1)
#print(edges, values)
else:
    for val in values:
        if values[val] == None:
            values[val] = 1
    # string = ""
    # for n in values:
    #     string += str((values[n]+1)%2+1)
    # print(string)
    for char in values:
        print((values[char]+1)%2+1, end="", sep="")