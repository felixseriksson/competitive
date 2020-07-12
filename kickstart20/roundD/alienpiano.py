from collections import deque
cases = int(input())
for case in range(1, cases+1):
    ctr = 0
    length = int(input())
    song = deque([int(x) for x in input().split()])
    curr = song.popleft()
    incr = False
    sublen = 1
    for tone in range(length-1):
        nextt = song.popleft()
        if curr == nextt:
            continue
        elif curr > nextt:
            #neråt
            
            incr = False
            sublen += 1
        elif curr < nextt:
            #uppåt
            upcounter += 1
            downcownter = 1
    print("Case #{}: {}".format(case, ctr))