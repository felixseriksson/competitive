def getbest(l, num, getvals = False):
    """
        Given list l of length > num containing binary strings, return those num 
        binary strings in list with least sum of hamming distances to binary strings in strings.
    """
    keyval = []
    for string in l:
        hammingsum = 0
        for i in range(len(string)):
            if string[i] == 0:
                hammingsum += onesat[i]
            else:
                hammingsum += zerosat[i]
        keyval.append((string, hammingsum))
    
    keyval = sorted(keyval, key= lambda x: x[1])[:num]
    if getvals:
        return keyval
    else:
        return [pair[0] for pair in keyval]

for ind in range(int(input())):
    n, m, p = [int(x) for x in input().split()]
    strings = [input() for _ in range(n)]
    forbidden = set([input() for _ in range(m)])
    # Careful: onesat[0] is # of ones at pos 0 from left, not from right
    onesat = [sum([1 if string[i] == "1" else 0 for string in strings]) for i in range(p)]
    zerosat = [sum([1 if string[i] == "0" else 0 for string in strings]) for i in range(p)]
    cands = [[]]
    for i in range(p):
        newcands = []
        for cand in cands:
            newc0, newc1 = cand[:], cand[:]
            newc0.append(0)
            newc1.append(1)
            newcands.append(newc0)
            newcands.append(newc1)
        if len(newcands) > m+1:
            cands = getbest(newcands, m+1)
        else:
            cands = newcands
    cands = [c for c in cands if "".join([str(a) for a in c]) not in forbidden]
    best = min([pair[1] for pair in getbest(cands, len(cands), getvals = True)])
    print(f"Case #{ind+1}: {best}")