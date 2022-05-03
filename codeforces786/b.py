d = dict()
ctr = 1
for i in range(97, 123):
    for j in range(97, 123):
        if i == j:
            continue
        string = chr(i) + chr(j)
        d[string] = ctr
        ctr += 1
for _ in range(int(input())):
    print(d[input()])