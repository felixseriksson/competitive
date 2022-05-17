from collections import defaultdict

n = int(input())

d, deg = defaultdict(list), defaultdict(int)
for _ in range(n-1):
    u, v = [int(x) for x in input().split()]
    d[u].append(v)
    d[v].append(u)
    deg[u] += 1
    deg[v] += 1

root, maxdeg  = max(deg.items(), key = lambda x: x[1])
leaves = set(key for key, val in deg.items() if val == 1)

s = [(root, 0)]
seen = set()
trav = []
branchcount = defaultdict(int)
while s:
    c, branch = s.pop()
    if not c in seen:
        seen.add(c)
        if c in leaves:
            trav.append((c, branch))
            branchcount[branch] += 1
        if c == root:
            for n in d[c]:
                s.append((n, n))
        else:
            for n in d[c]:
                s.append((n, branch))
print(trav)
print(branchcount)

leaves = sorted(leaves, key = lambda x: branchcount[x])
print(leaves)

if len(leaves) % 2 == 0:
    print(len(leaves))
    for i in range(len(leaves)//2):
        print(f"{leaves[i]} {leaves[-i-1]}")
else:
    print(len(leaves) + 1)
    for i in range(len(leaves)//2):
        print(f"{leaves[i]} {leaves[-i-1]}")
    print(f"{leaves[len(leaves)//2]} {root}")