def getname():
    cons = ["b", "c", "d", "f", "g", "h"]
    vow = ["a", "e", "i", "o", "u"]
    for c1 in cons:
        for v1 in vow:
            for c2 in cons:
                for v2 in vow:
                    for c3 in cons:
                        for v3 in vow:
                            for c4 in cons:
                                for v4 in vow:
                                    for c5 in cons:
                                        for v5 in vow:
                                            for c6 in cons:
                                                yield "".join([c1, v1, c2, v2, c3, v3, c4, v4, c5, v5, c6])

n = 0
N = int(input())
for val in getname():
    if n >= N:
        exit(0)
    print(val)
    n += 1