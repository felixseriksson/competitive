n, m = [int(x) for x in input().split()]
havebits = [int(x) for x in input().split()]
needbits = [0 for _ in range(n)]
inps = [int(x) for x in input().split()]
for item in inps:
    for index, val in enumerate(str(bin(item)[2:])[::-1]):
        if val == "1":
            needbits[index] += 1
for e in range(n):
    if havebits[e] < needbits[e]:
        print("nej")
        exit(0)
    else:
        havebits[e] -= needbits[e]
        try:
            havebits[e+1] += havebits[e]//2
        except IndexError:
            pass
print("ja")