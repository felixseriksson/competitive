n = int(input())
h = [int(x) for x in input().split()]
cmax = max(h)
m = h.index(cmax)
l, r = -1, n
count = 0
while l < r - 1:
    try:
        leftmax = max(h[l+1:m])
    except:
        leftmax = 0
    try:
        rightmax = max(h[m+1:r])
    except:
        rightmax = 0
    if leftmax == 0 and rightmax == 0:
        break
    if leftmax > rightmax:
        cmax = leftmax
        r = m
        m = h.index(leftmax)
        count += 1
    else:
        cmax = rightmax
        l = m
        m = h.index(rightmax)
        count += 1

print(count)