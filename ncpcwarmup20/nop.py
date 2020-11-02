# import re

# k = re.findall("[A-Z][a-z]*", input())
# print(sum([4- len(x) for x in k]))
instr = [c for c in input()]
nops = 0
dists = []
for i in instr:
    if i.upper() == i:
        dists.append(0)
    else:
        dists[-1] += 1
dists[-1] = dists[-1] - dists[-1]%4
for d in dists:
    nops += 3 - (d%4)
print(nops)