d = dict()
for _ in range(int(input())):
    inpp = input().split()
    n, i = inpp[0], int(inpp[1])
    d[i] = n

items = sorted(d.items(), key = lambda x: x[0])
print(items[1][1])