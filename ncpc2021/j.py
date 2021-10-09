l = [int(x) for x in input().split()]
d1 = ((l[0]- l[2])**2 + (l[1] - l[3])**2)**0.5
d2 = ((l[4]- l[6])**2 + (l[5] - l[7])**2)**0.5
print(max(d1, d2))