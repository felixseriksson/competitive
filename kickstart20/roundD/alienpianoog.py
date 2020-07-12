## SAMMA SOM ALLENPIANO.PY, FAST SÄTTER CURR LIKAMED NEXTT EFTER EN ITERATION (HADE GLÖMT DETTA)
from collections import deque
cases = int(input())
for case in range(1, cases+1):
    ctr = 0
    length = int(input())
    song = deque([int(x) for x in input().split()])
    curr = song.popleft()
    upcounter = 0
    downcownter = 0
    for tone in range(length-1):
        nextt = song.popleft()
        if curr == nextt:
            continue
        elif curr > nextt:
            #neråt
            downcownter += 1
            upcounter = 0
        elif curr < nextt:
            #uppåt
            upcounter += 1
            downcownter = 0
        if upcounter == 4 or downcownter == 4:
            upcounter = 0
            downcownter = 0
            ctr += 1
        curr = nextt
    print("Case #{}: {}".format(case, ctr))