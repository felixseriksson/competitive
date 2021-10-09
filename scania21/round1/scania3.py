l = [1, 9, 14, 12, 8, 4, 13, 15, 7, 18, 17, 2, 11, 10, 6, 31, 54, 77, 3, 0, 5, 16]
indexlist = sorted(l[:])
indexlist = {indexlist[i]:i+1 for i in range(len(indexlist))}
s = 0
curr = 11
while True:
    idx = l.index(curr) + 1
    wantedidx = indexlist[curr]
    if idx == wantedidx:
        break
    else:
        s += 1
        other = l[wantedidx-1]
        l[idx-1], l[wantedidx-1] = other, curr
        curr = other
print(s)