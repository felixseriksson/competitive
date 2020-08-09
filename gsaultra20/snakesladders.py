from random import randint

def solution(N, S, L):
    placementdict = {}
    for x in S:
        placementdict[x[0]] = x[1]
    for x in L:
        placementdict[x[0]] = x[1]
    av = 0
    for i in range(70):
        pos = 0
        turns = 0
        while pos < N-1:
            turns += 1
            pos += randint(1,6)
            try:
                pos = placementdict[pos]
            except KeyError:
                pass
        av += turns
    return av//70

#print(solution(10, [(2,1), (9,3)], [(4,5)]))