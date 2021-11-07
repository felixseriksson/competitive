n, q = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
opt = dict()
for i in range(1, 51):
    try:
        opt[i] = l.index(i) + 1
    except:
        pass
colors = opt.keys()
for q in [int(x) for x in input().split()]:
    best = opt[q]
    if best == 1:
        print(1, end=" ")
    else:
        for c in colors:
            if opt[c] <= best:
                opt[c] += 1
        print(best, end=" ")
    opt[q] = 1