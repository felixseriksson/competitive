from heapq import heapify, heappop, heappush, nlargest
from collections import OrderedDict

def contract(node, edges, neighbours, values, children): 
    #node n är den att kontrahera in i (en nod med barn där alla barn är löv)
    #children är dict där children[n] ger [a, b, c...] där a, b, c är barn
    #parents är dict där parents[n] gör ö där ö är den nod för vilken n är i children[ö]
    #values är dict där values[n] ger nuvarande tiden från att den noden nås
    maxtid = 0
    sortedchildrenvalues = sorted([values[ch] for ch in children], reverse=True)
    for char in range(1, len(sortedchildrenvalues)+1):
        activeval = sortedchildrenvalues.pop(0)
        maxtid = max(maxtid, activeval + char)
    values[node] = maxtid
    for tabort in children:
        for edge in edges:
            if edge[1] == tabort:
                edges.remove(edge)
        neighbours[node] -= 1

    return edges, neighbours, values

N = int(input())
edgeslist = []
neighbourslist = {n:0 for n in range(N)}
valueslist = {n:0 for n in range(N)}
leaflist = []
for n in range(N):
    siffror = [int(char) for char in input().split()]
    grannar = siffror.pop(0)
    neighbourslist[n] = grannar
    if grannar == 1:
        leaflist.append(n)
    while siffror != []:
        granne = siffror.pop(0)
        parent = min(granne, n)
        child = max(granne, n)
        if [parent, child] not in edgeslist:
            edgeslist.append([parent, child])

#neighbourslist = list(OrderedDict(sorted(neighbourslist.items(), key = lambda t: t[1])).items())

print("edgeslist: ", edgeslist)
print("neighbourslist: ", neighbourslist)
print("valueslist: ", valueslist)
print("leaflist: ", leaflist)

while len(edgeslist) != 0:
    tocheck = [n[0] for n in edgeslist if n[1] in leaflist]
    print("tocheck: ", tocheck)
    for nodetocheck in tocheck:
        allalöv = True
        nodetocheckchildren = []
        for edge in edgeslist:
            if edge[0] == nodetocheck:
                if neighbourslist[edge[1]] != 1:
                    allalöv = False
                    break
                nodetocheckchildren.append(edge[1])
        if allalöv == True:
            edgeslist, neighbourslist, valueslist = contract(nodetocheck, edgeslist, neighbourslist, valueslist, nodetocheckchildren)   
   
    #edgeslist, neighbourslist, valueslist = contract(nodetocontract, edgeslist, neighbourslist, valueslist)
    '''
    for kanskeparent in parentslist.keys():
        broke = False
        if childrenlist[kanskeparent] != []:
            for kanskeleaves in childrenlist[kanskeparent]:
                if childrenlist[kanskeleaves] != []:
                    broke = True
                    break
            if broke == False:
                childrenlist, parentslist, valueslist = contract(kanskeparent, childrenlist, parentslist, valueslist)
                break
    '''
#centralnod = list(parentslist.keys()).pop(0)
#print("det tar", valueslist[centralnod], "år att växa bonsaiträdet från rot", centralnod)
#print(valueslist[centralnod])
print(valueslist[0])