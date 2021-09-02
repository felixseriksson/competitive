from collections import defaultdict
with open("c1/test1.txt", "r") as inputfile:
    inp = [line.strip() for line in inputfile]

cases = int(inp[0])
i = 1
out = []

def solve(index):
    n = int(inp[index])
    value = [int(val) for val in inp[index+1].split(" ")]
    value.insert[0, 0]
    fromto = defaultdict(set)
    for offset in range(1, n):
        f, t = [int(node) for node in inp[index+1+offset].split(" ")]
        fromto[f].add(t)
        fromto[t].add(f)
    maxret = maxgiven(1, set(), fromto, value, 1)

    return maxret, index+n+1

def maxgiven(root, disallowededges, adj, val, k):
    candidatenodes = set([node for node in adj[root] if node not in disallowededges])
    # currentvalue = vals
    # if len(candidatenodes) > 0:
    #     for candidate in candidatenodes:
    #         tempdisallowed = set([x for x in disallowededges])
    #         tempdisallowed.add((root, candidate))
    #         tempemptynodes = set([x for x in emptynodes])
    #         tempemptynodes.add(root)
    #         tempcurrentvalue = currentvalue + val[root]
    #         maxgiven(candidate, tempdisallowed))
    currentval = val[root]
    newval = [a if a!=root else 0 for a in val]
    if len(candidatenodes) > 0:
        maxfromedge = 0
        for candidate in candidatenodes:
            pass
    else:
        maxfromedge = 0
    if k > 0:
        maxfromk = 0
        for candidate in range(1, n+1):
            pass
    else:
        maxfromk = 0
    


for ind in range(1,cases+1):
    gold, i = solve(i)


with open("c1/test1-out.txt", "w") as outfile:
    for line in out:
        outfile.write(line + "\n")