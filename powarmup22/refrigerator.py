from math import ceil
pa, ka, pb, kb, n = [int(a) for a in input().split()]
uppera, upperb = ceil(n/ka), ceil(n/kb)
besta, bestb, bestcost = None, None, 10000000000000
for i in range(uppera+1):
    for j in range(upperb+1):
        if i*ka + j*kb < n or i*pa+j*pb >= bestcost:
            continue
        else:
            bestcost = i*pa+j*pb
            besta, bestb = i, j

print(besta, bestb, bestcost)