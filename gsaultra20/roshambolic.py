from collections import deque

def solution(a, b):
    wins = {"R":"S", "S": "P", "P": "R"}
    a, b, ctr = deque(a), deque(b), 0
    goon = True
    while goon:
        try:
            at, bt = a.pop(), b.pop()
            ctr += 1
            if at == bt:
                a.appendleft(at)
                b.appendleft(bt)
            elif bt == wins[at]:
                a.appendleft(bt)
                a.appendleft(at)
            else:
                b.appendleft(at)
                b.appendleft(bt)
        except IndexError:
            goon = False
    return ctr

# print(solution("SRR", "PPS"))