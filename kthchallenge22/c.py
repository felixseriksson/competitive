n = int(input())
l1 = n - n%100 + 99
l2 = n - n%100 + 99 - 100
d1, d2 = abs(n-l1), abs(n-l2)
if l2 <= 0:
    print(l1)
else:
    print(l1 if d1 <= d2 else l2)