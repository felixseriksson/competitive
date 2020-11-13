n, m, k = [int(x) for x in input().split()]
sets = [set() for _ in range(m)]
for _ in range(n):
    line = input()
    for ind in range(m):
        sets[ind].add(line[ind])

disjoint = []
for s in sets:
    for d in disjoint:
        if not s.isdisjoint(d):
            disjoint.remove(d)
            disjoint.append(d.union(s))
            break
    else:
        disjoint.append(s)

print(len(disjoint))